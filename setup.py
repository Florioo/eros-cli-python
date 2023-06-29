from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='eros-view',
    version='0.1.0',
    py_modules=['main'],
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'eros-view = main:eros_log',
        ],
    },
)