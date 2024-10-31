from flask import Flask, render_template
app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 22, 'city': 'Los Angeles'}]

@app.route('/user_table')
def user_table():
    return render_template('q9.html', users=users)
app.run(debug=True)
