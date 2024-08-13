import random
lower='qazxswedcvfrtygbnhujmkiolp'
upper='PLOKIUJMNHYTGBVFREDCXSWQAZ'
sym='+/\+=(*&^%$#@!)|?'
num='1236547890'
chars=lower+upper+num+sym
l=int(input("ENTER THE LENGTH OF PASSWORD: "))
password=''.join(random.choices(chars,k=l))
print(password)
