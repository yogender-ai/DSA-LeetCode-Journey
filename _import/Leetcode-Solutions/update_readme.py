#!/usr/bin/env python3
import os
import glob
import json
from datetime import datetime
import re

def count_cpp_files():
    """Count all .cpp files in the repository"""
    cpp_files = glob.glob('**/*.cpp', recursive=True)
    return len(cpp_files)

def count_by_category():
    """Count files by folder (category)"""
    categories = {}
    
    # Get all directories
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for dir_name in dirs:
            if dir_name not in ['.git', '__pycache__']:
                cpp_count = len(glob.glob(f'{dir_name}/*.cpp'))
                if cpp_count > 0:
                    categories[dir_name] = cpp_count
    
    return categories

def generate_stars(count):
    """Generate star emojis"""
    stars = '⭐' * min(count, 50)
    if count > 50:
        stars += f' (+{count-50})'
    return stars

def update_readme():
    """Update README.md with current stats"""
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    total = count_cpp_files()
    categories = count_by_category()
    
    # Update total count
    content = re.sub(r'Progress Stars: <span id="star-count">\d+</span>', 
                    f'Progress Stars: <span id="star-count">{total}</span>', content)
    
    # Update stars display
    stars = generate_stars(total)
    content = re.sub(r'id="stars-display">.*?</div>', 
                    f'id="stars-display">{stars}</div>', content)
    
    # Update progress table
    for category, count in categories.items():
        cat_lower = category.lower().replace(' ', '-')
        content = re.sub(rf'id="{cat_lower}-count">\d+</td>', 
                        f'id="{cat_lower}-count">{count}</td>', content)
        
        # Update progress bars (assuming target of 50)
        progress = min((count / 50) * 100, 100)
        content = re.sub(rf'id="{cat_lower}-bar" style="width: \d+%"', 
                        f'id="{cat_lower}-bar" style="width: {progress}%"', content)
    
    # Update last updated time
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content = re.sub(r'Last Updated: <span id="last-updated">.*?</span>', 
                    f'Last Updated: <span id="last-updated">{now}</span>', content)
    
    # Update badges
    content = re.sub(r'Progress-\d+%2F500', f'Progress-{total}%2F500', content)
    content = re.sub(r'Stars-.*?-yellow', f'Stars-{generate_stars(min(total, 5))}-yellow', content)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated! Total solutions: {total}")
    for cat, cnt in categories.items():
        print(f"   {cat}: {cnt} solutions")
    
    # Update streak
    update_streak()

def update_streak():
    """Update daily streak"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    if not os.path.exists('.streak'):
        with open('.streak', 'w') as f:
            f.write(today + '\n1')
        streak = 1
    else:
        with open('.streak', 'r') as f:
            lines = f.readlines()
            last_date = lines[0].strip()
            streak = int(lines[1].strip())
            
            if last_date == today:
                # Already updated today
                pass
            else:
                # New day
                yesterday = (datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                if last_date == yesterday:
                    streak += 1
                else:
                    streak = 1
                
                with open('.streak', 'w') as f:
                    f.write(today + '\n' + str(streak))
    
    print(f"🔥 Current streak: {streak} days")
    return streak

if __name__ == '__main__':
    print("🔄 Updating README with current progress...")
    update_readme()
    print("🎉 Done! View your updated README.md")
