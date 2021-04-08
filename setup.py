import os
from setuptools import setup, find_packages

version = '0.0.1'

setup(name='mytardis_openid_login',
      version=version,
      description="TruDat@UWA specific login page for OpenID authentications",
      long_description="""\
MyTardis app to override default login template and use The University of Western Australia specific OpenID authentication methods.\
""",
      classifiers=[],
      keywords='TruDat UWA openID',
      author='Manish Kumar',
      author_email='manish.kumar@monash.edu',
      url='',
      license='',
      packages=find_packages(),
      include_package_data=True
      )
