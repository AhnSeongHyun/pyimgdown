# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

from setuptools import setup, find_packages

version = '0.2'

setup(name='pyimgdown',

      version=version,
      description="A module of downloading image from URL and resizing.",
      long_description=open("pip_desc.txt").read() + "\n",
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2.7',
      'Topic :: Utilities',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='image download http url',
      author='SeongHyun.Ahn',
      author_email='sh84.ahn@gmail.com',
      url='https://bitbucket.org/AhnSeongHyun/pyimgdown',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'wand',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,

      )