"""Packaging checks only; these do not exercise host/model behavior."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = ('claude', 'openai/chatgpt', 'openai/codex', 'microsoft/copilot',
             'cursor', 'gemini', 'perplexity')
NAME = 'fitness-and-body-composition'


class FitnessPackagingTests(unittest.TestCase):
    def test_standalone_snapshots_match_canonical_source(self):
        source = (ROOT / 'claude/instruction-sets' / NAME / 'instructions.md').read_bytes()
        self.assertGreater(len(source), 1000)
        for platform in PLATFORMS:
            with self.subTest(platform=platform):
                folder = ROOT / platform / 'instruction-sets' / NAME
                self.assertEqual(source, (folder / 'instructions.md').read_bytes())

    def test_drafts_are_not_published_and_host_cases_are_not_claimed_run(self):
        catalog = json.loads((ROOT / 'catalog.json').read_text())['instruction_sets']
        for platform in PLATFORMS:
            folder = ROOT / platform / 'instruction-sets' / NAME
            with self.subTest(platform=platform):
                meta = json.loads((folder / 'metadata.json').read_text())
                self.assertEqual(meta['status'], 'draft')
                self.assertEqual(meta['platform'], platform)
                self.assertEqual(meta['version'], '0.1.0')
                self.assertNotIn(folder.relative_to(ROOT).as_posix(), catalog)
                self.assertIn('NOT RUN', (folder / 'tests.md').read_text())
                self.assertIn('rollback', (folder / 'README.md').read_text().lower())


if __name__ == '__main__':
    unittest.main()
