from setuptools import setup, find_packages
import sys, os

version = '0.1'
long_description = ""

setup(name='netflow-indexer',
      version=version,
      description="Index netflow",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='netflow search index',
      author='Justin Azoff',
      author_email='JAzoff@uamail.albany.edu',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points = {
        'console_scripts': [
            'netflow-index-nfdump     = netflowindexer.indexer.nfdump:main',
            'netflow-index-flowtools  = netflowindexer.indexer.flowtools:main',
        ]
      }
  )
