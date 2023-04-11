
from flask import Flask
from transformers import pipeline, set_seed
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    text = request.args.get('text')
    max_length = request.args.get('len')
    num = request.args.get('num')
    if not num:
        num = 1
    else:
        num = int(num)
    if not max_length:
        max_length = 20
    else:
        max_length = int(max_length)
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    return generator(text, max_length=max_length, num_return_sequences=num)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')