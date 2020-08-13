# 
#   Plasma
#   Copyright (c) 2020 Homedeck, LLC.
#

from imageio import imwrite
from numpy import linspace, tile, uint16
from PIL import Image
from pytest import fixture, mark
from torchvision.transforms import Compose, Normalize, Resize, ToPILImage, ToTensor

from plasma.sampling import color_sample_1d, color_sample_3d, cuberead, lutread

IMAGE_PATHS = [
    "test/media/filter/1.jpg",
    "test/media/filter/2.jpg",
    "test/media/filter/3.jpg",
    "test/media/filter/4.jpg",
]

def tensorread (path, size=1024):
    to_tensor = Compose([
        Resize(size),
        ToTensor(),
        Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image = Image.open(path)
    image = to_tensor(image).unsqueeze(dim=0)
    return image

def tensorwrite (name, *images):
    to_image = Compose([
        Normalize(mean=[-1., -1., -1.], std=[2., 2., 2.]),
        ToPILImage()
    ])
    images = [to_image(image.squeeze()) for image in images]
    if len(images) > 1:
        images[0].save(name, save_all=True, append_images=images[1:], duration=100, loop=0)
    else:
        images[0].save(name)

def create_identity_lut ():
    lut = linspace(0., 1., num=4096)
    lut = tile(lut, (16, 1))
    lut = (lut * 65535).astype(uint16)
    imwrite("identity.tif", lut)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_lut (image_path):
    image = tensorread(image_path)
    lut = lutread("test/media/lut/ramp.tif")
    result = color_sample_1d(image, lut)
    tensorwrite("lut.jpg", result)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_load_cube (image_path):
    image = tensorread(image_path)
    cube = cuberead("test/media/lut/identity.cube")
    result = color_sample_3d(image, cube)
    tensorwrite("cube.jpg", result)