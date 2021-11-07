#!/usr/bin/python3
import random
class Prize:
    First=[]
    Second=[]
    Third=[]
    def __init__(self):
        self.First.clear()
        self.Second.clear()
        self.Third.clear()
        for i in range(5):
            self.First.append(random.randint(1,100))
            self.Second.append(random.randint(1,100))
            self.Third.append(random.randint(1,100))

    def  __del__(self):
        print(self.First)
        print(self.Second)
        print(self.Third)

    def GetPrize(self):
        count = 5
        while count:
            # 请用户输入数字
            count = count - 1
            try:
                num = int(input("Please intput your number:"))
            except ValueError:
                print("Your input is error,please try again!!")
                continue

            if num == 0:
                print("Thank you,bye bye!!")  # 与用户再见
                break
            elif num in self.First:  # 用户中一等奖
                print("Congratulations on winning the first prize")
            elif num in self.Second: #用户中二等奖
                print("Congratulations on winning the second prize")
            elif num in self.Third: #用户中三等奖
                print("Congratulations on winning the third prize")
            else : #用户未猜对
                print("Sorry,please try again!!")

if __name__ == '__main__':
    A = Prize()
    A.GetPrize()
    B = Prize()
    B.GetPrize()