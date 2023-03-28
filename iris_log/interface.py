from flask import Flask, jsonify,request,render_template
from project_data.utils import IrisPrediction
import config

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "welcome to Iris Prediction"

@app.route("/test")
def check():
    return render_template("index.html")

@app.route("/result",methods = ["GET","POST"])
def get_predict_iris():
    # sepal_length=6
    # sepal_width=2.8
    # petal_length=3.1
    # petal_width=0.6 
    if request.method == "POST":
        result= request.form
        sepal_length = result['SepalLengthCm']
        sepal_width = result['SepalWidthCm']
        petal_length = result['PetalLengthCm']
        petal_width = result['PetalWidthCm']

        iris_p = IrisPrediction(sepal_length,sepal_width,petal_length,petal_width)
        species = iris_p.get_species()

    # return jsonify({"return": f"predicted species is : {species}"})
        return render_template("result.html", species = species)

app.run()    
