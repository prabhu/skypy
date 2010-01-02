import sys
import skypy
from setuptools import setup, find_packages

setup(
    name="skypy",
    version=skypy.__VERSION__,
    packages=find_packages(exclude=['tests',]),
    install_requires = [],
    
    description="Python api for accessing EPG data from SKY TV (UK)",
    author="Prabhu Subramanian",
    author_email="prabhu.subramanian@gmail.com",
    maintainer="Prabhu Subramanian",
    maintainer_email="prabhu.subramanian@gmail.com",
    license="MIT",
    keywords="sky tv api",
    url="http://github.com/prabhu/skypy",
)
