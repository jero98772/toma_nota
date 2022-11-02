import asyncio
from flask import Flask
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
	return "hello"
@app.route('/2', methods=['GET', 'POST'])
def index2():
	return redirect("/")
		

async def main():
	print("hello")

print(main())

if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=9600)