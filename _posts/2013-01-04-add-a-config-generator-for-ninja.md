---
layout: post
title: "A little hacking on Ninja"
description: ""
category: 
tags: []
---
{% include JB/setup %}


### A Little hacking
我前段时间花了些时间来看Ninja这个开源项目，期间还是有一些收获。另外自己也做了一些修改，我希望有一个工具能帮忙生成Ninja的config(build.ninja)，现在的CMake和pyg都能做这个事情，但是我觉得稍微复杂了一点。很多时候我只是一些简单的几个文件的小项目，如果能有一个工具来分析代码然后生成build.ninja还是很方便的。所以我就做了一个Ninja的选项，使用方法是ninja -t config,当前的输出是打印到标准输出的，重定向以后就直接可以用了。当然如果你的项目用到了其他的一些库，还是需要稍微地修改一下的。

{% highlight sh %}
$ninja -t config >　build.ninja 
$ninja all  
//objects and executable file will output obj dir
{% endhighlight %}

其过程也很简单，就是分析当前项目的源码结构，最主要是找到main函数所在的源文件，其他的文件编译成为一个静态库，然后链接起来可执行文件。注意gcc(clang)的编译参数，这样才能使得某个头文件改变了重新编译所依赖的其他文件。源代码在这里可以。

###  Ninja代码的一些分析

Ninja 整个使用C++实现，一共1w行所有的代码。 

