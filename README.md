# NettyFinder :rocket:

This is a python verison of the original [netty-finder](https://github.com/BolajiAyodeji/netty-finder) that was written in JavaScript

# Installation

## GitHub

```bash
$ git clone https://github.com/CITGuru/netty-finder-python.git
$ cd netty-finder-python
$ python setup.py install
```

## PyPI

```bash
$ pip install netty_finder
```

# Usage

```python

from netty_finder import Network

detector = Network("08182315466")
network_name = detector.get_network_name()
print(network_name)

# >>> 9mobile

```

# About Author

This was originally built by [Bolaji Ayodeji](https://github.com/BolajiAyodeji) so all rights goes to him, I only interpreted the javascript code to python

# Contribution
 
For now, I dont accept contributions except its from the javascript [netty_finder](https://github.com/BolajiAyodeji/netty-finder), so I suggest you contribute there. Any changes from there will be added to the python version


