from setuptools import setup
from codecs import open

setup(
    name='lexpp',
    version='1.0.0',
    description='A lexical pre-processing module for Japanese text',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='earlsuke',
    author_email='ryosuke.mitani@gmail.com',
    url='https://github.com/earlsuke',
    license="Apache-2.0",
    packages=['lexpp', 'lexpp.res'],
    include_package_data=True,
    package_data={'lexpp':['res/*.dict']},
)

