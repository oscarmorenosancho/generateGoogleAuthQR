import pyotp

pyotp.parse_uri('otpauth://totp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App')

# >>> <pyotp.totp.TOTP object at 0xFFFFFFFF>

pyotp.parse_uri('otpauth://hotp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App&counter=0')

# >>> <pyotp.totp.HOTP object at 0xFFFFFFFF>



totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())