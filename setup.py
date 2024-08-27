# set up historical-price-stat
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as _f:
    requirements = [line for line in _f.read().split('\n')]

setup(
    name='historical-price-stat',
    description='find average, min, max of historical share prices, with price source from csv file',
    packages=find_packages(),
    author='Matana P',
    author_email="matana.po@duke.edu",
    entry_points="""
    [console_scripts]
    pricestat=pricestat.main:main
    """,
    install_requires=requirements,
    version='0.0.1',
    url='https://github.com/beungz/historical-price-stat',
)
