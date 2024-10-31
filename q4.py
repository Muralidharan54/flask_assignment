from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde' 

tasks = []

class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    form = TaskForm()
    if form.validate_on_submit():
        tasks.append(form.task.data)
        return redirect(url_for('todo'))  

    return render_template('q4.html', form=form, tasks=tasks)

app.run(debug=True)
