# ytsort.github.io

The marketing/install page for [YTSort](https://github.com/LunarWerxs/YTSort), served at
[ytsort.lunarwerx.com](https://ytsort.lunarwerx.com/). It is a single static `index.html`
(no build step) that offers the bookmarklet, the Tampermonkey userscript, and the Chrome
extension, plus a `?url=<playlist>` deep link that jumps straight to a sorted playlist on
YouTube.

[![Discord](https://img.shields.io/badge/Discord-join_the_community-5865F2?logo=discord&logoColor=white)](https://discord.gg/PsWpeNUzhk)

## Deploying

There is nothing to build. Edit `index.html` (and the `assets/` it references) and push to
`main`; GitHub Pages serves the repo directly, so a push is the deploy.

## Privacy / analytics

This page carries two small, first-party analytics mechanisms, both run by LunarWerx
(Connections' Studio), never a third party.

**Studio visit ping.** On page load, one fire-and-forget request goes to
`studio.connections.icu`. What it sends: a random visitor id kept in this browser's
`localStorage`, this page's build stamp, and, only when the visit came from another site,
that site's hostname (never the full referring URL, never anything you typed or clicked on
that other page). From that request, the server additionally derives and stores coarse
geolocation (country, region, city, timezone), the visiting network's ASN, browser locale,
and a truncated user agent string. It never stores your IP address. The request is skipped
entirely on `localhost` and `.local` hosts, and skipped entirely when your browser sends
**Do Not Track** or **Global Privacy Control**. Failures are silent and never retried, and
the ping can never block or slow down the page.

**ARGUS pixel.** The page also loads a small first-party analytics pixel
(`analytics.connections.icu`) for aggregate page-view counts. It honours Do Not Track and
Global Privacy Control the same way, and is skipped on `localhost`.

Neither mechanism uses cookies, and neither collects anything that identifies you
personally. For the extension/userscript's own privacy practices (what runs on YouTube
itself), see [PRIVACY.md](https://github.com/LunarWerxs/YTSort/blob/main/PRIVACY.md) in
the main YTSort repo.

## License

GPL-2.0, matching the parent [YTSort](https://github.com/LunarWerxs/YTSort) project. Not
affiliated with YouTube or Google.

## Checks

`scripts/copy-budget.mjs` runs in CI on every push that touches the page, and locally with
`node scripts/copy-budget.mjs`. It enforces two things the owner cares about:

- **No em-dashes in visitor-facing copy.** A hard zero. Use a comma, colon, semicolon or a
  full stop. Dashes inside `<style>` or `<script>` comments are ignored.
- **The page does not quietly grow back.** Length is a ratchet against the baseline in
  `scripts/copy-budget.json`, not a fixed bar, so the page may shrink freely and drift up a
  little. Cut copy on purpose? Re-record it with `node scripts/copy-budget.mjs --update` and
  commit the new baseline.

It measures what a visitor actually reads, so collapsed `<details>`, elements with a `hidden`
attribute and `<noscript>` do not count. A naive word count reads about three times high.

To see a change rather than measure it, use `~/.claude/tools/shot/shotpage.mjs`, which
screenshots the page with the scroll-reveal animations forced to their finished state.
