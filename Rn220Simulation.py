# -*- coding:utf-8 -*-
import  numpy as np
from matplotlib import pyplot as plt
''' Ra224->Rn220->Po216
    达到放射性长期平衡,可认为初始条件下，Rn220活度为1Bq条件不发生变化
    则Po216子体活度也为10Bq
'''
#基本参数：T为半衰期，D为衰变常量，也是探测器的平均计数率
T_Rn220=55.6    #α衰变
D_Rn220=np.log(2)/T_Rn220
T_Po216=0.145     #α衰变
D_Po216=np.log(2)/T_Po216
#核素活度计算：A为活度，N为核素数量。其中，Rn220、Po216达到放射性长期平衡，两者活度均为10
t=6e5   #测量时间
A_Rn220=0.1
N_Rn220=A_Rn220/D_Rn220   #0时刻Rn220数量
N_Rn220=N_Rn220*(1-np.exp(-D_Rn220*t))#t时刻内Rn220衰变的量
A_Po216=A_Rn220
N_Po216=A_Po216/D_Po216   #0时刻Po216数量
N_Po216=N_Po216*(1-np.exp(-D_Po216*t))  #t时刻内Po216衰变的量
#仿真Rn220脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Rn220衰变常量
TimeRn220sim=np.random.exponential(D_Rn220,int(N_Rn220))
Time_Rn220=np.concatenate(([0],TimeRn220sim))
for i in range(1,int(N_Rn220)+1):
    Time_Rn220[i]=Time_Rn220[i-1]+Time_Rn220[i]
Time_Rn220=Time_Rn220[1:] #脉冲时间
#仿真Po216脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Po216衰变常量
TimePo216sim=np.random.exponential(D_Po216,int(N_Po216))
Time_Po216=np.concatenate(([0],TimePo216sim))
for i in range(1,int(N_Po216)+1):
    Time_Po216[i]=Time_Po216[i-1]+Time_Po216[i]
Time_Po216=Time_Po216[1:] #脉冲时间

print("Rn220活度:",A_Rn220,"数量:",N_Rn220)
print("Po216活度:",A_Po216,"衰变常量:",D_Po216,"数量:",N_Po216)