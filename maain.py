import json
import random

running = True

def get_joke():
    with open('jokes.json') as json_file:
        jokes = json.load(json_file)

        lenght = len(jokes)

        joke_num = random.randint(0, lenght)
        print(jokes[joke_num]['joke'])


while running:
    user_input = input('Ask: YES/NO: ')
    if  user_input == 'YES':
        get_joke()
    elif user_input == 'NO':
        running = False
