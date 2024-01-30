import random
def validasi():
    while True:
        masukan = int(input("mau angka berapa:"))   
        if masukan == 1 or masukan == 2 or masukan == 3:
            break
        else:
            print("input only 1,2, or 3")
    return masukan

# 1 rock, 2 paper 3 scisors
def battle(bot_guess, human_guess):
    human_win = 0
    bot_win= 0
    if bot_guess == 1 and human_guess == 3:
        bot_win += 1 
        
    elif bot_guess == 1 and human_guess == 2:
        human_win +=1
        
    elif bot_guess == 2 and human_guess == 3:
        human_win += 1
        
    elif bot_guess == 3 and human_guess == 2:
        bot_win += 1
            
    elif bot_guess == 2 and human_guess == 1:
        bot_win += 1
            
    elif bot_guess == 3 and human_guess == 1:
        human_win += 1
    elif bot_guess == human_guess:
        bot_win += 1
        human_win += 1
    return human_win,bot_win

def compare(number1, number2):
    for i in range(3):
        if number1>number2:
            print("bot champion")
        else:
            print("human champion")
        return number1, "-", number2

for i in range(3):
    punya_bot = int(random.randint(1,3))
    punya_manusia = validasi()
    number1, number2 = battle(punya_bot,punya_manusia)
    a = compare(number1, number2)
    print(a)