class Task:
    def __init__(self, id, name, description, due_date, priority, status):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {self.status}"
    
    def add_task():
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        priority = input("Enter task priority: ")
        status = input("Enter task status: ")
        return Task(None, name, description, due_date, priority, status)
        
    def delete_task():
        pass