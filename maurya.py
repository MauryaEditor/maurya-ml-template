from flask import Flask, request
from flask_cors import CORS
import sys
from state import update_state, get_state

app = Flask(__name__)
CORS(app)

controller_file = sys.argv[1]

@app.route('/state', methods=['POST'])
def invoke_controller():
    update_state(request.get_json())
    exec(open(controller_file).read())
    return get_state()


app.run(host='127.0.0.1', port=4444)