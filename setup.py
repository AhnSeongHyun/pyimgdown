# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

from setuptools import setup, find_packages

version = '0.5.4'

setup(name='pyimgdown',
      version=version,
      description="A module of downloading image from URL and resizing.",
      long_description=open("pip_desc.txt").read() + "\n",
      classifiers=[
      'License :: OSI Approved :: MIT License',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
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