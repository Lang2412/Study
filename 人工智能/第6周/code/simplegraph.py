#-*- coding = utf-8 -*-
#@Time : 2020/10/10 15:45
#@Author : 冯朗
#@File ： simplegraph.py
#@Software : PyCharm

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def adjacentEdges(self , v):
        return self.edges[v]

G1 = SimpleGraph()
G1.edges = {
    '1' : ['2','3','4'],
    '2' : ['5','6'],
    '3' : [],
    '4' : ['7','8'],
    '5' : ['9','10'],
    '6' : [],
    '7' : ['11','12'],
    '8' : [],
    '9' : [],
    '10' : [],
    '11' : [],
    '12' : []
}