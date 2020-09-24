import requests

proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}


def addCourse(name, desc, display_idx):
    payload = {

        'action': 'add_course',

        'data': f'''{{


               "name":"{name}",


               "desc":"{desc}",


               "display_idx":"{display_idx}"


           }}


       '''

    }


url = 'f"http://{cfg.API_SERVER}/api/mgr/sq_mgr/",data=payload'

requests.post(url, proxies=proxies, verify=False)  # verify是否验证服务器的SSL证书
