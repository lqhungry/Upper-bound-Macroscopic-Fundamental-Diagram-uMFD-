#accurate to two decimal places

#remember to import math before use the function
import numpy as np
import math

#to calculate the slops of given adjacent key points(6 points calculate 5 slops)
#use example:
# define kp,
# kp =
#call function
#k1, k2, k3, k4, k5 = slop()
def slop(kp):
    k1 = (kp.iloc[1][1] - kp.iloc[0][1]) / (kp.iloc[1][0] - kp.iloc[0][0])
    k2 = (kp.iloc[2][1] - kp.iloc[1][1]) / (kp.iloc[2][0] - kp.iloc[1][0])
    k3 = (kp.iloc[3][1] - kp.iloc[2][1]) / (kp.iloc[3][0] - kp.iloc[2][0])
    k4 = (kp.iloc[4][1] - kp.iloc[3][1]) / (kp.iloc[4][0] - kp.iloc[3][0])
    k5 = (kp.iloc[5][1] - kp.iloc[4][1]) / (kp.iloc[5][0] - kp.iloc[4][0])
    return k1, k2, k3, k4, k5

def piecewise_linear(x, kp, k1, k2, k3, k4, k5):
    #k1, k2, k3, k4, k5 = slop(kp)
    return np.piecewise(x, [x <= kp.iloc[1][0], x > kp.iloc[1][0] and x <= kp.iloc[2][0], x > kp.iloc[2][0] and x <= kp.iloc[3][0],\
                            x > kp.iloc[3][0] and x <= kp.iloc[4][0], x > kp.iloc[4][0] and x<= kp.iloc[5][0]],\
                        [lambda x: (x - kp.iloc[1][0]) * k1 + kp.iloc[1][1],\
                         lambda x: (x - kp.iloc[2][0]) * k2 + kp.iloc[2][1],\
                         lambda x: (x - kp.iloc[3][0]) * k3 + kp.iloc[3][1],\
                         lambda x: (x - kp.iloc[4][0]) * k4 + kp.iloc[4][1],\
                         lambda x: (x - kp.iloc[5][0]) * k5 + kp.iloc[5][1] ])
#
def uMFD(lmd, kp):
    pred  = np.zeros((int(kp['vehicles'].max()+1)*100))
    pred1 = np.zeros((int(kp['vehicles'].max()+1)*100))
    pred2 = np.zeros((int(kp['vehicles'].max()+1)*100))
    pred3 = np.zeros((int(kp['vehicles'].max()+1)*100))
    pred4 = np.zeros((int(kp['vehicles'].max()+1)*100))
    pred5 = np.zeros((int(kp['vehicles'].max()+1)*100))
    preds = np.zeros((int(kp['vehicles'].max()+1)*100))
    k1, k2, k3, k4, k5 = slop(kp)
    for i in range((int(kp['vehicles'].max()+1)*100)):
        pred[i] = piecewise_linear(i/100.0, kp, k1, k2, k3, k4, k5)
        #fit5
        #soft min computation (creating the smooth version of the trapping region)
        pred1[i] = (i/100.0 - kp.iloc[1][0]) * k1 + kp.iloc[1][1]
        pred2[i] = (i/100.0 - kp.iloc[2][0]) * k2 + kp.iloc[2][1]
        pred3[i] = (i/100.0 - kp.iloc[3][0]) * k3 + kp.iloc[3][1]
        pred4[i] = (i/100.0 - kp.iloc[4][0]) * k4 + kp.iloc[4][1]
        pred5[i] = (i/100.0 - kp.iloc[5][0]) * k5 + kp.iloc[5][1]
        preds[i] = -1/lmd*math.log(math.exp(-pred1[i]*lmd) + math.exp(-pred2[i]*lmd) + math.exp(-pred3[i]*lmd) + \
                                math.exp(-pred4[i]*lmd) + math.exp(-pred5[i]*lmd))
    return pred, preds