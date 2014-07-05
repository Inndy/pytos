# -*- coding: utf8 -*-
import requests, urllib, time, json
from requests.exceptions import *
from random import randint
from hash import TOSHash

class TOSRequest:
    def __init__(self, url, settings):
        self.url = url
        self.settings = settings
        self.getParam = []
        self.postParam = []
        
    def send(self):
        """
            Fill hashes and send request
        """
        hash = TOSHash(self.settings, self)

        if not self.isLoginRequest():
            self.addGetParam([
                ("uid", self.settings["gamedata"]["user"]["uid"]),
                ("session", self.settings["gamedata"]["user"]["session"]),
            ])
        
        self.addGetParam([
            ("timestamp", int(time.time())),
            ("timezone", 8),
            ("nData", hash.nData()),
            ("language", "zh_TW"),
            ("platform", "android"),
            ("version", self.settings["api_version"])
        ])
        self.addGetParam("olv", hash.hash("olv"))
        self.addGetParam("hash", hash.hash())
        self.addPostParam([
            ("systemInfo", self.settings["post_sysinfo"]),
            ("frags", hash.hash("frags")),
            ("tvalid", "FALSE"),
            ("attempt", 1),
            ("afe", hash.hash("afe")),
            ("ness", hash.hash("ness"))
        ])
        
        if "send_hook" in self.settings:
            print self.buildURL(True)
            print self.buildData()
            if self.settings["send_hook"] == "block":
                return """{ "respond": 0 }"""
        url = self.buildURL(True)
        data = self.buildData()
        headers = {
            "Accept-Encoding": "gzip",
            "User-Agent": self.settings["user_agent"],
            "Content-type": "application/x-www-form-urlencoded"
        }
        proxies = None if "proxies" not in self.settings else self.settings["proxies"]
        return requests.post(url, data = data, headers = headers, proxies = proxies, verify = False).content
    
    def buildParam(self):
        """
            Build get param string
        """
        return urllib.urlencode(self.getParam, doseq = True)
        
    def buildData(self):
        """
            Build post data string
        """
        return urllib.urlencode(self.postParam, doseq = True)
        
    def buildURL(self, full = False):
        """
            Build URL for request
            
            full    Is full URL or not (only path)
        """
        url = self.settings["api_url"] if full else ""
        url += "/api" + self.url + "?" + self.buildParam()
        return url
    
    def __addDict(self, dictionary, key, value):
        """
            Add item into dictionary
            
            dictionary  dictionary to be added (must be a `list`)
            key         key
            value       value
        """
        if isinstance(key, dict):
            for k, v in key.iteritems():
                self.__addDict(dictionary, k, v)
        elif isinstance(key, list):
            for item in key:
                (k, v) = item
                self.__addDict(dictionary, k, v)
        else:
            for i, (k, v) in enumerate(dictionary):
                if k == key:
                    del dictionary[i]
                    break
            dictionary.append((str(key), str(value)))
        
    def addGetParam(self, key, value = None):
        """
            Add GET paramenter(s)
            
            >>> addGetParam([ (key1, val1), (key2, val2) ])
            
            >>> addGetParam({ "key1": "val1", "key2": "val2" })
                # This method doesn't guarantee order
            
            >>> addGetParam(key, value)
        """
        return self.__addDict(self.getParam, key, value)
        
    def addPostParam(self, key, value = None):
        """
            Add POST paramenter(s)
            
            Usage is same as 'addGetParam'
        """
        return self.__addDict(self.postParam, key, value)
    
    def __findDict(self, dictionary, key, callback = None):
        """
            Find an element in a dictionary
            
            dictionary  The dictionary
            key         The key
            callback    None or callback(dictionary, index)
        """
        key = str(key)
        for (k, v) in dictionary:
            if k == key:
                return v
        return None
    
    def findGetParam(self, key):
        """
            Find an element in GET params
        """
        return self.__findDict(self.getParam, key)
    
    def findPostParam(self, key):
        """
            Find an element in POST params
        """
        return self.__findDict(self.getParam, key)
    
    def isLoginRequest(self):
        """
            Is this a login request ?
        """
        return any(x in self.url for x in ("user/login", "user/register", "user/check_exist", "user/bind"))
