# Kaivalya Dabhadkar's Blog

A beautiful Quarto-based blog focused on Mathematics and Artificial Intelligence, featuring modern design and interactive content.

## 🚀 Features

- **Beautiful Design**: Modern, clean interface with gradient accents and smooth animations
- **Math Support**: Full LaTeX rendering for mathematical equations
- **Code Highlighting**: Syntax highlighting for multiple programming languages
- **Responsive Layout**: Mobile-friendly design that works on all devices
- **Categories & Tags**: Organized content with filterable categories
- **Search Functionality**: Built-in search to find content quickly
- **Comments**: Utterances integration for GitHub-based comments

## 📁 Project Structure

```
blog/
├── _quarto.yml           # Main configuration file
├── index.qmd             # Homepage
├── about.qmd             # About page
├── styles.css            # Custom CSS styles
├── theme-light.scss      # Light theme configuration
├── theme-dark.scss       # Dark theme configuration
├── profile.jpg           # Profile image
├── posts/                # Blog posts directory
│   ├── _metadata.yml     # Global post settings
│   ├── fourier-transform/
│   │   └── index.qmd     # Math concept post
│   └── transformers-explained/
│       └── index.qmd     # AI concept post
├── templates/            # Post templates
│   ├── POST_TEMPLATE.qmd # Basic post template
│   └── EXAMPLE_philosophy_post.qmd # Example for new topics
└── EXTENDING_BLOG.md     # Guide for extending the blog
```

## 🛠️ Setup & Installation

### Prerequisites

1. **Install Quarto**: Download and install from [quarto.org](https://quarto.org/docs/get-started/)
   ```bash
   # Ubuntu/Debian
   wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.549/quarto-1.4.549-linux-amd64.deb
   sudo dpkg -i quarto-1.4.549-linux-amd64.deb
   
   # macOS
   brew install quarto
   
   # Windows
   # Download installer from quarto.org
   ```

2. **Install Python dependencies** (optional, for code execution in posts):
   ```bash
   pip install jupyter matplotlib numpy pandas
   ```

### Building the Blog

1. **Preview locally** (with live reload):
   ```bash
   quarto preview
   ```
   This will open your blog at `http://localhost:4000`

2. **Build static site**:
   ```bash
   quarto render
   ```
   This creates the static site in `_site/` directory

## ✍️ Writing Posts

### Creating a New Post

1. Create a new directory in `posts/`:
   ```bash
   mkdir posts/my-new-post
   ```

2. Copy the template and customize it:
   ```bash
   cp templates/POST_TEMPLATE.qmd posts/my-new-post/index.qmd
   ```

3. Edit your post with the appropriate frontmatter:
   ```markdown
   ---
   title: "Your Post Title"
   subtitle: "Optional subtitle"
   author: "Kaivalya Dabhadkar"
   date: "2024-01-25"
   categories: [Mathematics, AI, Deep Learning]  # Choose relevant categories
   image: "thumbnail.jpg"  # Optional thumbnail
   draft: false  # Set to true to hide from listings
   toc: true
   ---
   
   ## Introduction
   
   Your content here...
   ```

### Writing Mathematics

Use LaTeX syntax for equations:

- **Inline math**: `$e^{i\pi} + 1 = 0$`
- **Display math**: 
  ```markdown
  $$
  \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
  $$
  ```

### Including Code

Use triple backticks with language specification:

````markdown
```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```
````

For executable code blocks:
````markdown
```{python}
#| echo: true
#| code-fold: true

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```
````

### Adding Images

Place images in your post directory and reference them:
```markdown
![Description](image.jpg)
```

### Using Callouts

Quarto supports various callout types:

```markdown
:::{.callout-note}
## Note Title
This is a note callout.
:::

:::{.callout-tip}
## Pro Tip
This is a tip callout.
:::

:::{.callout-warning}
## Warning
This is a warning callout.
:::

:::{.callout-important}
## Important
This is an important callout.
:::
```

## 🎨 Customization

### Modifying Themes

- Edit `theme-light.scss` for light mode colors
- Edit `theme-dark.scss` for dark mode colors
- Modify `styles.css` for custom styling

### Changing Navigation

Edit the `navbar` section in `_quarto.yml`:
```yaml
navbar:
  left:
    - text: "New Page"
      href: newpage.qmd
```

### Categories

Add new categories by using them in post frontmatter. They'll automatically appear in the filter UI.

## 🚀 Deployment

### GitHub Pages

1. Create a GitHub repository
2. Push your blog code
3. Enable GitHub Pages in repository settings
4. Add GitHub Actions workflow (`.github/workflows/publish.yml`):

```yaml
name: Publish Quarto Blog

on:
  push:
    branches: [main]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
```

### Netlify

1. Connect your GitHub repository to Netlify
2. Set build command: `quarto render`
3. Set publish directory: `_site`

### Custom Domain

Add a `CNAME` file in the root with your domain:
```
blog.yourdomain.com
```

## 📝 Tips for Writing

### For Mathematical Content

- Start with intuition before diving into formalism
- Use visualizations to explain complex concepts
- Provide concrete examples
- Include both theoretical and practical perspectives

### For AI/ML Content

- Include code implementations
- Explain the math behind algorithms
- Use diagrams for architecture visualization
- Provide practical applications and use cases

### General Best Practices

- Use descriptive titles and subtitles
- Include a compelling introduction
- Break content into digestible sections
- Add a conclusion summarizing key points
- Include references and further reading

## 🔧 Troubleshooting

### Common Issues

1. **LaTeX not rendering**: Ensure MathJax is properly loaded
2. **Images not showing**: Check file paths and extensions
3. **Dark mode not working**: Clear browser cache
4. **Build errors**: Run `quarto check` to diagnose

### Getting Help

- Quarto documentation: [quarto.org/docs](https://quarto.org/docs/websites/website-blog.html)
- Quarto discussions: [github.com/quarto-dev/quarto-cli/discussions](https://github.com/quarto-dev/quarto-cli/discussions)

## 📄 License

This blog template is open source. Feel free to use and modify it for your own blog!

## 🤝 Contributing

If you'd like to contribute posts or improvements:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📬 Contact

- GitHub: [@Kaivalya1997](https://github.com/Kaivalya1997)
- LinkedIn: [Kaivalya Dabhadkar](https://linkedin.com/in/kaivalya-dabhadkar-384a47151)

---

Happy blogging! 🎉 Feel free to reach out if you have any questions or suggestions.
