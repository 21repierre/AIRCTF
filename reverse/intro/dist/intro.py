realPassword = [101, 52, 83, 121, 95, 82, 51, 118, 101, 114, 115, 101]
password = input("Mot de passe: ")

assert len(password) == len(realPassword)

for i in range(len(realPassword)):
	assert ord(password[i]) == realPassword[i]

print("Bravo, tu peux valider avec AIRCTF{" + password + "}")