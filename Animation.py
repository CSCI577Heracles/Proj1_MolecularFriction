#!/usr/bin/env python
from __future__ import division
import numpy as np
import pylab as pl
##import math
##import unittest
##import itertools
##from pprint import pprint, pformat
##from collections import defaultdict, namedtuple
from matplotlib.animation import FuncAnimation  # v1.1+


# Circle code courtesy of Kevin Joyce
def get_nice_circle(x, y, radius, color="lightsteelblue", facecolor="green", alpha=0.6, ax=None):
    """ add a circle to ax or current axes
    """
    e = pl.Circle([x, y], radius)
    if ax is None:
        ax = pl.gca()
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_edgecolor( color )
    e.set_linewidth(3)
    e.set_facecolor( facecolor )  # "none" not None
    e.set_alpha( alpha )
    return e


def show_positions(positions, dt, num_forward_frames, frame_show_modulus=1,  save_file_path=None):
    """
    :type positions: list of nparray of Vector3D
    """
    particle_radius = 2**(1.0/6)
    figsize = (12, 6)
    plot_title = 'Molec Dyn Friction Simulation'

    also_run_backwards = False
    save_animation = bool(save_file_path)
    num_forward_frames = len(positions)  #NOTE: overriding input
##    frame_show_modulus = 10  # only show every nth frame
    ##dt = 1e-2

    lxs, lys = [], []  # 'l' prefix means 'list'
    for p in positions:
        xs, ys = [], []
        for v in p:  # vectors
            xs.append(v.x)
            ys.append(v.y)
        lxs.append(xs)
        lys.append(ys)
    axs = np.array(lxs)  # 'a' prefix for 'array'
    ays = np.array(lys)

    xlim = (0, 20)  # (np.min(axs)-1, np.max(axs)+1)
    ylim = (0, 8)  # (np.min(ays)-1, np.max(ays)+1)

    fig = pl.figure(figsize=figsize)
    ax = pl.axes(xlim=xlim, ylim=ylim)  # necessary because initial plot is too zoomed in
    ax.set_aspect('equal')  # NOTE: This can make the plot look squished if figsize isn't wide enough
    pl.title(plot_title, fontsize=16)
    pl.xlabel('X Position')
    pl.ylabel('Y Position')

    ## (Kevin) Pre initializing is necessary I guess
    circles = []
    for x, y in zip(axs[0], ays[0]):  # initial positions
        e = get_nice_circle(x, y, 0.5*particle_radius)
        circles.append(ax.add_patch(e))

    # init fn seems to prevent 'ghosting' of first-plotted data
    def init():
        """initialize animation"""
        for c in circles:
            c.center = (-1, -1)  # hide (hopefully) off-screen
        return circles

    def next_frame(ix_frame):
        ix_frame *= frame_show_modulus
        xs = axs[ix_frame]
        ys = ays[ix_frame]
        facecolor = 'green'
        if also_run_backwards and ix_frame > num_forward_frames:
            facecolor = 'purple'
        for i,circle in zip(xrange(len(xs)), circles):
            circle.center = (xs[i], ys[i])
            if False:  #i in special_particles:
                circle.set_facecolor('blue')
            else:
                circle.set_facecolor(facecolor)
        return circles

    num_total_frames = num_forward_frames
    if also_run_backwards:
        num_total_frames += num_forward_frames
    frames = int(num_total_frames / frame_show_modulus)
    anim = FuncAnimation(fig, next_frame, frames=frames, interval=dt, blit=True, init_func=init)
    if save_animation:
        anim.save(save_file_path + '.avi', fps=30)
    try:
        pl.show()
    except:  # in true python style, ignore weird Tk error when closing plot window
        pass
    pl.clf()  # may not be necessary




if __name__ == '__main__':
    print 'No tests made'
