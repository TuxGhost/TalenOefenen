from flask import Flask
from flask import render_template
from flask import request
import random

app = Flask(__name__)

fr = []
nl = []
tekstJ = 'correct.'
tekstF = 'incorrect.'
score = 0

lijst = open('data\Het eten.txt','r')
for text in lijst:
    w = text.split(",")
    nl.append(w[0])
    fr.append(w[1].replace("\n", "")) 

lengte = len(fr)
optieA = random.randint(0,lengte)
optieB = random.randint(0,lengte)  
optieC = random.randint(0,lengte) 
optieABC = random.randint(0,2)
if optieA == optieB or optieB == optieC or optieC == optieA:
    optieA = random.randint(0,lengte)
    optieB = random.randint(0,lengte)  
oplossingA = nl[optieA]
oplossingB = nl[optieB]
oplossingC = nl[optieC]
if optieABC == 0:
    fransWoord = fr[optieA]
    oplossing = 'A'
if optieABC == 1:
    fransWoord = fr[optieB]
    oplossing = 'B'
if optieABC == 2:
    fransWoord = fr[optieC]
    oplossing = 'C'

@app.route('/')
def index():
    return render_template('Frans.html', title='Quiz', vraag = fransWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC)

@app.route('/Frans', methods = ['GET'])
def frans():
    return render_template('Frans.html', title='Quiz', vraag = fransWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC)

        
@app.route('/controleer',methods=['POST'])
def controleer():
    antwoord = request.form.get("antwoord")
    tekst = 'Wat denk je zelf?'
    if antwoord == oplossing:
        tekst = 'Uw antwoord is correct.'
    else:
        tekst = 'Uw antwoord is foutief.'
    return render_template('controleer.html', title = 'controle', tekst = tekst)

app.run(host='0.0.0.0', port=9001)