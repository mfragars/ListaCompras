from datetime import date


class Lista:
    def __init__(self, id = None, listName = None, createDate = None, status = None):
        self.id = id
        self.listName = listName 
        self.createDate = createDate
        self.status = status