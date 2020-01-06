import os

from setuptools import setup, find_packages
from sphinx_collapse_admonitions import __version__

with open('./README.md', 'r') as ff:
    readme_text = ff.read()

setup(
    name='sphinx-collapse-admonitions',
    version=__version__,
    description="Add a copy button to each of your code cells.",
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author='Chris Holdgraf',
    author_email='choldgraf@berkeley.edu',
    url="https://github.com/choldgraf/sphinx-collapse-admonitions",
    license='MIT License',
    packages=find_packages(),
    package_data={'sphinx_collapse_admonitions': [
        '_static/collapse_admonitions.css',
        '_static/collapse_admonitions.js'
        ]
    },
    install_requires=["flit", "setuptools", "wheel", "sphinx"],
    classifiers=["License :: OSI Approved :: MIT License"]
)
