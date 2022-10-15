# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Plotting solutions of DEs
# Given
# \begin{equation*}%\label{eq:DGL1}
#     \dot{y}(t)+p(t)y(t)=q(t)
# \end{equation*}
# 1. What is the solution for y(t) when $q(t)=1$, $p(t)=2$ and $y_0=0$? Sketch the course of the solution for $t\in [0,4]$. Also sketch the asymptotes for $t\rightarrow 0$ and $t\rightarrow\infty$.
# 1. What is the solution for y(t) when $q(t)=0$, $p(t)=t$ and $y_0=1$?  Sketch the course of the solution for $t\in [0,4]$. Also sketch the asymptotes for $t\rightarrow 0$ and $t\rightarrow\infty$.

import numpy as np
import matplotlib.pyplot as plt


def y(x):
    return 0.5*(1-np.exp(-2*x))


# %matplotlib notebook
x = np.linspace(0,4)
fig, (ax1,ax2) = plt.subplots(1,2)
#
ax1.set_aspect(8)
ax1.set_ylim([0, 0.55])
ax1.set_title("Problem 1.")
ax1.plot(x,y(x))
ax1.plot(x,x,dashes=[4,2],label=r't$\rightarrow\infty$')
ax1.plot(x,0.5*np.ones(x.shape),dashes=[4,2],label=r't$\rightarrow 0$')
ax1.legend()
ax1.set_xlabel('t')
ax1.set_ylabel('y(t)')
ax2.set_aspect(4)
ax2.set_title("Problem 2.")
ax2.plot(x,np.exp(-x**2))
ax2.plot(x,np.ones(x.shape),dashes=[4,2],label=r't$\rightarrow 0$')
ax2.plot(x,np.zeros(x.shape),dashes=[4,2],label=r't$\rightarrow\infty$')
ax2.legend()
ax2.plot(x,np.exp(-x**2))
ax2.set_xlabel('t')
ax2.set_ylabel('y(t)')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
fig.savefig("A1Plots.png")


