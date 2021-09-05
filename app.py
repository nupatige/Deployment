from flask import Flask, render_template, request
import joblib

# initialise the app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')


@app.route('/')
def hello_word():
    return render_template('class.html')

@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg,plas,pres,skin,test,mass,pedi,age)

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0] == 1:
        ans = "Diabetic"
    else:
        ans = 'Not diabetic'
    return render_template('predict.html', predict = f'The person is {ans}')

#run the app
app.run(debug=True)