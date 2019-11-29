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


spisok = [(10,0),(10,3),(7,6),(14,8),(16,3),(15,7)]
tree = Node(0,data = 1)
for i in range(len(spisok)):
    tree.add_child(node(spisok[i][0],data=spisok[i][1]))
print(tree)
print(tree.self_check())