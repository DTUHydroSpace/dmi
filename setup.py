import os
from setuptools import (
    setup,
    find_packages,
)
setup(
    name='dmi',
    version='0.2.0',
    py_modules=['dmi'],
    url = 'https://github.com/chris3759/dmi',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'dmi = dmi.cli:main',
        ],
    },
 
)