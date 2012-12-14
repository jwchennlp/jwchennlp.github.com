---
layout: post
title: "use clang autocomplete mode"
description: ""
category: 
tags: []
---
{% include JB/setup %}

在Emacs下自动补全总是个问题，对于同一个buffer内的基于symbol补全auto-complete-mode做得非常好了，但是因为没有进行代码的分析，所以像结构体的成员变量或者类的成员函数的补全是不可能的。当然你可能试过这个号称最智能的[GCCSence](http://cx4a.org/software/gccsense/),但是我觉得这个东西够复杂的，在使用之前还需要手动运行一个命令来用Gcc处理一遍，它还会把一些东西放在sqlite数据库里面。这大概是因为Gcc确实巨大无比不易扩展造成的。

最近切换到Mac下，因为在Mac OS X下编译器变成了Clang， Clang是基于LLVM的。LLVM对于分析代码是有比较方便的支持的，所以基于LLVM有各种分析源程序的工具了。今天突然想到那么会不会有个东西来作为Emacs的自动补全的后端，一搜果然有了这个[auto-complete-clang](https://github.com/mikeandmore/auto-complete-clang)，使用了一下非常的方便。其实看看其代码是在后面调用Clang的，比如在main.cc源文件里面写一些代码:

{% highlight cpp %}

    #include <string>
    #include <vector>
    using namespace std;
    
    class Demo{
    public:
        void print();
        void test();
    
    private:
        int value;
    };
    
    int main() {
        std::string s;
        Demo demo;
    
        demo.
    }
{% endhighlight %}


后端运行的命令其实是:
{% highlight sh %}
    cmd: clang -cc1 main.cc -fsyntax-only -code-completion-at main.cc:18:10
{% endhighlight %}

所得到的结果是:
{% highlight sh %}
    COMPLETION: Demo : Demo::
    COMPLETION: operator= : [#Demo &#]operator=(<#const Demo &#>)
    COMPLETION: print : [#void#]print()
    COMPLETION: test : [#void#]test()
    COMPLETION: value : [#int#]value
    COMPLETION: ~Demo : [#void#]~Demo()
{% endhighlight %}

auto-complete-clang做的事情就是把这个结果再展示出来，其实这条命令也做了语法检查的，所以加上一个语法检查的功能应该也是可以的。
