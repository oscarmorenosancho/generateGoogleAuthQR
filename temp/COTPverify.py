# Counter-based OTPs
import pyotp

hotp = pyotp.HOTP('base32secret3232')
hotp.at(0) # => '260182'
hotp.at(1) # => '055283'
hotp.at(1401) # => '316439'

# OTP verified with a counter
hotp.verify('316439', 1401) # => True
hotp.verify('316439', 1402) # => False