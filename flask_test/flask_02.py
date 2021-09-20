from flask import Flask, jsonify

app = Flask(__name__)#객체 생성 필수

@app.route('/json_test')
def hello_json():
    data = {'name' : 'sarah', 'family' : 'byun'}
    return jsonify(data)


@app.route('/server_info')
def server_json():
    data = {'server_name':'0.0.0.0', 'server_port':'8080'}
    return jsonify(data)


if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080')