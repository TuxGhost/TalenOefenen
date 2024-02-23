from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from requests.auth import HTTPBasicAuth
from flask_cors import CORS
from logging.config import dictConfig
import requests
import random
import TaalModelPage
from webapi.woordenlijstFrans import woordenlijstFrans_bp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import MetaData, Table
from flask import jsonify
import os
import WoordCombinatie

random.seed()
app = Flask(__name__)

app.secret_key ="abcdefghijklmnopqrstuvwxyz"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///d:\\sources\\Python\\TalenOefenen\\woordCombinaties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

app.register_blueprint(woordenlijstFrans_bp)

woordenGenereren = True
fr = []
nl = []
en = []
Enl = []
lijstFr = open('./data/feest.txt','r')
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
oplossing =''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Frans', methods = ['GET'])
def frans():
    lengte = len(nl)
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
    return render_template('TaalFR.html', title='Quiz Frans', model = taalModelPage)

@app.route('/Engels', methods = ['GET'])
def engels():
    lengte = len(Enl)-1
    optieA = random.randint(0,lengte)
    optieB = random.randint(0,lengte)  
    optieC = random.randint(0,lengte)
    optieABC = random.randint(0,2)
    while optieA == optieB or optieB == optieC or optieC == optieA:
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
    taalModelPage =  TaalModelPage.TaalModelPage()
    taalModelPage.Vraag = engelsWoord
    taalModelPage.Antwoord = oplossingA
    taalModelPage.Antiwoord = oplossingB
    taalModelPage.Woordant = oplossingC
    return render_template('TaalEN.html', title='Quiz Engels', vraag = engelsWoord , antwoord = oplossingA, antiwoord = oplossingB, woordant = oplossingC,model = taalModelPage)

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
    antwoord = request.form.get("antwoord")
    opl = session.get("oplossing")
    print("oplossing: ")
    print(opl)
    tekst = 'Wat denk je zelf?'
    if antwoordA == session["oplossing"] or antwoordB == session["oplossing"] or antwoordC== session["oplossing"]:
        tekst = 'Uw antwoord is correct.'
    else:
        tekst = 'Uw antwoord is fout.'
    return render_template('controleerEN.html', title = 'controle', tekst = tekst)

# show list of words 
@app.route("/woordenlijst")
def woordenlijst():        
    try:        
        url = request.host_url + "woordenlijstjson"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()        
            return render_template("woordenlijst.html",woordcombinatie = json_data)
        else:    
            return render_template("woordenlijst.html")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# retrieve list of word combination in json format
@app.route("/woordenlijstjson")
def woordenlijstjson():
    try:                
        connection = db.engine.raw_connection()
        cursor = connection.cursor()        
        cursor.execute('SELECT Nederlands, Frans from WoordCombinaties')        
        result = cursor.fetchall()        
        cursor.close()
        connection.close()        
        data = []
        for woord in result:    
            woordCombinatie = {
                    'nederlands':  woord[0],
                    'frans': woord[1]                               
                }            
            data.append(woordCombinatie )
        return jsonify(data);            
    except Exception as e:        
        error_text = f"<p>{str(e)}</p>"
        print(f"An error occurred: {e}")
        return jsonify({"result" : "error", "message": str(e)})
@app.route("/db")
def dbinfo():
    try:
        database_path = os.path.abspath(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
        #folder_contents = os.listdir(database_folder)
        database_folder = os.path.dirname(database_path)        
        metadata = MetaData()
        metadata.reflect(bind=db.engine)
        table_names = metadata.tables.keys()
        return jsonify( {"result":"success", "tables": list(table_names) , "databaseFolder": database_folder })
    except Exception as e:        
        error_text = f"<p>{str(e)}</p>"
        print(f"An error occurred: {e}")
        return jsonify({"result" : "error", "message": str(e)})

@app.route("/nieuw")
def nieuwwoord():    
    return render_template("woordcombinationCreate.html")    

@app.route("/nieuwwoordpost",methods=['POST'])
def nieuwwoordPost():
    urlAction = request.host_url + "addwordcombination"
    nederlands = request.form.get("nederlands")
    frans = request.form.get("frans") 
    nieuw = { "nederlands": nederlands , "frans": frans}   
    try: 
        auth = HTTPBasicAuth('root','password')
        headers = {'Content-Type': 'application/json' , 'Accept': 'text/plain'}        
        response = requests.post(urlAction,  json=nieuw, auth=auth , headers=headers)
        print(f"{response}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template("woordcombinationCreate.html")    

# post data to the database table
@app.route('/addwordcombination',methods=['post'] )    
def addwoordencombinatie():
    data = request.json     
    nederlands = data.get('nederlands')
    frans = data.get('frans')
    try:
        connection = db.engine.raw_connection()
        cursor = connection.cursor()        
        cursor.execute('INSERT into WoordCombinaties ("nederlands", "frans") values (?, ? )', (nederlands,frans))                
        connection.commit()        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
    return jsonify('Ok')


@app.errorhandler(500)
def foutboodschap(error):
    render_template("error.html"),500

# run module as an application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001 ,debug=True)