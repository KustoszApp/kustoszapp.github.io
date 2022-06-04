---
author: "Mirek Długosz"
title: "Kustosz 22.06.0"
date: 2022-06-04
description: "Kustosz 22.06.0 release notes"
thumbnail: /thumbnails/post_22.06.0.png
---

I’m happy to announce immediate availability of Kustosz 22.06.0.

This release is all about making Kustosz easier to try and install.

[Container](https://docs.kustosz.org/en/stable/installation/containers.html) will automatically create new web user during start up. Now you can start the container with command below and immediately open [localhost:8000/ui/](http://localhost:8000/ui/) in the browser.

    docker run -p 127.0.0.1:8000:8000 quay.io/kustosz/app

Use `KUSTOSZ_USERNAME` and `KUSTOSZ_PASSWORD` to set username and password. When these variables are missing, user `admin` with random password will be created.

Additionally, if you pass `KUSTOSZ_IMPORT_CHANNELS_DIR` variable to container **and** ensure there's OPML file in specified directory, this OPML file will be imported during startup. You can get fully-working Kustosz instance along with some data thanks to one single command.

Read more on [container documentation page](https://docs.kustosz.org/en/stable/installation/containers.html).

If you are [Heroku](https://www.heroku.com/) customer, you can deploy Kustosz with single click on the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/KustoszApp/kustosz-heroku)

This Kustosz version is specially tailored to run on a **single dyno**. It can fit on a **free** tier, but we recommend using Hobby Basic tier for PostgreSQL database.

Read more on [Heroku documentation page](https://docs.kustosz.org/en/stable/installation/heroku.html).

Finally, we have initial version of [fully automated installer](https://docs.kustosz.org/en/stable/installation/vps-installer.html). Installer is designed to run on systems where you have superuser (root) access. Now you can spin up virtual machine in the cloud, assign it domain, run installer, and... that's it! Fully operational Kustosz instance will be available for you to use.

Read more on [automatic installation documentation page](https://docs.kustosz.org/en/stable/installation/vps-installer.html).

Happy reading!
