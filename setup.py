from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.2'


setup(
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.2",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description='Use a text area in the Plone control panel to\
        edit CSS and Javascript.',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    license='ZPL',
    long_description=(
        open("README.rst").read() +
        open(os.path.join("docs", "HISTORY.txt")).read()),
    keywords='plone theme',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='http://collective.github.com/collective.controlpanel.edit_css',
    name='collective.controlpanel.edit_css',
    namespace_packages=[
        'collective',
        'collective.controlpanel',
    ],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    version=VERSION,
    zip_safe=False,
)
