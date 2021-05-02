from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Main Site under construction</h1>'

@app.errorhandler(404)
def msg(err):
  return 'Page under construction!'

if __name__=='__main__':
  app.run(debug=True)
  
