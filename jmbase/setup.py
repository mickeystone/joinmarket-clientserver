from setuptools import setup


setup(name='joinmarketbase',
      version='0.3.5',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/Joinmarket-Org/joinmarket-clientserver/jmbase',
      author='',
      author_email='',
      license='GPL',
      packages=['jmbase'],
      install_requires=['twisted==16.6.0', 'service-identity'],
      zip_safe=False)
