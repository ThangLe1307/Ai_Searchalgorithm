from Space import *
from Constants import *
import queue
import math






def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()
    father[g.goal.value]=-1
    
    while (len(open_set)>0):

        currentValue=open_set.pop()
        
     
     
        current=g.get_node(currentValue)
        current.set_color(yellow)
        closed_set.append(current)
        g.draw(sc)

        if g.is_goal(current):
            break

        
        for node in g.get_neighbors(current):
            if node not in closed_set and node.value not in open_set:
                node.set_color(red)
                open_set.append(node.value)
                g.draw(sc)
                father[node.value]=currentValue

        current.set_color(blue)
        g.draw(sc)

    child=g.goal.value
    while (child != g.start.value):
        node= g.get_node(child)
        node.set_color(grey)
        g.draw(sc)
        child = father[child]

    node= g.get_node(child)
    node.set_color(grey)
    g.draw(sc)
    child = father[child]
       

   

    #TODO: Implement DFS algorithm using open_set, closed_set, and father
  
   



def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()
    father[g.goal.value]=-1
    
    while (len(open_set)>0):

        currentValue=open_set.pop(0)
        
     
     
        current=g.get_node(currentValue)
        current.set_color(yellow)
        closed_set.append(current)
        g.draw(sc)

        if g.is_goal(current):
            break

        
        for node in g.get_neighbors(current):
            if node not in closed_set and node.value not in open_set:
                node.set_color(red)
                open_set.append(node.value)
                g.draw(sc)
                father[node.value]=currentValue

        current.set_color(blue)
        g.draw(sc)

    child=g.goal.value
    while (child != g.start.value):
        node= g.get_node(child)
        node.set_color(grey)
        g.draw(sc)
        child = father[child]

    node= g.get_node(child)
    node.set_color(grey)
    g.draw(sc)
    child = father[child]

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}


    #open_set luu cost cua node [i]
    open_set[g.start.value] = 0

    #luu cua node
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0


    #set current va mau sua start
    current=g.start.value
    g.get_node(current).set_color(yellow)
    g.draw(sc)
    while (len(open_set)>0):
        for index in open_set.keys():
            constOfNode = open_set[index]
            # const cua node dang xet < const cua node hien tai
            if constOfNode<distance(g.get_node(current),g.get_node(g.goal.value)):
                current=index

        open_set.pop(current)
        closed_set.append(current)
        g.get_node(current).set_color(blue)
        g.draw(sc)
        if g.is_goal(g.get_node(current)):
            break


        #xet cac node hang xom cua node hien tai
        for node in g.get_neighbors(g.get_node(current)):
            if node.value not in closed_set and node.value not in list(open_set.keys()):
                node.set_color(red)
                open_set[node.value]=distance(node,g.get_node(g.goal.value))
                father[node.value]=current
                g.draw(sc)


#ve duong di
    child=g.goal.value
    while (child != g.start.value):
        node= g.get_node(child)
        node.set_color(grey)
        g.draw(sc)
        child = father[child]

    node= g.get_node(child)
    node.set_color(grey)
    g.draw(sc)
    child = father[child]













    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

#df
    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def distance(fatherNode:Node, node:Node):
    return math.sqrt((fatherNode.x - node.x) ** 2 + (fatherNode.y - node.y) ** 2)
