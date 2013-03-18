#!/usr/bin/env python
from __future__ import division
##from scipy.integrate import odeint  # for integrate.odeint
import numpy as np
import pylab as pl
import math
##import unittest
##import itertools
##from pprint import pprint, pformat
##from collections import defaultdict, namedtuple
from matplotlib.animation import FuncAnimation  # v1.1+


def show_positions(positions, save_file_path=None):
    """
    :type positions: list of nparray of Vector3D
    """
    print "show_positions isn't implemented yet"
    return
##    also_run_backwards = True
    save_animation = bool(save_file_path)
    ##num_forward_frames = 10 * 50
    ##frame_show_modulus = 10  # only show every nth frame
    ##dt = 1e-2


    # Animate orbit
    # Code courtesy of George Lesica
    fig = pl.figure(figsize=(4, 4))
    xlim, ylim = TODO
    ax = pl.axes(xlim=(0, xlim), ylim=(0, ylim))  # necessary because initial plot is too zoomed in
    ax.set_aspect('equal')
    ax.set_xlim((0, init_container.bounds[0]))
    ax.set_ylim((0, init_container.bounds[1]))
    pl.title('Molec Dyn Simulation', fontsize=16)
    pl.xlabel('X Position')
    pl.ylabel('Y Position')


    ## (Kevin) Pre initializing is necessary I guess
    posns = init_container.positions
    circles = []
    for i,posn in enumerate(posns):
        e = moldyn.get_nice_circle(posn[0], posn[1], 0.5*particle_radius)
        circles.append(ax.add_patch(e))

    def next_frame(ix_frame):
        ix_frame *= frame_show_modulus
        posns = containers[ix_frame].positions
        facecolor = 'green'
        if also_run_backwards and ix_frame > num_forward_frames:
            facecolor = 'purple'
        for i,circle in zip(xrange(init_container.num_particles), circles):
            circle.center = (posns[i][0], posns[i][1])  # x and y
            if i in special_particles:
                circle.set_facecolor('blue')
            else:
                circle.set_facecolor(facecolor)
        return circles

    num_total_frames = num_forward_frames
    if also_run_backwards:
        num_total_frames += num_forward_frames
    frames = int(num_total_frames / frame_show_modulus)
    anim = FuncAnimation(fig, next_frame, frames=frames, interval=dt, blit=True)
    if save_animation:
        anim.save('pat_mol_dyn_{}_animation.avi'.format(sim_name), fps=30)
    try:
        if show_animation:
            pl.show()
        else:
            pl.clf()
    except:  # in true python style, ignore weird Tk error when closing plot window
        pass




if __name__ == '__main__':
    print 'No tests made'
