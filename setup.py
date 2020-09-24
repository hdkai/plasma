# 
#   Plasma
#   Copyright (c) 2020 Homedeck, LLC.
#

from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="plasma",
    version="0.0.14",
    author="Homedeck, LLC",
    author_email="info@homedeck.io",
    description="The image editing toolkit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
	python_requires=">=3.6",
    install_requires=[
        "exifread",
        "lensfunpy",
        "imageio",
        "opencv-python",
        "piexif",
        "pillow",
        "python-dateutil",
        "rawpy",
        "scikit-learn",
        "torch",
        "torchvision"
    ],
    url="https://github.com/homedeck/Plasma",
    packages=find_packages(exclude=["examples", "playground", "test", "train"]),
    package_data={
        "plasma.io": ["data/*.tif"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries",
    ],
)