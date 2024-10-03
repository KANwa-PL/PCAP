# Your task is to implement the Queue class with two basic operations:
#
# put(element), which puts an element at end of the queue;
# get(), which takes an element from the front of the queue and returns it as the result
# (the queue cannot be empty to successfully perform it.)


class QueueError():
    def __init__(self):
        self.error = ""

    def set_queue_error(self, err):
        self.error = err

    def get_queue_error(self):
        return self.error


class Queue():
    def __init__(self):
        self.elements = []

    def put(self, elem):
        self.elements.insert(0, elem)

    def get(self):
        return self.elements.pop(-1)

    def get_queue_size(self):
        return len(self.elements)

    def is_queue_empty(self):
        if self.get_queue_size() == 0:
            return True
        else:
            return False


que = Queue()
que.put(1)
que.put("dog")
que.put("cat")
que.put(False)
que.put(True)
que.put(None)

try:
    for i in range(que.get_queue_size()):
        print(que.get())
    print("Empty:", que.is_queue_empty())
except IndexError:
    queError = QueueError()
    queError.set_queue_error("Queue Error occurred")
    print(queError.get_queue_error())
