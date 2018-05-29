import os.path
from sys import exit

from setuptools import setup
from setuptools.extension import Extension

import numpy as np

try:
    import cplex
except ImportError as err:
    msg = ('\nCPLEX is required to install qfit. '
           'Obtain it from the IBM website, or install it with conda:\n'
           '    conda install -c ibmdecisionoptimization cplex\n'
          )
    print(msg)
    exit()


def main():

    packages = ['qfit', 'qfit.structure', 'qfit.volume']
    package_data = {'qfit': [os.path.join('data', '*.npy'),]
    }

    ext_modules = [Extension("qfit._extensions",
                      [os.path.join("src", "_extensions.c")],
                      include_dirs=[np.get_include()],
                      ),
                   ]
    install_requires = [
        'numpy>=1.14',
        'scipy>=1.00',
        'cvxopt>=1.1.9',
    ]

    setup(name="qfit",
          version='3.0.0',
          author='Gydo C.P. van Zundert',
          author_email='gydo.vanzundert@schrodinger.com',
          packages=packages,
          package_data=package_data,
          ext_modules=ext_modules,
          install_requires=install_requires,
          entry_points={
              'console_scripts': [
                  'qfit_protein = qfit.qfit_protein:main',
                  'qfit_residue = qfit.qfit_residue:main',
                  'qfit_segment = qfit.qfit_segment:main',
                  ]
              },
         )


if __name__=='__main__':
    main()