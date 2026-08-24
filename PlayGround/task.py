class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_done(self):
        self.completed = True
    def __str__(self):
        if self.completed == True:
            return f"{self.title} & {self.priority}"
        else:
            return f"[X] {self.title} & {self.priority}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
       self.tasks.append(task)

    def get_pending_tasks(self):
        pending = []
        for task in self.tasks:
            if task.completed == False:
                pending.append(task)

        pending.sort(key=lambda t: t.priority)
        return pending

    def execute_next(self):
        pending = self.get_pending_tasks()

        if pending:
            next_task = pending[0]
            next_task.mark_done()
            print(f"Executed: {next_task}")
        else: 
            print("No pending Tasks!")

manager = TaskManager()

task_1 = Task("this is the task 1", 1)
task_2 = Task("this is the task 3", 2)
task_3 = Task("this is the task 2", 4)

manager.add_task(task_1)
manager.add_task(task_2)
manager.add_task(task_3)


manager.get_pending_tasks()
manager.execute_next()
manager.execute_next()
manager.execute_next()
manager.execute_next()