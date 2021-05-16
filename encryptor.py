import random

input_text = input("Введите текст: ")

alphabet_string_full = "мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` "
alphabet_string = "мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` "

key_key = "005:074:010:081:028:074:140:095:045:105:072:102:102:141:110:073:014:119:111:120:018:086:088:092:" #ключ шифрования для ключа шифрования :) выбран рандомно
key_key_split = key_key.split(":")[0:-1]

def key_generator(text):# функция генераци ключа. Он должен быть такой же длины, как и исходный код.
    key_array = []
    for i in text:
        if i.lower() in alphabet_string:
            symbol = str(random.randint(0, len(alphabet_string_full)/2-1))
            if len(symbol) < 3:
                while len(symbol) < 3:
                    symbol = '0' + symbol
                key_array.append(symbol + ':')
            else:
                key_array.append(symbol + ':')
    key_string = ''
    for i in key_array:
        key_string += i
    return key_array, key_string

def do_encrypt(text, key):
    global key_key_split
    for i in range(0, len(key_key_split)):
        key_key_split[i] += ':'
    
    text_encrypt = ''
    k = 0
    if len(key_generated_string) < len(key_key_split):
        while len(key_generated_string) < len(key_key_split):
            key_key_split.pop(-1)

    else:
        while len(key_generated_string) > len(key_key_split):
            key_key_split.append(key_key_split[k])
            k += 1        

    for i in range(0, len(key)): # Здесь происходит шифрования текста или ключа.
        text_encrypt += alphabet_string_full[alphabet_string.index(text[i]) + int(key[i][0:3])]
    
    return text_encrypt

key_generated_full = key_generator(input_text) #Это и массив чисел ключа шифрования и строка всех чисел ключа шифрования, то есть сам ключ
key_generated_string = key_generated_full[1]
key_generated_array = key_generated_full[0]

key_key_split_string = ''

for i in key_key_split:
    key_key_split_string += i[0:3] + ':'

print(do_encrypt(input_text, key_generated_array), ":ENCRYPTED TEXT")
#print(key_key_split_string)
#print(key_generated_string)
print(do_encrypt(key_generated_string, key_key_split), ":ENCRYPTED KEY") # здесь я зашифровываю ключ шифрования, для 100% криптографической стойкости.
                                                                         # То есть, не зная, как работает анкриптор или декриптор, взломать текст невозможно
                                                                         # Также не зная ключа, декриптовать текст невозможно.