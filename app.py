import os

aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"

aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"

private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwFakeKeyTestingOnly123456789
ZXhhbXBsZWtleQ==
-----END RSA PRIVATE KEY-----
"""

print("talisman")

########################

formula = input("Enter formula: ")

result = eval(formula)

print(result)
