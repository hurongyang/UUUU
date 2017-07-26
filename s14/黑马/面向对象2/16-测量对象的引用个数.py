__author = "Hu Rongyang"
import sys
class T():
    pass

t = T()
print(sys.getrefcount(t))   #2-1=1个引用 ==> getrefcount(t)传递t时也有一个引用 <==

tt = t
print(sys.getrefcount(t))   #3-1=2个引用

del tt
print(sys.getrefcount(t))   #2-1=1个引用

del t                       #0个引用(被释放，下面print报错)
print(sys.getrefcount(t))
