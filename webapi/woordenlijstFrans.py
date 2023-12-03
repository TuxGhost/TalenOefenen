from flask import Blueprint, render_template,abort,jsonify
from jinja2 import TemplateNotFound

woordenlijstFrans_bp = Blueprint("talenPagina",__name__)

#talenPagina.route('/', defaults={'page' : 'index'})    

@woordenlijstFrans_bp.route('/woordenlijst')
def woordenlijstFrans():
    lijnen = []
    woordenschat = []
    lijst = open('./data/feest.txt','r')    
    lijnen = [lijn.rstrip("\n") for lijn in lijst]    
        
            
    return jsonify(lijnen);
    
    