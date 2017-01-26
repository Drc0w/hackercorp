# HackerCorp

Hello World!

We are the HackerCorp team. The name has nothing to do with our activities, we
just enjoy to write articles on things we enjoy. This is mainly around
programming or playing with some boards. Recently, we decided to open-source
our articles on GitHub, but you can check the result on
[our blog](https://www.hackercorp.eu).

## Information about this repo

This repo uses [`Jekyll`](https://github.com/jekyll/jekyll). All articles are
generated from `Markdown` files. The theme used in our blog is
[`So Simple Theme`](https://github.com/mmistakes/so-simple-theme).

## So Simple Theme

Looking for a simple, responsive, theme for your Jekyll powered blog? Well look no further. Here be **So Simple Theme**, the followup to [**Minimal Mistakes**](http://mmistakes.github.io/minimal-mistakes/) -- by designer slash illustrator [Michael Rose](http://mademistakes.com).

### Notable features:

* Compatible with Jekyll 3 and GitHub Pages.
* Responsive templates. Looks good on mobile, tablet, and desktop devices.
* Gracefully degrading in older browsers. Compatible with Internet Explorer 9+ and all modern browsers.
* Minimal embellishments and subtle animations.
* Optional large feature images for posts and pages.
* [Custom 404 page](http://mmistakes.github.io/so-simple-theme/404.html) to get you started.
* Basic [search capabilities](https://github.com/mathaywarduk/jekyll-search)
* Support for Disqus Comments

![screenshot of So Simple Theme](http://mmistakes.github.io/so-simple-theme/images/so-simple-theme-preview.jpg)

See a [live version of So Simple](http://mmistakes.github.io/so-simple-theme/) hosted on GitHub.

## Jekyll

In order to write new articles, you should before read the docs from `Jekyll`
website.

## Setup your environment

First you have to install `bundler` :

```
gem install bundler
```

Then, you can go to the cloned repository and run:
```
bundler install
```

Once it is done, you can use:
```
bundler exec jekyll build
```
in order to render the result. The output is located in `_site`.

You can also call:
```
bundler exec jekyll serve
```
After this command, you can open your web browser on `localhost:4000`.
