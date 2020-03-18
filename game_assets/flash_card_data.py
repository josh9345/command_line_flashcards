from peewee import *

db = PostgresqlDatabase('cards', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Card(BaseModel):
    front = CharField()
    back = CharField()


db.connect()
db.drop_tables([Card])
db.create_tables([Card])

Card(front='Which fictional city is the home of Batman?', back='gotham').save()
Card(front='What is a Geiger Counter used to detect?', back='radiation').save()
Card(front='In the film Babe, what type of animal was Babe?', back='pig').save()
Card(front='What’s the total number of dots on a pair of dice?', back='42').save()
Card(front='Traditionally, how many Wonders of the World are there?', back='7').save()
Card(front='Which planet is the closest to Earth', back='venus').save()
Card(front='According to the old proverb, to which European capital city do all roads lead?', back='rome').save()
Card(front='Which is the tallest mammal?', back='giraffe').save()
Card(front='What is the name of the fairy in Peter Pan?', back='tinkerbell').save()
Card(front='How many strings does a violin have?', back='4').save()
Card(front='The hardest natural substance known is what?', back='diamond').save()
Card(front='In Greek mythology, who turned all that he touched into gold?',
     back='midas').save()
Card(front='How many sides does an octagon have?', back='8').save()
Card(front='What is the name of the city where the cartoon family The Simpsons live?',
     back='springfield').save()
Card(front='The hard white material of elephant tusks is called what?',
     back='ivory').save()
Card(front='Which atmospheric gas is the most common?', back='nitrogen').save()
Card(front='What kind of bird is often seen dashing along the roads and highways of the southern USA and Mexico... hence its name? (one word)', back='roadrunner').save()
Card(front='Immersing food in vinegar to prolong its lifespan is known as what?',
     back='pickling').save()
Card(front='A "Grand Slam" in tennis means a player winning how many major tournaments in a calendar year?', back='4').save()
Card(front='In what mountain range is Mount Everest located?', back='himalayas').save()
