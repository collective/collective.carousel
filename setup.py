from setuptools import setup, find_packages

version = '1.6.2'

setup(
    name='collective.carousel',
    version=version,
    description="Add-on for having Collections' results presented as a nice carousel",
    long_description=open("README.rst").read() + "\n" + open("CHANGES.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone zope collection carousel',
    author='Jarn [Denys Mishunov]',
    author_email='info@jarn.com',
    url='https://github.com/collective/collective.carousel',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'archetypes.schemaextender',
        'plone.app.jquerytools',
        'plone.portlet.collection',
    ],
    extras_require={'test': [
        'Products.PloneTestCase',
        'collective.testcaselayer'
    ]},
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
)
