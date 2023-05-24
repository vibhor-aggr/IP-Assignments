class Tree:
    def __init__(self, obj):
        self.data = obj
        self.ltree = None
        self.rtree = None
        
    def insert(self, obj):
        if self.data==None:
            self.data=obj
            return
        if obj == self.data:
            return  
        if obj < self.data:
            if self.ltree is None:
                self.ltree = Tree(obj)
            else:
                self.ltree.insert(obj)
        elif obj > self.data:
            if self.rtree is None:
                self.rtree = Tree(obj)
            else:
                self.rtree.insert(obj)
    def ispresent (self, obj):
        if self.data==None:
            return False
        if obj == self.data:
            return  True
        if obj < self.data:
            if self.ltree is None:
                return False
            else:
                return self.ltree.ispresent(obj) 
        elif obj > self.data:
            if self.rtree is None:
                return False
            else:
                return self.rtree.ispresent(obj)
    def isidpresent(self,id):
        if self.data==None:
            return None
        if self.data.uid==id:
            return self.data
        if self.ltree:
            a=self.ltree.isidpresent(id)
            if a!=None:
                return a
        if self.rtree:
            a=self.rtree.isidpresent(id)
            if a!=None:
                return a
        return None
    def print_detail(self):
        if self.data==None:
            return 
        if self.ltree:
            self.ltree.print_detail()
        print(self.data)
        if self.rtree:
            self.rtree.print_detail()
    def detail_by_name(self,name):
        if self.data==None:
            return 
        if self.ltree:
            self.ltree.detail_by_name(name)
        if self.data.name==name:
            print(self.data)
        if self.rtree:
            self.rtree.detail_by_name(name)
class Person:
    def __init__(self,name,dob,address):
        self.uid=None
        self.name=name
        self.dob=dob
        self.address=address
        self.auth=None
    def verify(self):
        i=0
        while i<3:
            key=input('Please enter secret password: ')
            if self.auth==key:
                return True
            print('Invalid key, Try again!')
        print('Number of attempts have exceeded the limit')
        return False 
    def changeadd(self):
        if self.verify():
            curr_add=input('Please enter current address for verification: ')
            if self.address==curr_add:
                new_add=input('Please enter new address: ')
                self.address=new_add
                print('Sucessfully changed!')
                return
        print('Unsucessful attempt')
        return
    def __str__(self):
        return f'UID: {self.uid}\nName: {self.name}\nDate of birth: {self.dob}\nAddress: {self.address}'
    def __eq__(self,other):
        if other==None:
            return False
        if self.name==other.name and self.dob==other.dob:
            return True
        return False
    def __lt__(self,other):
        if self.name<other.name:
            return True
        elif self.name==other.name and  time.strptime(self.dob, "%d/%m/%Y")<time.strptime(other.dob, "%d/%m/%Y"):
            return True
        return False
    def __gt__(self,other):
        if self<other or self==other:
            return False
        return True
    def set_id_auth(self,auth):
        global uid
        uid+=1
        self.uid=uid
        self.auth=auth    

import time
flag=1
t=Tree(None)
uid=0
while flag==1:
    query=int(input('Please selct an operation to be performed:\n1. New person\n2. Existing person\n3. View details(all)\n4. View details(by name)\n5. Exit application\n'))
    if query==1:
        name=input('Enter your name: ')
        dob=input('Enter date of birth in DD/MM/YYYY format: ')
        address=input('Enter your address: ')
        person=Person(name,dob,address)
        if t.ispresent(person):
            print('Person already exists')
        else:
            auth=input('Enter secret password: ')
            person.set_id_auth(auth)
            t.insert(person)
            print('Person added!')
    elif query==2:
        q=int(input('1. View details\n2. Change address\n'))
        if q==1:
            id=int(input('Enter your UID: '))
            a=t.isidpresent(id)
            if a==None:
                print('Wrong UID')
            else:
                print(a)
        elif q==2:
            id=int(input('Enter your UID: '))
            a=t.isidpresent(id)
            if a==None:
                print('Wrong UID')
            else:
                a.changeadd()
    elif query==3:
        t.print_detail()
    elif query==4:
        name=input('Enter name: ')
        t.detail_by_name(name)
    elif query==5:
        break