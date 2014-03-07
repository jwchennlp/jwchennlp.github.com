---
layout: post
title: "关于随机数"
description: ""
category:
tags: [Programming, Algorithms]
---

随机数在计算机中广泛使用，比如用作加密的key、密码的生成、模拟，扑克游戏中，还有一些经典的算法(比如[Monte Carlo](http://en.wikipedia.org/wiki/Monte_Carlo_method))依赖随机数的产生。



## 随机数产生，真随机和伪随机
随机数的产生和使用也是一个很有趣的问题。
我们希望只通过计算机来产生随机数的时候会有一些困难，计算机擅长做确定的事情，按照制定的指令去依次执行。
有两种大的产生随机数的方法，真随机数和伪随机数，这两种有各自的优点和缺点。


伪随机数生成器(PRNG)，顾名思义产生的不是严格意义上的随机数，一般是通过一些数学公式(或者计算好的表)来产生。比如简单的[Linear congruential generator](http://en.wikipedia.org/wiki/Linear_congruential_generator)，可以用来产生伪随机数。伪随机数的行为是可被预测的，但是在统计意义上来说是随机的，所以使用范围有限，比如一些模拟程序。而且伪随机数有可能出现固定的周期，比如下面这幅图是通过Windows下面的PHP的伪随机数生成器产生的，可以清楚地看到规律可循。http://www.random.org/analysis/#visual


真随机数生成器(RNG)，通过向计算机中引入一些不可预测的物理信息，比如键盘敲击和鼠标移动等。所以真随机数才是很难预测的或者根本来说不可预测。每个操作系统的实现有各自的区别。
比如Linux中产生随机数引入了物理噪音作为输入，比如mac地址可以用来初始化entropy pool，随机源可以加入中断时间，硬盘的寻址时间等等。
接口是/dev/random、/dev/urandom、get_random_bytes()，其中get_random_bytes在内核中使用。
/dev/random和/dev/urandom的区别是/dev/random强度更大并且是阻塞的，因为要收集更多熵。



## 随机数的使用

涉及到随机数的程序要特别小心。比如一个很简单的程序，我们知道C语言中的rand()产生的随机数是有范围的，0～600535，如果我要生成范围在0～10的随机数如何做？
可能你会简单认为:

{% highlight cpp %}
int my_rand() {
    return rand() % 10;
}
{% endhighlight %}

但是这真的是随机的吗?如果你把0～600535的所有数字依次%10，统计一下可以发现有的数出现的次数要大一些，因此最后出现某些数的概率相应的要大一些。

另外一个思考题：
产生随机数。


## 一些好玩的东西

摘自《思维的乐趣》一群同事围在一起，如何在不知道每个人工资的情况下得出大家的平均工资？这个简单的模型就是网络加密协议









{% include JB/setup %}
