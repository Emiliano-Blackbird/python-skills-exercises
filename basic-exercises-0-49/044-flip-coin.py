import random


while True:
    coin = random.randint(1, 2)
    if coin == 1:
        print("Heads")
    else:
        print("Tails")
    play_again = input("Do you want to flip again? (y/n): ")
    if play_again.lower() == 'n':
        break
print("Thanks for playing!")
