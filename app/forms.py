from flask_wtf import FlaskForm
# from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, FileField, RadioField, SubmitField
from wtforms.validators import DataRequired

class RosterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your name here"})
    rostertype = RadioField('Roster type',choices=['ED','MAPU'] ,validators=[DataRequired()])
    roster = FileField('Upload roster', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('SUBMIT')