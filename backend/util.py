from collections import Counter

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1'

def to_json(obj):
    my_dict = obj.__dict__
    if 'user' in my_dict.keys():
        del my_dict['user']
    #if 'header' in my_dict.keys():
    #    del my_dict['header']
    return my_dict

def freq(lst, n):
    return [x for x, cnt in Counter(lst).most_common(n)]

def intersect(a, b, n):
    r = list(set(a) & set(b))
    return r[:n]