from setuptools import setup, find_packages

setup(
    name='openchart',
    version='0.1.0',
    description='A Python library to download intraday and EOD historical data from NSE India',
    author='Rajandran R',
    author_email='rajandran@marketcalls.in',
    url='https://github.com/marketcalls/openchart',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'brotli',
        'tenacity',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
