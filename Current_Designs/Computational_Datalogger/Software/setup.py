from distutils.core import setup, Extension
setup(name = 'Logger', version = '1.0', ext_modules = [Extension('Logger', ['logger.c'])])

