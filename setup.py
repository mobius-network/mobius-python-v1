import os
from setuptools import setup


base_dir = os.path.dirname(__file__)


with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()


setup(
  name='pymobius',
  packages=['pymobius'],
  version='1.0.1',
  description='Mobius Python API Client',
  long_description=long_description,
  include_package_data=True,
  zip_safe=False,
  author='mobius-network',
  author_email='support@mobius.network',
  url='https://github.com/mobius-network/mobius-python',
  license='MIT',
  keywords=['mobius', 'api'],
  install_requires=[
      'requests',
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  python_requires='>=3.2',
)
