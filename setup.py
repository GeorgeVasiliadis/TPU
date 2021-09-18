from setuptools import setup

setup(
    name="tpu",
    version="0.1.0",
    description="A set of awesome scripts that aim to facilitate musicians with programming background ;)",
    long_description=open("README.md", 'r').read(),
    long_description_content_type="text/markdown",
    author="George Vasiliadis",
    author_email="geor.vasiliadis@gmail.com",
    url="https://github.com/GeorgeVasiliadis/TPU",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities"
    ],
    packages=["tpu"],
    license="LICENSE.txt"
)
