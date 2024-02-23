from flask import Blueprint, render_template,abort,jsonify,request
from jinja2 import TemplateNotFound
from flask_cors import CORS


woordenlijstFrans_bp = Blueprint("talenPagina",__name__ , url_prefix='/api')

#talenPagina.route('/', defaults={'page' : 'index'})    

@woordenlijstFrans_bp.route('/woordenlijst')
def woordenlijstFrans():
    lijnen = []
    woordenschat = []
    lijst = open('./data/feest.txt','r')    
    lijnen = [lijn.rstrip("\n") for lijn in lijst]    
    for woordcombi in lijnen:
        wc = woordcombi.split(',')          
        woordenschat.append({'nederlands': wc[0],'frans': wc[1]})
            
    return jsonify(woordenschat)
    
@woordenlijstFrans_bp.route('/addwordcombination',methods=['post'] )    
def addwoordencombinatie():
    data = request.json 
    print(data)
    nederlands = data.get('nederlands')
    frans = data.get('frans')    
    return jsonify('Ok')
