from distutils.core import setup


setup(
  name='pymobius',
  packages=['pymobius'],
  version='0.1.0',
  description='Mobius Python API Client',
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
