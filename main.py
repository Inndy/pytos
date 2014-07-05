# -*- coding: utf8 -*-
from pytos import TOSClient

settings = {
    "api_url"       : "https://zh.towerofsaviors.com",
    "key"           : "VmxST1UyRkhTblJWYkZwcFlteEtkMWxyV250a2JWSldWMjFvYVZJell6az0=",
    "user_agent"    : "Dalvik/1.6.0 (Linux; U; Android 4.1.2; LT26i Build/6.2.B.1.96)",
    # "login_type"    : "facebook",
    # "unique_key"    : "================================",
    "login_type"    : "================================",
    "device_key"    : "================================",
    "api_version"   : "4.61",
    # "system_info"   : {
    #     "operationSystem"           : "Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)",
    #     "processorType"             : "ARMv7 VFPv3 NEON",
    #     "processorCount"            : "2",
    #     "systemMemorySize"          : "686",
    #     "graphicsMemorySize"        : "256",
    #     "graphicsDeviceName"        : "Adreno (TM) 220",
    #     "isBlueStack"               : "FALSE",
    #     "graphicsDeviceVersion"     : "OpenGL ES 2.0 V@6.0 AU@  (CL@)",
    #     "npotSupport"               : "Full",
    #     "is_GT_N7000_or_GT_I9100"   : "FALSE",
    #     "maxTextureSize"            : "4096",
    #     "mac_addr"                  : "00:00:00:00:00:00",
    # },
    # SystemInfo.operatingSystem + "|" +
    # SystemInfo.processorType + "|" +
    # SystemInfo.processorCount + "|" +
    # SystemInfo.systemMemorySize + "|" +
    # SystemInfo.graphicsMemorySize + "|" +
    # SystemInfo.graphicsDeviceName + "|" + 
    # (SystemInfo.graphicsDeviceVendor.ToUpper().Contains("BLUESTACKS") ? "TRUE" : "FALSE") +  "|" +
    # SystemInfo.graphicsDeviceVersion + "|" +
    # SystemInfo.npotSupport + "|" + 
    # ((SystemInfo.deviceModel.ToUpper().Contains("GT-N7000") || SystemInfo.deviceModel.ToUpper().Contains("GT-I9100")) ? "TRUE" : "FALSE") + "|" +
    # SystemInfo.maxTextureSize + "|" +
    # Core.Config.VERSION.ToString("#,##0.00") + "|||" + GetMacAddress
    "sysinfo"       : "Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)|ARMv7 VFPv3 NEON|2|686|256|Adreno (TM) 220|FALSE|OpenGL ES 2.0 V@6.0 AU@  (CL@)|Full|FALSE|4096|4.61|||00:00:00:00:00:00",
    "post_sysinfo"  : '{"appVersion":"4.61","deviceModel":"Sony Ericsson LT26i","deviceType":"Handheld","deviceUniqueIdentifier":"00000000000000000000000000000000","operatingSystem":"Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)","systemVersion":"4.1.2","processorType":"ARMv7 VFPv3 NEON","processorCount":"2","systemMemorySize":"686","graphicsMemorySize":"256","graphicsDeviceName":"Adreno (TM) 220","graphicsDeviceVendor":"Qualcomm","graphicsDeviceVersion":"OpenGL ES 2.0 V@6.0 AU@  (CL@)","emua":"FALSE","emub":"FALSE","npotSupport":"Full","supportsAccelerometer":"True","supportsGyroscope":"True","supportsLocationService":"True","supportsVibration":"True","maxTextureSize":"4096","screenWidth":"720","screenHeight":"1280","screenDPI":"343.6441","IDFA":"","IDFV":"","MAC":"00:00:00:00:00:00","networkType":"WIFI"}',
    
    # "proxies" : { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080" },
    # "send_hook" : "",
    "device_key"    : "================================",
    "api_version"   : "4.61",
    # "system_info"   : {
    #     "operationSystem"           : "Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)",
    #     "processorType"             : "ARMv7 VFPv3 NEON",
    #     "processorCount"            : "2",
    #     "systemMemorySize"          : "686",
    #     "graphicsMemorySize"        : "256",
    #     "graphicsDeviceName"        : "Adreno (TM) 220",
    #     "isBlueStack"               : "FALSE",
    #     "graphicsDeviceVersion"     : "OpenGL ES 2.0 V@6.0 AU@  (CL@)",
    #     "npotSupport"               : "Full",
    #     "is_GT_N7000_or_GT_I9100"   : "FALSE",
    #     "maxTextureSize"            : "4096",
    #     "mac_addr"                  : "00:00:00:00:00:00",
    # },
    # SystemInfo.operatingSystem + "|" +
    # SystemInfo.processorType + "|" +
    # SystemInfo.processorCount + "|" +
    # SystemInfo.systemMemorySize + "|" +
    # SystemInfo.graphicsMemorySize + "|" +
    # SystemInfo.graphicsDeviceName + "|" + 
    # (SystemInfo.graphicsDeviceVendor.ToUpper().Contains("BLUESTACKS") ? "TRUE" : "FALSE") +  "|" +
    # SystemInfo.graphicsDeviceVersion + "|" +
    # SystemInfo.npotSupport + "|" + 
    # ((SystemInfo.deviceModel.ToUpper().Contains("GT-N7000") || SystemInfo.deviceModel.ToUpper().Contains("GT-I9100")) ? "TRUE" : "FALSE") + "|" +
    # SystemInfo.maxTextureSize + "|" +
    # Core.Config.VERSION.ToString("#,##0.00") + "|||" + GetMacAddress
    "sysinfo"       : "Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)|ARMv7 VFPv3 NEON|2|686|256|Adreno (TM) 220|FALSE|OpenGL ES 2.0 V@6.0 AU@  (CL@)|Full|FALSE|4096|4.61|||00:00:00:00:00:00",
    "post_sysinfo"  : '{"appVersion":"4.61","deviceModel":"Sony Ericsson LT26i","deviceType":"Handheld","deviceUniqueIdentifier":"00000000000000000000000000000000","operatingSystem":"Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)","systemVersion":"4.1.2","processorType":"ARMv7 VFPv3 NEON","processorCount":"2","systemMemorySize":"686","graphicsMemorySize":"256","graphicsDeviceName":"Adreno (TM) 220","graphicsDeviceVendor":"Qualcomm","graphicsDeviceVersion":"OpenGL ES 2.0 V@6.0 AU@  (CL@)","emua":"FALSE","emub":"FALSE","npotSupport":"Full","supportsAccelerometer":"True","supportsGyroscope":"True","supportsLocationService":"True","supportsVibration":"True","maxTextureSize":"4096","screenWidth":"720","screenHeight":"1280","screenDPI":"343.6441","IDFA":"","IDFV":"","MAC":"00:00:00:00:00:00","networkType":"WIFI"}',
    
    # "proxies" : { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080" },
    # "send_hook" : "",
}
# data = {
#     "IDFA": "", 
#     "IDFV": "", 
#     "MAC": "00:00:00:00:00:00", 
#     "appVersion": "4.61", 
#     "deviceModel": "Sony Ericsson LT26i", 
#     "deviceType": "Handheld", 
#     "deviceUniqueIdentifier": "00000000000000000000000000000000", 
#     "emua": "FALSE", 
#     "emub": "FALSE", 
#     "graphicsDeviceName": "Adreno (TM) 220", 
#     "graphicsDeviceVendor": "Qualcomm", 
#     "graphicsDeviceVersion": "OpenGL ES 2.0 V@6.0 AU@  (CL@)", 
#     "graphicsMemorySize": "256", 
#     "maxTextureSize": "4096", 
#     "networkType": "WIFI", 
#     "npotSupport": "Full", 
#     "operatingSystem": "Android OS 4.1.2 / API-16 (6.2.B.1.96/n7v_zg)", 
#     "processorCount": "2", 
#     "processorType": "ARMv7 VFPv3 NEON", 
#     "screenDPI": "343.6441", 
#     "screenHeight": "1280", 
#     "screenWidth": "720", 
#     "supportsAccelerometer": "True", 
#     "supportsGyroscope": "True", 
#     "supportsLocationService": "True", 
#     "supportsVibration": "True", 
#     "systemMemorySize": "686", 
#     "systemVersion": "4.1.2"
# }

client = TOSClient(settings)
if client.login():
    client.print_data()
    ret = client.get_helper(1)
    for usr in ret["data"]["alluserList"]:
        print usr
