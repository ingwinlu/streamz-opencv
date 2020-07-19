import pathlib

from setuptools import find_packages, setup

README = pathlib.Path(__file__).parent / "README.md".read_text()

setup(
    name="streamz-opencv",
    description="Provide opencv sources to streamz",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ingwinlu/streamz-opencv",
    packages=find_packages(),
    author="Lukas Winkler",
    author_email="<derwinlu@gmail.com>",
    license="MIT",
    keywords="streamz opencv",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "opencv-python",
        "streamz"
    ],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
)
