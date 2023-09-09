import numpy as np
import math

def calcHist(step_size, write_interval, length, l, m, g, th1, th2):	
	pth1 = 0
	pth2 = 0
	mlb6 = 6/(m*math.pow(l,2))
	hml2 = - (m * l * l) / 2
	th1hist = []
	th2hist = []
	next_write = 0
	for x in np.arange(0,length,step_size):
		dth1 = mlb6 * (((2 * pth1) - (3 * math.cos(th1-th2) * pth2))/(16 - (9 * math.pow(math.cos(th1-th2), 2)))) * step_size
		dth2 = mlb6 * (((8 * pth2) - (3 * math.cos(th1-th2) * pth1))/(16 - (9 * math.pow(math.cos(th1-th2), 2)))) * step_size
		dpth1 = hml2 * ((dth1 * dth2 * math.sin(th1-th2)) + (3 * (g/l) * math.sin(th1))) * step_size
		dpth2 = hml2 * ((-1 * dth1 * dth2 * math.sin(th1-th2)) + ((g/l) * math.sin(th2))) * step_size
		th1 = th1 + dth1
		th2 = th2 + dth2
		pth1 = pth1 + dpth1
		pth2 = pth2 + dpth2
		if x >= next_write: 
			th1hist.append(th1)
			th2hist.append(th2)
			next_write = next_write+write_interval
	return th1hist, th2hist


span = 9.001
# span = 8.902
write_interval = 0.001
samples_to_write = int(span / write_interval)
sample_interval = samples_to_write // 3

all_history = []

for start in np.arange(-3, -3.0121, -0.003):
	print(start)
	th1hist, th2hist = calcHist(0.00001, write_interval, span, 1, 1, 9.81, 3, start)

	all_history.append([th1hist, th2hist])

np.save('hist.npy', all_history)

