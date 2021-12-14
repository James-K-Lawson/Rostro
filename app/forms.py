from flask_wtf import FlaskForm
# from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired

class RosterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your name here"})
    roster = FileField('Upload roster', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('SUBMIT')