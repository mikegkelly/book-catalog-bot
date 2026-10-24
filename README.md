# Book Catalog: a Grok Bot template

A one-page website that shows off the free **Book Catalog** Grok Bot template: take a photo of your shelf and get a cataloged, valued, searchable library.

**Live site:** https://mikegkelly.github.io/book-catalog-bot/

It's plain HTML and CSS: no build step, no trackers, no outside fonts or scripts. GitHub Pages publishes it straight from the `main` branch.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole page (text, styles and the button code). |
| `og-image.png` | The 1200×630 preview picture X and other apps show when the link is shared. |
| `make_og.py` | Rebuilds `og-image.png` (needs Python with Pillow: `python3 make_og.py`). |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is. |

## Setting the "Get the template" link

Until the template link exists, both "Get the template" buttons say **Coming soon**. To turn them on:

1. Open `index.html` on GitHub and click the pencil (Edit) icon.
2. Near the very top, find this line:
   ```js
   const TEMPLATE_URL = "#";
   ```
3. Replace `#` with the template link, keeping the quotes:
   ```js
   const TEMPLATE_URL = "https://your-template-link-here";
   ```
4. Click **Commit changes**. The site updates in a minute or two.

That's the only place the link lives. Both buttons read it.

## Changing the text

Everything readable is in `index.html`. Edit the words between the tags and commit; Pages republishes automatically.

## Unpublishing

- **Take the site offline but keep the files:** on GitHub, go to the repo's **Settings > Pages** and click **Unpublish site**.
- **Remove everything:** **Settings > General > Danger Zone > Delete this repository**. This can't be undone.

Made with Grok Bot.
