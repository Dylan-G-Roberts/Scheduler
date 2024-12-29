

from time import sleep

def t1():
    print("t1")
    sleep(1)

def t2():
    print("t2")
    sleep(1)

def schedule(tasks):
    while(True):
        for task in tasks:
            task()

def main():
    tasks = [
        t1,
        t2
    ]
    schedule(tasks)

if __name__ == "__main__":
    main()