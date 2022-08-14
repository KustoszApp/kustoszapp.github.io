---
author: "Mirek Długosz"
title: "Kustosz 22.08.0"
date: 2022-08-14
description: "Kustosz 22.08.0 release notes"
thumbnail: /thumbnails/post_22.08.0.png
---

I’m happy to announce immediate availability of Kustosz 22.08.0.

This is small release that introduces one new feature - [OPML](https://en.wikipedia.org/wiki/OPML) export.

Kustosz promises you control over your data, and we are serious about this promise.
It also means that it should be easy to move away from Kustosz, if you decide it's not for you or you want to try out another tool.
With OPML export, this is easier than ever.

OPML is standard file format to store list of subscribed RSS / Atom channels.
Most feed readers have the ability to import OPML file.

There are two ways to export your channels into OPML file.
One is through web UI.
Click “Settings” at the bottom of navigation panel and scroll down to “Export data” section.
Then, click “Export channels as OPML” button.

Alternatively, use following command on a machine where Kustosz is installed:

    kustosz-manager export_channels --file /path/to/file.xml

If `file.xml` already exists and you want to overwrite it, pass `--force` flag.

Happy reading!
