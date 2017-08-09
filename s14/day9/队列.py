__author = "Hu Rongyang"
import queue


'''
#后进先出的queue
q = queue.Queue()
q.put("d1")
q.put("d2")
q.put("d3")
q.put("d4")
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
'''


'''
#先进先出的queque
q = queue.LifoQueue()
q.put("d1")
q.put("d2")
q.put("d3")
q.put("d4")
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
'''

#有优先级的queue
q = queue.PriorityQueue()
q.put((-1,"chenronghua"))
q.put((3,"hanyang"))
q.put((10,"alex"))
q.put((6,"wangsen"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())