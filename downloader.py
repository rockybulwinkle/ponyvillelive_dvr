import requests
import time

r = requests.get("http://dj.bronyradio.com:8000/pvfm1.ogg", stream=True, timeout=60)
r.raise_for_status()

size = 0
start = time.time()

f = open("test.ogg", "wb")

for chunk in r.iter_content(4096):
    if time.time() - start > 20:
        raise ValueError('timeout reached')

    size += len(chunk)
    f.write(chunk)
    print(size/1024/1024)
    
f.close()
