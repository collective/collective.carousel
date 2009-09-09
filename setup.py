from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.carousel',
      version=version,
      description="Small add-on for having Collections' results presented as a nice carousel",
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
