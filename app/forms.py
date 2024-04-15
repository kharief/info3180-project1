from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, DecimalField, FloatField, SelectField, FileField
from wtforms.validators import InputRequired, Length, Email

from flask_wtf.file import FileField, FileRequired, FileAllowed

i=1

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    numrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    numbathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price',validators=[InputRequired()],places=2,rounding=2)

    myChoices = [('House', 'House'), ('Apartment', 'Apartment')]
    propertytype = SelectField(u'Property Type', choices = myChoices, validators = [InputRequired()])

    location = StringField('Location', validators=[InputRequired()])

    propertypic = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only Images.')])



    

