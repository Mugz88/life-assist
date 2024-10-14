class task:
    def __init__(self, id, name, description, due_date, priority, status):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {self.status}"
    
    def add_task(self, id, name, description, due_date, priority, status):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        
    def delete_task(self):
        self.name = None
        self.description = None
        self.due_date = None
        self.priority = None
        self.status = None