from setuptools import setup

setup(
    name='lookup',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'lookup = lookup.lookup:main',
        ]
    }
    
)