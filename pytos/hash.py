# -*- coding: utf8 -*-
import hashlib, time
from random import randint

class TOSHash:
    def __init__(self, settings, req):
        self.settings = settings
        self.req = req
        
    def md5(self, x):
        """
            Calculate MD5 hash
        """
        return hashlib.md5(x).digest().encode("hex")

    def between(self, str, a, b = ""):
        """
            Return a string between a and b
        """
        if a not in str:
            return ""
        str = str[str.find(a) + len(a):]
        if b == "":
            return str
        if b not in str:
            return ""
        return str[:str.find(b)]
        
    def nData(self):
        """
            Generate 'nData' parameter
        """
        a = randint(0, 15)
        b = randint(0, 15)
        return self.md5(self.settings["device_key"][a:a + b])

    def hash(self, mode = "normal"):
        """
            Calculate hash (olv, hash, frags, afe, ness)
        """
        timestamp = self.req.findGetParam("timestamp")
        device_key = self.req.findGetParam("deviceKey")
        url = self.req.buildURL(False)
        islogin = self.req.isLoginRequest()
        if mode == "normal":
            if islogin:
                return self.hash("login")
            return self.md5(self.settings["key"] + url + self.settings["gamedata"]["user"]["uid"] + self.settings["gamedata"]["user"]["session"])
        elif mode == "login":
            return self.md5(self.settings["key"] + url + device_key)
        elif mode == "olv":
            if islogin:
                return self.hash("login_olv")
            data = self.settings["key"] + timestamp + self.settings["gamedata"]["user"]["level"] + self.settings["gamedata"]["user"]["exp"]
            return self.md5(data)[4:11]
        elif mode == "login_olv":
            data = self.settings["key"] + timestamp + "00"
            return self.md5(data)[4:11]
        elif mode == "frags":
            return self.md5(self.between(self.req.buildURL(True), "", "?"))
        elif mode == "afe":
            a = int(len(url) / 2)
            b = int(len(url) / 4)
            return self.md5(url[a:a + b])
        elif mode == "ness":
            return self.md5(self.md5(self.settings["key"] + timestamp)).encode("base64").strip()
        else:
            raise Exception("Unsupported mode")
