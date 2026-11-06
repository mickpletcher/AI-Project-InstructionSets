import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'tools/validate.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        # Mutation tests must not inherit shipped sets or their catalog.
        self.root.mkdir()
        for filename in v.REQUIRED:
            path = self.root / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Fixture\n", encoding="utf-8")
        for platform in v.PLATFORMS:
            area = self.root / platform
            (area / 'instruction-sets').mkdir(parents=True)
            (area / 'README.md').write_text('# Platform\n', encoding='utf-8')
        shutil.copytree(ROOT / 'templates/example-project', self.root / 'templates/example-project')
        (self.root / 'catalog.json').write_text('{"schema_version":1,"instruction_sets":[]}', encoding='utf-8')
        (self.root / 'CATALOG.md').write_text(v.render_catalog([]), encoding='utf-8')

    def errors(self):
        return '\n'.join(v.validate(self.root))

    def publish(self, status='published'):
        path = 'openai/codex/instruction-sets/example-project'
        target = self.root / path
        shutil.copytree(self.root / 'templates/example-project', target)
        meta = json.loads((target / 'metadata.json').read_text(encoding="utf-8"))
        meta.update(platform='openai/codex', surface='AGENTS.md', status=status)
        (target / 'metadata.json').write_text(json.dumps(meta))
        (self.root / 'catalog.json').write_text(json.dumps({'schema_version': 1, 'instruction_sets': [path]}))
        return target

    def test_empty_fixture_passes(self):
        self.assertEqual([], v.validate(self.root))

    def test_publish_and_regenerate(self):
        self.publish()
        self.assertEqual([], v.validate(self.root, True))
        self.assertEqual([], v.validate(self.root))
        self.assertIn('AGENTS', (self.root / 'openai/codex/instruction-sets/example-project/metadata.json').read_text(encoding="utf-8"))

    def test_draft_not_publishable(self):
        self.publish('draft')
        self.assertIn('is not published', self.errors())

    def test_missing_source(self):
        (self.publish() / 'instructions.md').unlink()
        self.assertIn('instructions.md: missing', self.errors())

    def test_malformed_metadata(self):
        (self.publish() / 'metadata.json').write_text('{')
        self.assertIn('cannot read JSON', self.errors())

    def test_wrong_platform_and_version(self):
        p = self.publish() / 'metadata.json'
        m = json.loads(p.read_text(encoding="utf-8")); m.update(platform='claude', version='latest')
        p.write_text(json.dumps(m))
        self.assertIn('platform mismatch', self.errors())
        self.assertIn('version must be', self.errors())

    def test_missing_heading(self):
        p = self.publish() / 'instructions.md'
        p.write_text(p.read_text(encoding="utf-8").replace('## Constraints', '## Other'), encoding="utf-8")
        self.assertIn('missing heading Constraints', self.errors())

    def test_published_missing_inventory(self):
        self.publish()
        (self.root / 'catalog.json').write_text('{"schema_version":1,"instruction_sets":[]}')
        self.assertIn('published set missing', self.errors())

    def test_duplicate_inventory(self):
        self.publish()
        p = self.root / 'catalog.json'; m = json.loads(p.read_text(encoding="utf-8")); m['instruction_sets'] *= 2; p.write_text(json.dumps(m))
        self.assertIn('duplicate path', self.errors())

    def test_unsafe_inventory(self):
        (self.root / 'catalog.json').write_text('{"schema_version":1,"instruction_sets":["../secret",12]}')
        self.assertIn('unsafe path', self.errors())

    def test_catalog_drift(self):
        (self.root / 'CATALOG.md').write_text('stale')
        self.assertIn('CATALOG.md: stale', self.errors())

    def test_broken_link(self):
        (self.root / 'broken.md').write_text('[missing](no-such-file.md)')
        self.assertIn('broken or escaping relative link', self.errors())

    def test_malformed_url(self):
        (self.root / 'broken.md').write_text('[bad](http://[)')
        self.assertIn('malformed link', self.errors())

    def test_escaped_link(self):
        (self.root / 'broken.md').write_text('[escape](../outside.md)')
        self.assertIn('broken or escaping relative link', self.errors())

    def test_invalid_inventory_shape(self):
        (self.root / 'catalog.json').write_text('[]')
        self.assertIn('expected schema_version', self.errors())

    def test_unlisted_draft_allowed(self):
        self.publish('draft')
        (self.root / 'catalog.json').write_text('{"schema_version":1,"instruction_sets":[]}')
        self.assertEqual([], v.validate(self.root))


class CheckoutTests(unittest.TestCase):
    def test_actual_checkout_passes(self):
        # Do not replace this with the synthetic mutation fixture.
        self.assertEqual([], v.validate(ROOT))

    def test_mutations_with_published_checkout(self):
        global ROOT
        original = ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'repo'
            shutil.copytree(original, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            path = 'claude/instruction-sets/published-fixture'
            folder = root / path
            shutil.copytree(root / 'templates/example-project', folder)
            meta = json.loads((folder / 'metadata.json').read_text(encoding='utf-8'))
            meta.update(id='published-fixture', platform='claude', status='published')
            (folder / 'metadata.json').write_text(json.dumps(meta), encoding='utf-8')
            inventory = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
            inventory['instruction_sets'].append(path)
            (root / 'catalog.json').write_text(json.dumps(inventory), encoding='utf-8')
            self.assertEqual([], v.validate(root, True))
            try:
                ROOT = root
                suite = unittest.TestSuite(ValidationTests(name) for name in (
                    'test_publish_and_regenerate', 'test_unlisted_draft_allowed'))
                result = unittest.TestResult()
                suite.run(result)
                self.assertEqual([], result.errors)
                self.assertEqual([], result.failures)
                self.assertEqual([], v.validate(ROOT))
            finally:
                ROOT = original


class LinkTests(unittest.TestCase):
    def test_destinations(self):
        cases = {
            '[x](guide_(draft).md)': ['guide_(draft).md'],
            r'[x](guide_\(draft\).md)': ['guide_(draft).md'],
            '[x](a_(b_(c)).md "Title")': ['a_(b_(c)).md'],
            "[x](missing.md 'Title')": ['missing.md'],
            '[x](missing.md (Title))': ['missing.md'],
            '[x](<guide draft.md> "Title")': ['guide draft.md'],
            '![x](image_(draft).png)': ['image_(draft).png'],
            '[x](one.md) [y](two.md "Title")': ['one.md', 'two.md'],
            r'[x](one.md "A \"quoted\" title")': ['one.md'],
            '[x](broken_(file.md)': [],
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(expected, list(v.inline_destinations(source)))

    def test_parenthesized_file_and_titled_missing_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'guide_(draft).md').write_text('# Guide\n', encoding='utf-8')
            (root / 'links.md').write_text(
                '[valid](guide_(draft).md)\n'
                r'[escaped](guide_\(draft\).md)' '\n'
                '[missing](missing.md "Guide")\n', encoding='utf-8')
            errors = []
            v.check_links(root, errors)
            self.assertEqual(['links.md: broken or escaping relative link missing.md'], errors)


if __name__ == '__main__':
    unittest.main()
