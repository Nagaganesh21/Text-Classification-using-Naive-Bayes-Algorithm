import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load('nb_text_classifier.pkl')  # loading the saved Naive Bayes Classifier model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    if request.method == "POST":
        input_text = request.form.get('input') # getting input from the form
        
        prediction = model.predict([input_text])

        labels_dict = {0:'Atheism', 
                       1:'Computer graphics', 
                       2:'Computer OS MS Windows', 
                       3:'Computer IBM PC hardware',
                       4:'Computer Mac hardware',
                       5:'Computer Windows.x',
                       6:'For sale', 
                       7:'Autos',
                       8:'Motorcycles',
                       9:'Baseball',
                       10:'Hockey',
                       11:'Crypto',
                       12:'Electronics',
                       13:'Medical',
                       14:'Space',
                       15:'Religion: christian',
                       16:'Politics: guns',
                       17:'Politics:mid east',
                       18:'Politics: misc',
                       19:'Religion: misc'}
        
        result = labels_dict.get(prediction[0])

    return render_template('index.html',
                               prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)