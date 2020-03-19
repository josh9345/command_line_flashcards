from peewee import *
from flash_card_data import Card
import random

db = PostgresqlDatabase('cards', user='postgres',
                        password='', host='localhost', port=5432)


card = list(Card.select())
random.shuffle(card)
counter = 0
print("\n \n \n \n \n \n \n \n \n \n Hello welcome to trivia night, have fun and good luck! \n")
# input("would you like to play the game or create some trivia cards of your own? enter 'game' or 'create' \n")


def game(card):
    global playing
    global counter
    print("Quickly answer this question to decide your fate ")
    print(f"\n{card[counter].front}")
    choice = input(" \nTake your best guess \n")
    if choice == card[counter].back:
        playing = True
        counter += 1
        return playing
    else:
        playing = False
        card[counter].wrong += 1
        update = Card.update(
            wrong=card[counter].wrong).where(Card.front == card[counter].front)

        update.execute()
        return playing


def hydra_fail(card, game):
    print("after a couple of hours you awaken to find yourself caught in the web of a great spider \n")
    print("No matter how you struggle you cant seem to free yourself.....Many hours pass when an old man withered from age walking along with his mule. \n")
    print("'You're in luck!' the man yells 'I can free you' hey says 'but you must have the answer too my question'")
    game(card)


print('you stumble upon a sleeping dragon you must attempt to sneak past it. \n')
game(card)
if playing == 0:
    print(' \n You accidentily step on a twig and are swiftly fried...medium rare i believe \n \n')
    exit()
else:
    print(" \n You gracefully tiptoe through the dark cave and escape into the night \n \n ")

print("After hours of walking you stumble upon a waterfall cascading down the side of mountain, and a lake encircled by torches \n")
print("the water begins to tremble, from its depths emerge a mighty hydra!")
game(card)
if playing == 0:
    print("You run to your right in an attempt to flank the beast, the hydra lashes out with one of its heads, narrowly avoiding death you are struck in the chest and sent tumbling down the mountain side")
    hydra_fail(card, game)
else:
    print(" \n You gracefully tiptoe through the dark cave and escape into the night \n \n ")
