from flask import Flask
from flask import render_template
from flask import request
from flask import session
import random
import TaalModelPage

random.seed()
app = Flask(__name__)
app.secret_key ="abcdefghijklmnopqrstuvwxyz"

woordenGenereren = True
fr = []
nl = []
en = []
Enl = []
lijstFr = open('./data/Het eten.txt','r')
for text in lijstFr:
    w = text.split(",")
    nl.append(w[0])
    fr.append(w[1].replace("\n", "")) 
lijstEn = open('./data/The food.txt','r')
for text in lijstEn:
    w = text.split(",")
    Enl.append(w[0])
    en.append(w[1].replace("\n", "")) 
tekstJ = 'correct.'
tekstF = 'incorrect.'
score = 0

oplossing =''
test = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Frans', methods = ['GET'])
def frans():
    lengte = len(nl)-1
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
    taalModelPage =  TaalModelPage.TaalModelPage()
    taalModelPage.Vraag = fransWoord
    taalModelPage.Antwoord = oplossingA
    taalModelPage.Antiwoord = oplossingB
    taalModelPage.Woordant = oplossingC
    return render_template('TaalFR.html', title='Quiz Frans', vraag = fransWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC, model = taalModelPage)

@app.route('/Engels', methods = ['GET'])
def engels():
    lengte = len(Enl)-1
    optieA = random.randint(0,lengte)
    optieB = random.randint(0,lengte)  
    optieC = random.randint(0,lengte) 
    optieABC = random.randint(0,2)
    if optieA == optieB or optieB == optieC or optieC == optieA:
        optieA = random.randint(0,lengte)
        optieB = random.randint(0,lengte)  
    oplossingA = Enl[optieA]
    oplossingB = Enl[optieB]
    oplossingC = Enl[optieC]
    if optieABC == 0:
        engelsWoord = en[optieA]
        session["oplossing"] = 'A'
    if optieABC == 1:
        engelsWoord = en[optieB]
        session["oplossing"] = 'B'
    if optieABC == 2:
        engelsWoord = en[optieC]
        session["oplossing"] = 'C'
    
    return render_template('TaalEN.html', title='Quiz Engels', vraag = engelsWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC)

@app.route('/Duits', methods = ['GET'])
def duits():
    return render_template('Duits.html', title='Quiz Duits')

@app.route('/controleerFR',methods=['POST'])
def controleerFR():
    antwoordA = request.form.get("antwoordA")
    antwoordB = request.form.get("antwoordB")
    antwoordC = request.form.get("antwoordC")
    opl = session.get("oplossing")
    print("oplossing: ")
    print(opl)
    tekst = 'Wat denk je zelf?'
    if antwoordA == session["oplossing"] or antwoordB == session["oplossing"] or antwoordC== session["oplossing"]:
        tekst = 'Uw antwoord is correct.'
    else:
        tekst = 'Uw antwoord is fout.'
    return render_template('controleerFR.html', title = 'controle', tekst = tekst)

@app.route('/controleerEN',methods=['POST'])
def controleerEN():
    antwoordA = request.form.get("antwoordA")
    antwoordB = request.form.get("antwoordB")
    antwoordC = request.form.get("antwoordC")
    opl = session.get("oplossing")
    print("oplossing: ")
    print(opl)
    tekst = 'Wat denk je zelf?'
    if antwoordA == session["oplossing"] or antwoordB == session["oplossing"] or antwoordC== session["oplossing"]:
        tekst = 'Uw antwoord is correct.'
    else:
        tekst = 'Uw antwoord is fout.'
    return render_template('controleerEN.html', title = 'controle', tekst = tekst)

app.run(host='0.0.0.0', port=9001)