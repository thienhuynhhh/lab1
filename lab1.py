import requests
#print(requests.__version__)                      
#result=requests.get("http://www.google.com")
#print(result.text)

result = requests.get("https://raw.githubusercontent.com/thienhuynhhh/lab1/main/lab1.py")
print(result.text)
