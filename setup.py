from os.path import dirname, join

import pm4pymdl
from setuptools import setup


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=pm4pymdl.__name__,
    version=pm4pymdl.__version__,
    description=pm4pymdl.__doc__.strip(),
    long_description=read_file('README.md'),
    author=pm4pymdl.__author__,
    author_email=pm4pymdl.__author_email__,
    py_modules=[pm4pymdl.__name__],
    include_package_data=True,
    packages=['ocel', 'ocel.exporter', 'ocel.importer', 'ocel.validation'],
    url='http://www.pm4py.org',
    license='GPL-3.0',
    install_requires=[
        "jsonschema",
        "lxml"
    ]
)
