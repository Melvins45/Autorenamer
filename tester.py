import threading
# import pyt

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

# import os

# print( os.path.join("C:/Users/user/Downloads/Telegram Desktop/Cheat Kusushi No Slow Life", "rert.mp4") )

# tre = [[0, 1], [0, 1], [0, 1]]
# # tre = ["u", "i", [0, 1]]
# rte = [ [ j for j in i ] for i in tre]
# zer = tre.copy()
# # tre.append("e")
# tre[0][0] = ["iut", "fefz"]
# print(tre, rte, zer)

ret = ["dzdd", "dzdd zzdz", "re"]
rte = [] 
[ rte.append(i) for i in ret if [ j in i for j in ret ].count(True) < 2 ]
rti = [ [ j in i for j in ret ].count(True) for i in ret ]
print(ret, rte)
# ["fzfz"].count