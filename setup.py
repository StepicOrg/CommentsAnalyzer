import os

from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
version = __import__('comments_analyzer').get_version()

setup(
    name='comments-analyzer',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author='Zaycev Denis',
    description='A simple API which could process comments',
    long_description=README,
    install_requires=[
        'pyenchant==1.6.6',
        'numpy==1.9.1',
        'scipy==0.14.1',
        'scikit-learn==0.15.2'
    ],
)