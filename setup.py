from setuptools import setup


setup(
    name='censusbatchgeocoder',
    version='0.0.3',
    description='A simple Python wrapper for U.S. Census Geocoding Services API batch service',
    author='Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/python-censusbatchgeocoder/',
    license="MIT",
    packages=("censusbatchgeocoder",),
    test_suite="censusbatchgeocoder.tests",
    include_package_data=True,
    install_requires=(
        'requests',
        'six'
    ),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ),
)
