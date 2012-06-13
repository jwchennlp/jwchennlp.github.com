---
layout: post
title: "使用Jekyll和GitPage搭建博客"
description: "基于GitPage提供平台，使用jekyll来写博客，这是非常适合程序员的博客环境"
category: Notes
tags: [jekyll, git]

---

{% include JB/setup %}

## 为什么要折腾
折腾了几次终于把博客从wordpress搬到GitPage了，迁徙这事本来是够麻烦的，而且也比较无聊。不过最终还是抑制不住诱惑，这有下面几点点好处。

- - -

+ __编辑方便，专注写作__

  在线下编辑，可以随便选择自己喜欢的编辑器。当然wordpress也有离线编辑工具，不过Linux下我还没找到合适的，
我平常是用[Muse](http://mwolson.org/projects/EmacsMuse.html)生成html，然后再粘贴到站上。其实还好，
就是插入图片不方便。使用GitPage和Jekyll是完全的离线，你甚至都不需要离开终端就可以发布文章，一切都只是简单的git push而已。
写的过程中还可以用jekyll  --server预览最终排版。

+ __可以使用Github进行版本管理__
	
像写程序一样写日志，这对程序员吸引很大。

+ __简洁__
  
我喜欢这套是因为感觉一切都很简单,在_post目录下写markdown格式的文章，生成网页、push上去就发布了。页面也非常整洁，这对于一个以文字和代码为主要内容的站点来说最合适不过了。而且因为全是静态网页，所以打开的速度也非常快。

- - - 

## 折腾过程

- - - 

 这套工具适合程序员，而且也正在开发中，所以转移过程中会碰上一些问题。不过如果你懂一点Ruby，这些都还是比较好解决的。我是自己写了一点小程序转移图片。

 + 申请GitHub，这个不少程序员有，直接跳过
 
 + 安装Jekyll 在本地，可能会遇上ruby版本的问题，我的机子上是1.8.7，需要1.9.2，使用[rvm](https://rvm.io//）来解决，具体参考[这里](http://lanvige.iteye.com/blog/857501)。
 + 在建立yourname.github.com项目

 + 从wordpress迁徙，我使用wordpress.xml这个方法，跟换域名解析。

 具体参考[这里](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)[这里](http://vitobotta.com/how-to-migrate-from-wordpress-to-jekyll/)，你所需要的全在这里了。

