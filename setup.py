import os
from setuptools import setup, find_packages

version = '0.1.dev0'

long_description = (
    open('README.txt').read()
    + '\n' +
    open(os.path.join("docs", "HISTORY.txt")).read())

tests_require = [
    'Cheetah',
    'templer.core',
    'unittest2',
]

setup(name='templer.affinitic',
      version=version,
      description="Templer templates for Affinitic",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Code Generators",
      ],
      keywords='zope buildout plone templer affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='https://github.com/affinitic/templer.affinitic',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
