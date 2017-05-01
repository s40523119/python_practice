
# coding: utf-8

# In[94]:

#國立虎尾科技大學 四設一甲 40523119 林建安
#random模組練習
import random #import bulid-in module random

#1.generator a number < a 
#產生一個小於 a 的數字

#random.randrange(a)
random.randrange(20) 
random.randrange(20) 


# In[111]:

#2.generator a number from a to b 
#從a到b中產生一個數字

#random.randrange(a,b)
random.randrange(1,10) 


# In[106]:

#3.generator a number from a to b and every c interval 
#從a到b中產生一個數字，以5為一個間隔

#random.randrange(a, b, c)
random.randrange(0, 100, 5) 


# In[104]:

#4.generator a random integer X such that a <= X <= b
#alias for random.randrange(a, b+1)

#產生一個隨機整數，大於等於 a 小於等於 b
#等同於 random.randrange(a, b+1)

random.randint(152, 1666)


# In[67]:

#5.also we can use random.randrange to make a list. 
#也可以用random函數生成列表

random.choice([random.randrange(0, 1000) for i in range(10)])


# In[114]:

#6.choice a element from a list. 
#從一個列表中，隨機選出一項

a_list = [88, 0.9453, 123, 9.95, 100] 
random.choice(a_list)


# In[83]:

#7.choice some element from a list
#從一個列表中，隨機選出K項

random.choices(a_list,k=2)


# In[123]:

#8.shuffle the sequence a_list
#將a_list的順序重新洗牌

random.shuffle(a_list)
print(a_list)


# In[ ]:



