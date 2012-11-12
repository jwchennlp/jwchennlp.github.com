---
layout: post
title: "A*算法解决kth-shortest路径问题"
description: ""
category: 
tags: []
---
{% include JB/setup %}


## open class

you may add methods to existing class, 

remember the bad fact and good face.


## all is class, even the basic object class


<pre class="prettyprint lang-ruby">
class MyDemoClass
  ;
end

obj1 = MyDemoClass.new()
obj2 = MyDemoClass.new()

puts obj1.class.superclass
puts obj2.class.superclass

super_class = obj1.class.superclass
puts super_class.methods.length()

class Object
  def add_methods()
    puts "this is add_methods()"
  end
end

puts super_class.methods.length()

</pre>


## Kernel is a module, which every class may get ancestor methods in it

<pre class="prettyprint lang-ruby">

class Demo
	  ;
end

obj = Demo.new()

module Kernel
  def demo_method()
    puts "this is an demo method"
  end
end

obj.demo_method

</pre>



