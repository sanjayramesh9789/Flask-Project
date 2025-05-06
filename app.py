from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/add-product')
def add_product():
    return render_template('add_product.html')
@app.route('/add-location')
def add_location():
    return render_template('add_location.html')
@app.route('/add-movement')
def add_movement():
    return render_template('add_movement.html')
    
if __name__ == '__main__':
    app.run(debug=True)
