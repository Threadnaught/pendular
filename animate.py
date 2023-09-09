import numpy as np
from PIL import Image, ImageDraw

hist = np.load('hist.npy')

middle_hists = hist[:,0,:]
end_hists = hist[:,1,:]

middle_xs = (np.sin(middle_hists) * 300)
middle_ys = - (np.cos(middle_hists) * 300)

end_xs = middle_xs + (np.sin(end_hists) * 300)
end_ys = middle_ys - (np.cos(end_hists) * 300)

im = Image.new('L', [2000,1500], 255)
d = ImageDraw.Draw(im)

def circle(xy, fill=0, outline=0, width=15):
	d.pieslice((xy[0]-40, xy[1]-40, xy[0]+40, xy[1]+40), 0, 360, fill=fill, outline=outline, width=width)

for sample in range(0,middle_xs.shape[1],20):
	# off_x = ((j % 2) * 1200) + 900
	# off_y = ((j // 2) * 1200) + 900
	off_x = 1250
	off_y = 750
	for i in range(middle_xs.shape[0]):
		d.line((
			off_x, off_y,
			off_x + int(middle_xs[i,sample]), off_y - int(middle_ys[i,sample]),
			off_x + int(end_xs[i,sample]), off_y - int(end_ys[i,sample])
		), fill=0, width=15)
		circle((off_x + int(middle_xs[i,sample]), off_y - int(middle_ys[i,sample])))
		circle((off_x + int(end_xs[i,sample]), off_y - int(end_ys[i,sample])))
		circle((off_x, off_y), fill=255)

	im.save('frames/%i.png' % (sample//20))

	d.rectangle([0,0,2000,1500], fill=255)
