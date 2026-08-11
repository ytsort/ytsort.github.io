# ytsort.github.io

The marketing/install page for [YTSort](https://github.com/LunarWerxs/YTSort), served at
[ytsort.lunarwerx.com](https://ytsort.lunarwerx.com/). It is a single static `index.html`
(no build step) that offers the bookmarklet, the Tampermonkey userscript, and the Chrome
extension, plus a `?url=<playlist>` deep link that jumps straight to a sorted playlist on
YouTube.

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
