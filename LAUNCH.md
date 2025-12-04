# Launching the Sacred Smoke Website

This guide explains how to launch and develop the Sacred Smoke website locally and deploy it online.

## 🚀 Quick Start - Local Development

### Option 1: Using the Launch Script (Recommended)

Simply run the provided launch script:

```bash
./launch.sh
```

This will start a local web server on port 8000. Visit http://localhost:8000 in your browser.

To use a different port:

```bash
./launch.sh 3000
```

### Option 2: Manual Launch

If you prefer to launch manually, use Python's built-in HTTP server:

```bash
python3 -m http.server 8000
```

Then open your browser to http://localhost:8000

### Option 3: Using Node.js

If you have Node.js installed, you can use `npx`:

```bash
npx http-server -p 8000
```

Or install and use `live-server` for auto-reload:

```bash
npm install -g live-server
live-server --port=8000
```

## 🌐 Online Deployment

### GitHub Pages (Automatic)

The repository is configured to automatically deploy to GitHub Pages when you push to the `main` branch.

1. **Enable GitHub Pages** in repository settings:
   - Go to Settings → Pages
   - Under "Source", select "GitHub Actions"

2. **Push to main branch**:
   ```bash
   git push origin main
   ```

3. **Access your site**:
   - Your site will be available at: `https://scaredsmoke-star.github.io/Sacred-smoke/`
   - Check the Actions tab for deployment status

### Manual GitHub Pages Setup

Alternatively, you can use the classic GitHub Pages approach:

1. Go to Settings → Pages
2. Under "Source", select "Deploy from a branch"
3. Choose `main` branch and `/ (root)` folder
4. Click Save

### Other Deployment Options

#### Netlify

1. Create a free account at [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub repository
4. Deploy settings:
   - Build command: (leave empty)
   - Publish directory: `.`
5. Click "Deploy site"

#### Vercel

1. Create a free account at [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Deploy with default settings

## 📝 Development

### File Structure

```
Sacred-smoke/
├── index.html          # Main website (already styled and ready)
├── launch.sh          # Quick launch script
├── README.md          # Project documentation
├── QUICKSTART.md      # Quick reference guide
├── docs/              # Additional documentation
├── examples/          # Python examples
└── .github/
    └── workflows/
        └── deploy-pages.yml  # GitHub Pages deployment
```

### Making Changes

1. **Edit the website**: Modify `index.html` to customize the site
2. **Test locally**: Run `./launch.sh` to preview your changes
3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update website"
   git push
   ```

### Customization Tips

The `index.html` file is a self-contained static website with:
- Embedded CSS styling (purple gradient theme)
- Responsive design for mobile devices
- Feature cards and quick start guide
- Download buttons and documentation links

To customize:
- **Colors**: Change the gradient in the `body` style (lines 18-19)
- **Content**: Update text directly in the HTML
- **Layout**: Modify the CSS grid and flexbox properties
- **Add pages**: Create new HTML files and link them

## 🛠️ Troubleshooting

### Port Already in Use

If port 8000 is already in use, try a different port:

```bash
./launch.sh 8080
```

### Permission Denied

Make sure the launch script is executable:

```bash
chmod +x launch.sh
```

### Python Not Found

Install Python 3:
- **Ubuntu/Termux**: `apt install python3`
- **macOS**: `brew install python3`
- **Windows**: Download from [python.org](https://python.org)

## 📚 Next Steps

- View the live site locally to see your changes
- Customize the design and content as needed
- Deploy to GitHub Pages for free hosting
- Share your site URL with others

## 🔗 Resources

- [GitHub Pages Documentation](https://docs.github.com/pages)
- [Python HTTP Server](https://docs.python.org/3/library/http.server.html)
- [HTML/CSS Basics](https://developer.mozilla.org/en-US/docs/Learn)

---

**Happy building!** 🔥
