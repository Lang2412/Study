#-*- coding = utf-8 -*-
#@Time : 2020/10/10 16:33
#@Author : 冯朗
#@File ： traversals.py
#@Software : PyCharm

#简单遍历simplegraph类
from myqueue import Queue
from simplegraph import *

def Traversals(G,v):
    frontier = Queue()                  #创建队列
    frontier.enqueue(v)                 #根节点入队
    while not frontier.is_empty():      #队列非空就循环
        v = frontier.dequeue()          #出队
        print(v,end='->')               #输出出队元素
        for w in G.adjacentEdges(v):    #遍历当前节点的子节点
            frontier.enqueue(w)         #入队


def main():
    start = '1'
    print('start:',start)

    Traversals(G1,start)
    print('end')

if __name__ == '__main__':
    main()