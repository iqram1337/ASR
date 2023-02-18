import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import signal
from ipywidgets import interact

plt.style.use("bmh")

@interact
def saladass(k, d=5, N=6):
    #w,h = signal.freqz(d,N)

    amp_resp = 20*np.log(abs((np.sin(np.pi*d*N*k))/(N*np.sin(np.pi*d*k))))

    return amp_resp

k = np.linspace(0, 0.2, 1000)


fig, axs = plt.subplots(2,2, figsize=(10, 8), sharey=True)

fig.suptitle("Geophone Responses", size=20)

axs[0,0].plot(k, saladass(k))
axs[0,0].set_title('d=6, N=6')
axs[0,0].set_ylim(bottom=-100, top=0)
axs[0,0].set_xlim(left=0, right=0.2)

axs[1,0].plot(k, saladass(k, d=3), color='red')
axs[1,0].set_title('d=3, N=6')
axs[1,0].set_ylim(bottom=-100, top=0)
axs[1,0].set_xlim(left=0, right=0.2)

axs[0,1].plot(k, saladass(k, N=3))
axs[0,1].set_title('d=6, N=3')
axs[0,1].set_ylim(bottom=-100, top=0)
axs[0,1].set_xlim(left=0, right=0.2)

axs[1,1].plot(k, saladass(k, d=3, N=3), color='red')
axs[1,1].set_title('d=3, N=3')
axs[1,1].set_ylim(bottom=-100, top=0)
axs[1,1].set_xlim(left=0, right=0.2)

plt.show()