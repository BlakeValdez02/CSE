import random
print("Welcome to Lucky 7's!")
money = 15
High_Score = 0
Best_round = 0
Rounds = 0

while money > 0:
    if High_Score < money:
        High_Score = money
        Best_round = money
    money -= 1
    Rounds += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    if total == 7:
        money += 5
        print("You Win!")
    print("The total is %d" % total)
    if money == 0:
        print("You have run out of de moneys. You lose!")
        print("Your Best Number of Rounds is %d and your balance of money was %d" % (Best_round, money))