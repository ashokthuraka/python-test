import random
secret_num=random.randint(1,10)
guess_num = 0
while True:
    guess_num=int(input(" enter the number between (1-10) : "))
    if guess_num<secret_num:
        print("too low")
    elif guess_num>secret_num:
        print("too high")
    elif guess_num == secret_num:
        print("you won")
        
        
        ###output###
 enter the number between (1-10) : 1
too low
 enter the number between (1-10) : 2
you won
