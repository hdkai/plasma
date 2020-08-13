# 
#   Plasma
#   Copyright (c) 2020 Homedeck, LLC.
#

from numpy import linspace
from PIL import Image
from pytest import fixture, mark
from torchvision.transforms import Compose, Normalize, Resize, ToPILImage, ToTensor

from plasma.linear import contrast, clarity, exposure, highlights, saturation, shadows, sharpen, temperature, tint

IMAGE_PATHS = [
    "test/media/1.jpg",
    "test/media/2.jpg",
    "test/media/3.jpg",
    "test/media/4.jpg",
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

@mark.parametrize("image_path", IMAGE_PATHS)
def test_clarity (image_path):
    image = tensorread(image_path)
    results = [clarity(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("clarity.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_contrast (image_path):
    image = tensorread(image_path)
    results = [contrast(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("contrast.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_exposure (image_path):
    image = tensorread(image_path)
    results = [exposure(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("exposure.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_highlights (image_path):
    image = tensorread(image_path)
    results = [highlights(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("highlights.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_saturation (image_path):
    image = tensorread(image_path)
    results = [saturation(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("saturation.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_shadows (image_path):
    image = tensorread(image_path)
    results = [shadows(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("shadows.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_sharpen (image_path):
    image = tensorread(image_path)
    results = [sharpen(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("sharpen.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_temsperature (image_path):
    image = tensorread(image_path)
    results = [temperature(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("temperature.gif", *results)

@mark.parametrize("image_path", IMAGE_PATHS)
def test_tint (image_path):
    image = tensorread(image_path)
    results = [tint(image, weight) for weight in linspace(-1., 1., 20)]
    tensorwrite("tint.gif", *results)