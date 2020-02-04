from setuptools import setup, find_packages

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

install_requires = [
    'pyaml'
]

dependency_links = [
]

tests_require = [
]

setup(
    name='common',
    description="Common tools for BB projects",
    license="No License",
    version=__versionstr__,
    author="Alex Crown",
    packages=["common",],
    install_requires=install_requires,
    dependency_links=dependency_links,
    python_requires="~=3.5",
    tests_require=tests_require,
    extras_require={'develop': tests_require},
)