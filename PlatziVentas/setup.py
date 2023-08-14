from setuptools import setup

setup(
    name='pv_ventas',
    version='0.1',
    py_modules=['pv_ventas'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv_ventas=pv_ventas:cli
    ''',

)