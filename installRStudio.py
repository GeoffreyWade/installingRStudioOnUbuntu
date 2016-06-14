#! /usr/bin/python

# This InstallRStudio.py program is designed and created to automate the
# installation of the RStudio IDE, and it's dependencies.
# author: GeoffreyWade

from subprocess import call

def part1():

    # part 1: create a list to hold the commands
    # that are needed to extract the tar.gz, install rstudio,
    # install r-base, and update the alternatives
    lstone = ['sudo mkdir -p -m0755 /usr/local/rStudio',
              'tar -xvf $HOME/Downloads/rstudio-0.99.893-amd64-debian.tar.gz',
              'sudo updatedb', 
              'sudo mv rstudio-0.99.893/* /usr/local/rStudio/',
              'sudo update-alternatives --install \"/usr/bin/rstudio\"'
              ' \"rstudio\" \"/usr/local/rStudio/bin/rstudio\" 1',
              'sudo updatedb', 'sudo apt-get update', 
              'sudo apt-get -y install r-base',
              'sudo rm -rf rstudio-0.99.893', 'sudo updatedb']

    # part 2: execute the commands in the list
    for line in lstone:
        call(line, shell=True)

def createDtop():

    # part 3: create the rstudio.desktop file     
    
    # part 3a: create a list of strings for the .desktop file
    # and output the strings to the rstudio.desktop file
    lsttwo = ['[Desktop Entry]', 'Exec=rstudio %F', 'Icon=/usr/local/rStudio/rstudio.png', 
              'Type=Application', 'Terminal=false', 'Name=RStudio IDE', 
              'GenericName=Integrated Development Environment', 
              'MimeType=text/rstudio/r-cran/c++-src/r-src/qt/applications/', 
              'Categories=R;Development;IDE;'] 

    rstudopen = open('rstudio.desktop', 'w')
    for line1 in lsttwo:
        rstudopen.write(line1 + "\n")
    rstudopen.close()
   
    # part 3b: move the file to the directory
    mvdotlocal = 'mv rstudio.desktop /usr/share/applications/'
  
    call(mvdotlocal, shell=True)
   
    upd = 'sudo updatedb'
    call(upd, shell=True)

def main():

    # abstract and execute the functions (function calls)
    part1()

    createDtop()

    print 'The RStudio IDE has been installed!\ndone.'

main()
