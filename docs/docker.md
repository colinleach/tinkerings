---
title: Docker
nav_order: 15
---

# {{ page.title }}

This page assumes we're talking about the (free) community edition, Docker CE. Anyone with the budget for the Enterprise Edition can also afford better advice than I can off.

## Installation

There is extensive advice on the [Docker website](https://docs.docker.com/install/). Docker Desktop is available for Windows (Pro/Enterprise only, not Home editions) and Mac.

Docker Engine is available (without the fancy GUI and Kubernetes integration) for many Linux versions. On Mint 19.2, the only problem was adding the apt repository: recent Mint versions seem to deviate from Ubuntu and give error messages. Leave out the `[arch=amd64]` bit and use the command below, perhaps changing `bionic` to match your upstream Ubuntu version (*not* the Mint version such as Tina).

```sh
sudo add-apt-repository "deb https://download.docker.com/linux/ubuntu bionic stable"
```

## Learning about Docker

There are plenty of thick, meaty books about this, a clue that there can be a lot to it.

The Docker website is good and detailed: [overview](https://docs.docker.com/engine/docker-overview/), [quickstart](https://docs.docker.com/get-started/) and plenty of other links in the menu panel.

Also *lots* of blog posts. These are just a few:
- Learn Enough Docker to be Useful: [part1](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b), [part 2](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8), [part 3](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5), [part 4](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e), [part 5](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421), [part 6](https://towardsdatascience.com/pump-up-the-volumes-data-in-docker-a21950a8cd8)
- Docker for Beginners: [docker-curriculum.com/(https://docker-curriculum.com/)]
