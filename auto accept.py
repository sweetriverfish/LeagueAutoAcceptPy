import os
import base64
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

command = "wmic process where \"caption=\'LeagueClientUx.exe\'\" get Caption,Processid,Commandline"

key = os.popen(command).read().split("remoting-auth-token=")[1].split('"')[0]
port = os.popen(command).read().split("app-port=")[2].split('"')[0]

basic = "Basic"
auth = "riot:"+key
authByte = auth.encode('ascii')
authBSFBytes = base64.b64encode(authByte)
authEncoded = authBSFBytes.decode('ascii')

print("Auto accept is now running. You can safely pee.")

while True:
	r = requests.post(	url="https://127.0.0.1:"+port+"/lol-matchmaking/v1/ready-check/accept",
						headers={'Authorization':'Basic '+authEncoded,"Accept":"application/json"},
						verify=False,
						data='')
	#print(r.status_code)
	if r.status_code == 204:
		print("accepted match")
	time.sleep(5)

