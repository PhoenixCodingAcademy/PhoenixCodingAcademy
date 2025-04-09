<!--
DESCRIPTION: Learn how to install and run MediaWiki, the free and open-source wiki software that powers Wikipedia, using Docker containers.
-->
[TOC]


```dos
docker pull mediawiki
docker run --name some-mediawiki -p 8080:80 -d mediawiki
```