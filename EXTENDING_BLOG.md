---
search: false
---

# 📚 How to Extend This Blog

This guide shows you how to add new topics, categories, and customize your blog.

## 🎯 Adding New Topics/Categories

### Step 1: Update Navigation (_quarto.yml)

Add new topic sections to the navbar in `_quarto.yml`:

```yaml
navbar:
  left:
    - text: "Home"
      href: index.qmd
    - text: "Mathematics"
      href: posts.qmd#category=Mathematics
    - text: "AI & ML"
      href: posts.qmd#category=AI
    # ADD YOUR NEW TOPIC HERE:
    - text: "Philosophy"
      href: posts.qmd#category=Philosophy
    - text: "History"
      href: posts.qmd#category=History
```

### Step 2: Update Homepage (index.qmd)

Add your new topic to the list in `index.qmd`:

```markdown
### Current Topics:
- **📐 Mathematics**: Deep dives into pure and applied mathematics
- **🤖 AI & Machine Learning**: Explorations of neural networks
- **🤔 Philosophy**: Philosophical implications of technology  # NEW
- **📚 History**: Historical perspectives on science        # NEW
```

### Step 3: Update About Page (about.qmd)

Add your interests in the new topics:

```markdown
#### 🤔 Philosophy
- Philosophy of Mind and AI Consciousness
- Ethics in Technology
- Epistemology and Knowledge Representation
```

## 📝 Available Categories

Categories are **automatically populated** from your posts. Simply use any of these (or create new ones) in your post's frontmatter:

### Current Categories:
- **Mathematics** - Pure and applied math topics
- **AI** - Artificial Intelligence
- **Machine Learning** - ML algorithms and theory
- **Deep Learning** - Neural networks, architectures
- **NLP** - Natural Language Processing
- **Signal Processing** - Signals and systems
- **Applied Math** - Practical mathematical applications
- **Statistics** - Statistical theory and methods
- **Algorithms** - Algorithm design and analysis

### Suggested New Categories:
```yaml
# For Philosophy posts:
categories: [Philosophy, Ethics, AI Ethics]

# For History posts:
categories: [History, History of Science, Mathematics History]

# For Physics posts:
categories: [Physics, Quantum Computing, Theoretical Physics]

# For Creative posts:
categories: [Creative Coding, Generative Art, Visualization]
```

## 🆕 Creating a New Post

### Quick Start:
```bash
# Create new post directory
mkdir posts/your-post-name

# Copy template
cp templates/POST_TEMPLATE.qmd posts/your-post-name/index.qmd

# Edit the post
nano posts/your-post-name/index.qmd
```

### Post Frontmatter Template:
```yaml
---
title: "Your Compelling Title Here"
subtitle: "A brief subtitle that expands on the title"
author: "Your Name"
date: "2024-01-25"  # Use format YYYY-MM-DD
categories: [Main Category, Subcategory, Another Tag]
image: "thumbnail.jpg"  # Optional: post thumbnail
draft: false  # Set to true to hide from listings
toc: true  # Table of contents
number-sections: true  # Number the sections
highlight-style: github  # Code highlighting theme
format:
  html:
    code-fold: true
    code-summary: "Show code"
execute:
  echo: true
  warning: false
  eval: false  # Set to true if you want code to execute
---
```

## 🎨 Customizing Appearance

### Adding Category Colors

Edit `styles.css` to add custom colors for new categories:

```css
/* Custom category colors */
.quarto-category[data-category="Philosophy"] {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.quarto-category[data-category="History"] {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}
```

### Custom Icons for Topics

In your posts or homepage, use emoji or icons:

```markdown
- **🤔 Philosophy**: Deep questions about mind and consciousness
- **📚 History**: Journey through the history of ideas
- **🔬 Physics**: Understanding the universe
- **🎨 Creative**: Artistic explorations with code
```

## 📊 Dynamic Category Behavior

Categories are **dynamically populated** - they only appear in filters when posts exist with those categories. This means:

- ✅ No empty categories in your filter UI
- ✅ Categories automatically appear when you add posts
- ✅ Clean, relevant navigation

## 🔧 Advanced Customization

### Multi-language Posts
```yaml
# In post frontmatter
lang: es  # Spanish post
# or
lang: fr  # French post
```

### Series of Posts
```yaml
# Link related posts
series: "Introduction to Category Theory"
series-order: 1
```

### Custom Layouts
```yaml
# Different layout options
page-layout: article  # Default
page-layout: full     # Full width
page-layout: custom   # Custom layout
```

## 📁 File Structure for New Topics

```
posts/
├── mathematics/          # Math posts
│   └── fourier-transform/
├── ai-ml/               # AI posts
│   └── transformers-explained/
├── philosophy/          # NEW: Philosophy posts
│   ├── ai-consciousness/
│   └── ethics-in-tech/
├── history/            # NEW: History posts
│   ├── history-of-calculus/
│   └── turing-biography/

templates/               # Templates for new content
├── POST_TEMPLATE.qmd   # Basic post template
└── EXAMPLE_philosophy_post.qmd  # Example philosophy post
```

## 🚀 Deployment Considerations

When adding new topics:

1. **Test locally** with `quarto preview`
2. **Check responsive design** on mobile
3. **Verify math rendering** if using equations
4. **Update README** with new topics
5. **Tag appropriately** for better discoverability

## 💡 Tips

1. **Consistent Categories**: Use consistent naming (e.g., always "Machine Learning" not "ML" sometimes)
2. **Meaningful Tags**: Categories should be meaningful to readers
3. **Limit Categories**: 3-5 categories per post is optimal
4. **Cross-reference**: Link between related posts
5. **Update Regularly**: Keep your topic list current

## 🤝 Need Help?

- Check Quarto docs: https://quarto.org/docs/websites/website-blog.html
- Review existing posts for examples
- Test changes with `quarto preview` before publishing
