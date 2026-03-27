#//////////////// date and password////////////////////
import re

password = "mishal20"
pattern = re.match(r"^[A-Za-z0-9]{8,}$", password)
print(pattern)

date = "27-03-2026"
pattern = re.match(r"^\d{2}-\d{2}-\d{4}$", date)
print(pattern)


password = "Aditya@123"
pattern = re.match(r"^[A-Za-z0-9@#$%^&+=]{8,}$", password)
print(pattern)