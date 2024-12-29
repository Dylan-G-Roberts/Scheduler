

def t1():
    pass

def t2():
    pass

def t3():
    pass

class Task():
    def __init__(self, name, func, arrival_time=0, burst_time=1, priority=0):
        self.name               = name
        self.func               = func
        self.arrival_time       = arrival_time
        self.burst_time         = burst_time
        self.remaining_time     = burst_time
        self.priority           = priority
        self.completed          = False
        self.completion_time    = None

    def execute(self):
        if self.remaining_time > 0:
            self.func()
            self.remaining_time -= 1
        if self.remaining_time == 0:
            self.completed = True

    def turnaround_time(self):
        if not self.completed:
            raise Exception("Task not Completed")
        if not self.completion_time:
            raise Exception("Completion Time is None")
        return self.completion_time - self.arrival_time

    def waiting_time(self):
        if not self.completed:
            raise Exception("Task not Completed")
        if self.completion_time is None:
            raise Exception("Completion Time is None")
        return self.turnaround_time() - self.burst_time

def fcfs_scheduler(tasks):
    time = 0
    while any(not task.completed for task in tasks):
        task_executed = False
        for task in tasks:
            if not task.completed and time >= task.arrival_time: # Only run uncompleted tasks that have arrived
                print(f"Time:{time} - Executing {task.name}")
                task.execute()
                task_executed = True
                if task.completed:
                    print(f"Time:{time+1} - Task {task.name} Complete")
                    task.completion_time = time + 1
                # Only run 1 task per CPU Tick
                break
    
        if not task_executed:
            # Check if a task is arriving in the next tick
            if any(task.arrival_time > time for task in tasks):
                print(f"Time:{time} - CPU Idle")
        
        # Time ticks forward
        time += 1

def print_stats(tasks):         
    for task in tasks:
        print(f"Task {task.name} turnaround time is {task.turnaround_time()}")
        print(f"Task {task.name} wait time is {task.waiting_time()}")
    
    print(f"Average turnaround time is {sum([task.turnaround_time() for task in tasks])/len(tasks)}")


def main():
    tasks = [
        Task("t1", t1, arrival_time=0, burst_time=100),
        Task("t2", t2, arrival_time=0, burst_time=10),
        Task("t3", t3, arrival_time=0, burst_time=10),
    ]
    fcfs_scheduler(tasks)

    print_stats(tasks)

if __name__ == "__main__":
    main()
