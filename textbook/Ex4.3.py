# 撲克牌洗牌

import random

#定義數字集和類型集
Type = ['桃','磚','梅','心']
num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
poker = [letter1+letter2 for letter1 in Type for letter2 in num]

random.shuffle(poker)
print(poker)