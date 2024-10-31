from flask import Flask, render_template, request, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde' 

class AuthForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password= StringField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/auth', methods=['GET', 'POST'])
def calculator():
    form = AuthForm()
    if form.validate_on_submit():
        u_name=form.username.data
        pwd=form.password.data
        if u_name=="user" and pwd=="password":
            return redirect(url_for('welcome'))


    return render_template('q6.html', form=form)


@app.route('/welcome')
def welcome():
    return "Welcome User!!"
app.run(debug=True)
