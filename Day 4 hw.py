
class node:
    node.left = node or none
    node.right = node or none
    node.value = something

def findnum(node,num):
    if num == node.value:
        return node.value
    if num > node.value:
        return findnum(node.right,num)
    return findum(node.left,num)
a = node(None,None,1)
b = node(None,None,4)
c = node(a,b,2)


    
