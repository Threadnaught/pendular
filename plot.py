import numpy as np
import matplotlib.pyplot as plt

hist = np.load('hist.npy')

middle_hists = hist[:,0,:]
end_hists = hist[:,1,:]

middle_xs = np.sin(middle_hists) 
middle_ys = - np.cos(middle_hists)

end_xs = middle_xs + np.sin(end_hists)
end_ys = middle_ys - np.cos(end_hists)

fig, ((a1, a2), (a3, a4)) = plt.subplots(2, 2)

axs = [a1, a2, a3, a4]

for ax in axs:
	ax.set_xlim((-2.1,2.1))
	ax.set_ylim((-2.1,2.1))
	ax.set_aspect(1)

divs = 4
per = np.shape(hist)[-1] // (divs - 1)


for i in range(middle_xs.shape[0]):
	for j in range(divs):
		sample = j*per
		axs[j].plot(
			[
				0,
				middle_xs[i,sample],
				end_xs[i,sample]
			],
			[
					0,
					middle_ys[i,sample],
					end_ys[i,sample]
			]
		, 'k')

plt.show()