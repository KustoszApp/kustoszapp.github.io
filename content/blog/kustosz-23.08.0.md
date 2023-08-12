---
author: "Mirek Długosz"
title: "Kustosz 23.08.0"
date: 2023-08-12
description: "Kustosz 23.08.0 release notes"
thumbnail: /thumbnails/post_23.08.0.png
---

I’m happy to announce immediate availability of Kustosz 23.08.0.

This is maintenance update that provides fixes around adding content.

Previously, tags field was ignored when adding article manually. Now tags are properly saved.

When content autodetection fails, correct error message is displayed in web UI.

In last released version, due to Celery update, content autodetection always failed. This is now fixed, as long as you use Celery 5.3.0 or newer.

Happy reading!
