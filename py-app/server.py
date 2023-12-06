from flask import Flask
import json

app = Flask(__name__)
@app.route('/status/', methods=['GET', 'POST'])
def get_status():
    response_data = json.dumps(
                {"my_key": "my_value"}
            )
    return response_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)