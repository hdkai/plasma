# 
#   Plasma
#   Copyright (c) 2020 Homedeck, LLC.
#

from PIL import Image
from torch import float32, tensor, Tensor
from torchvision.transforms import Compose, Grayscale, Normalize, Resize, ToTensor

def lutread (path: str) -> Tensor:
    """
    Load a 1D LUT from file.

    Parameters:
        path (str): Path to LUT file.

    Returns:
        Tensor: 1D LUT with shape (L,) in [-1., 1.].
    """
    image = Image.open(path)
    to_tensor = Compose([
        Grayscale(),
        Resize((1, image.width)),
        ToTensor(),
        Normalize(mean=[0.5], std=[0.5])
    ])
    lut = to_tensor(image)
    lut = lut.squeeze()
    return lut

def cuberead (path: str) -> Tensor:
    """
    Load a 3D LUT from file.

    Parameters:
        path (str): Path to CUBE file.

    Returns:
        Tensor: 3D LUT with shape (L,L,L,3) in [-1., 1.].
    """
    # Read coeffients
    with open(path) as file:
        domain_min = tensor([ 0., 0., 0. ], dtype=float32)
        domain_max = tensor([ 1., 1., 1. ], dtype=float32)
        rows = []
        for line in file:
            tokens = line.split()
            if not tokens:
                continue
            elif tokens[0][0] == "#":
                continue
            elif tokens[0] == "TITLE":
                continue
            elif tokens[0] == "LUT_3D_SIZE":
                size = int(tokens[1])
            elif tokens[0] == "DOMAIN_MIN":
                domain_min = tensor([float(x) for x in tokens[1:]], dtype=float32)
            elif tokens[0] == "DOMAIN_MAX":
                domain_max = tensor([float(x) for x in tokens[1:]], dtype=float32)
            else:
                rows.append([float(x) for x in tokens])
    # Create cube
    cube = tensor(rows, dtype=float32)
    cube = cube.view(size, size, size, 3)
    # Rescale
    cube = (cube - domain_min) / (domain_max - domain_min)
    cube = 2 * cube - 1.
    return cube
