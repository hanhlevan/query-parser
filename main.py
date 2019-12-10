from flask import Flask
from flask import request, jsonify
from models.correct import Correct

class App:

	def __init__(self):
		self.correcter = Correct()
	
	def search(self, text):
		queries = self.correcter.predict(text)
		print(queries)
		return queries

_app = App()
app = Flask(__name__)
@app.route("/", methods=['POST'])
def search():
    if request.method == "POST":
        query = request.form.get('query')
        data = _app.search(query)
        return jsonify(isError=False, message="Success", statusCode=200, data=data), 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8082")