from peewee import *
from flash_card_data import Card
import random

db = PostgresqlDatabase('cards', user='postgres',
                        password='', host='localhost', port=5432)


card = list(Card.select())
random.shuffle(card)
counter = 0
playing = None
print("Hello welcome to trivia night, have fun and good luck! \n")
# input("would you like to play the game or create some trivia cards of your own? enter 'game' or 'create' \n")


def game(card, counter):
    print(f"\n{card[counter].front}")
    choice = input(" \nTake your best guess \n")
    if choice == card[counter].back:
        playing = True
        counter += 1
        print('hey')
        return playing
    else:
        playing = False
        print('ho')
        card[counter].wrong += 1
        update = Card.update(
            wrong=card[counter].wrong).where(Card.front == card[counter].front)

        update.execute()
        return playing


print('Prompt 1')
game(card, counter)
if playing == True:
    print('boo')
else:
    print("goodjob")
