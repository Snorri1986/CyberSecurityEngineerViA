import requests

URL = "https://unsplash.com/photos/syuhhPwu-hk/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjY0NzgwNzM1&force=true"
ourPicture = requests.get(URL)
open("ukraineFlag","wb").write(ourPicture.content)