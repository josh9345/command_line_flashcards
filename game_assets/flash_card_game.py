from peewee import *
from flash_card_data import Card
import random

db = PostgresqlDatabase('cards', user='postgres',
                        password='', host='localhost', port=5432)


card = Card.select()


def game(card):
    for Card in list(card):
        print(Card.front)
        choice = input(" \nTake your best guess \n")
        if choice == Card.back:
            print('hey')
        else:
            print('ho')


game(card)
