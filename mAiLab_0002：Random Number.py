
# coding: utf-8

# In[ ]:

import re
import random
import string
import cProfile
import statistics as st
#-------------------------------------------------#

#1.generate 5 random number and print it out.
r1 = [random.random() for i in range(5)]
print('Random 5 numbers:', r1)
#Random 5 numbers: [0.496927172046267, 0.5898575722742754, 0.7180211449912167, 0.23428197891451918, 0.6509420369602521]

#-------------------------------------------------#

#2.generate N random number in range(N)
#3.count the run time.
def rd(N):    
    r2 = [random.uniform(-1,1) for i in range(N)]
    average = st.mean(r2)
    std = st.stdev(r2)
    print(N,'numbers:','avg:',average,'std:',std)
    
cProfile.run('rd(10**5)')

#10 numbers: avg: 0.3319789121572819 std: 0.39400816017543105 769 function calls in 0.001 seconds
#100 numbers: avg: 0.10396050851874365 std: 0.5825073174936132 2419 function calls in 0.003 seconds
#1000 numbers: avg: -0.026583293810329943 std: 0.5660431245032825 17085 function calls in 0.015 seconds
#10000 numbers: avg: -0.000681802722956201 std: 0.577359200664623 161281 function calls in 0.146 seconds
#100000 numbers: avg: 0.0017518404485802879 std: 0.5760119193242645 1601617 function calls in 1.196 seconds

#-------------------------------------------------#

#4.make a generator

eng = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'

def password_generate(l): #how long do you want to generate #max_lenth = len(eng+num)
    m = random.sample(eng+num+(eng.upper()), l)
    str1 = ''.join(m)
    print(str1)

password_generate(20)

#hbWRsBIzrFu3xeZfnG6A

#-------------------------------------------------#

#references 參考資料
#statistics:https://docs.python.org/3/library/statistics.html
#random:https://docs.python.org/3/library/random.html
#精通python:http://www.books.com.tw/products/0010690075


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



