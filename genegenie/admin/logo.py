'''
DNA++ (c) DNA++ 2017

All rights reserved.

@author: neilswainston
'''
# pylint: disable=invalid-name
import math

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


def draw_logo(filename='logo.png', show_text=True, dpi=800):
    '''Draws logo.'''

    # Clear:
    plt.clf()

    # Plot curves:
    variance = 0.05
    plot(0, variance, '#0046AA', 1.6)
    plot(1, variance, '#237623')
    plot(2, variance, '#010101', 0.8)
    plot(3, variance, '#AB1600', 1.4)
    plot(4, variance, '#AB1600', 1.35)

    # Plot line:
    plt.plot(np.linspace(-1, 5, 100), [0] * 100, linewidth=4, color='#010101')

    if show_text:
        # Write text:
        y_offset = -0.33
        fontsize = 12

        for idx, c in enumerate('GENEGENIE'):
            plt.text((idx - 0.8) * 0.6, y_offset, c, color='#010101',
                     fontsize=fontsize)

    # Clean:
    plt.axis('off')

    # Save:
    plt.savefig(filename, transparent=False, bbox_inches='tight',
                pad_inches=0.1, dpi=dpi)


def plot(mu, variance, color, scale=1):
    '''Plot curve.'''
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 20 * variance, mu + 20 * variance, 100)
    plt.plot(x, scale * mlab.normpdf(x, mu, sigma), linewidth=4, color=color)


def main():
    '''main method.'''
    draw_logo()
    draw_logo(filename='logo_no_text.png', show_text=False)


if __name__ == '__main__':
    main()
