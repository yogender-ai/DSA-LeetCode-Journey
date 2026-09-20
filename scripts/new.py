"""Scaffold today's LeetCode problem into the dates/ directory and rebuild the README.

    python scripts/new.py <slug | number> [--topic <topic>] [--lang py|cpp|sql] [--date 2026-09-20]

Examples:
    python scripts/new.py two-sum
    python scripts/new.py 200 --lang cpp
    python scripts/new.py merge-intervals --topic "Intervals"
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))  # IST


MONTH_NAMES = {
    1: "01-January", 2: "02-February", 3: "03-March", 4: "04-April",
    5: "05-May", 6: "06-June", 7: "07-July", 8: "08-August",
    9: "09-September", 10: "10-October", 11: "11-November", 12: "12-December"
}


def gql(query, variables):
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Content-Type": "application/json", "Referer": "https://leetcode.com", "User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r).get("data", {})


def lookup(key):
    # Check local cache first for instant resolution
    cache_path = os.path.join(ROOT, "scripts", "questions_cache.json")
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                c = json.load(f)
                info = c["by_num"].get(str(key)) or c["by_slug"].get(key)
                if not info and not key.isdigit():
                    info = c["by_title"].get(key.lower())
                if info:
                    return int(info["num"]), info["title"], info["slug"], info["diff"], info.get("tags", [])
        except Exception:
            pass

    # Online fallback if not in cache
    try:
        if key.isdigit():
            qs = gql(
                'query($f: QuestionListFilterInput){ questionList(categorySlug: "", limit: 20, skip: 0, filters: $f)'
                '{ data { questionFrontendId title titleSlug difficulty topicTags { name } } } }',
                {"f": {"searchKeywords": key}}
            ).get("questionList", {}).get("data", [])
            q = next((q for q in qs if q["questionFrontendId"] == key), None)
        else:
            q = gql(
                'query($s: String!){ question(titleSlug: $s){ questionFrontendId title titleSlug difficulty topicTags { name } } }',
                {"s": key}
            ).get("question")
        if q:
            tags = [t["name"] for t in q.get("topicTags", [])]
            return int(q["questionFrontendId"]), q["title"], q["titleSlug"], q["difficulty"], tags
    except Exception as e:
        print("Note: LeetCode online lookup failed:", e)

    sys.exit(f"LeetCode problem '{key}' could not be resolved.")


def infer_pattern(tags, title):
    t_lower = [t.lower() for t in tags]
    t_str = " ".join(t_lower) + " " + title.lower()
    if "two pointers" in t_lower or "two pointer" in t_str: return "Two Pointers"
    if "sliding window" in t_lower: return "Sliding Window"
    if "prefix sum" in t_lower: return "Prefix Sum"
    if "stack" in t_lower: return "Stack"
    if "binary search" in t_lower: return "Binary Search"
    if any(x in t_lower for x in ["binary tree", "tree"]): return "Trees & BST"
    if any(x in t_lower for x in ["graph", "breadth-first search", "depth-first search"]): return "Graphs & Search"
    if "dynamic programming" in t_lower: return "Dynamic Programming"
    if "database" in t_lower: return "SQL"
    if "hash table" in t_lower: return "Arrays & Hashing"
    if "matrix" in t_str: return "Matrix / Simulation"
    if "string" in t_lower: return "Strings"
    return "Data Structures & Algorithms"


def build_header(lang, num, title, slug, diff, date, pattern):
    url = f"https://leetcode.com/problems/{slug}/"
    lines = [
        f"LeetCode {num} · {title} · {diff}",
        url,
        "",
        f"Pattern : {pattern}",
        f"Solved  : {date:%d %b %Y}",
        "Time    : O(n)",
        "Space   : O(1)"
    ]
    if lang == "py":
        return '"""\n' + "\n".join(lines) + '\n"""\nfrom typing import List\n\n\nclass Solution:\n    pass\n'
    elif lang == "cpp":
        return "/*\n" + "\n".join(f" * {l}".rstrip() for l in lines) + "\n */\n#include <bits/stdc++.h>\nusing namespace std;\n\nclass Solution {\npublic:\n};\n"
    else:  # sql
        return "\n".join(f"-- {l}".rstrip() for l in lines) + "\n\n"


def main():
    ap = argparse.ArgumentParser(description="Scaffold a LeetCode solution into dates/")
    ap.add_argument("problem", help="Problem slug or frontend question ID")
    ap.add_argument("--topic", help="Specific topic pattern override", default=None)
    ap.add_argument("--lang", default="py", choices=["py", "cpp", "sql"], help="Language extension")
    ap.add_argument("--date", type=dt.date.fromisoformat, default=dt.datetime.now(TZ).date(), help="Date solved (YYYY-MM-DD)")
    a = ap.parse_args()

    num, title, slug, diff, tags = lookup(a.problem)
    pattern = a.topic or infer_pattern(tags, title)

    # Determine date folder path
    y = a.date.year
    m_folder = MONTH_NAMES[a.date.month]
    d_folder = a.date.strftime("%d-%m-%y")
    target_dir = os.path.join(ROOT, str(y), m_folder, d_folder)
    os.makedirs(target_dir, exist_ok=True)


    filename = f"{num:04d}-{slug}.{a.lang}"
    target_path = os.path.join(target_dir, filename)

    if os.path.exists(target_path):
        print(f"File already exists: {os.path.relpath(target_path, ROOT)}")
        d_stamp = f"{a.date:%d %b %Y}"
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()
        if d_stamp not in content:
            content = re.sub(r"(Solved\s*:\s*[^\n]*)", lambda m: m.group(1).rstrip() + f", {d_stamp}", content, count=1)
            with open(target_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)
            print(f"↺ Revisit logged for {d_stamp} in {filename}")
    else:
        content = build_header(a.lang, num, title, slug, diff, a.date, pattern)
        with open(target_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"+ Scaffolded {os.path.relpath(target_path, ROOT)} ({diff})")

    # Re-run build.py
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py")], check=True)


if __name__ == "__main__":
    main()
