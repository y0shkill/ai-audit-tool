import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Landing Page minimalista
INDEX_HTML = """
<!DOCTYPE html>
<html>
<body style="background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:50px;">
    <h1>HumanScore</h1>
    <p>Audit your content for AI-detection penalties.</p>
    <form action="/audit" method="POST">
        <textarea name="text" style="width:80%; height:100px;"></textarea><br>
        <button type="submit" style="padding:10px 20px; margin-top:10px;">Audit</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/audit', methods=['POST'])
def audit():
    text = request.form.get('text', '')
    score = 85 if len(text) > 100 else 40
    return f"<h1>Score: {score}/100</h1><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
