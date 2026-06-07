import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Landing Page minimalista com estilo Linear
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HumanScore | Audit Your Content</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto; background: #000; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { text-align: center; max-width: 600px; padding: 20px; }
        h1 { font-weight: 500; letter-spacing: -1px; font-size: 2.5rem; }
        p { color: #888; margin-bottom: 20px; }
        textarea { width: 100%; height: 150px; background: #111; border: 1px solid #333; color: #fff; padding: 10px; border-radius: 5px; margin-bottom: 15px; }
        button { background: #fff; color: #000; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-weight: 600; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Is your content truly yours?</h1>
        <p>Ensure your brand authority is safe from AI-detection penalties.</p>
        <form action="/audit" method="POST">
            <textarea name="text" placeholder="Paste your content here..."></textarea><br>
            <button type="submit">Start Audit</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/audit', methods=['POST'])
def audit():
    text = request.form.get('text', '')
    # Algoritmo simples de detecção de "Humanidade"
    # Em produção, usaremos lógica baseada em entropia e perplexidade
    score = 85 if len(text) > 100 else 40
    
    # Grava lead num ficheiro local para posterior seguimento
    with open('leads.csv', 'a') as f:
        f.write(f"{score}\n")
        
    return f"<h1>Score: {score}/100</h1><p>Your content has been audited.</p><a href='/'>Go back</a>"

if __name__ == '__main__':
    # O Railway injecta a porta através da variável de ambiente PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
