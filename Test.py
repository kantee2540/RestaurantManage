import random
import datetime

x = datetime.datetime.now()
print(x.strftime("%x"))
print(x.strftime("%X"))

if x.strftime("%x") == "03/03/20":
    print("YES")