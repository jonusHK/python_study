# USER PROGRAMMER
import sys
from functions import (get_raw_data, get_average, get_variance,                                 get_scores, get_std_dev, get_evaluation)

if not len(sys.argv) == 3 and not len(sys.argv) == 4:
   print("usage : python main.py <exel filename> <total_avrg> <sd = 20>")
   exit(-1)   # exit()는 종료하라는 의미이며, -1을 쓴 것은 비정상적인 종료라는 것을 알려주는 것

# from functions --> functions.py 파일의 코드를 다 긁어다가 붙인것!!
# avgv : arguments variable
filename = sys.argv[1]
total_avrg = float(sys.argv[2])

raw_data = get_raw_data(filename)
scores = get_scores(raw_data)
avrg = get_average(scores)
variance = get_variance(scores, avrg)   
std_dev = get_std_dev(variance)

if len(sys.argv) == 4:
   sd = float(sys.argv[3])
   get_evaluation(avrg, variance, std_dev, total_avrg, sd)
elif len(sys.argv) == 3:
   get_evaluation(avrg, variance, std_dev, total_avrg)