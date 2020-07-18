from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField,BooleanField

fonts = []
numbs = [x for x in range(1,16)]
font_size = [2*x for x in range(6,38)] 
with open("static/fonts.txt", "r") as font_file: # fonts.txt stores all the fonts
    fonts_list = font_file.read()
    fonts = fonts_list.split("\n")


class FileForm(FlaskForm):

    exp_num = SelectField("Number of experiments: ", choices=numbs)

    # Aim of the Experiments
    aim_font = SelectField("Font of the aim of the experiment : ", choices=fonts)
    aim_size =  SelectField("Size of the font of the aim: ", choices=font_size)
    aim_alignment = RadioField(" Alignment: ", choices=["Left", "Center"])
    aim_bold = BooleanField("Bold: ")
    aim_italics = BooleanField("Italics: ")
    aim_underline = BooleanField("Underline: ")

    # the word "CODE"
    word_code_font = SelectField("Font of the word 'code' : ", choices=fonts)
    word_code_size =  SelectField("Size of the font of the word 'CODE' : ", choices=font_size)
    word_code_alignment = RadioField(" Alignment: ", choices=["Left", "Center"])
    word_code_bold = BooleanField("Bold: ")
    word_code_italics = BooleanField("Italics: ")
    word_code_underline = BooleanField("Underline: ")

    # CODE
    code_font = SelectField("Font of the code : ", choices=fonts)
    code_size =  SelectField("Size of the font of the code : ", choices=font_size)
    code_alignment = RadioField(" Alignment: ", choices=["Left", "Center"])
    code_bold = BooleanField("Bold: ")
    code_italics = BooleanField("Italics: ")
    code_underline = BooleanField("Underline: ")

    # word "OUTPUT"
    word_output_font = SelectField("Font of the word_output : ", choices=fonts)
    word_output_size =  SelectField("Size of the font of the word_output : ", choices=font_size)
    word_output_alignment = RadioField(" Alignment: ", choices=["Left", "Center"])
    word_output_bold = BooleanField("Bold: ")
    word_output_italics = BooleanField("Italics: ")
    word_output_underline = BooleanField("Underline: ")

    submit = SubmitField("Create Practical File Template")