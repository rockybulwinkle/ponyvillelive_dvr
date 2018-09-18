import json
import requests
from requests import get


def get_req(path):
    resp = get(path)
    if resp.status_code != 200:
        if resp.status_code == 401:
            print("WARNING: 401 for path %s"%path)
            return None
        raise Exception("Status %d: %s"%(resp.status_code, path))

    j = json.loads(resp.content.decode("utf-8"))
    if j["status"] != "success":
        print("nonsucessful in getting %s"%path)
        return None

    return j["result"]


nowplaying=get_req("http://ponyvillelive.com/api/nowplaying")
sched=get_req("http://ponyvillelive.com/api/schedule")
