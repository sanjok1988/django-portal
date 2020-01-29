import base64
import collections
import itertools
import random, string
import uuid

from blog import settings
from blog.settings import BASE_DIR

password = "".join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
print(password)
ran_nums = "".join(random.choice(string.digits) for i in range(5))
upper = "".join(random.choice(string.ascii_uppercase + string.digits + string.punctuation) for i in range(8))
print(ran_nums)
print(upper)

ch = "█"


def col(sz):
    mn, mx = min(sz), max(sz)
    print(mn, mx)
    df = (mx - mn)
    bkt = [(el - mn) for el in sz]
    print(bkt)
    print([(ch * (el + 1), " " * (5 - el)) for el in bkt])
    hrz = [f"{b}{c}" for b, c in [(ch * (el + 1), " " * (5 - el)) for el in bkt]]
    return "\n".join([' '.join(el) for el in list(map(list, zip(*hrz)))[::-1]])


series = [random.randint(10, 99) for _ in range(25)]
print(series)
print(col(series))

print('\n'.join([(6 - x) * ' ' + ''.join(['{} '.format(p) for p in str(11 ** x)]) for x in range(6) if x != 1]))
print('\n'.join([''.join(['*' for _ in range(x + 1)]) for x in range(5)]))
print('\n'.join([(x + 1) * '#' + (7 - x) * '*' for x in range(7)]))

import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))


import urllib.request, json
ip = json.loads(urllib.request.urlopen('http://jsonip.com').read())['ip']
print(ip)

print(set([1,1,4,5,6,2,2,4,3,5]))

print(collections.Counter([1,2,2,3,3,4,4,4,4,4,6,6,6,6,6,6,6,6,6,7]))

y={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
print(dict(sorted(y.items())))
y={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
print(dict(sorted(y.items(), key=lambda kv: kv[1])))
print("".join(itertools.chain(*zip([random.choice(string.ascii_lowercase) for _ in range(6)],  [random.choice('aeiou') for _ in range(6)]))))

from string import ascii_uppercase as upr, ascii_lowercase as lwr
def caesar_cipher(txt, offset=1):
    _map = dict(list(zip(upr, upr[offset:] + upr[:offset])) + list((zip(lwr, lwr[offset:] + lwr[:offset]))))
    return "".join([_map[el] if el in upr+lwr else el for el in txt])

print(uuid.uuid4())

print(base64.urlsafe_b64encode(uuid.uuid4().bytes)[:16])

def shuffled_deck():
    deck = list(
        itertools.product("♠♣♥♦♤♧♢♡", "AKQJ🔟98765432")
    )
    random.shuffle(deck)
    return "\n".join([f"{n} of {suit}" for suit, n in deck])

print(shuffled_deck())


len(open(settings.BASE_DIR+'\test.txt', 'r').read().split())

print(os.path.dirname(BASE_DIR))