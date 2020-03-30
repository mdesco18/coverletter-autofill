https://cx-freeze.readthedocs.io/en/latest/distutils.html#distutils

The script is invoked as follows:

python setup.py build
This command will create a subdirectory called build with a further subdirectory starting with the letters exe. and ending with the typical identifier for the platform that distutils uses. This allows for multiple platforms to be built without conflicts.

On Windows, you can build a simple installer containing all the files cx_Freeze includes for your application, by running the setup script as:

python setup.py bdist_msi
On Mac OS X, you can use bdist_dmg to build a Mac disk image.