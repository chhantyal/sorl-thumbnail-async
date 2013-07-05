import thumbnail
from setuptools import setup, find_packages
from setuptools.command.test import test


class TestCommand(test):
    def run(self):
        from tests.runtests import runtests
        runtests()


setup(
    name='sorl-thumbnail-async',
    version=0.1,
    description='Asynchronous thumbnailing app in django with remote storages like S3',
    long_description=open('README.md').read(),
    author='Nar Kumar Chhantyal',
    author_email='neokya@gmail.com',
    license='BSD',
    url='https://github.com/neokya/sorl-thumbnail-async',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 01 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Framework :: Django',
    ],
    cmdclass={"test": TestCommand},
)

