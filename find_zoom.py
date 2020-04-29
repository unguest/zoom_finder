import requests
from random import randint


"""
Zoom invite codes are made of three parts :
  - 2 numbers between 0 & 999
  - The last one is between 0 & 10'000
I made this code pretty explicit so anyone can see where's the problem...
"""

while True:
    p1 = randint(0,999)
    p2 = randint(0,999)
    p3 = randint(0,99999)
    z = 'https://zoom.com/j/'+str(p1)+str(p2)+str(p3)
    r = requests.get(z)
    if r.status_code == 200:
        with open('zoom.txt', 'a') as f:
            f.write(z)
            f.write('\n')
