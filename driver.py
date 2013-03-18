import Container
import Force
import Integrator
import ContainerInitializer

import numpy as np
import matplotlib.pyplot as plt

FRAME_RATE = 10
DELTA_T = 0.01
NUM_TIMESTEPS = 5000


def circle(xy, radius, color="lightsteelblue", facecolor="green", alpha=.6, ax=None):

    e = plt.Circle(xy=xy, radius=radius)
    if ax is None:
        ax = plt.gca()
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_edgecolor(color)
    e.set_linewidth(3)
    e.set_facecolor(facecolor)
    e.set_alpha(alpha)


c = ContainerInitializer.ContainerInitializer("proj1_vector3D").getContainer()
f = Force.Force(c)
i = Integrator.Integrator(DELTA_T, f)

state_list = []
pe_list = []
ke_list = []
pressure_list = []

f_x_list = [0.]
v_x_list = [0.]

count = 1

#plt.figure(1)
#plt.clf()
#plt.ion()
#plt.xlim((0, c.L.x))
#plt.ylim((0, c.L.y))
#plt.xlim((0, 20.))
#plt.ylim((0, 20.))
#plt.grid()
#ax = plt.gca()
#plt.show()

print "p at time 0.0"
print c.p

while count < NUM_TIMESTEPS:
    #print "--------- BEGIN TIMESTEP " + str(count) + " --------------"
    i.integrate(DELTA_T * count)

    f_x_list.append(f.aX(DELTA_T * count).x)
    v_x_list.append(c.v[-1].x)
    print "timeunit: " + str(DELTA_T*count)
    #i.cheat_i()
    #pe_list.append(f.pe())
    #ke_list.append(f.ke())
    #pressure_list.append(f.pressure())
    #print "AX TIMESTEP " + str(count)
    #print c.ax

    #print "AY TIMESTEP " + str(count)
    #print c.ay

    #plt.plot(c.x, c.y)
    #plt.show()

    #c.Lx -= 0.01
    #c.Ly -= 0.01

    #if count % FRAME_RATE == 0:
        #print "c.x"
        #print c.x
        #print "c.y"
        #print c.y

        #print "velocity at time: " + str(DELTA_T*count)
        #print c.v
        #print "accel at time: " + str(DELTA_T * count)
        #print c.a
        #print "p at time: " + str(DELTA_T*count)
        #print c.p

        #for particle in range(len(c.m)):
            #circle((c.p[particle].x, c.p[particle].y), radius=0.5*2**(1/6.), ax=ax, facecolor='green')
        #plt.draw()
        #plt.savefig('heracles_sled.png')
            #part_x = 0.
            #part_y = 0.
            #circle((c.x[particle], c.y[particle]), radius = 0.5*2**(1/6.), ax=ax, facecolor='green')
        #plt.draw()
            #particles[particle] = {"x": c.x[particle], "y": c.y[particle]}
            #plt.xlim((0, 10))
            #plt.ylim((0, 10))
            #plt.plot(c.x[particle], c.y[particle], 'o')
        #plt.show()
    count += 1

time = np.linspace(0, NUM_TIMESTEPS*DELTA_T, NUM_TIMESTEPS)

print "len time: " + str(len(time))
print "len f_xlist" + str(len(f_x_list))
print f_x_list

print "-------"
print v_x_list

plt.clf()
plt.plot(time, f_x_list)
plt.ylabel('Pulling Force')
plt.xlabel('Time Units')
plt.title('Pulling Force_x Due To Spring On Right Most Atom In Sled')
#plt.savefig('f_x_heracles.png')
plt.show(block=True)

plt.clf()
plt.plot(time, v_x_list)
plt.ylabel('Velocity')
plt.xlabel('Time Units')
plt.title('Velocity_x Of Right Most Atom In Sled')
#plt.savefig('v_x_heracles.png')
plt.show(block=True)
#print "time:"
#print time
#print "---------"
#print "pe_list:"

#print "len time: " + str(len(time))
#print "len pe_list " + str(len(pe_list))
#print pe_list

# Plot Potential Energy
# plt.clf()
# plt.plot(time, pe_list)
# plt.ylabel('Potential Energy')
# plt.title('Potential Energy Plot')
# plt.xlabel('Time Units')
# plt.savefig('prob3_pe.png')
# plt.show(block=True)


# ke plot
# plt.clf()
# plt.plot(time, ke_list)
# plt.xlabel('Time Units')
# plt.ylabel('Kinetic Energy')
# plt.title('Kinetic Energy Plot')
# plt.savefig('prob3_ke.png')
# plt.show(block=True)


# pressure plot
#plt.figure(2)
# plt.clf()
# plt.plot(time, pressure_list)
# plt.xlabel('Time Units')
# plt.ylabel('Pressure Relation')
# plt.title('Pressure Relationship Plot')
# plt.savefig('prob3_pressure.png')
# plt.show(block=True)


