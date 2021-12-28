from setuptools import find_packages, setup

setup(
    name='github_issues_to_project',
    packages=find_packages(include=['github_issues_to_project']),
    version='0.1.0',
    description='Github: Add Issues To Project Script',
    author='Kate Donaldson',
    license='MIT',
    install_requires=['requests==2.26.0'],
    setup_requires=['pytest-runner==5.3.1'],
    tests_require=['pytest==6.2.5'],
    test_suite='tests',
)