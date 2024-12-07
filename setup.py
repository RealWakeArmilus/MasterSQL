from setuptools import setup, find_packages

# def readme():
#   with open('README.rst', 'r') as file_readme:
#     return file_readme.read()

setup(
  name='MasterSQL',
  version='1.0.0',
  author='RealWakeArmilus',
  author_email='jordanman1300@gmail.com',
  description='Modern SQL framework and Object Relational Mapper',
  long_description='Modern SQL framework and Object Relational Mapper',
  long_description_content_type='text/markdown',
  url='https://github.com/RealWakeArmilus/MasterSQL',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='SQL SQLite Python ORM Framework',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)