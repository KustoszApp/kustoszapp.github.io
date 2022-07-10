---
author: "Mirek Długosz"
title: "Kustosz 22.07.0"
date: 2022-07-10
description: "Kustosz 22.07.0 release notes"
thumbnail: /thumbnails/post_22.07.0.png
---

I’m happy to announce immediate availability of Kustosz 22.07.0.

The main feature of this release is content autodetection.

In previous releases, adding new content to Kustosz was a little hard.
If you have found an interesting site that you wanted to subscribe to, you needed to find full URL of RSS / Atom feed.
In many cases, that required checking HTML code of the page, which is especially hard to do on mobile devices.
Adding specific article required SSH client or obtaining Kustosz authorization token, which was only visible in browser development tools.

Now, all you have to do is click the "Add content" button on top of navigation pane.
Just paste the URL that you have - be it a specific article or the main page of the website - and let Kustosz detect article and RSS / Atom feeds for you.
If you are unsure which of multiple channels you want to add, click a channel name to reveal few of the latest articles published by this channel.

{{< figure src="/screenshots/22.07.0-content-autodetection.png" caption="Kustosz 22.07.0 - content autodetection" >}}

The old way of adding channels is still available - click down arrow right next to "Add content" and click "Add channel".

There's also new form, available after clicking "Add article".
It allows you to quickly add specific link without checking site for possible RSS / Atom feeds.
It is especially handy if you use Kustosz as bookmark manager, or when you want to add link to PDF file.

What's more, adding content without visiting Kustosz is now easier to set up.
There's a bookmarklet link at the bottom of "Settings" page.
It's ready to be used on any page that you visit, as it already includes token!

While you are at "Settings" page, you will notice many more changes.

One is ability to choose between Light and Dark theme.

{{< gallery hover-effect="none" caption-effect="appear" >}}
    {{< figure src="/screenshots/22.07.0-dark-theme-main-page.png" caption="Kustosz 22.07.0 - main page in dark mode" >}}
    {{< figure src="/screenshots/22.07.0-dark-theme-reading.png" caption="Kustosz 22.07.0 - reading article in dark mode" >}}
    {{< figure src="/screenshots/22.07.0-dark-theme-editing-channel.png" caption="Kustosz 22.07.0 - editing channel window in dark mode" >}}
{{< /gallery >}}

You can choose when, if ever, entries should be marked as read automatically.
Available options are: upon opening entry, when entry has been opened for few seconds, and after you have read some part of the article.

Another new option tells Kustosz to always scroll article to top of the page upon opening.
Unchecking it will retain previous behavior, where only articles at the bottom half of the screen are scrolled up.

In the past, creating new filter required you to fill the entire form.
That was a little annoying when you wanted to create filter similar to one that you already have, i.e. one looking for another text in article title.
Now this task is easier, thanks to new "Copy filter" button.

Finally, this version introduces two new search fields: `reading_time` and `reader_position`.
They make it easier to find long (or short!) articles to read, as well as articles that you have started reading, but didn't finish.

Happy reading!

{{< load-photoswipe >}}
