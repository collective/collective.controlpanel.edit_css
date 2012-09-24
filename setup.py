from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.4.0'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.2",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description='Use a text area in the Plone control panel to\
        edit CSS and Javascript.',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    keywords='plone theme',
    license='ZPL',
    long_description=(
        open("README.rst").read() +
        open(os.path.join("docs", "HISTORY.txt")).read()),
    name='collective.controlpanel.edit_css',
    namespace_packages=[
        'collective',
        'collective.controlpanel',
    ],
    packages=find_packages(),
    url='http://collective.github.com/collective.controlpanel.edit_css',
    version=VERSION,
    zip_safe=False,
)
