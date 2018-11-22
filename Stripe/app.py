import os
from flask import Flask, render_template, request,redirect,url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_FzniVv5eiHRWAknHDpYK9vHm"

stripe_keys = "sk_test_PVahTzNmDwc6lBwmwM7Qp7Sg"

# {'secret_key': os.environ['SECRET_KEY'],'publishable_key': os.environ['PUBLISHABLE_KEY']}

# stripe.api_key = stripe_keys['secret_key']



@app.route('/')
def index():
    return render_template('index.html',public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment', methods=['POST'])
def payment():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email= request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    # return render_template('charge.html', amount=amount)
    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)
