from setuptools import setup, find_packages

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
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-flake8",
            "pytest-mypy",
            "pytest-tornado",
            "pytest-xdist",
            "flake8",
            "flake8-import-order",
            "mypy"
        ]
    }
)
