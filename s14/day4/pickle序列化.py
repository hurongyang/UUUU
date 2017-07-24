__author = "Hu Rongyang"
#import json
import pickle

def sayhi(name):
    print('hello',name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi,
}

f = open("test.txt",'wb')
#print(pickle.dumps(info))
f.write(pickle.dumps(info))

f.close()

#json只能处理简单的数据,而pickle能处理复杂的