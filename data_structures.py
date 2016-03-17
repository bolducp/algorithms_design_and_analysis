class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item_to_pop = self.items[-1]
        self.items = self.items[:-1]
        return item_to_pop

class Queue(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def next(self):
        next_item = self.items[0]
        self.items = self.items[1:]
        return next_item
