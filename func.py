import requests
import time
import json
from types import SimpleNamespace

server = "http://ip:port/api/xSign"

currentTime = time.time()
x_khronos = str(currentTime).split(".")[0]
_rticket = str(int(x_khronos) * 1000).split(".")[0]

url = f"http://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/follow/user/?item_id=7053726027234708737&from_pre=-1&sec_user_id=MS4wLjABAAAAmLRke2_FbiBZzzzJGSQjURNCkVDTOC5QeU3h5qu9yEaxJYXJHB1cmDZcBjakYKZ4&city&link_sharer=0&channel_id=0&from=13&enter_from=homepage_hot&type=1&iid=7097364930195113733&device_id=6883465806400194059&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=240305&version_name=24.3.5&device_platform=android&ab_version=24.3.5&ssmix=a&device_type=SM-G973N&device_brand=Iphone&language=ru&os_api=25&os_version=7.1.2&openudid=a27dfc98d47579e3&manifest_version_code=2022403050&resolution=720*1280&dpi=240&update_version_code=2022403050&_rticket={_rticket}&current_region=RU&app_type=normal&sys_region=RU&mcc_mnc=25001&timezone_name=Africa%2FNairobi&carrier_region_v2=250&residence=RU&ts={x_khronos}&timezone_offset=10800&build_number=24.3.5&region=RU&uoo=0&app_language=ru&carrier_region=RU&locale=ru-RU&op_region=RU&ac2=wifi&host_abi=x86&cdid=f888ffb7-88b1-4892-bff5-4e0cb3e2daa0"

responseGorgon = requests.request("POST", server, data = {
	'token': 'token',
	'url': url,
	'cookies': '1',
	'stub': '1'
}).text

res = json.loads(responseGorgon, object_hook = lambda d: SimpleNamespace(**d))

x_gorgon = res.x_gorgon
x_Ladon = res.x_Ladon
x_Argus = res.x_Argus

print(res)

headers = {
	"X-Gorgon": x_gorgon,
	"X-Argus": x_Argus,
	"X-Ladon": x_Ladon,
	"X-Khronos": x_khronos,
	"multi_login": "1",
	"sdk-version": "2",
	"passport-sdk-version": "19",
	"Accept-Encoding": "gzip",
	"X-SS-REQ-TICKET": _rticket,
	"User-Agent": "TikTok 25.4.0 rv:254012 (iPhone; iOS 12.5.5; en_US) Cronet",
	"Host": "api16-normal-c-alisg.tiktokv.com",
	"Connection": "Keep-Alive",
	"x-tt-token": "01ce196c7354f7d5f029b48065315737b302d31a15d816c39ba96e860d6b87bc3160bcc73694b5bc008a255c32cae27b3bbf8611beed573e2d1c824802b0a7a8acc02143d4f61158cad5b69664835ac66c0aa03ea3f3ca62104c691f21a4a599b1e8a-CkA0MjM5N2E0MDY2YTRlNWQxYjgxZGE3YTM2YTZjYmNhNTkxODQ6ZDZiYmM3ZjhiZGZjZjMyNmU2ZjI5OTYzNDdk-2.0.0"
}

response = requests.get(url, headers = headers)

print(response.text)
