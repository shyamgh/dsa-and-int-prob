
import json


def parse_json(s):
    k = []
    v = []
    l = json.loads(s)
    for key, val in l.items():
        k.append(key)
        if type(val) != list and type(val) != dict:
            v.append(val)
        elif type(val) == list:
            v.extend(val)
        elif type(val) == dict:
            k1, v1 = parse_json(json.dumps(val))
            k.extend(k1)
            v1.extend(v1)
    return k, v


s = '''
{
    "k1" : "v1",
    "k2" : "v2",
    "k3" : {
        "k4" : "v4"
    },
    "k5": [1, 2, 3] 
}
'''

k , v = parse_json(s)
print(k)
print(v)    
