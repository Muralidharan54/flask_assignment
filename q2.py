from flask import Flask,render_template
app=Flask(__name__)

name="Muralidharan V"
age="21"
Hobbies="Playing Cricket, Listening to Music"
@app.route('/bio')
def bio():
    return render_template('q2.html',name=name,age=age,hobbies=Hobbies)
app.run(debug=True)