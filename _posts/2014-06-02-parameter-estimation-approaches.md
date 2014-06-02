---
layout: post
title: "参数评估方法"
modified: 2014-06-02 21:27:24 +0800
tags: [参数评估,主题模型,极大似然估计,最大后验,贝叶斯估计]
image:
  feature: abstract-3.jpg
  credit: dargadgetz
  creditlink: http://www.dargadgetz.com/ios-7-abstract-wallpaper-pack-for-iphone-5-and-ipod-touch-retina/
comments: true
share: true 
---

pLSA和LDA主题模型是当前统计自然语言处理领域非常热门的问题,这些主题模型一般都是对文本的生成过程提出自己的概率图模型,然后利用已有的文本数据做参数评估.本文主要介绍其中会用到的三种参数评估方法,包括极大似然估计(MLE),最大后验(MAL)和贝叶斯估计.	

我们主要考虑两个推理问题:		

(1). 评估参数$\theta$的值以最好的拟合观察到的数据集X.		
(2). 根据已观测到的数据集X计算新的观察值$\widetilde x$的概率		

第一个问题可以看成是估计问题,第二个问题可以看成是预测或是回归问题.		theta
在贝叶斯统计中,参数估计问题可以表述为:		

$$p(\theta｜X) = \frac{p(\theta)p(X｜\theta)}{p(X)}$$	

并且我们可以用如下术语定义:

$$posterior=\frac{likelihood*prior}{evidence}$$

##1.极大似然估计(MLE)		
---------------

极大似然估计主要是求使似然函数值最大的参数值($\theta$),似然函数为:		

$$L(\theta｜X) = \prod_{x\in X}p(x｜\theta)$$		

对似然函数取对数并另偏导数为0,则可求得参数的解:		

$$\theta_{ML} = argmax_{\theta}L(\theta｜X) = argmax_{\theta}\sum_{x\in X}\log{p(x｜\theta)}$$

对上述函数关于参数$\theta_k$求偏导并是的偏导值为0:		

$$\frac{\partial L(\theta｜X)}{\partial \theta_k} = 0, \forall \theta_k\in theta$$		

根据已观测到的数据集X计算新的观察值$\widetilde x$的概率为:		

![image](../images/140530/mle.png)

以抛硬币的贝努利实验为例,每次抛硬币时正面出现的概率为p(未知),假设进行抛硬币N次得到结果集合C.用极大似然估计来求解参数p:		

$$l(p)=\sum_{i=1}^N\log{p(C=c_i｜p)} \\
	  =n^{(1)}log{p(C=1｜p)}	+n^{(0)}log{p(C=0｜p)} \\
	  =n^{(1)}log{p}+n^{(0)}log{(1-p)}$$		

其中$n^{(1)}表示N次实验结果中正面出现的次数,n^{(0)}$表示反面出现的次数.对似然函数求偏导得:		

$$\frac{\partial l}{\partial p} = \frac{n^{(1)}}{p}-\frac{n^{(0)}}{1-p}=0$$

$$\hat{p}_{ML} = \frac{n^{(1)}}{n^{(1)}+n^{(0)}}=\frac{n^{(1)}}{N}$$		

假设抛硬币20次,其中正面出现的次数为12次,则由极大似然估计得出正面出现的概率p=0.6,并且可以预测下一次抛硬币正面向上的概率为0.6．

##2.最大后验估计(MAP)	
------------

最大后验估计(Maximum a posteriori estimation,MAP)和极大似然估计十分相似,但是最大后验估计中加入了对参数的先验信念(priori belief),它的权重设定为先验分布$p(\theta)$,最大后验估计不是要求似然函数最大化,而是要求由贝叶斯公式算出的整个后验概率最大.		


<img src="../images/140530/map.png" align="center">

