from flask import Flask, jsonify, request, render_template
#request는 플라스크안에서 uri에 쓰인 파라미터를 사용하기위해서 import함
app = Flask(__name__)


@app.route('/login')
def login():
    username = request.args.get('user_name')
    passwd = request.args.get('pw')
    email = request.args.get('email_address')
    print (username, passwd, email)
    
    if username == 'dave':
        return_data_username = {'auth': 'success'}
    else:
        return_data_username = {'auth': 'fail'}

    if passwd == '111':
        return_data_pw = {'pw' : 'success'}
    else: 
        return_data_pw = {'pw' : 'fail'}

    if email == 'korea@gmail.com':
        return_data_email = {'email':'success'}
    else:
        return_data_email = {'email':'fail'}

    
    return jsonify(return_data_username, return_data_pw, return_data_email)

#jsonify로 데이터를 return하면 key, value값으로 전달되는데 value값을 가지고 프론트엔드
#영역에서 적절한 ui를 제공해주게 되는것

@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    # flask로 정적웹사이트 보여주는 방법
    # render_template라는 함수로 가능
    # login.html파일을 templates라는 폴더에서 찾아서 보여주는 방식
    return render_template('./login_test.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")