.. _users/installation/linux


Linux installation
===================================

You can download the latest version of QElectroTech from http://qelectrotech.org/download.html. 
For GNU/Linux systems, source files can be downloaded and configured. Ready made packages for some Linux distros are also available for download.

 1. For installation in Fedora use:
   | ``sudo yum -y install qelectrotech``

   |  or

   |  Refer to http://copr.fedoraproject.org/coprs/remi/qelectrotech/ to keep your QElectroTech installation always updated.
   
 2. For installation in debian use (0.5 version):
   | ``sudo apt-get install qelectrotech qelectrotech-data qelectrotech-examples``

   |  or 

   |  For a nightly build devel version  - 
   
   for stable Debian aka Stretch with Qt5.9 
   | ``sudo apt-add-repository 'deb http://debian.qelectrotech.org/qet/debian/ stable main'`` 
   
   for unstable Debian aka Sid with latest Qt version
   | ``sudo apt-add-repository 'deb http://debian.qelectrotech.org/qet/debian/ unstable main'`` 
   
   |APT key
   
   | ``$ gpg --keyserver pgpkeys.mit.edu --recv-key 1D4FB6C1``
   | ``$ gpg -a --export 1D4FB6C1 | sudo apt-key add -``

   |  or
   
   | ``wget -q -O - http://download.tuxfamily.org/qet/debian/Qelectrotech_Repository.asc | sudo apt-key add -``

   |Pinning : to get latest 0.7-dev version and not the older 0.5 version in official Debian repositories
   
   |# echo -e 'Package: qelectrotech* \nPin: version 0.70.* \nPin-Priority: 1001' > /etc/apt/preferences.d/40qelectrotech-devel
   
   | ``sudo apt-get install qelectrotech qelectrotech-data qelectrotech-examples qet-tb-generator``
   
   
 3. For installation in Ubuntu, Mint, etc use (0.5):

  | ``sudo apt-get install qelectrotech qelectrotech-data qelectrotech-examples``
  
  |  or 
  
  |  For a stable version (0.6) - 
  
  | ``sudo apt-add-repository ppa:scorpio/ppa``
  | 

  | Create manually the file 40qelectrotech-devel in /etc/apt/preferences.d/ and add these 3 lines:

  | Package: qelectrotech*
  | Pin: version 0.60.*
  | Pin-Priority: 1001
  
  |  apt-get update
  
  | ``sudo apt-get install qelectrotech qelectrotech-data qelectrotech-examples qet-tb-generator``
  
  |  For a nightly build devel version (0.7) - 
  
  | ``sudo add-apt-repository ppa:scorpio/qelectrotech-dev``
  
  | Create manually the file 40qelectrotech-devel in /etc/apt/preferences.d/ and add these 3 lines:

  | Package: qelectrotech*
  | Pin: version 0.70.*
  | Pin-Priority: 1001
  
  | or use sed to upgrade PPA
  
  | ``sudo sed -i 's/'"version 0.60.*"'/'"version 0.70.*"'/' /etc/apt/preferences.d/40qelectrotech-devel``
  
  |  apt-get update
  
  | ``sudo apt-get install qelectrotech qelectrotech-data qelectrotech-examples qet-tb-generator``
  
  
 4. Use AppImages, no installation required: see https://qelectrotech.org/forum/viewtopic.php?pid=8388#p8388

 | Download the version you want here :
 
 | https://download.tuxfamily.org/qet/builds/AppImage/
 
 |  Make it executable
 | ``chmod a+x QElectroTech_0.*.AppImage``
 
 | launch AppImage
 | ``$ ./QElectroTech_0.7-r5444-x86_64.AppImage`` or click to launch
