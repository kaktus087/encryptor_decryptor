input_key = input("Enter the key: ")
input_text = input("Enter the text: ")

alphabet_string_full = "мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` "
alphabet_string = "мДokуыъпсlmщбхeлгцоLMU45678Vrsn,./)bчBO$№Kж*RSNнЕЁЙЪСjuфтg9+yюяаhDA^:ZPQGHTи%>@еёйwJWXш0зрьYIПЫИЩТЗРЬЭЮЯАEF(123Х_д?;zpqfxaкCЖБКЛМНЧ&-!вэcvГЦШВОУФtid='<\"~` "

key_key = "005:074:010:081:028:074:140:095:045:105:072:102:102:141:110:073:014:119:111:120:018:086:088:092:" #ключ шифрования для ключа шифрования :) выбран рандомно
key_key_split = key_key.split(":")[0:-1]

for i in range(0, len(key_key_split)):
    key_key_split[i] += ':'

k = 0
if len(input_key) > len(key_key_split):
    while len(input_key) > len(key_key_split):
        key_key_split.append(key_key_split[k])
        k += 1
else:
    while len(input_key) < len(key_key_split):
        key_key_split.pop(-1)

#print(key_key_split)
text_decrypt = ''
key_decrypt = ''
for i in range(0, len(key_key_split)):
    if key_key_split[i][-1] == ":":
        key_decrypt += alphabet_string_full[alphabet_string.index(input_key[i]) - int(key_key_split[i][0:3])] #key_decrypt это расшифрованный ключ

#print(key_decrypt)

key_array = []
d = 0
while d+4 <= len(key_decrypt): 
    key_array.append(key_decrypt[d:d+4])
    d += 4
#print(key_array)

for i in range(0, len(input_text)): #Здесь я расшифровываю исходный текст с помощью расшифрованного исходного ключа
    if key_array[i][-1] == ":":
        text_decrypt += alphabet_string_full[alphabet_string.index(input_text[i]) - int(key_array[i][0:3])]
print(text_decrypt)