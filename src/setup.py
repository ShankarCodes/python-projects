from setuptools import setup
setup(name='shankar-tools',
      version='0.2',
      description='sct package for crypto tools',
      url='https://github.com/ShankarCodes/sct',
      author='shankar',
      author_email='mailstoshankar@gmail.com',
      license='MIT',
      packages=['sct','sutil'],
      zip_safe=True,
      install_requires=[
          'cryptography',
      ]
      )
    
