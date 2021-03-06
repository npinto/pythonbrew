from pythonbrew.installer.pythonbrewinstaller import PythonbrewInstaller
from pythonbrew.log import logger
from pythonbrew.define import INSTALLER_ROOT, ROOT, PATH_ETC

def install_pythonbrew():
    PythonbrewInstaller().install(INSTALLER_ROOT)
    # pythonbrew is only for bash
    shrc = yourshrc = "bashrc"
    logger.info("""
Well-done! Congratulations!

The pythonbrew is installed as:
    
  %(ROOT)s

Please add the following line to the end of your ~/.%(yourshrc)s

  source %(PATH_ETC)s/%(shrc)s

After that, exit this shell, start a new one, and install some fresh
pythons:

  pythonbrew install 2.6.6
  pythonbrew install 2.5.5

For further instructions, run:

  pythonbrew help

The default help messages will popup and tell you what to do!

Enjoy pythonbrew at %(ROOT)s!!
""" % {'ROOT':ROOT, 'yourshrc':yourshrc, 'shrc':shrc, 'PATH_ETC':PATH_ETC})

def upgrade_pythonbrew():
    PythonbrewInstaller().install(INSTALLER_ROOT)
