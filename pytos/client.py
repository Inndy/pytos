# -*- coding: utf8 -*-
import requests, urllib, time, json
from requests.exceptions import *
from random import randint
from request import TOSRequest

class TOSClient:
    def __init__(self, settings):
        settings["gamedata"] = {}
        self.settings = settings
    
    def load_json(self, data):
        if not isinstance(data, dict):
            data = json.loads(data)
        if data["respond"] == 1:
            self.settings["gamedata"] = data
            return True
        else:
            return False
    
    def login(self):
        req = TOSRequest("/user/login", self.settings)
        req.addGetParam([
            ("type", self.settings["login_type"]),
            ("uniqueKey", self.settings["unique_key"]),
            ("deviceKey", self.settings["device_key"]),
            ("sysInfo", self.settings["sysinfo"]),
            ("session", ""),
            ("idfv", ""),
            ("mac", self.settings["system_info"]["mac_addr"]),
        ])
        req.addPostParam([
            ("deviceName", "<unknown>"),
            ("API_DATA_SKILL_JSON", "46cd6ecb015920b70e4c6d28ae466ed2"), ("API_DATA_MONSTER_JSON", "a3d2b4e24e4f3002304d332a4592701f"), ("API_DATA_COMBINE_SKILL_JSON", "72e171f43291fe4426c4fdae4bf98656"), ("API_DATA_TEAM_SKILL_JSON", "0037e96c6ebe89038cad0dc6ddb3ad75"), ("API_DATA_STORY_JSON", "11833b05a72583da130532c302cc3cb3"), ("API_DATA_STAGE_JSON", "12963c6e3cf97a89e817303c22bb97b6"), ("API_DATA_FLOOR_JSON", "80bbdd1bbd668a500a018c41812be631"),
        ])
        ret = req.send()
        return self.load_json(ret)

    def get_helper(self, floorid):
        req = TOSRequest("/floor/helpers", self.settings)
        req.addGetParam("floorId", floorid)
        ret = req.send()
        return json.loads(ret)
    
    def print_data(self):
        game = self.settings["gamedata"]
        user = game["user"]
        print "Name    : [%s]" % user["name"]
        print "Uid     : [%s]" % user["uid"]
        print "Level   : [%s]" % user["level"]
        print "Exp     : [%s]" % user["exp"]
        print "Stamina : [%s / %s]" % (user["currentStamina"], user["maxStamina"])
        print "Coin    : [%s]" % user["coin"]
        print "Diamond : [%s]" % user["diamond"]
        
        guild = None
        if int(user["guildId"]) != 0:
            guild = user["guild"]
        guild_name = "[%s]" % "--None--" if guild is None else guild["name"]
        print "Guild   : %s" % guild_name
        if guild is not None:
            for line in user["guild"]["announcement"].replace("\r", "\n").split("\n"):
                print "        > %s" % line
