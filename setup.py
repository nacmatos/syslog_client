
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="syslog_client",
    version="0.0.1",
    author="Christian Stigen Larsen",
    description="A UDP syslog client in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://csl.name/post/python-syslog-client/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: PUBLIC DOMAIN",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
