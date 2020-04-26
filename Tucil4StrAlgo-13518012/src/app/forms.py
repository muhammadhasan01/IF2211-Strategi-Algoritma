from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class inputForm(FlaskForm):
    filenames = StringField('Filenames', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    algochoice = RadioField('Algorithms',
        choices=[(1, 'Boyer-Moore'), (2, 'KMP'), (3, 'Regex')], default=1, coerce=int) 
    submit = SubmitField('Extract')