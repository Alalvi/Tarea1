class Node:
    def __init__(self,Initialdata):
        self.data = Initialdata
        self.next = None
        Trend = list(range(10))
        a=10
    def obtaindata(self):
        return self.data

    def obtainnext(self):
        return self.next

    def asigndata(self,newdata):
        self.data = newdata

    def asignnext(self,newnext):
        self.next = newnext

class ListaEnlazada:

    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self,item):
        temp= Node(item)
        tem.asignnext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        counter = 0
        while current !=None:
            counter = counter + 1
            current = current.obtainnext()
    def search (self, item):
        finded == False
        it=item
        for a in Trend[a]:
            if it==a:
                finded=True
        current = self.head
        while current !=None and not finded:
            if current.obtaindata() == item:
                finded = True
            else:
                current = current.obtainnext()
        if a==10:
            a=0
        else:
            a=a+1
        c=0
        for b in Trend:
            if item==b:
                c=1
        if c==1:
            Trend[a] = item
        return finded
    def remove (self,item):
        current = self.head
        prev = None
        finded = False
        while not finded and current:
            if current.obtaindata() == item:
                finded = True
            else:
                prev = current
                current = current.obtainnext()
        if prev == None:
            self.head = current.obtainnext()
        else:
            prev.asignnext(current.obtainnext())

