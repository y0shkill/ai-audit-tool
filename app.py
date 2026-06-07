from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/audit', methods=['POST'])
def audit():
    text = request.form.get('text')
    # Lógica de auditoria simplificada
    score = 85 if len(text) > 100 else 40
    return {"score": score}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
