from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/check_username')
def check_username():
    username = request.args.get('username')
    userlst = list(username)
    upcase = False
    lowcase = False
    num = False
    for i in range(0,len(username)):
        if username[i].istitle():
            upcase = True
        if username[i].islower():
            lowcase = True
    if username[-1].isdigit():
        num = True

    return render_template('check.html',username=username,upcase=upcase,lowcase=lowcase,num=num)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=True)
