from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password,'wrongpassword')

check1 = bcrypt.check_password_hash(hashed_password,'supersecretpassword')

print(check)
print(check1)

from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('mypassword')

print(hashed_pass)

check2 = check_password_hash(hashed_pass,'wrong')
check3 = check_password_hash(hashed_pass,'mypassword')

print(check2)
print(check3)
