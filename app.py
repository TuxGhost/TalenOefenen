from flask import Flask
from flask import render_template
from flask import request
from flask import session
import random

random.seed()

app = Flask(__name__)
app.secret_key ="abcdefghijklmnopqrstuvwxyz"

woordenGenereren = True
fr = []
nl = []
lijst = open('./data/Het eten.txt','r')
for text in lijst:
    w = text.split(",")
    nl.append(w[0])
    fr.append(w[1].replace("\n", "")) 
tekstJ = 'correct.'
tekstF = 'incorrect.'
score = 0
lengte = len(fr)
oplossing =''


test = ""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Frans', methods = ['GET'])
def frans():
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
        session["oplossing"] = 'A'
    if optieABC == 1:
        fransWoord = fr[optieB]
        session["oplossing"] = 'B'
    if optieABC == 2:
        fransWoord = fr[optieC]
        session["oplossing"] = 'C'
    return render_template('Frans.html', title='Quiz Frans', vraag = fransWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC)

@app.route('/Engels', methods = ['GET'])
def engels():
    return render_template('Engels.html', title='Quiz Engels')

@app.route('/Duits', methods = ['GET'])
def duits():
    return render_template('Duits.html', title='Quiz Duits')

@app.route('/controleer',methods=['POST'])
def controleer():
    antwoord = request.form.get("antwoord")
    opl = session.get("oplossing")
    print("oplossing: ")
    print(opl)
    tekst = 'Wat denk je zelf?'
    if antwoord == session["oplossing"]:
        tekst = 'Uw antwoord is correct.'
    else:
        tekst = 'Uw antwoord is fout.'
    return render_template('controleer.html', title = 'controle', tekst = tekst)

app.run(host='0.0.0.0', port=9001)