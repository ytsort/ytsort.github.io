# YTSort site

> Marketing/install site for YTSort, a tool that reorders any YouTube playlist you own by video length in seconds.

<!-- odin:about HAND-OWNED above the GENERATED marker. Edit freely; `odin codex about --ingest` carries it back into Odin's Codex. -->

## What it is

A marketing and installation page for YTSort, a YouTube playlist sorting tool. Served as a static site via GitHub Pages at ytsort.lunarwerx.com, it presents three installation methods (bookmarklet, userscript, browser extension) and deep-link support to sort playlists directly from a URL parameter.

## Things not to forget

_The intricacies worth remembering: the gotchas, the half-built parts, the decisions whose
reason lives nowhere else. Odin never overwrites this section._

- The bookmarklet is the recommended zero-maintenance path on purpose: it fetches ytsort2.user.js fresh from raw.githubusercontent.com on every click (cache: 'no-cache') and evals it, wrapped in a trustedTypes policy when available, so it always runs the latest version with nothing to update - do not 'simplify' this into a pinned/cached copy, that would defeat the whole design. anchors: `index.html:516`
- The ?url=<playlist-id-or-url> deep link is parsed and redirected in a script placed in <head>, deliberately before DOMContentLoaded, so a shared/bookmarked link redirects to YouTube before the landing page paints; the actual sign-in check and sort happen on YouTube via the installed userscript/extension, not on this site. anchors: `index.html:16`
- Analytics is two separate first-party pings (ARGUS pixel plus a Studio Connections visit ping), both deliberately self-throttled: the ARGUS key is a public ingest key meant to ship in client JS, it honors DNT/Sec-GPC itself, is grant-by-default outside EU/EEA/UK/CH, and skips localhost/127.0.0.1/.local hosts so local previews cannot inflate numbers. anchors: `index.html:242`
- The FAQ content is written twice on purpose: nine Q&A cards rendered visibly on the page and the same content duplicated into FAQPage JSON-LD schema, so editing one without the other will desync what users see from what search engines/AI answer engines read. anchors: `index.html:368`
- The site publishes llms.txt, llms-full.txt and a machine-readable pricing.md specifically so AI answer engines/agents can read the product summary and pricing terms without scraping the HTML - these are separate files that need updating in lockstep with index.html copy changes. anchors: `llms.txt:1`
- sitemap.xml has hardcoded lastmod dates (e.g. 2026-08-23) with no build step or workflow to regenerate them on deploy, so they silently go stale after every content push; there is no CI automation for this yet. anchors: `sitemap.xml:5`
- This is a pure static site with no build step - edits go straight into index.html and a push to main deploys via GitHub Pages, so there is no compilation step to catch mistakes before they go live. anchors: `index.html:1`
- The comparison section exists to pre-empt the objection 'why not just use YouTube's own sort or drag manually' by naming exactly where those two alternatives fall short, so it should stay pointed at real competing options rather than becoming generic feature marketing. anchors: `index.html:631`

<!-- odin:about GENERATED BEGIN - rewritten by `odin codex about --publish`; edit the Codex, not this -->

## What Odin knows about this project

Everything from here down is generated from this project's Codex dossier
(`codex/projects/ytsort-github-io.md` in the Odin clone) and is **rewritten on every publish** -
edit the dossier, not this block. Everything ABOVE the marker is yours.

### At a glance

- **Ships as:** static site - GitHub Pages (ytsort.lunarwerx.com)
- **Live at:** https://ytsort.lunarwerx.com
- **Entry points:** `site_root`
- **Deploys via:** github-pages
- **Domain:** YouTube, playlist sorting, duration filtering, bookmarklet, userscript, browser extension, free tool
- **Remote:** https://github.com/ytsort/ytsort.github.io.git

### Architecture

- `index.html` - Single-page marketing site with sticky nav, hero section, three installation option cards, features grid, usage guide, deep-link documentation, FAQ schema markup, and first-party analytics integration
- `assets/` - Static images and visual assets: logo, icon, screenshots of YTSort UI, and OG image for social sharing
- `docs/` - Documentation index and todo folder for open project work

### Features

12 recorded - 12 shipped, 0 partial, 0 planned. Each `path:line` is where the feature is DEFINED, checked by `odin codex check`.

**Shipped**

- **Bookmarklet installation** - Drag-to-bookmarks button that fetches and runs YTSort from GitHub on demand, always current with zero maintenance. - `index.html:474`, `index.html:516`
- **Userscript installation** - Link to Greasy Fork for Tampermonkey or Violentmonkey installation with automatic background updates. - `index.html:480`, `index.html:529`
- **Chrome/Edge extension** - Zero-permission extension available via Chrome Web Store, seamlessly integrated into Chrome and Edge browsers. - `index.html:484`, `index.html:538`
- **Playlist deep linking** - Query parameter ?url=<playlist-id-or-url> redirects to YouTube and auto-triggers sorting on page load. - `index.html:16`, `index.html:591`
- **Installation instructions** - Step-by-step visual guide: set playlist to Manual mode, open YTSort panel, pick sort direction, apply changes. - `index.html:570`, `index.html:578`
- **Feature showcase** - Grid of YTSort capabilities: fast reordering, verification, dry-run preview, duration filters, stats export, theme matching, drag fallback. - `index.html:551`, `index.html:566`
- **Analytics tracking** - First-party ARGUS pixel and Studio visit ping for page traffic, honors Do Not Track and Global Privacy Control. - `index.html:242`, `index.html:282`, `index.html:764`
- **Responsive design** - Sticky navigation with mobile-responsive menu collapse and hero/content sections that scale fluidly to viewport. - `index.html:71`, `index.html:84`
- **FAQ section** - Nine rendered question-and-answer cards (pricing, accounts, usage steps, install methods, deep links, speed, safety, offline behavior) visible on the page itself, not just embedded in schema.org markup. - `index.html:656`, `index.html:662`
- **Comparison section** - Three-card comparison of YTSort against YouTube's built-in sort, other extensions/scripts, and manual dragging, explaining where each falls short. - `index.html:631`, `index.html:636`
- **Screenshot gallery** - 'A look inside' section showing three product screenshots (dark-mode panel, settings, duration stats). - `index.html:619`
- **AI-agent readable content (llms.txt / pricing.md)** - Publishes llms.txt, llms-full.txt, and a machine-readable pricing.md so AI answer engines/agents can read the product summary and pricing terms without scraping the HTML. - `llms.txt:1`, `pricing.md:1`

### Where to add a new one

- **a new installation method card** - Add a .card div to the .cards grid in the #install section following the structure of existing cards anchors: `index.html:508`
- **a new feature item in the grid** - Add a .feat-item div to the .feats grid in the #features section with emoji icon, heading, and description anchors: `index.html:556`
- **a new instruction step** - Add a .step div to the .steps grid in the #how section with numbered step counter and description anchors: `index.html:574`
- **new deep-link documentation or examples** - Extend the #link section by adding cards or documentation rows for additional ?url parameter examples anchors: `index.html:593`
- **new analytics or tracking mechanism** - Add or modify tracking script in <head>, extend ARGUS configuration, or add new measurement pixel anchors: `index.html:247`, `index.html:282`

### Gaps and wants

_Withheld: this repository is public, and the gap list is not published outside the private index._
_Read it with `python odin.py codex brief ytsort-github-io` in the Odin clone._

---

_Generated by `odin codex about --publish ytsort-github-io` on 2026-09-09 from a Codex dossier stamped 2026-09-04. Regenerate after the product moves; `odin codex about` reports drift._
<!-- odin:about GENERATED END sha=37a42b14a37b -->
