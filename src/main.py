from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values, load_dotenv
import os

config = dotenv_values("src/.env")

app = Flask(__name__)

openai.api_key = config['API_KEY']
conversations = []

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = 'Yo: ' + request.form['question'] 
        print("incoming: ", question)
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            presence_penalty = 0.6
        )
        answer = 'Misa Bot: ' + response.choices[0].text.strip()
        print("outcoming: ", answer)

        conversations.append(question)
        conversations.append(answer)

        return render_template('index.html', chat=conversations)
    else: 
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)