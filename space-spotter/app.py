from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/parking-grid')
def parking_grid():
    return render_template('parking-grid.html')



if __name__ == '__main__':
    app.run(debug=True)