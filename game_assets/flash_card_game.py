from peewee import *
from flash_card_data import Card
import random

db = PostgresqlDatabase('cards', user='postgres',
                        password='', host='localhost', port=5432)


card = list(Card.select())
random.shuffle(card)
counter = 0
print("\n \n \n \n \n \n \n \n \n \n Hello welcome to the trivia dungeon, have fun and good luck! \n")
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
    print("'You're in luck!' the man yells 'I can free you' hey says 'but you must have the answer to my question'\n")
    game(card)
    if playing == 0:
        print("The man simply shakes his head and walks away, the web begins to vibrate, you look back just in time to see the great spider bring its fangs down...maybe next time")
        exit()
    else:
        print("With a small knife that seems to lighty glow the man swiftly cuts you free, he shakes your hand and continues on his way\n")
        print("Just in time, as you stand you see the great spider fall from the tree top, you turn but the old man is gone\n")
        print("You turn and run as fast as you can, you feel the air burn in your lungs, you run until you reach a clearing, you see a 'clearly' long forgotten bridge, as you cross the bridge the hand rail on the right begins to unravel!\n\n)


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
    print(" \n The hydra lashes out, you you dive to the ground narrowly avoiding death, you grab a torch...the beast lunges towards you this is your only chance to survive \n \n ")
    game(card)
    if playing == 0:
        print("A small mistep is all it takes the hydra sinks its teeth in.....this is the end for you adventurer")
        exit()
    else:
        print("You side step the beasts attack, thrusting the torch into its eye...the hydra lets out a mighty roar, you make a break for it and run to the edge of the mountain the only way out is to slide down....so down you go\n\n ")
        print("You reach the bottom no worse for wear, you notice the web of a great spider a few feet away.. you were lucky to have missed it \n\n")
        print("You continue down the mountain, after walking for a while you pass an old man withered with age, he smiles and says 'be carefull, the persuer will be looking for you, good luck'\n\n")
        print("'The persuer? what could that mean' you think while descending the mountain....you come to a 'clearly' long forgotten bridge, as you cross the bridge the hand rail on the right begins to unravel!\n\n")
game(card)
