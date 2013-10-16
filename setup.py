from setuptools import setup, find_packages

version = '0.5.2'

setup(
    name='sorl-thumbnail-async',
    version=version,
    description='Asynchronous thumbnailing app in django with remote storages like S3',
    author='Nar Kumar Chhantyal',
    author_email='nkchhantyal@gmail.com',
    url='https://github.com/chhantyal/sorl-thumbnail-async',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)