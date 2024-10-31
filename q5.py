from flask import Flask, render_template
import random

app = Flask(__name__)
quotes = [
    "The best way to predict the future is to invent it.",
    "Do one thing every day that scares you.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your time is limited, so don't waste it living someone else's life.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream."
]

@app.route('/quote')
def quote():
    random_quote = random.choice(quotes)
    return render_template('q5.html', quote=random_quote)

app.run(debug=True)
