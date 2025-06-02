from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html') 

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')  

if __name__ == '__main__':
    app.run(debug=True)
