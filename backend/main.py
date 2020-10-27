import flask
import json
from postProcess.similarData import getdef
from postProcess.findSimilar import newUrl
import pandas

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, you are on backend flask server"


testDict = [
    {
        'id': 0,
        'data': "test1"
    },
    {
        'id': 1,
        'data': 'test2' 
    }
]

@app.route('/api/test', methods=['GET'])
def test():
    # https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
    #get key from url

    argList = []
    valueList = []

    for arg in flask.request.args:
        argList.append(arg) #access to all key
        valueList.append(flask.request.args[arg]) #access to all value

    return flask.jsonify(dict(zip(argList,valueList)))

@app.route('/api/getData/')
def data():

    baseUrl = 'https://www.hemnet.se/salda/'
    city = 'soderkopings-kommun'
    urlStr = newUrl(baseUrl+city)
    df = getdef(urlStr)
    return flask.jsonify(df.to_dict(orient='index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)