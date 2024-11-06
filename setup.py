from setuptools import setup, find_packages

setup(
    name='monte_carlo',
    version='0.3',
    description='A montecarlo simulator written for DS5100',
    url='https://github.com/pfost-bit/monte_carlo',
    author='Pat Foster',
    author_email='ezq9qu@virginia.edu',
    license='MIT',
    packages=["monte_carlo"],
    install_requires=[
    "numpy",
    "pandas"
    ]
)
