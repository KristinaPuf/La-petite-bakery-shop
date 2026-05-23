from flask import Flask, render_template

app = Flask(__name__)

# Ovo je početna strana
@app.route('/')
def home():
    return render_template('index.html')

# Ovo su stranice za svaki proizvod
@app.route('/croissant')
def croissant():
    return render_template('croissant.html')

@app.route('/cupcake')
def cupcake():
    return render_template('cupcake.html')

@app.route('/macarons')
def macarons():
    return render_template('macarons.html')

@app.route('/cake')
def cake():
    return render_template('cake.html')

@app.route('/biscuits')
def biscuits():
    return render_template('biscuits.html')

@app.route('/bread')
def bread():
    return render_template('bread.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

    #test