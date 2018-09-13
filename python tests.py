class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        nodo = Node(data)
        if self.empty():
            self.head = nodo
        else:
            nodo.prev = self.head
            self.head = nodo
        self.count += 1

    def pop(self):  
        if self.empty():
            return False
        else:
            self.head = self.head.prev
            self.count -= 1

    def top(self):
        return self.head

    def empty(self):
        return self.head == None


def Transfromar(a):
    pila = Stack()
    b=0
    number=0
    D=0
    if a[0].isdigit()==True and a[len(a)-1].isdigit()==True:
        D=3
    elif a[0].isdigit()==True:
        D=1
    elif a[len(a)-1].isdigit()==True:
        D=2
    else:
        D=3
    while (b!=len(a)):
        if D==1:
            break
        if a[b].isdigit()==True:
            while(a[b].isdigit==True):
                number=number*10+a[b]
                b+1
            pila.push(number)
            number=0
        else:
            if a[b]=="":
                b=b+1
            elif a[b]=="+":
                pila.push(a[b])
                b=b+1
            elif a[b]=="-":
                pila.push(a[b])
                b=b+1
            elif a[b]=="*":
                pila.push(a[b])
                b=b+1
            elif a[b]=="/":
                pila.push(a[b])
                b=b+1
    return pila,D

def Polaca (self,D):
    if D==2:
        stack = Stack()
        while (self.top()):
            stack.push(self.top())
            self.pop()
        self = stack
        stack = Stack()
    number=0
    A=True
    oterm=""
    term1=0
    term2=0
    term3=0
    counter=1
    #aqui se realiza la notación polaca
    while (A):
        while(self.top()):
            if (self.top()).isdigit()==False:
                stack.push(self.top())
                self.pop()
                oterm=""
            elif (self.top()).isdigit()==False and term2=0:
                if self.top()=="+":
                    term3=term1+self.top()
                elif self.top()=="-":
                    term3=term1-term2
                elif self.top()=="*":
                    term3=term1*term2
                else:
                    term3=term1/term2
                term2=0
                oterm=""
                self.pop()
                stack.pop()
                stack.pop()
                stack.push(term3)
            c=0
            while (stack.top()):
                self.push(stack.top())
                stack.pop()
                c+1
            if c==1:
                A=False
    Return self.top()
    
    
    
#El input al parecer no finaliza la entrada de datos
a = input("ingrese notación polaca: ")
pila = Stack()
pila,D = Transfromar(a)

    
