from flask_wtf import FlaskForm
from wtforms import StringField, FileField, RadioField, SubmitField
from wtforms.validators import DataRequired

class RosterForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    rostertype = RadioField('Roster Type:',choices=['ED','MAPU'] ,validators=[DataRequired()])
    roster = FileField('Upload Roster', validators=[DataRequired()])
    submit = SubmitField('Run Rostro')