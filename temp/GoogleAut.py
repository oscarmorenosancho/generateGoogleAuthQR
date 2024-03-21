# Google Authenticator Compatible
import pyotp

pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App')

# >>> 'otpauth://totp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App'

pyotp.hotp.HOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name="alice@google.com", issuer_name="Secure App", initial_count=0)

# >>> 'otpauth://hotp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App&counter=0'