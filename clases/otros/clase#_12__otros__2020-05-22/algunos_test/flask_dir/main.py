from flask import Flask,abort,render_template,request,redirect,url_for,send_from_directory
import os
app=Flask(__name__)
isFile=lambda x: not os.path.isdir(x)
isFolder=lambda x:  os.path.isdir(x)
addPath=lambda x,y: x+y 

@app.route('/', methods=['GET', 'POST'])
#this work for B-feelLog
def index():
	directory=os.getcwd()+"/uploads"
	directories=os.listdir(directory)
	files=list(filter(isFile,directories))
	files.sort()
	folders=list(filter(isFolder,directories))
	return render_template("index.html",files=files,folders=folders)
	

@app.route('/files/<string:path>', methods=['GET', 'POST'])
def filesistem(path):
	directory=os.getcwd()+"/"+path
	names=os.listdir(directory)
	directories=[]
	for i in range(len(names)):
		directories.append(os.getcwd()+"/"+path+"/"+names[i])
	files=list(filter(isFile,directories))
	folders=list(filter(isFolder,directories))
	htmlCode=""
	for i in folders:
		htmlCode+='<a href="/files/'+i+'">'+i+'</a><br>'
	#for i in files:	
	#'<a href="/files/{{ i }}">{{ i }}</a><br>'
	return render_template("index.html",files=files,folders=folders)

@app.route('/sendfile/<string:path>', methods=['GET', 'POST'])
def sfile(path):
	slash=0
	file=""
	for i in range(len(path)):
		if path[i]=="/":
			slash=i
		if path[i]==".":
			file=path[slash:]
	print(file)
	return send_from_directory(directory=path, path=file, as_attachment=True, cache_timeout=0)

@app.route('/download/<filename>', methods = ["GET", "POST"])
def download(filename):
	fname="uploads/"+filename
	uploads = os.path.join(app.root_path, "")
	print(fname,uploads)
	return send_from_directory(directory=uploads,path=fname,as_attachment=True)
if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=9600)
