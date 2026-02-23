import threading
def numbers():
    for i in range(5):
        print(f"Number {i}")

def letters():
    for k in "ABCD":
        print(f"Letter {k}")

t1=threading.Thread(target=numbers)
t2=threading.Thread(target=letters)

t1.start()
t2.start()
t1.join()
t2.join()