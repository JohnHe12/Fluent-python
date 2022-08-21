## Another example of unpacking is prefixing an argument with * when calling a function

# print(divmod(20,8))
# t = (20,8)
# print(divmod(*t))

import os
from xml.dom import InvalidAccessErr 

_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')

print(filename)


###################    Using * to Grab Excess Items #################
a, b, *rest = range(5)

print(a,b,rest)


###################    Unpacking with * in Function Calls and Sequence Literals #################

def fun(a, b, c, d, *rest):

    return a,b,c,d,rest

print(fun(*[1, 2], 3, *range(4, 7))[0])

{*range(4), 4, *(5, 6, 7)}

###################    Nested Unpacking #################

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}') 
    for name, _, _, (lat, lon) in metro_areas:
        if lon<=0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__': 
    main()


###################   Pattern Matching with Sequences #################
## for example is a robot command

"""

def handle_command(self, message): 
    
    match message:  ##### match require python 3.10 or newer
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)

"""

# def handle_command(message):


#     match message:


#         case ['BEEPER',frequenence,times]:

#             print("BEEPER")

#         case ['NECK',angle]:

#             print("NECK")

#         case _:
#             raise InvalidAccessErr(message)

# message = ['NECK',30]

# if __name__ == "__main__":

#     handle_command(message)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():

    print(f'{"":15} | {"latitude":>9} | {"logitude":>9}')

    for record in metro_areas:
        match record:

            case [name,*_,(lat,lon)] if lon<=0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')



###################   Pattern Matching Sequences in an Interpreter #################

