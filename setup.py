import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Rafflesia",  ## 소문자 영단어
    version="0.0.1",  ##
    author="QU4R7Z",  ## ex) Sunkyeong Lee
    author_email="shio7113@gmail.com",  ##
    description="Rafflesia Framework",  ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QU4R7Z/Rafflesia",  ##
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
