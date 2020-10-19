#-*- coding = utf-8 -*-
#@Time : 2020/10/10 15:44
#@Author : 冯朗
#@File ： simplegraph_bfs.py
#@Software : PyCharm

from myqueue import Queue
from stack import Stack
from simplegraph import *

def BFS(G,v,goal,came_from):
    frontier = Queue()
    frontier.enqueue(v)             #入队
    came_from[v] =  None            #字典类型，key为v,value为节点v的前驱节点
    visited = {}
    print(f'搜索过程为:')
    while not frontier.is_empty():
        v = frontier.dequeue()      #出队
        print(f'{v}',end='->')
        if visited.get(v) == None:  #判断节点v是否未访问过，未访问过的节点value为None
            #print(v,end="   ")
            #print(visited.get(v))
            if v == goal:
                print('end')
                return  v

            else:
                visited[v] = True   #访问过节点value设置为True
                #print(visited.get(v))
                for w in G.adjacentEdges(v):        #遍历节点v的子节点
                    frontier.enqueue(w)             #v的子节点顺序入队
                    came_from[w] = v                #设置w的前驱节点为v
    return None

def main():
    came_from = {}
    start = '1'
    goal = '12'
    found = BFS(G1,start,goal,came_from)
    print('start:',start)
    print('goal:',goal)
    if found != None:
        s = Stack()
        s.push(found)
        #print(came_from)
        found = came_from.get(found)
        print(found)
        while found !=  None:
            s.push(found)
            found = came_from.get(found)
            print(found)
        while not s.is_empty():
            print(s.pop(),end='->')
        print('end')
    else:
        print('Path not fount!')

if __name__ == '__main__':
    main()

