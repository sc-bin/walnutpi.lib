from setuptools import setup, Extension, find_packages

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

with open("version", "r") as file:
    version_str = file.read().strip()

setup(
    name="walnutpi",
    version=version_str,
    author="sc-bin",
    author_email="3335447573@qq.com",
    description="A module to import all walnutpi libs",
    platforms=["manylinux"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/sc-bin/",
    packages=find_packages(),
)
