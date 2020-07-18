import os
from flask import Flask, render_template, redirect, url_for, send_from_directory,after_this_request
from form import FileForm
from file_create import PracFile
from varstore import aim,word_code,code,word_output
import secrets 
import string 

file_name = ""

app =Flask(__name__)
app.config['SECRET_KEY'] = "885eeereg5646456wreef5656egege"
app.config['UPLOAD_PATH'] = "static/uploads/" # Directory where Doc files are stored temporarily 

@app.route("/")
@app.route("/about")    # About Page
def about():
    return render_template("about.html")

@app.route("/download")
def download():
    global file_name 
    @after_this_request # Special Decorator which incovoces the contained function after the request to which it is applied
    def remove_file(response):
        try:
            os.remove(os.path.dirname(__file__) + f"/static/uploads/{ file_name }")
            file_handle.close() # Removing the temp Doc file that is  generated
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    return send_from_directory(app.config['UPLOAD_PATH'], filename = file_name, as_attachment=True)
    


@app.route("/create", methods=["GET", "POST"])
def create_file():
    form = FileForm()
    global file_name # refereing to the global variable

    if form.is_submitted():

        var_list = [] # All the variables will be passed as a list
        l1 = aim(form)
        var_list.append(l1)
        l2 = word_code(form)
        var_list.append(l2)
        l3 = code(form)
        var_list.append(l3)
        l4 = word_output(form)
        var_list.append(l4)

        num_prac = int(form.exp_num.data)
        
        # Generating Random File name to avoid parellel Request Clash
        file_name = ''.join(secrets.choice(string.ascii_lowercase + string.digits) 
                                                  for i in range(num_prac)) 
        
        file_name = str(file_name) + ".docx"
        file = PracFile() # Object of class from the Script
        file.create_exp(num_prac=num_prac, var_list=var_list, file_name=file_name)
        

        try:
            return redirect(url_for('download'))

        except Exception as e:
            return str(e)

        
    return render_template("create.html", form=form)  



if __name__ == '__main__':
    app.run()

