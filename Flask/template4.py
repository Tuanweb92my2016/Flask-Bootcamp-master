from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = [1,2,3,4,5]
    puppies =['Fluffy','Rufus1','Spike']
    user_logged_in = False
    return render_template('basic.html',mylist=mylist,puppies=puppies,
            user_logged_in =user_logged_in)



if __name__ == '__main__':
    app.run(debug=True)
