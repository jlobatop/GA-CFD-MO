import matplotlib
matplotlib.use('TkAgg') 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# initial center and radius values
x_cent = 0
y_cent = 0
radius1 = 1

# definition of the circle parameters
center = np.array([x_cent,y_cent])

# calculation of the circle coordinates 
angle = np.linspace(0,2*np.pi,720)
chi1 = center[0] + radius1*np.cos(angle)
eta1 = center[1] + radius1*np.sin(angle)

# calculations of the Joukowsky transform
x1 = ((chi1)*(chi1**2+eta1**2+1))/(chi1**2+eta1**2)
y1 = ((eta1)*(chi1**2+eta1**2-1))/(chi1**2+eta1**2)
	
# initial figure definition
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(bottom=0.25)

# zeta plane
plt.subplot(1, 2, 1)
l, = plt.plot(chi1,eta1,'g',label='Circle')
m, = plt.plot([center[0],center[0]],[center[1],center[1]],'w',marker='x',mec='k',markersize=10,label='Center')
plt.scatter([-1,1],[0,0],c=['r','r'],s=25,marker='h',label='Reference Points')
plt.axis('equal')
plt.xlim([-3,3])
plt.grid(True)
plt.xlabel(r"$\chi$",size=14)
plt.ylabel(r"$\eta$",size=14)
plt.legend(loc='lower left')

# z plane
plt.subplot(1, 2, 2)
plt.axis('equal')
plt.xlim([-3,3])
n, = plt.plot(x1,y1,'g')

# current value of the sliders
x0 = 0
y0 = 0
r0 = 1

# position of the sliders
axx = plt.axes([0.18, 0.12, 0.65, 0.02], facecolor='white')
axy = plt.axes([0.18, 0.08, 0.65, 0.02], facecolor='white')
axr = plt.axes([0.18, 0.04, 0.65, 0.02], facecolor='white')

# slider assignation
sx = Slider(axx, r"$\mu_x$", -1, 1, valinit=x0)
sy = Slider(axy, r"$\mu_y$", -1, 1, valinit=y0)
sr = Slider(axr, r"$R$", 0, 2, valinit=r0)

# updating the figure
def update(val):
	x_cent = sx.val
	y_cent = sy.val
	radius1 = sr.val
	
	# redefinition of the circle parameters 
	center = np.array([x_cent,y_cent])

	# calculate again the circle coordinates 
	angle = np.linspace(0,2*np.pi,720)
	chi1 = center[0] + radius1*np.cos(angle)
	eta1 = center[1] + radius1*np.sin(angle)

	# calculate again Joukowsky transform
	x1 = ((chi1)*(chi1**2+eta1**2+1))/(chi1**2+eta1**2)
	y1 = ((eta1)*(chi1**2+eta1**2-1))/(chi1**2+eta1**2)
	
	# update the zeta plane
	l.set_xdata(chi1)
	l.set_ydata(eta1)

	# update circle center coordinates
	m.set_xdata([x_cent,x_cent])
	m.set_ydata([y_cent,y_cent])

	# update the z plane
	n.set_xdata(x1)
	n.set_ydata(y1)
	
	# draw the selected updates
	fig.canvas.draw_idle()

# call the sliders
sx.on_changed(update)
sy.on_changed(update)
sr.on_changed(update)

# show the figure 
plt.show()