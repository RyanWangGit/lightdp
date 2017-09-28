from setuptools import setup, find_packages
from codecs import open
from os import path
import lightdp

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LightDP',
    version=lightdp.__version__,
    description=lightdp.__doc__.strip(),
    long_description=long_description,
    url='',
    author='Danfeng Zhang/Daniel Kifer/Yuin Wang/Ding Ding',
    author_email='{dkifer,zhang,yxwang}@psu.edu,dingsquared@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Programming Language :: Differential Privacy',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='Programming Language, Differential Privacy',
    packages=find_packages(exclude=['tests']),
    install_requires=['ply'],
    extras_require={
        'dev': [],
        'test': ['pytest', 'coverage'],
    },
    entry_points={
        'console_scripts': [
            'lightdp=lightdp.__main__:main',
        ],
    },
)
