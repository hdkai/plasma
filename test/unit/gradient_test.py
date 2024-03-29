# 
#   Plasma
#   Copyright (c) 2021 Yusuf Olokoba.
#

from pytest import fixture, mark
from torch import linspace, zeros
from .common import tensorwrite

from torchplasma.gradients import radial_gradient, top_bottom_gradient, bottom_top_gradient, left_right_gradient, right_left_gradient

def test_radial_gradient ():
    input = zeros(1, 1, 720, 1280)
    weights = linspace(0., 2., 20).unsqueeze(dim=1)
    masks = radial_gradient(input, weights)
    tensorwrite("radial.gif", *masks.split(1, dim=0))

def test_top_bottom_gradient ():
    input = zeros(1, 1, 720, 1280)
    weights = linspace(0., 1., 20).unsqueeze(dim=1)
    masks = top_bottom_gradient(input, weights)
    tensorwrite("top_bottom.gif", *masks.split(1, dim=0))

def test_bottom_top_gradient ():
    input = zeros(1, 1, 720, 1280)
    weights = linspace(0., 1., 20).unsqueeze(dim=1)
    masks = bottom_top_gradient(input, weights)
    tensorwrite("bottom_top.gif", *masks.split(1, dim=0))

def test_left_right_gradient ():
    input = zeros(1, 1, 720, 1280)
    weights = linspace(0., 1., 20).unsqueeze(dim=1)
    masks = left_right_gradient(input, weights)
    tensorwrite("left_right.gif", *masks.split(1, dim=0))

def test_right_left_gradient ():
    input = zeros(1, 1, 720, 1280)
    weights = linspace(0., 1., 20).unsqueeze(dim=1)
    masks = right_left_gradient(input, weights)
    tensorwrite("right_left.gif", *masks.split(1, dim=0))

def test_vignette_gradient ():
    input = zeros(1, 1, 720, 1280)
    mask = 1. - radial_gradient(input, 2.5)
    mask = 2. * mask - 1.
    tensorwrite("vignette.jpg", mask)