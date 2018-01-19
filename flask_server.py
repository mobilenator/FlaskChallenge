from flask import Flask
app = Flask(__name__)
@app.route("/lowercase", methods=['Post'])
def lowercase():
    content = request.get_json
    print (content)
    return "Hello World!"

if __name__ == "__main__":
    app.run()
