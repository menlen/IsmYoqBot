# This example show how to use inline keyboards and process button presses
import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os, sys
from PIL import Image, ImageDraw, ImageFont
import random

TELEGRAM_TOKEN = '1486165557:AAFKKNyr3-92Ia68bae2edWLItrXJwRj9ik'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

channelId = -1001390673326
channelId1 = -1001462619192
user_dict = {}

markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = KeyboardButton("😈 UdarLari 😎")
btn2 = KeyboardButton("👮🏾‍♂️ Xarbiycha Bollarga 🔫")
btn3 = KeyboardButton("👩🏻‍🎤 Xarbiycha Qizlarga 👮🏻‍♀️")
btn4 = KeyboardButton("💞 Sevishganlarga 👩‍❤️‍👨")
btn5 = KeyboardButton("🛡 Xarbiycha Bollaga 🖤")
markup.add(btn1, btn2, btn3, btn4, btn5)


def TextToImgx(ext):
    IMAGES = [
        'o01.jpg',
        'o02.jpg',
        'o03.jpg',
        'o04.jpg',
        'o05.jpg',
        'o06.jpg',
        'o07.jpg',
        'o08.jpg',
        'o09.jpg',
        'o10.jpg',
        'o11.jpg',
        'o12.jpg',
        'o13.jpg',
        'o14.jpg',
        'o15.jpg',
        'o16.jpg',
        'o17.jpg',
        'o18.jpg',
        'o19.jpg',
        'o20.jpg',
        'o21.jpg',
        'o22.jpg',
        'o23.jpg',
        'o24.jpg',
        'o25.jpg',
        'o26.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("New Year.ttf", 100)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 80)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1300)/2), text, font=fnt, fill=(0,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgch(ext):
    IMAGES = [
        'b01.jpg',
        'b02.jpg',
        'b03.jpg',
        'b04.jpg',
        'b05.jpg',
        'b06.jpg',
        'b07.jpg',
        'b08.jpg',
        'b09.jpg',
        'b10.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("Pacifico.ttf", 80)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 80)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1300)/2), text, font=fnt, fill=(0,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgjch(ext):
    IMAGES = [
        'g01.jpg',
        'g02.jpg',
        'g03.jpg',
        'g04.jpg',
        'g05.jpg',
        'g06.jpg',
        'g07.jpg',
        'g08.jpg',
        'g09.jpg',
        'g10.jpg',
        'g11.jpg',
        'g12.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    fnt = ImageFont.truetype("The Tide.ttf", 70)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1320)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgd(ext):
    IMAGES = [
        'l1.jpg',
        'l1.jpg',
        'l3.jpg',
        'l4.jpg',
        'l5.jpg',
        'l6.jpg',
        'l7.jpg',
        'l8.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("WinterYesterday.ttf", 50)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 50)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1320)/2), text, font=fnt, fill=(255,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename

def TextToImgb(ext):
    IMAGES = [
        'bb01.jpg',
        'bb02.jpg',
        'bb03.jpg',
        'bb04.jpg',
        'bb05.jpg',
        'bb06.jpg',
        'bb07.jpg',
        'bb08.jpg',
        'bb09.jpg',
        'bb10.jpg',
        'bb11.jpg',
        'bb12.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    try:
        fnt = ImageFont.truetype("New Year.ttf", 100)
    except:
        fnt = ImageFont.truetype("OpenSans-BoldItalic.ttf", 80)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/2,(1300)/2), text, font=fnt, fill=(0,0,0,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,35)
    g = out.save(f'{filename}.png')
    return filename


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Azo bo'ling", url='t.me/onideal'), InlineKeyboardButton("Azo bo'ling", url='t.me/quyichirchiq_bozori'),
                               InlineKeyboardButton("Tasdiqlash", callback_data="yes"))
    return markup

def getUserFromChannel(userId):
    u = bot.get_chat_member(channelId, userId)
    u1 = bot.get_chat_member(channelId1, userId)
    a = 'left'
    if u.status == 'member':
        if u1.status == 'member':
            a = 'member'
        else:
            a = 'left'
    return a


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes":
        u = getUserFromChannel(call.from_user.id)
        if u == 'member':
            bot.send_message(call.from_user.id, "Juda soz!!!, Tugmalardan birini bosing", reply_markup=markup)
        else:
            bot.send_message(call.from_user.id, f"Salom {call.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


def process_name_step_x(message):
    try:
        name = message.text
        myfile = TextToImgx(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : Rasm Tayyor \n@ismborbot \n@ismYoqbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_ch(message):
    try:
        name = message.text
        myfile = TextToImgch(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : Rasm Tayyor \n@ismborbot \n@ismYoqbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_jch(message):
    try:
        name = message.text
        myfile = TextToImgjch(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : Rasm Tayyor \n@ismborbot \n@ismYoqbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_d(message):
    try:
        name = message.text
        myfile = TextToImgd(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : Rasm Tayyor \n@ismborbot \n@ismYoqbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_name_step_b(message):
    try:
        name = message.text
        myfile = TextToImgb(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f'{name} : Rasm Tayyor \n@ismborbot \n@ismYoqbot'
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')



@bot.message_handler(commands=['start','help'])
def start(message):
    us = getUserFromChannel(message.chat.id)
    if us == 'member':
        bot.send_message(message.chat.id, "Assalomu Aleykum Tugmalardan birini bosing keyin ismingizni yozing", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, Kanalimizga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tasdiqlang", reply_markup=gen_markup())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    us = getUserFromChannel(message.chat.id)
    msg = bot.send_message(message.chat.id, """\
                Juda soz!!!, Ismingizni yozing
                """)
    if us == 'member':
        if message.text == "😈 UdarLari 😎":
            bot.register_next_step_handler(msg, process_name_step_x)
        elif message.text == "👮🏾‍♂️ Xarbiycha Bollarga 🔫":
            bot.register_next_step_handler(msg, process_name_step_ch)
        elif message.text == "👩🏻‍🎤 Xarbiycha Qizlarga 👮🏻‍♀️":
            bot.register_next_step_handler(msg, process_name_step_jch)
        elif message.text == "💞 Sevishganlarga 👩‍❤️‍👨":
            bot.register_next_step_handler(msg, process_name_step_d)
        elif message.text == "🛡 Xarbiycha Bollaga 🖤":
            bot.register_next_step_handler(msg, process_name_step_b)
        else:
            bot.send_message(message.chat.id, "Avval tugmalardan birini bosing keyin ismingizni yozing")
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


bot.polling(none_stop=True)
