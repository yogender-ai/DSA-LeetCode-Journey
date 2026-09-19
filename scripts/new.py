"""Scaffold today's LeetCode problem (or log a revisit) and rebuild the README.

    python scripts/new.py <slug | number> <topic-number | topic-folder> [--lang py|cpp|sql] [--date 2026-09-20]

    python scripts/new.py two-sum 01
    python scripts/new.py 3 03 --lang cpp
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))


def gql(query, variables):
    req = urllib.request.Request("https://leetcode.com/graphql", data=json.dumps({"query": query, "variables": variables}).encode(),
                                 headers={"Content-Type": "application/json", "Referer": "https://leetcode.com", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)["data"]


def lookup(key):
    if key.isdigit():
        qs = gql("query($f: QuestionListFilterInput){ questionList(categorySlug: \"\", limit: 20, skip: 0, filters: $f)"
                 "{ data { questionFrontendId title titleSlug difficulty } } }", {"f": {"searchKeywords": key}})["questionList"]["data"]
        q = next((q for q in qs if q["questionFrontendId"] == key), None)
    else:
        q = gql("query($s: String!){ question(titleSlug: $s){ questionFrontendId title titleSlug difficulty } }", {"s": key})["question"]
    if not q:
        sys.exit(f"LeetCode problem '{key}' not found")
    return int(q["questionFrontendId"]), q["title"], q["titleSlug"], q["difficulty"]


def header(lang, num, title, slug, diff, date):
    lines = [f"LeetCode {num} · {title} · {diff}", f"https://leetcode.com/problems/{slug}/", "",
             "Pattern : ", f"Solved  : {date:%d %b %Y}", "Time    : ", "Space   : "]
    if lang == "py":
        return '"""\n' + "\n".join(lines) + '\n"""\nfrom typing import List\n\n\nclass Solution:\n    pass\n'
    if lang == "cpp":
        return "/*\n" + "\n".join(f" * {l}".rstrip() for l in lines) + "\n */\n#include <bits/stdc++.h>\nusing namespace std;\n\nclass Solution {\npublic:\n};\n"
    return "\n".join(f"-- {l}".rstrip() for l in lines) + "\n\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("problem")
    ap.add_argument("topic")
    ap.add_argument("--lang", default="py", choices=["py", "cpp", "sql"])
    ap.add_argument("--date", type=dt.date.fromisoformat, default=dt.datetime.now(TZ).date())
    a = ap.parse_args()

    folder = next((f for f in sorted(os.listdir(ROOT)) if f == a.topic or f.startswith(a.topic.zfill(2) + "-")), None)
    if not folder:
        sys.exit(f"no topic folder matches '{a.topic}'")
    if folder == "08-sql":
        folder, a.lang = "08-sql/leetcode", "sql"
    num, title, slug, diff = lookup(a.problem)
    path = os.path.join(ROOT, folder, f"{num:04d}-{slug}.{a.lang}")

    if os.path.exists(path):  # revisit → append today's date
        text = open(path, encoding="utf-8").read()
        stamp = f"{a.date:%d %b %Y}"
        if stamp in text:
            print("already logged for", stamp)
        else:
            text = re.sub(r"(Solved\s*:\s*[^\n]*)", lambda m: m[1].rstrip() + f", {stamp}", text, count=1)
            open(path, "w", encoding="utf-8", newline="\n").write(text)
            print(f"↺ revisit logged → {os.path.relpath(path, ROOT)}")
    else:
        open(path, "w", encoding="utf-8", newline="\n").write(header(a.lang, num, title, slug, diff, a.date))
        print(f"+ created {os.path.relpath(path, ROOT)}  ({diff})")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py")], check=True)


if __name__ == "__main__":
    main()
