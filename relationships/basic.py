from models import db,Puppy,Owner,Toy

# Create 2 puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

db.session.add_all([rufus,fido])

db.session.commit()

print(Puppy.query.all())

# rufus = Puppy.query.filter_by(name='Rufus').all()[0]
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create Owner

jose = Owner('Jose',rufus.id)

# Give Rufus some report_toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# Grab rufus after those additions

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
