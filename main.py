from nicegui import ui
import wikipedia
import random
import nltk
import re

# nltk.download('punkt')

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Game Setup
result = "Emmanuel Macron"
para = wikipedia.summary(result)
para = re.sub("Emmanuel", "XXXX", para)
para = re.sub("Macron", "XXXX", para)
para = re.sub("\(.*?\)","[XXXX]", para)

punkt_params = PunktParameters()
punkt_params.abbrev_types = set(['Mr', 'Mrs', 'LLC', 'fl'])
tokenizer = PunktSentenceTokenizer(punkt_params)

tokens = tokenizer.tokenize(para)
hint_1 = random.choice(tokens)
hint_2 = random.choice([ele for ele in tokens if ele != hint_1])
hint_3 = random.choice([ele for ele in tokens if ele != hint_1 or ele != hint_2])
hint_4 = random.choice([ele for ele in tokens if ele != hint_1 or ele != hint_2 or ele != hint_3])

def guess(x):

    if x == result:
        return "Congratulations you won!"
    else:
        return "Guess again!"


def final_guess(x):

    if x == result:
        return "Congratulations you won!"
    else:
        return "The correct answer is " + result


ui.label('Welcome to the Wikipedia name game')

with ui.dialog() as dialog, ui.card():
    ui.label(hint_1)
    ui.button('Close', on_click=dialog.close)
ui.button('Click for First Hint', on_click=dialog.open)

ui.input(label='Guess 1', placeholder='press ENTER to apply',
         on_change=lambda e: input_result.set_text(guess(e.value)))
input_result = ui.label()    

with ui.dialog() as dialog, ui.card():
    ui.label(hint_2)
    ui.button('Close', on_click=dialog.close)
ui.button('Click for Second Hint', on_click=dialog.open)

ui.input(label='Guess 2', placeholder='press ENTER to apply',
         on_change=lambda e: input_result.set_text(guess(e.value)))
input_result = ui.label()    

with ui.dialog() as dialog, ui.card():
    ui.label(hint_3)
    ui.button('Close', on_click=dialog.close)
ui.button('Click for Third Hint', on_click=dialog.open)

ui.input(label='Guess 3', placeholder='press ENTER to apply',
         on_change=lambda e: input_result.set_text(guess(e.value)))
input_result = ui.label()    

with ui.dialog() as dialog, ui.card():
    ui.label(hint_4)
    ui.button('Close', on_click=dialog.close)
ui.button('Click for Final Hint', on_click=dialog.open)

ui.input(label='Guess 4', placeholder='press ENTER to apply',
         on_change=lambda e: input_result.set_text(final_guess(e.value)))
input_result = ui.label()  

ui.run()