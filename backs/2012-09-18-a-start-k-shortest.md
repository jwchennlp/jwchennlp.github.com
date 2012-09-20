---
layout: post
title: "A*算法解决kth-shortest路径问题"
description: ""
category: 
tags: []
---
{% include JB/setup %}


## 问题描述

无向图G，需要求出S->T点的前k短路径，要求路径中没有环。(所有的边的权值不为负)


## A*算法求解kth-shortest问题

`A*`算法已经被广泛运用于路径规划问题中，同时`A*`算法作为一种启发式算法的框架，可用于多种搜索问题。`A*`算法已经完全足够解决这个问题。还是先回顾一下`A*`的基本符号：

--------

`f(s)=g(s)+h(s)`，其中`h(s)<=h*(s)`(s到终点的真实代价)，

并且对s的任意后继t有：`h(t)+w(s,t)>=h(s)`，其中`w(s,t)`是从s转移到t的代价，

那么可以证明满足`f(s)<=f (w)`，于是可以证明f的最优性。

--------

所以如果能确切的计算出来`h*(s)`，那么评估函数f(s)将是s点的最短路径。可以利用Dijkstra算法来求解出各个点到T点的最短路径，假设第i个节点到T的最短路径计为`Dist_T(i)`，`Dist_T(i)`作为`A*`函数中的启发函数`h(s)`，从S开始搜索，因此算法描述如下：

	Dijkstra(T); //计算各个点到T点的最短路径
        int Astar(){
            if(dist[S]==INF) return -1;
            priority_queue<Node> Q;      //极小堆，定点为f(s)=g(s)+h(s)最小的节点
            Q.push(Node(S,0));           //源点S加入堆，估计代价为0
            while(!Q.empty()){
                int len=Q.top().len;
                int u=Q.top().v;
                Q.pop();
                cnt[u]++;
                if(cnt[T]==K)
                    return len; //第K次从队列弹出的值未kth-shortest的值
                if(cnt[u]>K) 
                    continue;
                for(int i=0;i<Adj[u].size();i++) {//取v节点的临接节点计算评估函数并加入优先队列 
                    int v = Adj[u][i].v;
                    int eval = len + Dist(u,v) + Dist_T(v);
                    Q.push(Node(v, eval));
                }
        }
            return -1;
        }
    

因为没有标识哪些节点访问过哪些节点没有访问过，所以这种方法计算出来的结果路径可能含有环，即可能出现1->2->3->2->5，为了避免这样的情况可以在每个扩张Node里面增加当前路径已经访问过的点，在进行下一次扩张的时候可以避免访问这些已经在路径中的节点。但是这样所需要的空间复杂度是巨大的，所以需要再次用一些剪枝办法来避免过多的扩展。

## 一个优化

`A*`算法在扩展节点的时候，如果我们能筛除掉更多无用的节点，那么都可以利于减少搜索的空间复杂度和时间复杂度。当k取值较小的时候，即当我们并不需要知道所有路径长度和其排序，而只需要知道前k(假设k<=10)段的路径，这里加上一个剪枝会有很大的优化。 假设我们事前知道kth-shortest的最大值，就能在扩张的时候加入这个限制，避免大部分的无用的节点扩张。

         for(int i=0;i<Adj[u].size();i++) {//取v节点的临接节点计算评估函数并加入优先队列 
             int v = Adj[u][i].v;
             int eval = len + Dist(u,v) + Dist_T(v);
             if(eval > max_dist) 
                 continue;
             else 
                 Q.push(Node(v, eval));
         }

如何知道kth-shortest的最大值这个临界点呢?假设我们知道某条经过点v的S->T路径的最短长度，即对于所有的点v1,v2,v3,....vn,有dist(v1)为S->...->v1-> ...->路径的长度，一共n个dist，把这n个dist排序以后，取第k小的dist(v_kth_smallest)即为kth-shortest。如何计算出dist(v)，通过Dijkstra(T)可以计算出v到T的最短路径，同样可以通过Dijkstra(S)可以计算出S到v的最短路径Dist_S(v)，这里有如下定理：
  
    对于任意最短路径S->K中，假设经过点v，则必有: min(S->v)和min(v->T)。
    因此要计算经过v的从S->K的最短路径可以用: min_dist(v) = Dist_S(v) + Dist_T(v)

因此如果我们用这种方法计算出Dist(v)，那么最后第k小的dist(v_kth_smallest) >= kth-shortest。这对于`A*`算法的最后结果没有影响，但是同样可以作为一个条件来删除掉大部分不符合条件的节点，因此得到一个很好的优化方案。
这个优化可以用于`k<N`时的kth最短路径问题，可以预见k越小剪枝效果越好。

据我实现在18600个节点的图上，这个算法比[Yen's算法](http://mansci.journal.informs.org/content/17/11/712.abstract)快了很多倍，甚至在我的PC(3G内存)机上，后者在算到k=3的时候内存就支持不住了。


## 算法复杂度分析
假设图G有m条边和n个节点，
Dijkstra算法的复杂度为`((m+n)log n)`(二叉树实现的优先队列)。
`A*`算法的时间复杂度取决于启发函数，对于`h*(x)`总是为常数的启发函数，`A*`算法退化为BFS算法。因为这里用了Dijkstra算法来求x点到T点的最短路径，所以为最优启发函数，
其时间复杂度和空间复杂度都是`O(delta*V^2*(lgV+lg(delta))`的，其中delta为一个冗余量。

