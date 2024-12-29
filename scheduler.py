

from time import sleep

def t1():
    sleep(1)

def t2():
    sleep(1)

def t3():
    sleep(1)

class Task():
    def __init__(self, name, func, atime=0, rtime=1, priority=0):
        self.name       = name
        self.func       = func
        self.atime      = atime
        self.rtime      = rtime
        self.priority   = priority
        self.completed  = False


    def execute(self):
        if self.rtime > 0:
            print(f"Executing {self.name}")
            self.func()
            self.rtime -= 1
        else:
            print(f"Task {self.name} completed")
            self.completed = True

def schedule(tasks):
    while(len(tasks)):
        for task in tasks:
            task.execute()
        
        # Remove completed tasks
        tasks = [task for task in tasks if task.completed is False]

                

def main():
    tasks = [
        Task("t1", t1),
        Task("t2", t2),
        Task("t3", t3),
    ]
    schedule(tasks)

if __name__ == "__main__":
    main()