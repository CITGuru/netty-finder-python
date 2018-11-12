from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))

# long description from the README file

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='netty_finder',
    version='1.0.0',
    description=(
          'This is a python verison of the original netty-finder that was written in JavaScript,'
    ),
    long_description=long_description,
    license='MIT',
    url='https://github.com/CITGuru/netty-finder-python/',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: '
        'Libraries :: Application Frameworks',
    ],
    keywords='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='Oyetoke Toby',
    download_url='https://github.com/CITGuru/netty-finder-python/archive/1.0.0.tar.gz',
    author_email='oyetoketoby80@gmail.com',
)
