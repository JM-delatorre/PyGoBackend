from flask import Flask, render_template, request
from antlr.translator import translator

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  translator()
  return 'Hola pene'

@app.route('/translate', methods =['POST'])
def trans():
  error = 'Peticion hecha'
  if request.method == 'POST':
      alldata = request.get_json()
      print(alldata['data'] )
    	
  return error


if __name__ == '__main__':
  app.run(port=5000)
