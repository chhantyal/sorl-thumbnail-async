from setuptools import setup, find_packages

version = '0.6.0'

setup(
    name='sorl-thumbnail-async',
    version=version,
    description='Asynchronous thumbnailing app in django with remote storages like S3',
    author='Nar Kumar Chhantyal',
    author_email='nkchhantyal@gmail.com',
    url='https://github.com/chhantyal/sorl-thumbnail-async',
    packages=find_packages(),
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Environment :: Web Environment',
        ],
    zip_safe=False,
    include_package_data=True,
)