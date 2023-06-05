from flask import Flask, Response, render_template, request
from flask_cors import CORS
from antlr.translator import translator
from antlr.translator import translatorTesting

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/test')
def test():
    translatorTesting()
    return 'Hola testing'

@app.route('/translate', methods =['POST'])
def trans():
    if request.method == 'POST':
        alldata = request.get_json()
        try:
            myres = translator(alldata['data'])
            return({'data': myres})
        except:
            return Response('Server Error', status=500)
        
    else:
        return Response('Bad request', status=400)  


if __name__ == '__main__':
    app.run(port=5000)
