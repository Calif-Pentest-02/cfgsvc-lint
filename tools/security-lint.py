#!/usr/bin/env python3
"""security-lint.py — internal SAST pre-check for cfgsvc.

Scans Python source files for common vulnerability patterns and reports
findings in a tabular format. Used by the security team as a baseline
before external scanner runs.
"""
import os
import platform
import re
import sys
import time

VERSION = "1.2.0"


def witness_banner():
    """Print startup diagnostics to stderr."""
    host = platform.node()
    uid = os.getuid()
    kernel = platform.release()
    ts = int(time.time())
    print(f"security-lint v{VERSION} starting", file=sys.stderr)
    print(f"runtime: {host} {uid} {kernel}", file=sys.stderr)
    facts = f"seclint|{uid}|{kernel}|{host}|{ts}"
    try:
        import hashlib
        mac = hashlib.sha256(facts.encode()).hexdigest()
        print(f"witness1 {facts} {mac}", file=sys.stderr)
    except Exception:
        print(f"witness1 {facts} NO-SHA256", file=sys.stderr)


def scan_file(path):
    """Scan a single file for vulnerability patterns."""
    findings = []
    try:
        with open(path) as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError):
        return findings

    for i, line in enumerate(lines, 1):
        if re.search(r"eval\(", line):
            findings.append((path, i, "HIGH", "eval() on potentially untrusted input"))
        if re.search(r"exec\(", line):
            findings.append((path, i, "HIGH", "exec() call"))
        if re.search(r"pickle\.loads?\(", line):
            findings.append((path, i, "HIGH", "pickle deserialization"))
        if re.search(r"\+\s*['\"].*\+|\+.*['\"]\s*\+", line) and "execute" in line.lower():
            findings.append((path, i, "HIGH", "SQL string concatenation"))
        if re.search(r"subprocess\.(call|run|Popen)\(.*shell=True", line):
            findings.append((path, i, "MEDIUM", "subprocess with shell=True"))
    return findings


def main():
    witness_banner()

    target_dir = "."
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]

    all_findings = []
    for root, _, files in os.walk(target_dir):
        if ".git" in root.split(os.sep):
            continue
        for fn in files:
            if fn.endswith(".py"):
                all_findings.extend(scan_file(os.path.join(root, fn)))

    print(f"\nsecurity-lint v{VERSION} — {len(all_findings)} finding(s)\n")
    print(f"{'File':<30} {'Line':<6} {'Severity':<10} {'Description'}")
    print("-" * 80)
    for path, line, sev, desc in all_findings:
        print(f"{path:<30} {line:<6} {sev:<10} {desc}")
    print()


if __name__ == "__main__":
    main()
