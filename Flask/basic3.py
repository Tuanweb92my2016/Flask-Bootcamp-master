from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello Puppy ! </h1>"


@app.route('/information')
def info():
    return "<h1> Puppy are cute !</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    # return "<h1> This is a page for  {}</h1>".format(name)
    # return "<h1> Uppercase :  {}</h1>".format(name.upper())
    return "<h1> 100th letter :  {}</h1>".format(name[100])

@app.route('/puppy_latin/<name1>')
def puppylatin(name1):
    # return "<h1> This is a page for  {}</h1>".format(name)
    # return "<h1> Uppercase :  {}</h1>".format(name.upper())
    if name1[-1] != 'y':
        name1 = name1 + "y"
    else:
        name1 = name1[:(len(name1)-1)] + "iful"
    return "<h1> Puppy latin :  {}</h1>".format(name1)


if __name__ == "__main__":

    app.run(debug=True)
