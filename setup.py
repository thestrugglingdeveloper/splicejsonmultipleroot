import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="splicejsonmultipleroots-thestrugglingdeveloper",
    version="0.1.1",
    author="TheStrugglingDeveloper",
    author_email="github@thestrugglingdeveloper.com",
    description="A small package to extract an array of json root elements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thestrugglingdeveloper/splicejsonmultipleroots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)