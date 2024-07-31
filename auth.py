import pyotp
import qrcode
import io
import base64
from models import db, User

def generate_qr_code(secret_key, username, issuer_name):
    totp_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(username, issuer_name=issuer_name)
    qr = qrcode.make(totp_uri)
    img = io.BytesIO()
    qr.save(img, 'PNG')
    img.seek(0)
    return base64.b64encode(img.read()).decode('ascii')

def register_user(username, password):
    secret_key = pyotp.random_base32()
    user = User(username=username, secret_key=secret_key)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return secret_key

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

def verify_totp(secret_key, user_totp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_totp)