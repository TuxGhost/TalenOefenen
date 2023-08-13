from flask import Flask
from flask import render_template
from flask import request
import random

app = Flask(__name__)

fr = []
nl = []
fake1 = []
fake2 = []
hoeveelste = 0
how = 0
many = 0
#question = fransWoord[willekeurig]
@app.route('/')
@app.route('/index')

def index():
    if request.method ==  "GET":
        hoeveelste = random.randint(0,165)
        how = random.randint(0,165)
        many = random.randint(0,165)
        fake1 = nl[how]
        fake2 = nl[many]
        fransWoord = fr[hoeveelste]
        nederlandsWoord = nl[hoeveelste]
        return render_template('index.html', title='Quiz', vraag = fransWoord , antwoord = nederlandsWoord, fout = fake1, wrong = fake2)    
    else:
        return render_template('index.html', title='Quiz', vraag = fransWoord , antwoord = nederlandsWoord, fout = fake1, wrong = fake2)    
    #return 'Web app with python Flask!'

@app.route('/controleer',methods=['POST'])
def controleer():
    #antwoord = request.forms['antwoord']
    antwoord = request.form.get("antwoord")
    return 'functie moet verder uitgewerkt worden'

lijst = open('Het eten.txt','r')
for text in lijst:
    w = text.split(",")
    nl.append(w[0])
    fr.append(w[1].replace("\n", "")) 

  

app.run(host='0.0.0.0', port=9001)