from setuptools import setup, find_packages
from pkg_resources import parse_version, get_distribution, ResolutionError
import os.path
import re

from io import open

NAME = "bin_tree"

# Base version (removes any pre, post, a, b or rc element)
BASE = "0.0.0"
try:
    BASE = get_distribution(NAME).parsed_version.base_version
except ResolutionError:
    # Try to read from version.py file
    try:
        import ast

        rx = re.compile(r'.*version.*=\s*(.*)')
        with open(os.path.join(NAME, "version.py")) as fd:
            for line in fd:
                m = rx.match(line)
                if m:
                    BASE = parse_version(ast.literal_eval(m.group(1))).base_version
                    break
    except OSError:
        pass  # give up here and stick to 0.0.0

# In long description, replace "master" in the build status badges
#  with the current version we are building
with open("README.md") as fd:
    long_description = next(fd).replace("master", BASE)
    long_description += "".join(fd)

setup(
    name=NAME,
    description="Rename image files according to exif tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["setuptools_scm"],
    use_scm_version={"write_to": os.path.join(NAME, 'version.py')},
    author="SBA",
    author_email="s-ball@laposte.net",
    url="https://github.com/s-ball/bin_tree",
    license="MIT License",
    project_urls={
        "Changelog":
            "https://github.com/s-ball/bin_tree/blob/master/CHANGES.txt"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3",
)
