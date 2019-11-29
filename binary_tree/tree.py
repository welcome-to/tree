class Node(object):
    def __init__(self,key,data=None):
        self.lchild = None
        self.rchild = None
        self.under_left = 0
        self.under_right = 0
        self.key = key
        self.data = data

        pass

    def add_child(self,child):
        if self.key >= child.key:
            self.under_left += 1
            if self.lchild == None:
                self.lchild = child
            else:
                self.lchild.add_child(child)
        else:
            self.under_right += 1
            if self.rchild == None:
                self.rchild = child
            else:
                self.rchild.add_child(child)
    def clear_data(self):
        if self.lchild!=None:
            self.lchild.clear_data()
        if self.rchild!=None:
            self.rchild.clear_data()
        self.data = None
        self.under_left = 0
        self.under_right = 0

    def add_data_to_node(self,key,data):
        if self.key==key:
            self.data=data
        elif self.key>key:
            self.under_left+=1
            self.lchild.add_data_to_node(key,data)
        else:
            self.under_right+=1
            self.rchild.add_data_to_node(key,data)

    def strange_find(self,strange_key,add=0):
        if self.under_left+add==strange_key:
            return self.data
        elif self.under_left+add>strange_key:
            return self.lchild.strange_find(strange_key,add=add)
        else:
            return self.rchild.strange_find(strange_key,add=add+self.under_left+1)

    def get_data_of_node(self,key,current_l = 0):
        if key == current_l+self.under_left:
            return self.data
        elif key > current_l:
            return self.lchild.get_data_of_node(key,current_l)
        else:
            return self.rchild.get_data_of_node(key,current_l+self.current_l)
    
    def self_check(self):
        return (self.lchild.self_check() and (self.key >= self.lchild.key) if self.lchild != None else True) and ((self.key < self.rchild.key) and self.rchild.self_check() if self.rchild!=None else True)
    
    def __str__(self):
        return self.printer()
    
    def printer(self,rec_deep=0):
        return ('' if self.rchild == None else (self.rchild.printer(rec_deep=rec_deep+1)+'\n')) + \
             '      '*rec_deep + str((self.key,self.data)) + \
             ('' if self.lchild== None else ('\n'+self.lchild.printer(rec_deep=rec_deep+1)))

'''
spisok = [(10,0),(10,3),(7,6),(14,8),(16,3),(15,7)]
tree = Node(0,data = 1)
for i in range(len(spisok)):
    tree.add_child(node(spisok[i][0],data=spisok[i][1]))
print(tree)
print(tree.self_check())
'''

def load_tree(listik,tree=None,add = 0):
    if tree == None:

        tree = Node(len(listik)//2,data=listik[len(listik)//2])
    else:
        tree.add_child(Node(add+len(listik)//2,data=listik[len(listik)//2]))
    if len(listik[:(len(listik)//2)])>=1:
        load_tree(listik[:(len(listik)//2)],tree=tree,add=add)
    if len(listik[(len(listik)//2):])>1:
        load_tree(listik[(len(listik)//2)+1:],tree=tree,add=add+len(listik)//2+1)
    return tree


a = int(input())
listik = list(map(int,input().split(' ')))
listik1 = sorted([(i,listik[i]) for i in range(len(listik))],key=lambda x: (-x[1],x[0]))
tree = load_tree(listik)
tree.clear_data()

ask = int(input())
unsorted_asks = list(enumerate([list(map(int,input().split(' '))) for i in range(ask)]))
asks = sorted(unsorted_asks,key=lambda x:x[1][0])
current_k = 0
for i in range(len(asks)):
    while current_k<asks[i][1][0]:
        tree.add_data_to_node(listik1[current_k][0],listik1[current_k][1])
        current_k+=1
    asks[i][1].append(tree.strange_find(asks[i][1][1]-1))
len(asks)
for i in sorted(asks,key=lambda x:x[0]):
    print(i[1][2])