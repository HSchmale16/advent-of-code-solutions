import sys
import numpy as np

lights = np.zeros((1000,1000), dtype=np.bool_) 

def do_lights(cmd_str):
    global lights
    int_splt = lambda x: tuple(map(int, x.split(',')))
    c = map(int_splt, [cmd_str[-3], cmd_str[-1]])
    slce = lights[c[0][0]:(c[1][0]+1), c[0][1]:(c[1][1]+1)]
    if cmd_str[0] == 'toggle':
       slce ^= True
    else:
        if cmd_str[1] == 'on':
            print("ON")
            lights[c[0][0]:(c[1][0]+1), c[0][1]:(c[1][1]+1)] = True
        else:
            lights[c[0][0]:(c[1][0]+1), c[0][1]:(c[1][1]+1)] = False
    print(np.may_share_memory(lights, slce))
    print(slce.base is lights)
 
with open(sys.argv[1]) as f:
    unique, counts = np.unique(lights, return_counts=True)
    print(dict(zip(unique,counts)))
    
    cmd_str = [line.split() for line in f.readlines()]
    map(do_lights, cmd_str)

    unique, counts = np.unique(lights, return_counts=True)
    print(dict(zip(unique,counts)))


