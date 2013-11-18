from setuptools import setup, find_packages

setup(
    name='cmsplugin-simplenews',
    version='1.0.0',
    description='Simple news plugin for Django-CMS',
    long_description='Simple news plugin for Django-CMS',
    author='Boris Savelev',
    author_email='boris.savelev@gmail.com',
    url='https://github.com/bsavelev/cmsplugin_simplenews',
    packages=find_packages(),
    keywords='django cms django-cms news',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
