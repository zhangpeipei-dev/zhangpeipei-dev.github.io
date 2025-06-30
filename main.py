import datetime

def generate(title):
    # 获取当前时间并格式化为 YYYY-MM-DD HH:MM:SS
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    template = f"""---
title: {title}
date: {current_time} +0800
categories: [TOP_CATEGORY, SUB_CATEGORY]
tags: [TAG]     # TAG names should always be lowercase
---"""
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f'_posts/{current_date}-{title}.md'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python main.py <title>")
        print("Example: python main.py 'My New Blog Post'")
        sys.exit(1)
    
    title = sys.argv[1]
    generate(title)
    print(f"Successfully created blog post: {title}")
