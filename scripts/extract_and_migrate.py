"""Extract and migrate all LeetCode & DSA practice solutions from multiple repos
into a Date-first and Streak-first directory structure under dates/YYYY/MM-Month/DD-MM-YY/.
"""
import os
import re
import json
import shutil
import datetime as dt
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE_PATH = r'C:\Users\yashk\.gemini\antigravity\brain\8e3502bc-69ad-4d5b-b84f-6e9822abc7f2\scratch\all_questions_cache.json'
SOURCES = {
    'leetcode': r'C:\Users\yashk\.gemini\antigravity\brain\8e3502bc-69ad-4d5b-b84f-6e9822abc7f2\scratch\repo_leetcode',
    'dsa_practice': r'C:\Users\yashk\.gemini\antigravity\brain\8e3502bc-69ad-4d5b-b84f-6e9822abc7f2\scratch\repo_dsa_practice',
    'dsa_python': r'C:\Users\yashk\.gemini\antigravity\brain\8e3502bc-69ad-4d5b-b84f-6e9822abc7f2\scratch\repo_dsa_python',
    'current': ROOT
}

MONTH_NAMES = {
    1: "01-January", 2: "02-February", 3: "03-March", 4: "04-April",
    5: "05-May", 6: "06-June", 7: "07-July", 8: "08-August",
    9: "09-September", 10: "10-October", 11: "11-November", 12: "12-December"
}

with open(CACHE_PATH, 'r', encoding='utf-8') as f:
    cache = json.load(f)
by_num = cache['by_num']
by_slug = cache['by_slug']
by_title = cache['by_title']

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def map_tags_to_pattern(tags, title=""):
    t_lower = [t.lower() for t in tags]
    t_str = " ".join(t_lower) + " " + title.lower()
    if "two pointers" in t_lower or "two pointer" in t_str:
        return "Two Pointers"
    if "sliding window" in t_lower:
        return "Sliding Window"
    if "prefix sum" in t_lower:
        return "Prefix Sum"
    if "monotonic stack" in t_lower or "stack" in t_lower:
        return "Stack"
    if "binary search" in t_lower:
        return "Binary Search"
    if any(x in t_lower for x in ["binary tree", "tree", "binary search tree"]):
        return "Trees & BST"
    if any(x in t_lower for x in ["graph", "breadth-first search", "depth-first search", "topological sort", "union find"]):
        return "Graphs & Search"
    if "dynamic programming" in t_lower:
        return "Dynamic Programming"
    if "hash table" in t_lower or "counting" in t_lower:
        return "Arrays & Hashing"
    if "database" in t_lower:
        return "SQL"
    if "sorting" in t_lower:
        return "Sorting & STL"
    if "bit manipulation" in t_lower:
        return "Bit Manipulation"
    if "string" in t_lower:
        return "Strings"
    if "array" in t_lower:
        return "Arrays & Hashing"
    if "math" in t_lower:
        return "Math & Logic"
    return "Data Structures & Algorithms"

def lookup_problem(num=None, title=None, slug=None):
    if num is not None and str(num) in by_num:
        return by_num[str(num)]
    if slug and slug in by_slug:
        return by_slug[slug]
    if title:
        t_clean = title.lower().strip()
        if t_clean in by_title:
            return by_title[t_clean]
        s = slugify(title)
        if s in by_slug:
            return by_slug[s]
    return None

def parse_date_str(s):
    if not s: return None
    for fmt in ['%d %b %Y', '%Y-%m-%d', '%d-%m-%y', '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y']:
        try:
            return dt.datetime.strptime(s, fmt).date()
        except:
            pass
    m = re.search(r'(\d{1,2})[-/](\d{1,2})[-/](\d{2,4})', s)
    if m:
        d, mth, y = m.groups()
        y = int(y)
        if y < 100: y += 2000
        try:
            return dt.date(y, int(mth), int(d))
        except:
            pass
    m2 = re.search(r'(Aug|Sep|Oct|Nov|Dec|Jan|Feb|Mar|Apr|May|Jun|Jul)_(\d{1,2})_(\d{4})', s, re.I)
    if m2:
        mth_str, d, y = m2.groups()
        mth = dt.datetime.strptime(mth_str[:3].title(), '%b').month
        return dt.date(int(y), mth, int(d))
    m3 = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:\s+(\d{2,4}))?', s, re.I)
    if m3:
        d, mth_str, y_str = m3.groups()
        d = int(d)
        y = int(y_str) if y_str else 2026
        if y < 100: y += 2000
        mth = dt.datetime.strptime(mth_str[:3].title(), '%b').month
        return dt.date(y, mth, d)
    return None

def extract_file_meta(content, rel_path, filename):
    # Check for existing header
    meta = {
        'num': None, 'title': None, 'slug': None, 'diff': None,
        'pattern': None, 'time': None, 'space': None, 'date': None,
        'kind': 'leetcode'
    }
    # LeetCode 15 · 3Sum · Medium
    m = re.search(r'LeetCode\s+(\d+)\s*[·\-\|]\s*(.+?)\s*[·\-\|]\s*(Easy|Medium|Hard)', content, re.I)
    if m:
        meta['num'] = int(m.group(1))
        meta['title'] = m.group(2).strip()
        meta['diff'] = m.group(3).title()
    
    # Check filename for problem number e.g. "1011. Capacity..." or "0217-contains..."
    if not meta['num']:
        m_fn = re.match(r'^(\d+)\.\s*(.+)', filename)
        if m_fn:
            meta['num'] = int(m_fn.group(1))
            meta['title'] = m_fn.group(2).rsplit('.', 1)[0].strip()
        else:
            m_fn2 = re.match(r'^(\d{3,4})-(.+)', filename)
            if m_fn2:
                meta['num'] = int(m_fn2.group(1))
                meta['title'] = m_fn2.group(2).rsplit('.', 1)[0].replace('-', ' ').title()

    # Check for date in header
    m_d = re.search(r'(?:Solved|Written|Date)\s*:\s*([^\n]+)', content)
    if m_d:
        p = m_d.group(1).split(',')[0].strip()
        meta['date'] = parse_date_str(p)
    
    # If no date in header, check path
    if not meta['date']:
        meta['date'] = parse_date_str(rel_path)
    
    # Check for pattern / time / space
    m_pat = re.search(r'Pattern\s*:\s*([^\n]+)', content)
    if m_pat: meta['pattern'] = m_pat.group(1).strip()
    m_time = re.search(r'Time\s*:\s*([^\n]+)', content)
    if m_time: meta['time'] = m_time.group(1).strip()
    m_space = re.search(r'Space\s*:\s*([^\n]+)', content)
    if m_space: meta['space'] = m_space.group(1).strip()

    # Fallback to June 26, 2026 for un-dated git files
    if not meta['date']:
        meta['date'] = dt.date(2026, 6, 26)

    # Problem lookup
    info = lookup_problem(num=meta['num'], title=meta['title'])
    if info:
        meta['num'] = info['num']
        meta['title'] = info['title']
        meta['slug'] = info['slug']
        meta['diff'] = info['diff']
        if not meta['pattern']:
            meta['pattern'] = map_tags_to_pattern(info.get('tags', []), info['title'])
    else:
        # Check if title corresponds to DSA lesson
        meta['kind'] = 'lesson'
        if not meta['title']:
            meta['title'] = filename.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
        if not meta['pattern']:
            meta['pattern'] = "Data Structures & Algorithms"

    return meta

def strip_old_header(content, ext):
    lines = content.splitlines()
    body_start = 0
    if ext == '.cpp':
        # check /* ... */
        if lines and lines[0].strip().startswith('/*'):
            for i, l in enumerate(lines):
                if '*/' in l:
                    body_start = i + 1
                    break
    elif ext == '.py':
        # check """ ... """
        if lines and (lines[0].strip().startswith('"""') or lines[0].strip().startswith("'''")):
            delim = lines[0].strip()[:3]
            for i in range(1, len(lines)):
                if delim in lines[i]:
                    body_start = i + 1
                    break
    elif ext == '.sql':
        # check leading -- lines
        while body_start < len(lines) and lines[body_start].strip().startswith('--'):
            body_start += 1

    clean_body = "\n".join(lines[body_start:]).lstrip("\n")
    return clean_body

def build_header(meta, ext):
    d_str = meta['date'].strftime('%d %b %Y')
    pat = meta.get('pattern') or "Data Structures & Algorithms"
    tm = meta.get('time') or "O(n)"
    sp = meta.get('space') or "O(1)"
    if meta['kind'] == 'leetcode' and meta.get('num'):
        url = f"https://leetcode.com/problems/{meta['slug']}/"
        lines = [
            f"LeetCode {meta['num']} · {meta['title']} · {meta['diff']}",
            url,
            "",
            f"Pattern : {pat}",
            f"Solved  : {d_str}",
            f"Time    : {tm}",
            f"Space   : {sp}"
        ]
    else:
        lines = [
            f"DSA Lesson · {meta['title']}",
            "",
            f"Pattern : {pat}",
            f"Written : {d_str}",
            f"Time    : {tm}",
            f"Space   : {sp}"
        ]
    
    if ext == '.cpp':
        return "/*\n" + "\n".join(f" * {l}".rstrip() for l in lines) + "\n */\n\n"
    elif ext == '.py':
        return '"""\n' + "\n".join(lines) + '\n"""\n\n'
    else: # .sql
        return "\n".join(f"-- {l}".rstrip() for l in lines) + "\n\n"

def process_python_file_with_multiple_solutions(path, rel_p, filename):
    # Splits files like Sep_19_2026.py into individual problem files
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    date_val = parse_date_str(filename) or dt.date(2026, 9, 19)
    # Split by # Problem Name or # Number. Problem Name
    chunks = re.split(r'\n(?=#\s*(?:\d+\.|\b[A-Z]))', text)
    results = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk: continue
        m = re.match(r'^#\s*(\d+)?\.?\s*([^\n]+)', chunk)
        if m:
            num_str = m.group(1)
            title = m.group(2).strip()
            num = int(num_str) if num_str else None
            info = lookup_problem(num=num, title=title)
            meta = {
                'num': info['num'] if info else num,
                'title': info['title'] if info else title,
                'slug': info['slug'] if info else slugify(title),
                'diff': info['diff'] if info else 'Medium',
                'pattern': map_tags_to_pattern(info.get('tags', []), title) if info else 'Arrays & Hashing',
                'time': 'O(n)', 'space': 'O(1)',
                'date': date_val,
                'kind': 'leetcode' if (info or num) else 'lesson'
            }
            hdr = build_header(meta, '.py')
            results.append((meta, hdr + chunk + "\n"))
        else:
            meta = {
                'num': None, 'title': 'Python Practice Snippet', 'slug': 'python-practice-snippet',
                'diff': 'Easy', 'pattern': 'Python Basics', 'time': 'O(1)', 'space': 'O(1)',
                'date': date_val, 'kind': 'lesson'
            }
            hdr = build_header(meta, '.py')
            results.append((meta, hdr + chunk + "\n"))
    return results

def main():
    print("Starting migration to dates/ structure...")
    dates_dir = os.path.join(ROOT, "dates")
    os.makedirs(dates_dir, exist_ok=True)
    
    migrated_count = 0
    seen_destinations = {}

    # Scan and process each source
    # Priority order: current -> repo_leetcode -> repo_dsa_practice -> repo_dsa_python
    for src_name in ['current', 'leetcode', 'dsa_practice', 'dsa_python']:
        src_root = SOURCES[src_name]
        print(f"\nProcessing source: {src_name} ({src_root})")
        
        for root, dirs, files in os.walk(src_root):
            if any(x in root for x in ['.git', 'assets', 'scripts', '.github', 'dates']):
                continue
            for f in sorted(files):
                ext = os.path.splitext(f)[1].lower()
                if ext not in ['.cpp', '.py', '.sql']:
                    continue
                full_p = os.path.join(root, f)
                rel_p = os.path.relpath(full_p, src_root).replace('\\', '/')
                
                # Check if multi-solution python file in dsa_python
                if src_name == 'dsa_python' and f.startswith(('Aug_', 'Sep_')):
                    sub_items = process_python_file_with_multiple_solutions(full_p, rel_p, f)
                    for meta, full_content in sub_items:
                        y = meta['date'].year
                        m_folder = MONTH_NAMES[meta['date'].month]
                        d_folder = meta['date'].strftime('%d-%m-%y')
                        target_dir = os.path.join(dates_dir, str(y), m_folder, d_folder)
                        os.makedirs(target_dir, exist_ok=True)
                        if meta['kind'] == 'leetcode' and meta.get('num'):
                            fn = f"{meta['num']:04d}-{meta['slug']}.py"
                        else:
                            fn = f"{meta['slug']}.py"
                        dest = os.path.join(target_dir, fn)
                        with open(dest, 'w', encoding='utf-8', newline='\n') as out_f:
                            out_f.write(full_content)
                        migrated_count += 1
                        seen_destinations[fn] = dest
                    continue

                with open(full_p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                
                meta = extract_file_meta(content, rel_p, f)
                clean_body = strip_old_header(content, ext)
                new_header = build_header(meta, ext)
                full_content = new_header + clean_body + "\n"

                y = meta['date'].year
                m_folder = MONTH_NAMES[meta['date'].month]
                d_folder = meta['date'].strftime('%d-%m-%y')
                target_dir = os.path.join(dates_dir, str(y), m_folder, d_folder)
                os.makedirs(target_dir, exist_ok=True)

                if meta['kind'] == 'leetcode' and meta.get('num'):
                    fn = f"{meta['num']:04d}-{meta['slug']}{ext}"
                else:
                    fn = f"{slugify(meta['title'])}{ext}"

                dest = os.path.join(target_dir, fn)
                
                # If file already migrated on same date, keep the longer / better body
                if os.path.exists(dest):
                    with open(dest, 'r', encoding='utf-8', errors='ignore') as existing_f:
                        existing_content = existing_f.read()
                    if len(existing_content) >= len(full_content):
                        continue
                
                with open(dest, 'w', encoding='utf-8', newline='\n') as out_f:
                    out_f.write(full_content)
                migrated_count += 1
                seen_destinations[fn] = dest

    print(f"\nSuccessfully migrated {migrated_count} solution files into {dates_dir}!")

if __name__ == '__main__':
    main()
