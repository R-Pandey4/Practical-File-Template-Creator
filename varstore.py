"""
These Classes are used to sort out 24/26 variables obtained from the form
"""
class aim: 
    
    def __init__(self, form):
        self.message = "Enter the aim of the experiment\n"
        self.font = form.aim_font.data
        self.size = form.aim_size.data
        self.alignment = form.aim_alignment.data
        self.bold = form.aim_bold.data
        self.italics = form.aim_italics.data
        self.underline = form.aim_underline.data

class word_code:
    
    def __init__(self, form):
        self.message = "CODE\n"
        self.font = form.word_code_font.data
        self.size = form.word_code_size.data
        self.alignment = form.word_code_alignment.data
        self.bold = form.word_code_bold.data
        self.italics = form.word_code_italics.data
        self.underline = form.word_code_underline.data


class code:
    
    def __init__(self, form):
        self.message = "Select this piece of text and Paste your code from IDE or Text Editor here ,with option unformated(Libre Office) or merge formating(Microsoft Word) \n\n"
        self.font = form.code_font.data
        self.size = form.code_size.data
        self.alignment = form.code_alignment.data
        self.bold = form.code_bold.data
        self.italics = form.code_italics.data
        self.underline = form.code_underline.data


class word_output:
    
    def __init__(self, form):
        self.message = "OUTPUT\n"
        self.font = form.word_output_font.data
        self.size = form.word_output_size.data
        self.alignment = form.word_output_alignment.data
        self.bold = form.word_output_bold.data
        self.italics = form.word_output_italics.data
        self.underline = form.word_output_underline.data
