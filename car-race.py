#countdown in python
import time, sys

MAX_NUMBER = 20

def countdown():
    while True:
        num = input('Enter the number you want to countdown: ')
        if num.isdecimal():
            num = int(num)
            if 1 <= num <= MAX_NUMBER:  #if a value is in between two values Greater than or equal to 1 and less than or equal to MAX_NUMBER
                break
            else:
                print("Number must be between 1 - 20")
        else:
            print("Enter a valid number")
            print("")
            
        if num == 'quit':
            print('Thanks for playing!')
        sys.exit()
    return num
      
print("countdown timer by tobe")
num=countdown()

for i in range(num):
        time.sleep(0.5) 
        print(num - i-1) #try removing the -1 or adding +1 
print("ended")

        