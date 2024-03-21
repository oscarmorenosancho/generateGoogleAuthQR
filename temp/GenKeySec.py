#Generating a Secret Key
import pyotp

pyotp.random_base32()

#Some applications want the secret key to be formatted as a hex-encoded string:

pyotp.random_hex()  # returns a 40-character hex-encoded secret