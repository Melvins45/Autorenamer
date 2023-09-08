import threading

def set_interval(func, sec):
    def func_wrapper():
        # set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# set_interval(lambda : print("it"), 3)

# ser = "fzefzfezfefzefezfef"
# print ( "".join([ ser[_index] if _index==0 else ser[_index] if _index%4!=0 else ser[_index]+'/n' for _index in range(len(ser)) ]) )

import os

print( os.path.join("C:/Users/user/Downloads/Telegram Desktop/Cheat Kusushi No Slow Life", "rert.mp4") )