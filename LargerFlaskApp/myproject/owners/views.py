#myproject/owners/views.py

from flask import Flask,Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners',__name__,
        template_folder='templates/owners')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add_owner.html',form=form)
