from setuptools import setup, find_packages
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '2.0.1'

setup(name='collective.js.datatables',
      version=version,
      description="Plone Integration of jquery.dataTables plugin",
      long_description=read('README.rst') + read('docs', 'HISTORY.txt'),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        ],
      keywords='',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='jeanmichel.francois@makina-corpus.com',
      url='https://github.com/collective/collective.js.datatables',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require = dict(
          test=['plone.app.testing'],
      ),
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
