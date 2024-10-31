from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
feedback_list = []
class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        feedback = form.feedback.data
        feedback_list.append({'name': name, 'feedback': feedback})
        return redirect(url_for('feedback'))
    return render_template('q8.html', form=form, feedback_list=feedback_list)

app.run(debug=True)
