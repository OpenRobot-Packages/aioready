from setuptools import setup

from setuptools import setup
import re

with open("aioready/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

#with open("README.md", "r") as f:
    #long_desc = f.read()

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

#extras_require = ["asyncmg"]

setup(
    name="aioready",
    install_requires=install_requires,
	#extras_require={"rust": extras_require},
    packages=["aioready"],
    version=version,
    license="MIT",
    url="https://github.com/OpenRobot-Packages/aioready",
    #long_description=long_desc,
    #long_description_content_type="text/markdown",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A simple ODM/ORM written in Python for `asyncio` and supports a couple of databases.",  # Give a short description about your library
    author="Alex Hutz",
    author_email="frostiiweeb@gmail.com", 
    keywords=["orm", "odm"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10"
    ],
)
