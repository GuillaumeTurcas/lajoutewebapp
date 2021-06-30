from backend.util.importControler import *

class Request():
    
    def headers():
        account = session["account"] \
                if session["account"] \
                else {
                    "admin" : 0,
                    "token" : None,
                    "id" : -1
                }
           
        return {
            "admin" : str(account["admin"]),
            "token" : str(account["token"]),
            "id" : str(account["id"])
        }

    def delete(url):
        headers = Request.headers()
        
        return requests.delete(f"{BASE}{SECRET}{url}", 
            headers = headers).json()

    def get(url):
        headers = Request.headers()

        return requests.get(f"{BASE}{SECRET}{url}", 
            headers = headers).json()


    def post(url, data = None):
        headers = Request.headers()
        
        return requests.post(f"{BASE}{SECRET}{url}", 
            headers = headers,
            data = json.dumps(data)).json()


    def put(data = None):
        headers = Request.headers()

        return requests.put(f"{BASE}{SECRET}{url}", 
            headers = json.dumps(headers), 
            data = json.dumps(data)).json()
