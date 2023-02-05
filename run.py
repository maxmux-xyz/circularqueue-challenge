
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = []
        for i in range(k):
            self.queue.append("o")
        self.first = 0
        self.ix = 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.ix] != "o":
            return False

        self.queue = self.queue[:self.ix] + [value] + self.queue[self.ix +1:]

        if self.ix == self.size - 1:
            self.ix = 0
        else:
            self.ix += 1

        # print(self.queue, print(self.ix), print(self.first))
        return True
        

    def deQueue(self) -> bool:
        if self.queue[self.first] == "o":
            return False
        self.queue = self.queue[:self.first] + ["o"] + self.queue[self.first +1:]
        if self.first == self.size - 1:
            self.first = 0
        else:
            self.first += 1
        # print(self.queue, print(self.ix), print(self.first))
        return True

    def Front(self) -> int:
        if self.ix == 0:
            value = self.queue[self.size - 1]
        else:
            value = self.queue[self.ix - 1]
        if value == "o":
            return -1
        return value

    def Rear(self) -> int:
        value = self.queue[self.first]
        if value == "o":
            return -1
        return value

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(4)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(1)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(2)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(3)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(4)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(5)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(6)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_2 = obj.deQueue()
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(1)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(2)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(3)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)
param_1 = obj.enQueue(4)
print("Front: ", obj.Front(), "Rear", obj.Rear())
print(obj.queue, obj.ix, obj.first)

# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()