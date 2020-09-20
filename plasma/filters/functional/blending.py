# 
#   Plasma
#   Copyright (c) 2020 Homedeck, LLC.
#

from torch import where, Tensor

def blend_overlay (base: Tensor, overlay: Tensor) -> Tensor:
    """

    """
    # Rescale
    base = (base + 1.) / 2.
    overlay = (overlay + 1.) / 2.
    # Compute sub blending modes
    multiply = 2. * base * overlay
    screen = 1. - 2. * (1. - base) * (1. - overlay)
    # Blend and rescale
    result = where(base < 0.5, multiply, screen)
    result = 2. * result - 1.
    return result

def blend_soft_light (base: Tensor, overlay: Tensor) -> Tensor: # Use Photoshop blending
    """

    """
    # Rescale
    base = (base + 1.) / 2.
    overlay =  (overlay + 1.) / 2.
    # Blend
    result = (1. - 2. * overlay) * base.pow(2.) + 2. * base * overlay
    ps_correct = 2 * base * (1. - overlay) + base.sqrt() * (2. * overlay - 1.)
    result = where(overlay < 0.5, result, ps_correct)
    # Rescale
    result = 2. * result - 1.
    return result