from flask import Flask, request
import json
import pickle
import re


from sklearn.datasets import load_iris
import pickle

from transformers import BertForSequenceClassification, AdamW, BertConfig

model = BertForSequenceClassification.from_pretrained('DeepPavlov/rubert-base-cased/', local_files_only=True)

app = Flask(__name__)


@app.route('/')
def hello():
    return "Rubert RusCola server"

@app.route('/rubert', methods=["GET", "POST"])
def iris():
    if request.method == 'POST':
        data = request.get_json(force=True)
        y_hat = clf.predict([data['iris']])
        response = {
            "result": y_hat
        }

        return json.dumps(response)
    else:
        return "You should use only POST query"

if __name__ == '__main__':
#     app.run("0.0.0.0", 8000)
    app.run("localhost", 8000)
