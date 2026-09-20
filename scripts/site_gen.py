"""Render the GitHub Pages site: index.html, sitemap.xml, robots.txt.

The solution rows are written into the HTML rather than fetched by JavaScript
at load time. Google can execute JS, but it does so on a slower second pass and
often not at all, so a list that only exists after a fetch may never be
indexed. Written this way every title is in the page source.
"""
import datetime as dt
import json
import os
import re

TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))
SITE_URL = "https://yogender-ai.github.io/DSA-LeetCode-Journey/"

VIOLET, CYAN, LIME, AMBER, TEAL = "#8b5cf6", "#22d3ee", "#a3e635", "#fbbf24", "#2dd4bf"


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _rows(items, repo):
    out = []
    for it in items:
        haystack = f"{it['title']} {it['num'] or ''} {it['pattern']}".lower()
        num = f"#{it['num']}" if it["num"] else "&mdash;"
        link = (f'<a href="{esc(it["url"])}" rel="noopener">{esc(it["title"])}</a>'
                if it["url"] else esc(it["title"]))
        src = f'https://github.com/{repo}/blob/main/{it["path"]}'
        date = it["dates"][-1] if it["dates"] else ""
        out.append(
            f'    <li data-diff="{esc(it["difficulty"])}" data-pattern="{esc(it["pattern"])}" '
            f'data-lang="{esc(it["lang"])}" data-search="{esc(haystack)}">\n'
            f'      <span class="num">{num}</span>\n'
            f'      <div>\n'
            f'        <div class="title">{link}</div>\n'
            f'        <div class="meta">'
            f'<span class="chip {esc(it["difficulty"])}">{esc(it["difficulty"])}</span>'
            f'<span class="chip pat">{esc(it["pattern"])}</span>'
            f'<span class="chip lang">{esc(it["lang"])}</span>'
            f'<a class="chip src" href="{esc(src)}" rel="noopener">code &#8599;</a>'
            f'</div>\n'
            f'      </div>\n'
            f'      <span class="date">{esc(date)}</span>\n'
            f'    </li>'
        )
    return "\n".join(out)


def _options(values):
    return "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in sorted(values))


def _jsonld(desc, items, leetcode_user, repo):
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": SITE_URL + "#website",
                "url": SITE_URL,
                "name": "Yogender - DSA & LeetCode Journey",
                "description": desc,
                "inLanguage": "en",
                "author": {"@id": SITE_URL + "#person"},
            },
            {
                "@type": "Person",
                "@id": SITE_URL + "#person",
                "name": "Yogender",
                "alternateName": leetcode_user,
                "url": "https://github.com/yogender-ai",
                "sameAs": [
                    "https://github.com/yogender-ai",
                    f"https://leetcode.com/u/{leetcode_user}/",
                ],
                "knowsAbout": ["Data Structures", "Algorithms", "Python", "C++", "SQL",
                               "Dynamic Programming", "Graph Algorithms", "Coding Interviews"],
            },
            {
                "@type": "SoftwareSourceCode",
                "name": "DSA-LeetCode-Journey",
                "codeRepository": f"https://github.com/{repo}",
                "programmingLanguage": sorted({it["lang"] for it in items}),
                "author": {"@id": SITE_URL + "#person"},
                "description": desc,
            },
        ],
    }, indent=1, ensure_ascii=False)


def write_site(root, items, s, algo, leetcode_user, repo):
    docs = os.path.join(root, "docs")
    os.makedirs(docs, exist_ok=True)

    tpl_path = os.path.join(root, "scripts", "site.template.html")
    if not os.path.exists(tpl_path):
        print("No site template found; skipping docs/index.html")
        return

    tiles = [
        ("Solved", s["solved_total"], f'{s["easy"]} easy - {s["medium"]} med - {s["hard"]} hard', VIOLET),
        ("Streak", f'{s["current"]}d', f'longest {s["longest"]}d', LIME),
        ("Active days", s["active"], "lifetime", CYAN),
        ("Contest", s["rating"], f'top {s["top_pct"]}%', AMBER),
        ("In this repo", len(items), "files tracked", TEAL),
    ]
    tiles_html = "".join(
        f'<div class="tile"><div class="k" style="color:{c}">{esc(k)}</div>'
        f'<div class="v">{esc(v)}</div><div class="m">{esc(m)}</div></div>'
        for k, v, m, c in tiles
    )

    title = f'Yogender - {s["solved_total"]} LeetCode Solutions in C++, Python and SQL | DSA Journey'
    desc = (f'{s["solved_total"]} LeetCode problems solved and filed by date and pattern: '
            f'{s["easy"]} easy, {s["medium"]} medium, {s["hard"]} hard, with a {s["current"]}-day '
            f'streak. Browse every solution by topic, difficulty or language, with the source for each.')
    keywords = ("leetcode solutions, dsa, data structures and algorithms, python, c++, sql, "
                "two pointers, sliding window, binary search, dynamic programming, "
                "coding interview preparation, yogender")

    values = {
        "TITLE": esc(title),
        "DESCRIPTION": esc(desc),
        "KEYWORDS": esc(keywords),
        "URL": SITE_URL,
        "IMAGE": SITE_URL + "algo_replay.svg",
        "ALGO_ALT": esc(f'{algo["name"]} executing step by step'),
        "JSONLD": _jsonld(desc, items, leetcode_user, repo),
        "TILES": tiles_html,
        "ROWS": _rows(items, repo),
        "COUNT": str(len(items)),
        "OPT_DIFF": _options({it["difficulty"] for it in items}),
        "OPT_PAT": _options({it["pattern"] for it in items}),
        "OPT_LANG": _options({it["lang"] for it in items}),
        "GENERATED": dt.datetime.now(TZ).strftime("%d %b %Y"),
        "LEETCODE_USER": leetcode_user,
        "REPO": repo,
    }

    with open(tpl_path, encoding="utf-8") as fh:
        tpl = fh.read()
    html = re.sub(r"\{\{(\w+)\}\}", lambda m: values.get(m[1], ""), tpl)
    with open(os.path.join(docs, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)

    today = dt.datetime.now(TZ).date().isoformat()
    with open(os.path.join(docs, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 f'  <url><loc>{SITE_URL}</loc><lastmod>{today}</lastmod>'
                 '<changefreq>daily</changefreq><priority>1.0</priority></url>\n'
                 '</urlset>\n')

    with open(os.path.join(docs, "robots.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")

    print(f"Wrote docs/index.html ({len(items)} rows in the HTML), sitemap.xml, robots.txt")
