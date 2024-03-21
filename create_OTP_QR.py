import time 
import pyotp 
import qrcode 


k = pyotp.random_base32()
print (k)

secret_key = "GeeksforGeeksIsBestForEverything"


totp_auth = pyotp.totp.TOTP( 
  secret_key).provisioning_uri( 
  name='David_San', 
  issuer_name='morsan')
  
print(totp_auth)

qrcode.make(totp_auth).save("qr_auth.png") 
psd_uri = pyotp.parse_uri(totp_auth)
print (psd_uri)
totp_qr = pyotp.TOTP(secret_key)

while True:
    print("Current OTP:", psd_uri.now())
    time.sleep(3)