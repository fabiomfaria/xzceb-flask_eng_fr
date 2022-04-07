from machinetranslation import translator
from flask import Flask, render_template, request
from translator import english_to_french, french_to_english
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text_In_French = english_To_French(textToTranslate)
    return text_In_French

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    text_In_English = french_to_english(textToTranslate)
    return text_In_English

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
