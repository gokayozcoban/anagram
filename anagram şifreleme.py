print("Anagram Şifreleme")
dizi=["a","b","c","ç","d","e","f","g","h","ı","i","j",
      "k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v",
      "y","z","w","x","q"]
metin = input("Anagram Şifrelenecek olan metni giriniz : ")
i=8#0
i2=5#1
j=0
j2=1
adet =0
tex=""
while i<len(dizi):
    j = 0
    adet = 0
    while j<len(metin):
        if(metin[j]==dizi[i]):
            adet = adet + 1
        j = j + 1
    if adet>0:
        if adet==1:
            tex+=dizi[i]
        elif adet>1:
            tex+=str(adet) + dizi[i]
    i = i + 1
print(tex)
