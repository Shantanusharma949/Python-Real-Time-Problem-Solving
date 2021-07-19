class Queue:

    l = []
    front = -1 
    rear = -1

    def __init__(self, maxSize = 1):
        self.maxSize = maxSize
    
    def isEmpty(self):
        if self.front == -1 or self.front > self.rear:
            return True 
        else:
            return False
    
    def isFull(self):
        if self.rear == self.maxSize - 1:
            return True
        else: 
            return False

    def insert(self, ele):
        if self.isFull():
            print("Queue Overflow")
        else:
            if self.isEmpty():
                self.front += 1
                self.rear += 1
            else:
                self.rear += 1
            self.l.append(ele)
    
    def delete(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            self.front += 1
            return self.l.pop(0)
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            print("Front ->", end = " ")
            for ele in self.l:
                print(ele, end = " ")
            print("")


st = Queue(5)
st.insert(3)
st.insert(4)
st.insert(3)
st.insert(1)
st.insert(5)
st.insert(4)

st.printQueue()

st.delete()
st.delete()
st.delete()
st.delete()
st.delete()
st.delete()
