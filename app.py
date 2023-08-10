from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

fr = []
nl = []
answerB = []
answerC = []
vertaalWoord = 0
optieB = 0
optieC = 0
lengte = len(nl)
@app.route('/')
@app.route('/index')





def index():
    vertaalWoord = random.randint(0,165)
    optieB = random.randint(0,165)
    optieC = random.randint(0,165)
    answerB = nl[optieB]
    answerC = nl[optieC]
    fransWoord = fr[vertaalWoord]
    nederlandsWoord = nl[vertaalWoord]
    return render_template('index.html', title='Quiz', vraag = fransWoord , antwoord = nederlandsWoord, fout = answerB, incorrect = answerC)
    #return 'Web app with python Flask!'

lijst = open('Het eten.txt','r')
for text in lijst:
    w = text.split(",")
    nl.append(w[0])
    fr.append(w[1].replace("\n", "")) 

  

app.run(host='0.0.0.0', port=9001)