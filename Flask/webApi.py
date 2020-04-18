import flask
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route('/', methods=["GET"])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di WebAPI</p>"

@app.route('/allBooks', methods=["GET"])
def api_all():
    return jsonify(books)

@app.route('/ricercaId',methods=["GET"])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: no id field provided. Please specify an id"
    
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    
    print(str(request.args))

    return jsonify(results)

books = [{'id': 0,'title': 'Il nome della Rosa','author': 'Umberto Eco','year_published': '1980'},
         {'id': 1,'title': 'Il problema dei tre corpi','author': 'Liu Cixin','published': '2008'},     
         {'id': 2,'title': 'Fondazione','author': 'Isaac Asimov','published': '1951'} 
        ] 

app.run()
