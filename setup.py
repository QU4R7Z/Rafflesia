import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setuptools.setup(
    name="Rafflesia",
    version="0.0.9.8",
    author="QU4R7Z",
    author_email="shio7113@gmail.com",
    description="Rafflesia Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QU4R7Z/Rafflesia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.6',
    package_data={'Rafflesia': ['Resources/*.ico']},
)
