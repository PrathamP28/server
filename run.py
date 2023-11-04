import time
from time import gmtime, strftime
an = 0
an1 = 2
an2 = 4

while True:
    time.sleep(60)
    an = an + 1
    an1 = an1 + 1
    an2 = an2 + 1
    if an is 360:
        break

    curr = time.time()
    s = strftime("%H:%M:%S", 
             gmtime(curr))

    file = open("text.txt", "r")
    r = file.read()
    file.close()

    file = open("text.txt", "w")
    a = file.write(f"""{r} 
{s} a0 = {an} a1 = {an1} an2 = {an2}""")
    file.close()
