class Queue:
    def __init__(self):
        self.__list = []
        return

    def dequeue(self):
        if not self.isEmpty():
            return self.__list.pop(0)
        else:
            return None

    def enqueue(self, item):
        return self.__list.append(item)

    def get(self):
        return self.__list[0]

    def size(self):
        return len(self.__list)

    def isEmpty(self):
        return self.__list == []

    def __str__(self):
        output = '['
        for i in range(len(self.__list)):
            item = self.__list[i]
            if i < len(self.__list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += ']'
        return output

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

  
