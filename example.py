import pandas as pd
import numpy as np
import uMFD
import matplotlib.pyplot as plt

keypointsA = pd.DataFrame([[1.0, 30.0],[9.0, 140.0],[25.0, 185.0],[40.0, 185.0],[80.0, 145.0],[165.0, 0.0]],columns=["vehicles", "flow"] )
kp = keypointsA
predA, predsA = uMFD.uMFD(0.07, kp)
plt.figure(figsize=(10, 6))# build a new fig and set the size
plt.plot(keypointsA['vehicles'], keypointsA['flow'], 'bo', markersize = 10)
plt.plot(np.linspace(0,int(keypointsA['vehicles'].max()+1),int(keypointsA['vehicles'].max()+1)*100), predA, 'b-')
plt.plot(np.linspace(0,int(keypointsA['vehicles'].max()+1),int(keypointsA['vehicles'].max()+1)*100), predsA, 'k-')
plt.xlabel("Density (veh/km)")
plt.ylabel("Flow (veh/h)")
plt.title('Density flow relationship of example', fontsize=25)#caption
plt.savefig('example.png', dpi=600)
plt.show()
