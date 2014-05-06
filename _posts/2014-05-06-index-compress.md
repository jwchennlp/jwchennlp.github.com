---
layout: post
title: "索引压缩"
modified: 2014-05-06 17:01:16 +0800
tags: [信息检索,索引压缩]
image:
  feature: abstract-6.jpg
  credit: dargadgetz
  creditlink: http://www.dargadgetz.com/ios-7-abstract-wallpaper-pack-for-iphone-5-and-ipod-touch-retina/
comments: true
share: true
---
###为什么要进行索引压缩？
------
进行索引压缩有以下优点：  
 
 * 节省磁盘空间．  
 * 增加高速缓存(cache)的利用率.  
   倒排索引词典是放在内存中的，倒排记录表放在磁盘上．对与到拍记录上的某些词项ｔ，我们是需要经常访问的，如果将这次词项ｔ所对应的到拍记录表压缩后放在高速缓存中，只要采用得当的解压缩算法，那么当查询词项ｔ的倒排记录表时，只需要访问cache，而不用从磁盘读取数据，能充分减少IR系统的响应时间． 
 * 压缩能够加快从磁盘读取数据的速度．
 
压缩技术分为有损压缩和无损压缩，有损压缩指的是压缩后，原始数据的所有信息都保存下来了．词干还原，大小写转换都属于有损压缩．   
   
###Heaps定律：词项数目的估计  

heaps定律认为，文档集大小和词汇量之间存在对数上的线性关系．    

$$a^2 + b^2 = c^2$$

