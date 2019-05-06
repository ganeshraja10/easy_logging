import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-logging-ganeshraja10",
    version="0.0.1",
    author="Ganesh",
    author_email="ganeshraja1010@gmail.com",
    description="A quick Log Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ganeshraja10/easy_logging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
    ],
)