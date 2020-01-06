import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="resourceprovider",
    version="1.0.0",
    author="PyOneers",
    author_email="sutharpanks.opensource@gmail.com",
    description="Single Instance of Resource needed in Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyOneers/resource-provider",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
