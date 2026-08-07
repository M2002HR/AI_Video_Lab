import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LAB = ROOT / "11_TOOLS" / "lab.py"


class LabSmokeTests(unittest.TestCase):
    def run_lab(self, *args):
        return subprocess.run(
            [sys.executable, str(LAB), *args], cwd=ROOT, text=True,
            capture_output=True, check=True,
        )

    def test_project_and_experiment_allocation(self):
        spec = importlib.util.spec_from_file_location("lab", LAB)
        lab = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lab)
        paths = [Path("P0001_a"), Path("P0003_b")]
        self.assertEqual(lab.next_id("P", paths), "P0004")
        self.assertEqual(lab.next_id("EXP-", [Path("EXP-0002")]), "EXP-0003")

    def test_validate_current_repository(self):
        result = self.run_lab("validate")
        self.assertIn("Validation passed.", result.stdout)


if __name__ == "__main__":
    unittest.main()
