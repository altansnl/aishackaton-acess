from flask import Flask, render_template, request
from pdfreader import SimplePDFViewer
import summarize
from pdf_to_text import convert
from scrap import scrap_articles
import re

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        if not f:
            return render_template("index.html", data={})
        
        filepath = 'pdfs/' + f.filename
        f.save(filepath) 
        text = convert(filepath)
        summary = re.sub('<.*?>', "", summarize.summarizeWithT5(text, summarize.model_imported, summarize.tokenizer))
        keyword_list = [''.join(filter(str.isalpha, s)) for s in summary.split(" ")[-3:]]
        related_papers = scrap_articles(keyword_list)
        data = {
            "summary": summary,
            "paper1_name": related_papers[0][0],
            "paper1_url": related_papers[0][1],

            "paper2_name": related_papers[1][0],
            "paper2_url": related_papers[1][1],

            "paper3_name": related_papers[2][0],
            "paper3_url": related_papers[2][1],

            "paper4_name": related_papers[3][0],
            "paper4_url": related_papers[3][1]
        }
        return render_template("index_filled.html", data=data)  
