from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category=SelectField('category',
       choices=[('Inspiration', 'Inspiration'), ('Pickuplines', 'Pickuplines'), ('Tech', 'Tech'),
        ('411', '411')], validators = [Required()])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')


class ContentForm(FlaskForm):
   content = TextAreaField('YOUR PITCH')
   submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   comment_id = TextAreaField('WRITE COMMENT')
   submit = SubmitField('SUBMIT')