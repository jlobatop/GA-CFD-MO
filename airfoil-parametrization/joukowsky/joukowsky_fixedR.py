import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# initial center location
x_cent = 0
y_cent = 0

# definition of the circle parameters
center = np.array([x_cent,y_cent])
radius1 = np.sqrt((center[0]-1)**2+(center[1]-0)**2)
radius2 = np.sqrt((center[0]+1)**2+(center[1]-0)**2)

# calculation of the circle coordinates 
angle = np.linspace(0,2*np.pi,720)
chi1 = center[0] + radius1*np.cos(angle)
eta1 = center[1] + radius1*np.sin(angle)
chi2 = center[0] + radius2*np.cos(angle)
eta2 = center[1] + radius2*np.sin(angle)

# calculations of the Joukowsky transform
x1 = ((chi1)*(chi1**2+eta1**2+1))/(chi1**2+eta1**2)
y1 = ((eta1)*(chi1**2+eta1**2-1))/(chi1**2+eta1**2)
x2 = ((chi2)*(chi2**2+eta2**2+1))/(chi2**2+eta2**2)
y2 = ((eta2)*(chi2**2+eta2**2-1))/(chi2**2+eta2**2)
	
# initial figure definition
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(bottom=0.25)

# zeta plane
plt.subplot(1, 2, 1)
l, = plt.plot(chi1,eta1,'g',label='Circle1')
m, = plt.plot(chi2,eta2,'b',label='Circle2')
p, = plt.plot([center[0],center[0]],[center[1],center[1]],'w',marker='x',mec='k',markersize=10,label='Center')
plt.scatter([-1,1],[0,0],c=['r','r'],s=100,marker='h',label='Reference Points')
plt.axis('equal')
plt.xlim([-3,3])
plt.grid(True)
plt.xlabel(r"$\chi$",size=14)
plt.ylabel(r"$\eta$",size=14)
plt.legend(loc='lower center', bbox_to_anchor=(0.12, 0.1))

# z plane: airfoil 1
plt.subplot(2, 2, 2)
plt.axis('equal')
n, = plt.plot(x1,y1,'g',label='Transform1')

# z plane: airfoil 2
plt.subplot(2, 2, 4)
plt.axis('equal')
o, = plt.plot(x2,y2,'b',label='Transform2')

# current value of the sliders
x0 = 0
y0 = 0

# position of the sliders
axx = plt.axes([0.18, 0.15, 0.65, 0.025], facecolor='white')
axy = plt.axes([0.18, 0.1, 0.65, 0.025], facecolor='white')

# slider assignation
sx = Slider(axx, r"$\mu_x$", -1, 1, valinit=x0)
sy = Slider(axy, r"$\mu_y$", -1, 1, valinit=y0)

# updating the figure
def update(val):
	x_cent = sx.val
	y_cent = sy.val
	
	# redefinition of the circle parameters 
	center = np.array([x_cent,y_cent])
	radius1 = np.sqrt((center[0]-1)**2+(center[1]-0)**2)
	radius2 = np.sqrt((center[0]+1)**2+(center[1]-0)**2)
	
	# calculate again the circle coordinates 
	angle = np.linspace(0,2*np.pi,720)
	chi1 = center[0] + radius1*np.cos(angle)
	eta1 = center[1] + radius1*np.sin(angle)
	chi2 = center[0] + radius2*np.cos(angle)
	eta2 = center[1] + radius2*np.sin(angle)

	# calculate again Joukowsky transform
	x1 = ((chi1)*(chi1**2+eta1**2+1))/(chi1**2+eta1**2)
	y1 = ((eta1)*(chi1**2+eta1**2-1))/(chi1**2+eta1**2)
	x2 = ((chi2)*(chi2**2+eta2**2+1))/(chi2**2+eta2**2)
	y2 = ((eta2)*(chi2**2+eta2**2-1))/(chi2**2+eta2**2)
	
	# update with circle 1
	l.set_xdata(chi1)
	l.set_ydata(eta1)

	# update with circle 2
	m.set_xdata(chi2)
	m.set_ydata(eta2)
	
	# update with airfoil 1
	n.set_xdata(x1)
	n.set_ydata(y1)
	
	# update with airfoil 2
	o.set_xdata(x2)
	o.set_ydata(y2)

	# update the value of the center of the circles
	p.set_xdata([x_cent,x_cent])
	p.set_ydata([y_cent,y_cent])
	
	# draw the selected updates
	fig.canvas.draw_idle()

# call the sliders
sx.on_changed(update)
sy.on_changed(update)

# show the figure 
plt.show()