from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.2'


setup(
    name='collective.controlpanel.edit_css',
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
    long_description=(
        open("README.rst").read() +
        open(os.path.join("docs", "HISTORY.txt")).read()),
    keywords='plone theme',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.controlpanel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    version=VERSION,
)
