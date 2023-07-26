import time
from threading import Thread, Lock


class SaveOrSpend:
    def __init__(self):
        self.money = 100
        self.mutex = Lock()

    def save(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Saving Complete")
        return self.money

    def spend(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spending Complete")
        return self.money


s = SaveOrSpend()

Thread(target=s.save, args=()).start()
Thread(target=s.spend, args=()).start()
time.sleep(3)

print("Current account balance: ", s.money)
