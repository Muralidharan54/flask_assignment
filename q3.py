from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde' 

class CalculatorForm(FlaskForm):
    num1 = DecimalField('Num 1', validators=[DataRequired()])
    num2 = DecimalField('Num 2', validators=[DataRequired()])
    submit = SubmitField('Calculate')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    result = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        result = num1 + num2  

    return render_template('q3.html', form=form, result=result)

app.run(debug=True)
