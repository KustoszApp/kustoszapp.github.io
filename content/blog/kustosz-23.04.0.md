---
author: "Mirek Długosz"
title: "Kustosz 23.04.0"
date: 2023-04-10
description: "Kustosz 23.04.0 release notes"
thumbnail: /thumbnails/post_23.04.0.png
---

I’m happy to announce immediate availability of Kustosz 23.04.0.

This is maintenance update that brings latest ecosystem improvements to Kustosz users.

Kustosz has been verified against Django 4.2. This is newest LTS release that will be supported until April 2026, providing us with stable and safe foundation for years to come. One of notable improvements, included in Django 4.0, is native Redis cache backend.

We have also verified our codebase against Python 3.11, which is on average 25% faster than previous versions.

node-readability script has been verified against Node.js 18.

[Container image](https://docs.kustosz.org/en/stable/installation/containers.html) and [automated installer](https://docs.kustosz.org/en/stable/installation/vps-installer.html) have been updated to use and provide Django 4.2, Python 3.11 and Node.js 18, allowing users to smoothly transition into newest baseline. Users who are not yet ready to upgrade their running environment can still use older Django (down to 3.2), Python (down to 3.9) and Node.js (down to 16) versions, as long as they are supported upstream.

Happy reading!
