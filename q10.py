from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
class TempForm(FlaskForm):
    celsius = StringField('Celsius', validators=[
        DataRequired(),
        Regexp(r'^-?\d*(\.\d+)?$', message="Please enter a valid number.")
    ])
    submit = SubmitField('Convert')

@app.route('/temp_convert', methods=['GET', 'POST'])
def converter():
    form = TempForm()
    fahrenheit = None 
    if form.validate_on_submit():
        celsius = float(form.celsius.data)
        fahrenheit = (celsius * 9/5) + 32  
    return render_template('q10.html', form=form, fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
