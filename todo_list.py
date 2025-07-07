class Task:
    def __init__(self, name, status="Pending"):
        self.name = name
        self.status = status

    def __eq__(self, other):
        return isinstance(other, Task) and self.name.lower() == other.name.lower()

    def __repr__(self):
        return f"{self.name} ({self.status})"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def list_tasks(self):
        return self.tasks

    def clear(self):
        self.tasks = []

    def mark_completed(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                task.status = "Completed"
                return True
        return False

    def edit_task(self, old_name, new_name):
        for task in self.tasks:
            if task.name.lower() == old_name.lower():
                task.name = new_name
                return True
        return False

    def contains(self, name):
        return any(task.name.lower() == name.lower() for task in self.tasks)

    def get_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                return task
        return None