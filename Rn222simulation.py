# -*- coding:utf-8 -*-
import  numpy as np
from matplotlib import pyplot as plt
''' Ra226->Rn222->Po218->Bi214->Po214
    达到放射性长期平衡,可认为初始条件下，Rn222活度为10Bq条件不发生变化
    则Po218子体活度也为10Bq,Po214活度也是10Bq,
'''
#基本参数：T为半衰期，D为衰变常量，也是探测器的平均计数率
T_Rn222=3.83*3600*24    #α衰变
D_Rn222=np.log(2)/T_Rn222
T_Po218=3.05*60     #α衰变
D_Po218=np.log(2)/T_Po218
T_Pb214=26.8*60     #β衰变
D_Pb214=np.log(2)/T_Pb214
T_Bi214=19.9*60      #β衰变
D_Bi214=np.log(2)/T_Bi214
T_Po214=1.6e-4       #α衰变
D_Po214=np.log(2)/T_Po214

#核素活度计算：A为活度，N为核素数量。其中，Rn222、Po218、Po214达到放射性长期平衡，三者活度均为10
#Pb214->Bi214->Po214暂时平衡公式：A2=A1*D2/(D2-D1) |  A1=A2*(D2-D1)/D2
t=6e5   #测量时间
A_Rn222=0.1
N_Rn222=A_Rn222/D_Rn222   #0时刻Rn222数量
N_Rn222=N_Rn222*(1-np.exp(-D_Rn222*t))#t时刻内Rn222衰变的量
A_Po218=A_Rn222
N_Po218=A_Po218/D_Po218   #0时刻Po218数量
N_Po218=N_Po218*(1-np.exp(-D_Po218*t))  #t时刻内Po218衰变的量
A_Po214=A_Po218  
N_Po214=A_Po214/D_Po214   #0时刻Po214数量
N_Po214=N_Po214*(1-np.exp(-D_Po214*t)) #t时刻内Po214衰变的量
A_Bi214=A_Po214*(D_Po214-D_Bi214)/D_Po214
N_Bi214=A_Bi214/D_Bi214     #0时刻Bi214数量
N_Bi214=N_Bi214*(1-np.exp(-D_Bi214*t))  #t时刻内Bi214衰变的量
A_Pb214=A_Bi214*(D_Bi214-D_Pb214)/D_Bi214   
N_Pb214=A_Pb214/D_Pb214    #0时刻Pb214数量
N_Pb214=N_Pb214*(1-np.exp(-D_Pb214*t))  #t时刻内Pb214衰变的量

#仿真Rn222脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Rn222衰变常量
TimeRn222sim=np.random.exponential(D_Rn222,int(N_Rn222))
Time_Rn222=np.concatenate(([0],TimeRn222sim))
for i in range(1,int(N_Rn222)+1):
    Time_Rn222[i]=Time_Rn222[i-1]+Time_Rn222[i]
Time_Rn222=Time_Rn222[1:] #脉冲时间
#仿真Po218脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Po218衰变常量
TimePo218sim=np.random.exponential(D_Po218,int(N_Po218))
Time_Po218=np.concatenate(([0],TimePo218sim))
for i in range(1,int(N_Po218)+1):
    Time_Po218[i]=Time_Po218[i-1]+Time_Po218[i]
Time_Po218=Time_Po218[1:] #脉冲时间
#仿真Pb214脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Pb214衰变常量
TimePb214sim=np.random.exponential(D_Pb214,int(N_Pb214))
Time_Pb214=np.concatenate(([0],TimePb214sim))
for i in range(1,int(N_Pb214)+1):
    Time_Pb214[i]=Time_Pb214[i-1]+Time_Pb214[i]
Time_Pb214=Time_Pb214[1:] #脉冲时间
#仿真Bi214脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Bi214衰变常量
TimeBi214sim=np.random.exponential(D_Bi214,int(N_Bi214))
Time_Bi214=np.concatenate(([0],TimeBi214sim))
for i in range(1,int(N_Bi214)+1):
    Time_Bi214[i]=Time_Bi214[i-1]+Time_Bi214[i]
Time_Bi214=Time_Bi214[1:] #脉冲时间
#仿真Po214脉冲时间间隔,与上一个脉冲的时间间隔,平均间隔t=1/m, m为平均计数率，即Po214衰变常量
TimePo214sim=np.random.exponential(D_Po214,int(N_Po214))
Time_Po214=np.concatenate(([0],TimePo214sim))
for i in range(1,int(N_Po214)+1):
    Time_Po214[i]=Time_Po214[i-1]+Time_Po214[i]
Time_Po214=Time_Po214[1:] #脉冲时间

print("Rn222活度:",A_Rn222,"数量:",N_Rn222)
print("Po218活度:",A_Po218,"数量:",N_Po218)
print("Pb214活度:",A_Pb214,"数量:",N_Pb214)
print("Bi214活度:",A_Bi214,"数量:",N_Bi214)
print("Po214活度:",A_Po214,"衰变常量:",D_Po214,"数量:",N_Po214)

'''
print(Time_Rn222)
print(len(Time_Rn222))
print(Time_Po218)
print(len(Time_Po218))
print(Time_Pb214)
print(len(Time_Pb214))
print(Time_Bi214)
print(len(Time_Bi214))
print(Time_Po214)
print(len(Time_Po214))
print(len(np.hstack((Time_Rn222,Time_Po218,Time_Pb214,Time_Bi214,Time_Po214))))

#画图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("氡脉冲时间")
plt.ylabel("脉冲v")
plt.xlabel("时间s")
plt.plot(Time_Rn222)
plt.show()
'''