[![Travis-CI Build Status](https://travis-ci.com/s-ball/bin_tree.svg?branch=master)](https://travis-ci.com/s-ball/pyimgren)
<!--
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/salqj2q1h8mid74t/branch/master?svg=true)](https://ci.appveyor.com/project/s-ball/pyimgren/branch/master)
[![Documentation Status](https://readthedocs.org/projects/bin_tree/badge/?version=latest)](https://pyimgren.readthedocs.io/en/latest/?badge=latest)
-->
# bin_tree
A python module that provides mutable mappings and sets implemented with binary trees.

## Current status

This package is distributed in PyPI starting with version 0.2.0. It is a full
implementation of MutableSet and MutableMapping for both AVL and Red-Black
trees. Test coverage is > 90%, but it should be considered at beta quality
because it still lacks real world application testing.

Starting with version 0.3.0, it is tested on [Travis-CI](https://travis-ci.com/github/s-ball/bin_tree),
for Python versions >= 3.5 and <=3.9

Its full source is available from [GitHUB](https://github.com/s-ball/pyimgren).

## Goals

This module intends to be used as a normal mapping. It provides various
implementations, a non balancing one, an AVL one, and a red-black
one.

Portability is very important here:
* few dependencies: a Python 3 (tested for version >= 3.5)
* no additional module requirements

## Usage:
To be done

## Installing

### End user installation

With pip: `pip install bin_tree`.

### Developer installation

If you want to contribute or integrate `bin_tree` in your own code, you should get a copy of the full tree from [GitHUB](https://github.com/s-ball/pyimgren):

```
git clone https://github.com/s-ball/bin_tree [your_working_copy_folder]
```

#### Running the tests

As the project only uses unittest, you can simply run tests from the main folder with:

```
python -m unittest discover
```

## Contributing

As this project is developed on my free time, I cannot guarantee very fast feedbacks. Anyway, I shall be glad to receive issues or pull requests on GitHUB. 

## Versioning

This project uses a standard Major.Minor.Patch versioning pattern. Inside a major version, public API stability is expected (at least after 1.0.0 version will be published).

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details
