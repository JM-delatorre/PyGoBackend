from flask import Flask, render_template
from antlr.translator import translator
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  translator()
  return 'Hola pene'

if __name__ == '__main__':
  app.run(port=5000)
