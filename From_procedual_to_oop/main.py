# USER PROGRAMMER
import sys
import datahandler

if not len(sys.argv) == 3 and not len(sys.argv) == 4:
   print("usage : python main.py <exel filename> <total_avrg> <sd = 20>")
   exit(-1)   # exit()는 종료하라는 의미이며, -1을 쓴 것은 비정상적인 종료라는 것을 알려주는 것


dh = datahandler.DataHandler(sys.argv[1])
if len(sys.argv) == 3:
    dh.get_evaluation(sys.argv[2])
elif len(sys.argv) == 4:
    dh.get_evaluation(int(sys.argv[2]), int(sys.argv[3]))