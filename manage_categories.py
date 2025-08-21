#!/usr/bin/env python3
"""
Category Management Script for Quarto Blog
==========================================
This script helps manage and analyze categories in your blog posts.

Usage:
    python manage_categories.py        # List all categories and their usage
    python manage_categories.py check  # Check for unused categories
    python manage_categories.py suggest # Suggest new categories based on content
"""

import os
import yaml
import json
from pathlib import Path
from collections import Counter, defaultdict
from typing import List, Dict, Set

def get_all_posts(posts_dir: str = "posts") -> List[Path]:
    """Find all .qmd files in the posts directory."""
    posts = []
    for root, dirs, files in os.walk(posts_dir):
        # Skip template and example files
        if 'TEMPLATE' in root or 'EXAMPLE' in root:
            continue
        for file in files:
            if file.endswith('.qmd') and not file.startswith('_'):
                # Skip template and example files
                if 'TEMPLATE' in file or 'EXAMPLE' in file:
                    continue
                posts.append(Path(root) / file)
    return posts

def extract_categories(post_path: Path) -> List[str]:
    """Extract categories from a post's frontmatter."""
    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract YAML frontmatter
        if content.startswith('---'):
            yaml_end = content.find('---', 3)
            if yaml_end != -1:
                yaml_content = content[3:yaml_end]
                metadata = yaml.safe_load(yaml_content)
                
                # Get categories
                categories = metadata.get('categories', [])
                if isinstance(categories, str):
                    categories = [categories]
                    
                # Skip draft posts unless specified
                if metadata.get('draft', False):
                    return []
                    
                return categories
    except Exception as e:
        print(f"Error reading {post_path}: {e}")
    return []

def analyze_categories():
    """Analyze category usage across all posts."""
    posts = get_all_posts()
    category_count = Counter()
    category_posts = defaultdict(list)
    
    print("\n📊 CATEGORY ANALYSIS")
    print("=" * 50)
    
    for post in posts:
        categories = extract_categories(post)
        for cat in categories:
            category_count[cat] += 1
            category_posts[cat].append(post.stem)
    
    if not category_count:
        print("No categories found in posts!")
        return
    
    # Sort by frequency
    sorted_categories = category_count.most_common()
    
    print(f"\n📁 Found {len(sorted_categories)} unique categories across {len(posts)} posts:\n")
    
    # Display categories with usage
    print("Category                     | Posts | Used In")
    print("-" * 50)
    for category, count in sorted_categories:
        posts_list = category_posts[category]
        posts_preview = ", ".join(posts_list[:2])
        if len(posts_list) > 2:
            posts_preview += f", ... (+{len(posts_list)-2} more)"
        print(f"{category:<28} | {count:^5} | {posts_preview}")
    
    # Category statistics
    print("\n📈 STATISTICS:")
    print(f"  • Total unique categories: {len(sorted_categories)}")
    print(f"  • Average categories per post: {sum(category_count.values()) / len(posts):.1f}")
    print(f"  • Most used category: {sorted_categories[0][0]} ({sorted_categories[0][1]} posts)")
    if len(sorted_categories) > 1:
        print(f"  • Least used category: {sorted_categories[-1][0]} ({sorted_categories[-1][1]} posts)")

def check_config_categories():
    """Check which categories are defined in config but not used in posts."""
    print("\n🔍 CONFIGURATION CHECK")
    print("=" * 50)
    
    # Get categories from posts
    posts = get_all_posts()
    used_categories = set()
    for post in posts:
        used_categories.update(extract_categories(post))
    
    # Check _quarto.yml for hardcoded categories
    config_categories = []
    try:
        with open('_quarto.yml', 'r') as f:
            content = f.read()
            # Look for category references in navbar
            if '#category=' in content:
                import re
                matches = re.findall(r'#category=([^\s\'"]+)', content)
                config_categories.extend(matches)
    except:
        pass
    
    if config_categories:
        print("\n📝 Categories referenced in _quarto.yml:")
        for cat in set(config_categories):
            status = "✅ Used" if cat in used_categories else "❌ Not used in any posts"
            print(f"  • {cat}: {status}")
    
    print("\n💡 TIP: Categories are dynamically populated from posts.")
    print("    Only categories with actual posts will appear in filters.")

def suggest_category_organization():
    """Suggest category organization and hierarchy."""
    print("\n💡 CATEGORY SUGGESTIONS")
    print("=" * 50)
    
    posts = get_all_posts()
    all_categories = []
    for post in posts:
        all_categories.extend(extract_categories(post))
    
    category_count = Counter(all_categories)
    
    # Suggest main categories vs tags
    main_threshold = 2  # Categories used in 2+ posts could be main categories
    
    main_categories = [cat for cat, count in category_count.items() if count >= main_threshold]
    tags = [cat for cat, count in category_count.items() if count < main_threshold]
    
    print("\n🏷️  Suggested Category Organization:\n")
    print("MAIN CATEGORIES (used frequently):")
    for cat in sorted(main_categories):
        print(f"  • {cat} ({category_count[cat]} posts)")
    
    if tags:
        print("\nTAGS (used sparingly, consider consolidating):")
        for tag in sorted(tags):
            print(f"  • {tag} ({category_count[tag]} post)")
    
    # Suggest groupings
    print("\n🔗 Suggested Category Groups:")
    
    # Group by common prefixes or themes
    math_cats = [c for c in category_count if 'Math' in c or 'Algebra' in c or 'Calculus' in c]
    ai_cats = [c for c in category_count if 'AI' in c or 'Learning' in c or 'Neural' in c]
    
    if math_cats:
        print(f"  Mathematics Group: {', '.join(math_cats)}")
    if ai_cats:
        print(f"  AI/ML Group: {', '.join(ai_cats)}")

def generate_category_json():
    """Generate a JSON file with category metadata for dynamic use."""
    posts = get_all_posts()
    category_info = defaultdict(lambda: {"count": 0, "posts": [], "description": ""})
    
    for post in posts:
        categories = extract_categories(post)
        for cat in categories:
            category_info[cat]["count"] += 1
            category_info[cat]["posts"].append(str(post))
    
    # Add descriptions (you can customize these)
    descriptions = {
        "Mathematics": "Pure and applied mathematical concepts",
        "AI": "Artificial Intelligence topics",
        "Machine Learning": "ML algorithms and applications",
        "Deep Learning": "Neural networks and deep architectures",
        "Philosophy": "Philosophical implications of technology",
        "History": "Historical perspectives on science and math",
        "Signal Processing": "Signals, systems, and transformations",
    }
    
    for cat in category_info:
        if cat in descriptions:
            category_info[cat]["description"] = descriptions[cat]
    
    # Save to JSON
    output_file = "_category_metadata.json"
    with open(output_file, 'w') as f:
        json.dump(dict(category_info), f, indent=2)
    
    print(f"\n✅ Category metadata saved to {output_file}")

def main():
    """Main function to run the category analysis."""
    import sys
    
    print("\n" + "=" * 50)
    print("    📚 BLOG CATEGORY MANAGER")
    print("=" * 50)
    
    # Analyze categories
    analyze_categories()
    
    # Check configuration
    check_config_categories()
    
    # Provide suggestions
    suggest_category_organization()
    
    # Generate metadata file
    if len(sys.argv) > 1 and sys.argv[1] == 'generate':
        generate_category_json()
    
    print("\n" + "=" * 50)
    print("\n✨ To add new topics/categories:")
    print("  1. Simply use them in your post's frontmatter")
    print("  2. They'll automatically appear in filter UI")
    print("  3. Update navbar in _quarto.yml for main topics")
    print("\n📝 See EXTENDING_BLOG.md for detailed instructions")

if __name__ == "__main__":
    main()
