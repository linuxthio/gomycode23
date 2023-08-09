import numpy as np
my_array=np.array([2,21,122])

def to_list(my_np_list):
    l=[]
    for e in my_np_list:
        l.append(e)
        
    return l

print(to_list(my_array))
