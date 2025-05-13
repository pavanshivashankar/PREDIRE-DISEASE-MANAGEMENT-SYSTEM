
from asyncio.windows_events import NULL
from email.policy import default
from importlib.resources import path
import mimetypes
from re import template
from flask import Flask, request, Response, render_template
import pickle
import numpy as np
import os.path
import subprocess
from sklearn.ensemble import RandomForestRegressor


model = pickle.load(open('model.pkl', 'rb'))

template_dir = 'C:/Users/nisha/OneDrive/Desktop/ML Final Code project/templates'
app = Flask(__name__, static_url_path ='/static', template_folder = template_dir)

app.config.from_object(__name__)


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['Symptom1']
    data2 = request.form['Symptom2']
    data3 = request.form['Symptom3']
    data4 = request.form['Symptom4']
    data5 = request.form['Symptom5']
    data6 = 0
    data7 = 0
    data8 = 0
    data9 = 0
    data10 = 0
    data11 = 0
    data12 = 0
    data13 = 0
    data14 = 0
    data15 = 0
    data16 = 0
    data17 = 0
    if (data1 == data2 and data2 == data3 and data3 == data4 and data4 == data5 and data5 == data1):
         return render_template('predictionPage.html', prediction_text='Predicted Disease is {}'.format(data1))
    else :    
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17]])

        pred = model.predict(arr)
        
        return render_template('predictionPage.html', prediction_text='Predicted Disease is {}'.format(pred),)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')    

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/predictionPage')
def prediction_page():
    return render_template('/predictionPage.html')

@app.route('/blog')
def blog_page():
    return render_template('/blog.html')


@app.route('/contactUs')
def contactUs_page():
    return render_template('contactUs.html')

@app.route('/contact-form.php')
def contact_form():
    cmd = ["php", "./contactact-form.php"]
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    script_response = proc.stdout.read()
    subprocess.call("php contact-form.php")

# @app.route('/contact-form.php')
# def contact_form():
#     cmd = ["php", "./contactact"]
#     proc = subprocess.Popen("php C:/Users/nisha/OneDrive/Desktop/BE Project final (2)/BE Project final/BE Project/TY Project/templates/contact-form.php", shell=True, stdout=subprocess.PIPE)
#     script_response = proc.stdout.read()
#     subprocess.call("php C:/Users/nisha/OneDrive/Desktop/BE Project final (2)/BE Project final/BE Project/TY Project/templates/contact-form.php")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)





