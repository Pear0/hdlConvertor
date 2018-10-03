from skbuild import setup
from os import path

setup(
cmake_args= [
'-DANTLR_JAR_LOCATION='+path.abspath('antlr4/antlr-4.7-complete.jar')
],
    name='hdlConvertor',
    version='1.1',
    description='Vhdl and verilog parser written in c++, this module is primary used for hw_toolkit library for hdl manipulation',
    url='https://github.com/Nic30/hdlConvertor',
    author='Michal Orsak',
    author_email='michal.o.socials@gmail.com',
    keywords=['vhdl', 'verilog', 'system verilog', 'parser', 'hdl'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3',
    ],
    packages=['hdlConvertor']
)
