from flask import Flask, render_template

app = Flask(__name__)

@app.route('/gallery')
def gallery():
    return render_template('q7.html')

app.run(debug=True)
