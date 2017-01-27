---
title: Setting up HomeAssistant on a Raspberry Pi
author: Dr_c0w
layout: post
image:
  feature: ha-logo-history.png
date: 2017-01-27 18:43
categories: articles
tags: ['HomeAssistant']
---

## Introduction

The goal of this article is to show you how to use HomeAssistant and what it
is. I will not discuss how to configure HomeAssistant in this article, but this
will probably be the subject of another article.

HomeAssistant is a very cool project about home automation. The project is
open-source, and you can check it
[there](https://github.com/home-assistant/home-assistant). They also got a wiki
on how to configure your own assistant that can be found
[here](https://home-assistant.io/). HomeAssistant can be installed using
several alternate ways. For example, the first time I tried this tool, I
used their Docker container. In this article, I will show you how to
setup HomeAssistant on a dedicated Rasperry Pi.

But this article is also about setting up some cool stuff along
HomeAssistant. Indeed, I will show you how to control it from your iOS devices
through HomeKit. Right before that, I will tell you how to setup Mosquitto (a
lightweight MQTT server).

In this article I will mainly use Linux and its command line (it might also
work on MacOS). I will not cover the details in order to work with Windows, but
it is feasible :smile:.

## Installing HomeAssistant

In order to install HomeAssistant easily, we will use the HassBian image that
is available on [GitHub](https://github.com/home-assistant/pi-gen/releases).
Once the last available released is downloaded, you are able to unzip it.

If you want to download it directly from the command line, you can run the
following commands:

```
wget https://github.com/home-assistant/pi-gen/releases/download/v1.01/2017-01-21-HASSbian.zip
unzip 2017-01-21-HASSbian.zip
```

The URL and the name of the file to unzip might be changing so you should check
the repository beforehand.

After the file is unzipped, you obtain an IMG file. This file can be written on
the SD card with `dd` as in the following command:
```
dd bs=4M if=2017-01-11-raspbian-jessie.img of=/dev/sdd
```

You have to change the `if=...` in order to match the HASSbian image's name.
You should also check the name of the device. In my case, it was
`of=/dev/mmcblk0`. If you have issues with `dd`, I recommend using
`Win32DiskImager` (available on Windows :stuck_out_tongue_winking_eye:).

##  First boot

After this step, you can put the SD card back in the Raspberry Pi and power it
on. You will have to wait for a short time (1 to 5 minutes).

When it has finished booting up, you can access your Pi. If you are running an
UNIX-based system, you should be able to run the following command:
```
ssh pi@raspberrypi.local
```

If it does not work, you should check if your Raspberry Pi is connected to your
router. If you still cannot access your Pi this way, you have to get its IP
address through your router's interface.

The password corresponding to the user `pi` is `raspberry`.

## Update configuration

After the first successful connection to the Pi, I changed a little bit of
configuration on it. In order to avoid using all the password all the time, I
updated the configuration of SSH. The goal is to make it use the authorized
keys instead of passwords. This can be done by editing the file
`/etc/ssh/sshd_config`.

## Setting up Mosquitto

## Setting up HomeBridge

## Configuration of HomeBridge

## Enable HomeBridge at boot
