<!--
DESCRIPTION: Learn how to quickly create and deploy a static website using GitHub Pages with markdown and HTML support.
-->
[TOC]


# Github Pages

Suppose you want to create a static fluent website quickly that looks good across different devices. You know HTML but would also like to use markdown to speed up the content creation. If you have a Github account, then making a web site is easy using Github Pages.

# Steps

* Sign into your Github account, e.g. `https://github.com/USERNAME`
* Create a new repo, e.g. `https://github.com/USERNAME/repo1` - this repo1 will be the name of your web site.
* Clone the repo to a local folder and open it in Visual Code
* Create a file called `index.md` and put some markdown in it.
* Push to Github
* In Github for the selected repo, click Settings, Pages
* Wait a minute for the site to deploy.
* `https://USERNAME.github.io/repo1`

# Troubleshooting

## make sure you configure your 'user.name' and 'user.email' in git

You get this error when you try to push your local repo.

![alt text](/static/images/git-error-message.webp)

SOLUTION:

From the command line, run this:
```
git config --global user.name "Fred Flintstone"
git config --global user.email "fred@slate.com"
```

# References

* [GitHub Pages documentation](https://docs.github.com/en/pages)
* [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
* [YouTube Getting Started with GitHub Pages](https://www.youtube.com/watch?v=QyFcl_Fba-k)