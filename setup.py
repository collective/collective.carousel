from setuptools import setup, find_packages
import os

version = '1.0'

tests_require = ['collective.testcaselayer']

setup(name='collective.carousel',
      version=version,
      description="Add-on for having Collections' results presented as a nice carousel",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope collection carousel',
      author='Jarn [Denys Mishunov]',
      author_email='info@jarn.com',
      url='http://svn.plone.org/svn/collective/collective.carousel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
