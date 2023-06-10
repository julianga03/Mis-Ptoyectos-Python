import requests
from Bot_Telegram_Avisar_Precio import precio
from Bot_Telegram_Avisar_Precio import precioDeseado

def telegram_bot_sendtext(bot_message):
    
    bot_token = '6204041676:AAFU7QJg3m6MbcZl3zYflTQWxtFz_4MDsUI'
    bot_chatID = '5466981590'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

if precio <= precioDeseado:
    print("hola")
    test = telegram_bot_sendtext("hay oferta")

else:
    print("holaaaa")
    test = telegram_bot_sendtext("Emvia Bien cuando no hay oferta")



