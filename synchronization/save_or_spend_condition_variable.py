import time
from threading import Thread, Condition


class SaveOrSpend:
    def __init__(self):
        self.money = 100
        self.condition_variable = Condition()

    def save(self):
        for i in range(1000000):
            self.condition_variable.acquire()
            self.money += 10
            self.condition_variable.notify()
            self.condition_variable.release()
        print("Saving Complete")
        return self.money

    def spend(self):
        for i in range(500000):
            self.condition_variable.acquire()
            while self.money < 20:
                self.condition_variable.wait()
            self.money -= 20
            if self.money < 0:
                print("Money is available", self.money)
            self.condition_variable.release()
        print("Spending Complete")
        return self.money


s = SaveOrSpend()

Thread(target=s.save, args=()).start()
Thread(target=s.spend, args=()).start()
time.sleep(3)

print("Current account balance: ", s.money)
