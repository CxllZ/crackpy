import os, sys, hashlib, requests

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")

elif sys.platform == "win32":
    os.system("cls")

hashed = input("\033[1;32m Hash: \033[1;m")
# replace the url in rq variable to your own if you want, this one has 10mil passwords
rq = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")
wdlist = rq.text.split("\n")

for pwd in wdlist:
	pwdlist = pwd.strip()
	hashingmd5 = hashlib.md5(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppermd5 = hashingmd5.upper()
		
	hashingsha1 = hashlib.sha1(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppersha1 = hashingsha1.upper()
		
	hashingsha224 = hashlib.sha224(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppersha224 = hashingsha224.upper()
		
	hashingsha256 = hashlib.sha256(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppersha256 = hashingsha256.upper()
		
	hashingsha384 = hashlib.sha384(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppersha384 = hashingsha384.upper()
		
	hashingsha512 = hashlib.sha512(pwdlist.encode("utf-8")).hexdigest()
	hashing_uppersha512 = hashingsha512.upper()
	print("\033[1;32m Trying: {0}".format(pwd))
		
	if hashingmd5 == hashed or hashing_uppermd5 == hashed:
		print("\033[1;36m Hash Cracked: {0}".format(pwd))
		break
	if hashingsha1 == hashed or hashing_uppersha1 == hashed:
		print("\033[1;36m Hash Cracked: {0}".format(pwd))   
		break
	if hashingsha224 == hashed or hashing_uppersha224 == hashed: 
		print("\033[1;36m Hash Cracked: {0}".format(pwd))
		break
	if hashingsha256 == hashed or hashing_uppersha256 == hashed:
		print("\033[1;36m Hash Cracked: {0}".format(pwd))
		break
	if hashingsha384 == hashed or hashing_uppersha384 == hashed:
		print("\033[1;36m Hash Cracked: {0}".format(pwd))
		break
	if hashingsha512 == hashed or hashing_uppersha512 == hashed:
		print("\033[1;36m Hash Cracked: {0}".format(pwd))
		break