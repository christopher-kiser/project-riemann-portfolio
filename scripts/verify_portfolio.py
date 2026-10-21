"""Bounded standard-library checks for the public portfolio, not an RH checker."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled; do not use -O.")

    claims = list(csv.DictReader((ROOT / "data/claims.csv").open()))
    assert len(claims) == len({c["id"] for c in claims}) == 76
    for claim in claims:
        assert claim["status"] and claim["evidence_class"] and claim["dependencies"]
        for relative in claim["source_notes"].split(" | "):
            assert (ROOT / relative).is_file(), relative
    assert next(c for c in claims if c["id"] == "OCT20:RH042")["status"] == "SUPPLEMENTARY_NOT_ADOPTED"

    sources = list(csv.DictReader((ROOT / "research/source-index.csv").open()))
    for source in sources:
        assert digest(ROOT / source["public_file"]) == source["public_sha256"], source
        assert re.fullmatch(r"[0-9a-f]{64}", source["original_sha256"])
    assert digest(ROOT / "lean/MarkedGate.lean") == "2499f8f6dd0c2aea0951b2c786e3021b0099e97bd4e4352227c06822f6fc2e3f"

    process = subprocess.run([sys.executable, "-I", "-B", "scripts/check_exact_gate.py"],
                             cwd=ROOT, text=True, capture_output=True, timeout=30)
    assert process.returncode == 0, process.stdout + process.stderr
    actual = json.loads((ROOT / "build/exact-gate.json").read_text())
    actual.pop("seconds", None)
    expected = json.loads((ROOT / "evidence/expected-exact-gate.json").read_text())
    assert actual == expected, "The exact certificate differs from the authenticated reference."
    assert len(actual["box_certificates"]) == 19
    assert all(actual["negative_controls"].values())

    process = subprocess.run([sys.executable, "-I", "-B", "scripts/nested_prime_demo.py"],
                             cwd=ROOT, text=True, capture_output=True, timeout=15)
    assert process.returncode == 0, process.stdout + process.stderr
    nested = json.loads(process.stdout)
    assert nested["missing_correction_rejected"]

    # Check the navigable public documentation and reject accidental local-path release.
    documents = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    for document in documents:
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
            if link.startswith(("https://", "http://", "#")):
                continue
            target = (document.parent / link.split("#")[0]).resolve()
            assert target.is_relative_to(ROOT) and target.is_file(), (document.name, link)
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", "build", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text()
        private_roots = ("/" + "home" + "/", "/" + "mnt" + "/")
        assert not any(prefix in text for prefix in private_roots), path
        assert not re.search(r"C:[\\/]Users|ghp_[A-Za-z0-9]{20}|github_pat_[A-Za-z0-9_]{20}|-----BEGIN [A-Z ]*PRIVATE KEY-----", text), path

    result = {"status": "PASS", "claims": len(claims), "research_notes": len(sources),
              "exact_continuum_inequalities": 19, "Bernstein_boxes": 1216,
              "fixed_comparisons": 16, "negative_controls": actual["negative_controls"],
              "nested_prime_examples": nested,
              "scope": "Public finite checks, source hashes and documentation; no RH or full Haglund proof."}
    (ROOT / "build/local-checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
