from flask import Flask,abort,render_template,request,redirect,url_for,send_from_directory
import os
app=Flask(__name__)
isFile=lambda x: not os.path.isdir(x)
@app.route('/index', methods=['GET', 'POST'])
def index():
	directory=os.getcwd()
	#directies=os.listdir()
	directories=list(os.walk(directory))
	print(directories)
	files=list(filter(isFile,directories))
	return render_template("index.html",fs=files)
	
if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=9600)
