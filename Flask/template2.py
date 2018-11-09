from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    some_variable = "Jose"
    name = "Tuan"
    letters = list(name)
    puppy_dict = {'pup_name':'Sammy','pup_type':'Berger'}
    # return render_template('basic.html',my_variable=some_variable)
    return render_template('basic.html',name=name,letters=letters,
                puppy_dict=puppy_dict)



if __name__ == '__main__':
    app.run(debug=True)
