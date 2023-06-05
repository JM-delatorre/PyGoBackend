from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  return 'Hola pene'

if __name__ == '__main__':
  app.run(port=5000)
