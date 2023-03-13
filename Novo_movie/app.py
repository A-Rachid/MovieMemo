from flask import Flask, request, render_template
import openai

app = Flask(__name__)
app.debug = True

# Définir votre clé API OpenAI
openai.api_key = "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"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/support.html', methods=['GET'])
def support():
    return render_template('new/support.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    # Récupérer le prompt à partir du corps de la requête
    prompt = request.json.get('prompt')
    
    # Vérifier si le texte contient les mots-clés pertinents pour une recherche de film
    if "description" not in prompt.lower() and "film" not in prompt.lower() and "série" not in prompt.lower():
        return "Je ne comprends pas votre demande. Veuillez fournir une description de film."
    
    # Appeler l'API OpenAI pour générer une réponse basée sur le prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Récupérer la réponse de l'API OpenAI
    title = response.choices[0].text

    # Renvoyer le titre en tant que réponse HTTP
    return title

if __name__ == '__main__':
    app.run()
