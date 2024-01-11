import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)

print("---------------")

print(x.headers['Server'])

print("---------------")

print(x.status_code)

print("---------------")

if x.status_code == 200:
    print("Success!")
elif x.status_code == 404:
    print("Not found!")

print("---------------")

print(x.elapsed)

print("---------------")

print(x.cookies)

print("---------------")

print(x.content)

print("---------------")

print(x.text)

print("---------------")

x = requests.get("http://httpbin.org/get", params={"id": "1"})
print(x.url)

print("---------------")

x = requests.get("http://httpbin.org/get?id=2")
print(x.url)

print("---------------")

x = requests.get('http://httpbin.org/get', params={"id": "3"}, headers={"Accept": "application/json", "Test_header": "test"})
print(x.text)

print("---------------")

x = requests.delete("http://httpbin.org/delete")
print(x.text)

print("---------------")

x = requests.post('http://httpbin.org/post', data={"a": "b", "c": "d", "e": "f"})
print(x.text)

print("---------------")

files = {"file": open("google.png", "rb")}    #rb --> read bytes
x = requests.post("http://httpbin.org/post", files=files)
print(x.text)

print("---------------")

x = requests.get("http://httpbin.org/get", auth=("username", "password"))
print(x.text)

print("---------------")

x = requests.get("https://expired.badssl.com", verify=False)

print("---------------")

x = requests.get("http://github.com", allow_redirects=False)
print(x.headers)

print("---------------")

# x = requests.get("http://httpbin.org/get", timeout=0.01)
# print(x.content)

print("---------------")

#above are stateless requests
#access data based on our session, using session for future requests
x = requests.get("http://httpbin.org/cookies", cookies={"a": "b"})
print(x.content)

print("---------------")

x = requests.Session()
x.cookies.update({"a": "b"})
print(x.get("http://httpbin.org/cookies").text)
print(x.get("http://httpbin.org/cookies").text)

print("---------------")

x = requests.get("http://api.github.com/events")
print(x.json())

print("---------------")

x = requests.get("https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png")
with open("google2.png", "wb") as f:
    f.write(x.content)

print("---------------")

#for more visit https://pypi.org/projects/requests/