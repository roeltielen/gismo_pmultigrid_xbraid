from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os
import sys
# import numpy

braid_dir = "../../braid"

##
# This setup.py file has been tested on High Sierra with Homebrew, and Ubuntu LTS.
# This example requires Python 3 and the installation of Cython.
#
# To Install,
#
# 1) Make sure that braid_dir (defined above) points to the location of "braid"
#    This is used by library_dirs and include_dirs below
#
# 2) Type (using whatever install location you want)
#
#    $ python3 drive_adv_diff_1D-setup.py install --prefix=$HOME/.local
#
#    Note that you may have to tweak the compilers and flags.
#    Some comments on this are below.
#
# To Run, 
#
# 1) Make sure that the install directory and the location of MPI4PY 
#    is in your PYTHONPATH, e.g.,
# 
#     export PYTHONPATH="$HOME/.local/lib/python3.6"
#     or perhaps, 
#     export PYTHONPATH="$HOME/.local/lib/python3.7/site-packages"
#
# 2) Type 
#    python3
#    >>> import drive_adv_diff_1D
#    >>> core, app = drive_adv_diff_1D.InitCoreApp()
#    >>> drive_adv_diff_1D.run_Braid(core, app)
#
#    Output:
#
#    Braid: Begin simulation, 60 time steps
#    Braid: || r_0 || = 2.449744e+01, conv factor = 1.00e+00, wall time = 3.41e-02
#    Braid: || r_1 || = 1.202467e-02, conv factor = 4.91e-04, wall time = 5.34e-02
#    Braid: || r_2 || = 4.237590e-04, conv factor = 3.52e-02, wall time = 7.28e-02
#    Braid: || r_3 || = 1.693387e-05, conv factor = 4.00e-02, wall time = 9.18e-02
#    ...
#    ...
#
# 3) For runs where you control various solver and problem parameters and can use
#    multiple processors in time, try 
#
#    $$ mpirun -np K  python3 drive_adv_diff_1D_run.py
#
#    where you control parameters by editing drive_adv_diff_1D_run.py 
## 

##
# Other notes:
#  1) Some systems may need to find Numpy headers, which are located in 
#     include_dirs=["../braid", numpy.get_include()],
#  2) Some compilers may require "-fPIC" to be added to extra_compile_args
#
##


os.environ["CC"] = "mpicc"
if sys.platform != 'darwin':
    os.environ["LDSHARED"] = "mpicc -shared"    # Needed by Ubuntu LTS, leave out for Mac

drive_adv_diff_1D_extension = Extension(
                                 name="drive_adv_diff_1D",
                                 sources=["drive_adv_diff_1D.pyx"],
                                 libraries=["braid"],
                                 library_dirs=[braid_dir],
                                 include_dirs=[braid_dir], 
                                 extra_compile_args=["-Wno-incompatible-pointer-types", "-Wno-unused-function" ] 
)
setup(
    name="drive_adv_diff_1D",
    ext_modules=cythonize([drive_adv_diff_1D_extension], language_level = "3")
)

