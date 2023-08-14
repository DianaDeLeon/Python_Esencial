from setuptools import setup

setup(
    name = 'cianv',
    version='0.1',
    py_modules=['cianv'],
    install_requires= [
        'Click',
    ],
    entry_points = ''' 
        [console_scripts]
        cianv = cianv:cli
    '''   
)