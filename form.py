from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField,BooleanField,FormField

fonts = []
numbs = [x for x in range(1,16)]
font_size = [2*x for x in range(6,38)] 
with open("static/fonts.txt", "r") as font_file: # fonts.txt stores all the fonts
    fonts_list = font_file.read()
    fonts = fonts_list.split("\n")

# Class representing different attributes of at text
class Exp(FlaskForm):
    font = SelectField("Font : ", choices=fonts)
    size =  SelectField("Size of the font : ", choices=font_size)
    alignment = RadioField(" Alignment: ", choices=["Left", "Center"])
    bold = BooleanField("Bold: ")
    italics = BooleanField("Italics: ")
    underline = BooleanField("Underline: ")
    message = ""

# Class representing different parts of an Experiment
# Created Sub-Forms within a form
class FileForm(FlaskForm):

    exp_num = SelectField("Number of experiments: ", choices=numbs)
    aim = FormField(Exp)
    word_code = FormField(Exp)
    code = FormField(Exp)
    word_output = FormField(Exp)
    submit = SubmitField("Create Practical File Template")