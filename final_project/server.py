from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    if textToTranslate.isspace() or len(textToTranslate) == 0 or textToTranslate == None :
        return "Type Something"
    else:
        translated_text = translator.english_to_french(textToTranslate)
    return "Traduction: " + translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    
    if textToTranslate.isspace() or len(textToTranslate) == 0 or textToTranslate == None :
        return "Tape quelque chose"
    else:
        translated_text = translator.french_to_english(textToTranslate)
    return "Translated: " + translated_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
