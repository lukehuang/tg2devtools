# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='tg.devtools',
    version="1.9.7",
    description="",
    long_description="""""",
    classifiers=[],
    keywords='turbogears',
    author="TurboGears Team 2008",
    author_email="",
    url="www.turbogears.org",
    license="MIT",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'TurboGears2', 'sqlalchemy-migrate >= 0.4.4',
        'tw.forms', 'DBSprockets',
    ],
    entry_points='''
        [paste.global_paster_command]
        quickstart = devtools.commands.quickstart:QuickstartCommand
        [paste.paster_command]
        crud = devtools.commands.crud:CrudCommand
        migrate = devtools.commands.migration:MigrateCommand
        [turbogears2.command]
        quickstart = devtools.commands.quickstart:QuickstartCommand
        crud = devtools.commands.crud:CrudCommand
        migrate = devtools.commands.migration:MigrateCommand
        [paste.paster_create_template]
        turbogears2=devtools.pastetemplate:TurboGearsTemplate
        [turbogears2.template]
        turbogears2=devtools.pastetemplate:TurboGearsTemplate
    ''',
)