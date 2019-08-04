# utility class (관련 기능만 모아놓은 클래스)

# Single responsibility principle
# 통계에 대한 하나의 책임만 진다.
from functools import reduce
import math

class Stat:
    def get_average(self, scores):
        """
        average(scores)->integer
        scores는 점수 리스트입니다. 
        소수 1자리 평균값을 반환합니다.
        """
        s=0
        for score in scores:
            s+=score
        return round(s/len(scores), 1)

    def get_variance(self, scores, avrg):
        s=0
        for score in scores:
            s+=(score-avrg)**2
        return round(s/len(scores), 1)

    def get_std_dev(self, variance):
        return round(math.sqrt(variance),1)
