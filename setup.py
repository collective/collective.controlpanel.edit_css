from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.controlpanel.edit_css',
      version=version,
      description="Use a text area in the Plone control panel to save *just* CSS (no dtml because now-a-days I just find it confusing and unnecessary) to a page template called ploneCustom.css (optionallly  allow filename to be specified e.g. my_theme.css) in portal_skins/custom, for quick and dirty UI prototyping.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='http://svn.plone.org/svn/collective/collective.controlpanel.edit_css/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.controlpanel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
