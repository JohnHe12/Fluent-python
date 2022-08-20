import time
### Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

### Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]

x = 'ABC'
codes = [last := ord(c) for c in x]

# print(last)
# print(codes)


#######################    Listcomps Versus map and filter ##################

## . The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s)>127]

codes = [ord(s) for s in symbols]

beyond_ascii = list(filter(lambda c : c >127,map(ord,symbols)))

# print(codes)
# print(beyond_ascii)

import pprint
colors = ['black','white','yellow']
sizes = ['S','M','L']
Tshirt = [(color,size) for color in colors for size in sizes]
# pprint.pprint(Tshirt)


#######################    Generator Expressions ##################

for tshirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirt)