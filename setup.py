from setuptools import setup, find_packages

setup(
    name='openchart',
    version='0.1.0',
    description='A library to download historical data from NSE India',
    author='Rajandran R',
    author_email='rajandran@marketcalls.in',
    url='https://github.com/marketcalls/openchart',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)