from setuptools import setup, find_packages

setup(
    name='CLI_AddressBook',
    version='v0.01',
    description='The Personal Assistant module is a tool'
                'designed to facilitate the organization'
                'of contacts and maintain personal notes.',
    author='Aleksandra, Mikolaj, Pawel, Olek',
    author_email='niemozliwyj.bajer@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['enter_cli_addressbook = Modules.commands:main']},
)
