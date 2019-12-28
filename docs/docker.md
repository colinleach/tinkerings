---
title: Docker
nav_order: 15
---

# {{ page.title }}

This page assumes we're talking about the (free) community edition, Docker CE. Anyone with the budget for the Enterprise Edition can also afford better advice than I can off.

## Installation
There is extensive advice on the [Docker website](https://docs.docker.com/install/). Docker Desktop is available for Windows and Mac, though I gave up on the Windows version when it wanted to obliterate my VirtualBox installation.

Docker Engine is available (without the fancy GUI) for many Linux versions. On Mint 19.2, the only problem was adding the apt repository: recent Mint versions seem to deviate from Ubuntu and give error messages. Leave out the `[arch=amd64]` bit and use the command below, perhaps changing `bionic` to match your upstream Ubuntu version (*not* the Mint version such as Tina).

```sh
sudo add-apt-repository "deb https://download.docker.com/linux/ubuntu bionic stable"
```


[Learn Enough Docker to be Useful](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)