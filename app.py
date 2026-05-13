import os
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
