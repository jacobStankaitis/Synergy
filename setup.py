from setuptools import setup, find_packages

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

with open('README.md') as file:
    README = file.read()

setup(
    name='Synergy',
    version=VERSION,
    packages=find_packages(exclude=['venv']),
    description='Domain for electricity providers and users allowing to get fair-priced deals.',
    long_description=README,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[

        # --------------------------------------
        # Internal dependencies.
        # --------------------------------------

        # --------------------------------------
        # External dependencies.
        # --------------------------------------

 
    ]
)
