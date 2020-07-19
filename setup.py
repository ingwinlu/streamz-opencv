from setuptools import find_packages, setup

setup(
    name="streamz-opencv",
    description="Provide opencv sources to streamz",
    version="0.1.0",
    packages=find_packages(),
    author="Lukas Winkler",
    author_email="<derwinlu@gmail.com>",
    keywords="streamz opencv",
    install_requires=[
        "opencv-python",
        "streamz"
    ]
)
