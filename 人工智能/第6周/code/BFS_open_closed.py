from simplegraph import *
from stack import Stack

def BFS(G,v,goal,came_from):
    '''came_from: dic 该节点来自于某个节点'''
    '''BFS的队列实现'''
    print(f'搜索过程为:')
    open = [v]  #未访问节点列表
    closed = [] #已访问节点列表
    came_from[v] = None
    while len(open) != 0 :
        v = open.pop(0)
        print(f'{v}', end='->')
        if v == goal:
            print(f'end')
            return v
        else:
            closed.append(v)
            for w in G.adjacentEdges(v):
                if w not in closed:
                    open.append(w)  #未搜索过的才添加进open列表
                    came_from[w] = v
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = BFS(G1,start,goal, came_from)
    print('start:', start)
    print('goal:', goal)
    #print(came_from)
    if found != None:
        s = Stack()
        #print(found)
        s.push(found)
        found = came_from.get(found)
        while found != None:
            s.push(found)
            #print(found)
            found = came_from.get(found)
        while not s.is_empty():
            print(s.pop(),end='->')
        print('end')
    else:
        print('Patj not found')

if __name__ == "__main__":
    main()