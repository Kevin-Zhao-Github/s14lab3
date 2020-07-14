from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Enter')


class DeleteForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    submit = SubmitField('Delete User', render_kw={"onclick": "confirm('You are about to delete this user.')"}) #Lmao doesn't actually work


class UpdateForm(FlaskForm):
    id = IntegerField('User Id', validators=[DataRequired()])
    first_name = StringField('New Name', validators=[DataRequired()])
    age = IntegerField('New Age', validators=[DataRequired()])
    submit = SubmitField('Update User', render_kw={"onclick": "confirm('You are about to update this user.')"})


class CreateForm(FlaskForm):
    n = IntegerField('Number of users to create', validators=[DataRequired()])
    submit = SubmitField('Create mock users')
