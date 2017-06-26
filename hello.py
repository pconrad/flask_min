from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def home():
  return current_app.send_static_file('index.html')
