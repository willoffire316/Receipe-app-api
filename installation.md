esak@esak-VirtualBox:~$ sudo apt-get remove docker docker-engine docker.io containerd runc
[sudo] password for esak: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Package 'docker-engine' is not installed, so not removed
Package 'docker' is not installed, so not removed
Package 'containerd' is not installed, so not removed
Package 'docker.io' is not installed, so not removed
Package 'runc' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  efibootmgr fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0
  gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0
  grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5
  libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14
  libfreerdp-client2-2 libfreerdp2-2 libfwup1 libgc1c2 libgee-0.8-2
  libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4
  liblangtag-common liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0
  libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0
  libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1
  libwayland-egl1-mesa libwinpr2-2 libxapian30 libxmlsec1 libxmlsec1-nss
  lp-solve media-player-info python3-mako python3-markupsafe syslinux
  syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
esak@esak-VirtualBox:~$ sudo apt-get install \
>     apt-transport-https \
>     ca-certificates \
>     curl \
>     gnupg-agent \
>     software-properties-common
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ca-certificates is already the newest version (20180409).
ca-certificates set to manually installed.
software-properties-common is already the newest version (0.96.24.32.12).
software-properties-common set to manually installed.
The following packages were automatically installed and are no longer required:
  efibootmgr fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0
  gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0
  grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5
  libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14
  libfreerdp-client2-2 libfreerdp2-2 libfwup1 libgc1c2 libgee-0.8-2
  libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4
  liblangtag-common liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0
  libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0
  libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1
  libwayland-egl1-mesa libwinpr2-2 libxapian30 libxmlsec1 libxmlsec1-nss
  lp-solve media-player-info python3-mako python3-markupsafe syslinux
  syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libcurl4
The following NEW packages will be installed:
  apt-transport-https curl gnupg-agent libcurl4
0 upgraded, 4 newly installed, 0 to remove and 3 not upgraded.
Need to get 380 kB of archives.
After this operation, 1,234 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 apt-transport-https all 1.6.12 [1,692 B]
Get:2 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libcurl4 amd64 7.58.0-2ubuntu3.8 [214 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 curl amd64 7.58.0-2ubuntu3.8 [159 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 gnupg-agent all 2.2.4-1ubuntu1.2 [4,880 B]
Fetched 380 kB in 0s (937 kB/s)   
Selecting previously unselected package apt-transport-https.
(Reading database ... 157328 files and directories currently installed.)
Preparing to unpack .../apt-transport-https_1.6.12_all.deb ...
Unpacking apt-transport-https (1.6.12) ...
Selecting previously unselected package libcurl4:amd64.
Preparing to unpack .../libcurl4_7.58.0-2ubuntu3.8_amd64.deb ...
Unpacking libcurl4:amd64 (7.58.0-2ubuntu3.8) ...
Selecting previously unselected package curl.
Preparing to unpack .../curl_7.58.0-2ubuntu3.8_amd64.deb ...
Unpacking curl (7.58.0-2ubuntu3.8) ...
Selecting previously unselected package gnupg-agent.
Preparing to unpack .../gnupg-agent_2.2.4-1ubuntu1.2_all.deb ...
Unpacking gnupg-agent (2.2.4-1ubuntu1.2) ...
Setting up apt-transport-https (1.6.12) ...
Setting up libcurl4:amd64 (7.58.0-2ubuntu3.8) ...
Setting up gnupg-agent (2.2.4-1ubuntu1.2) ...
Setting up curl (7.58.0-2ubuntu3.8) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
esak@esak-VirtualBox:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
OK
esak@esak-VirtualBox:~$ sudo apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]

esak@esak-VirtualBox:~$ sudo add-apt-repository \
>    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
>    $(lsb_release -cs) \
>    stable"
Hit:1 http://in.archive.ubuntu.com/ubuntu bionic InRelease
Hit:2 http://in.archive.ubuntu.com/ubuntu bionic-updates InRelease             
Hit:3 http://in.archive.ubuntu.com/ubuntu bionic-backports InRelease           
Get:4 https://download.docker.com/linux/ubuntu bionic InRelease [64.4 kB]      
Hit:5 http://security.ubuntu.com/ubuntu bionic-security InRelease              
Hit:6 http://ppa.launchpad.net/alexlarsson/flatpak/ubuntu bionic InRelease     
Get:7 https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages [10.7 kB]
Fetched 75.1 kB in 2s (33.7 kB/s)                        
Reading package lists... Done
esak@esak-VirtualBox:~$ sudo apt-get update
Hit:1 https://download.docker.com/linux/ubuntu bionic InRelease
Hit:2 http://in.archive.ubuntu.com/ubuntu bionic InRelease                     
Hit:3 http://in.archive.ubuntu.com/ubuntu bionic-updates InRelease             
Hit:4 http://in.archive.ubuntu.com/ubuntu bionic-backports InRelease           
Hit:5 http://ppa.launchpad.net/alexlarsson/flatpak/ubuntu bionic InRelease     
Hit:6 http://security.ubuntu.com/ubuntu bionic-security InRelease              
Reading package lists... Done                                                  
esak@esak-VirtualBox:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  efibootmgr fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0
  gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0
  grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5
  libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14
  libfreerdp-client2-2 libfreerdp2-2 libfwup1 libgc1c2 libgee-0.8-2
  libgexiv2-2 libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4
  liblangtag-common liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0
  libmspub-0.1-1 libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0
  libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1
  libwayland-egl1-mesa libwinpr2-2 libxapian30 libxmlsec1 libxmlsec1-nss
  lp-solve media-player-info python3-mako python3-markupsafe syslinux
  syslinux-common syslinux-legacy usb-creator-common
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  aufs-tools cgroupfs-mount pigz
The following NEW packages will be installed:
  aufs-tools cgroupfs-mount containerd.io docker-ce docker-ce-cli pigz
0 upgraded, 6 newly installed, 0 to remove and 3 not upgraded.
Need to get 85.7 MB of archives.
After this operation, 385 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 pigz amd64 2.4-1 [57.4 kB]
Get:2 https://download.docker.com/linux/ubuntu bionic/stable amd64 containerd.io amd64 1.2.13-1 [20.1 MB]
Get:3 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 aufs-tools amd64 1:4.9+20170918-1ubuntu1 [104 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu bionic/universe amd64 cgroupfs-mount all 1.4 [6,320 B]
Get:5 https://download.docker.com/linux/ubuntu bionic/stable amd64 docker-ce-cli amd64 5:19.03.7~3-0~ubuntu-bionic [42.5 MB]
Get:6 https://download.docker.com/linux/ubuntu bionic/stable amd64 docker-ce amd64 5:19.03.7~3-0~ubuntu-bionic [22.9 MB]
Fetched 85.7 MB in 13s (6,457 kB/s)                                            
Selecting previously unselected package pigz.
(Reading database ... 157349 files and directories currently installed.)
Preparing to unpack .../0-pigz_2.4-1_amd64.deb ...
Unpacking pigz (2.4-1) ...
Selecting previously unselected package aufs-tools.
Preparing to unpack .../1-aufs-tools_1%3a4.9+20170918-1ubuntu1_amd64.deb ...
Unpacking aufs-tools (1:4.9+20170918-1ubuntu1) ...
Selecting previously unselected package cgroupfs-mount.
Preparing to unpack .../2-cgroupfs-mount_1.4_all.deb ...
Unpacking cgroupfs-mount (1.4) ...
Selecting previously unselected package containerd.io.
Preparing to unpack .../3-containerd.io_1.2.13-1_amd64.deb ...
Unpacking containerd.io (1.2.13-1) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../4-docker-ce-cli_5%3a19.03.7~3-0~ubuntu-bionic_amd64.deb ...
Unpacking docker-ce-cli (5:19.03.7~3-0~ubuntu-bionic) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../5-docker-ce_5%3a19.03.7~3-0~ubuntu-bionic_amd64.deb ...
Unpacking docker-ce (5:19.03.7~3-0~ubuntu-bionic) ...
Setting up aufs-tools (1:4.9+20170918-1ubuntu1) ...
Setting up containerd.io (1.2.13-1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.
Setting up cgroupfs-mount (1.4) ...
Setting up docker-ce-cli (5:19.03.7~3-0~ubuntu-bionic) ...
Setting up pigz (2.4-1) ...
Setting up docker-ce (5:19.03.7~3-0~ubuntu-bionic) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Processing triggers for systemd (237-3ubuntu10.39) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
esak@esak-VirtualBox:~$ apt-cache madison docker-ce
 docker-ce | 5:19.03.7~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.6~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.5~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.4~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.3~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.2~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.1~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:19.03.0~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.9~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.8~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.7~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.6~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.5~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.4~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.3~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.2~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.1~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 5:18.09.0~3-0~ubuntu-bionic | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.3~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.2~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.1~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
 docker-ce | 18.06.0~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
esak@esak-VirtualBox:~$ sudo apt-get install docker-ce=5:19.03.7~3-0~ubuntu-bionic docker-ce-cli=5:19.03.7~3-0~ubuntu-bionic containerd.io
Reading package lists... Done
Building dependency tree       
Reading state information... Done
containerd.io is already the newest version (1.2.13-1).
docker-ce-cli is already the newest version (5:19.03.7~3-0~ubuntu-bionic).
docker-ce is already the newest version (5:19.03.7~3-0~ubuntu-bionic).
The following packages were automatically installed and are no longer required:
  efibootmgr fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0
  grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1 libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libfwup1 libgc1c2 libgee-0.8-2 libgexiv2-2
  libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1
  libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwayland-egl1-mesa libwinpr2-2
  libxapian30 libxmlsec1 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy
  usb-creator-common
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
esak@esak-VirtualBox:~$ sudo apt autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  efibootmgr fonts-liberation2 fonts-opensymbol gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0
  grilo-plugins-0.3-base gstreamer1.0-gtk3 libboost-date-time1.65.1 libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-locale1.65.1
  libcdr-0.1-1 libclucene-contribs1v5 libclucene-core1v5 libcmis-0.5-5v5 libcolamd2 libdazzle-1.0-0 libe-book-0.1-1 libedataserverui-1.2-2 libeot0
  libepubgen-0.1-1 libetonyek-0.1-1 libevent-2.1-6 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libfwup1 libgc1c2 libgee-0.8-2 libgexiv2-2
  libgom-1.0-0 libgpgmepp6 libgpod-common libgpod4 liblangtag-common liblangtag1 liblirc-client0 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1
  libodfgen-0.1-1 libqqwing2v5 libraw16 librevenge-0.0-0 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwayland-egl1-mesa libwinpr2-2
  libxapian30 libxmlsec1 libxmlsec1-nss lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common syslinux-legacy
  usb-creator-common
0 upgraded, 0 newly installed, 63 to remove and 3 not upgraded.
After this operation, 44.7 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 157650 files and directories currently installed.)
Removing efibootmgr (15-1) ...
Removing fonts-liberation2 (2.00.1-7~18.04.2) ...
Removing fonts-opensymbol (2:102.10+LibO6.0.7-0ubuntu0.18.04.10) ...
Removing gir1.2-gst-plugins-base-1.0:amd64 (1.14.5-0ubuntu1~18.04.1) ...
Removing gir1.2-gstreamer-1.0:amd64 (1.14.5-0ubuntu1~18.04.1) ...
Removing gir1.2-gudev-1.0:amd64 (1:232-2) ...
Removing usb-creator-common (0.3.5ubuntu18.04.2) ...
Removing gir1.2-udisks-2.0:amd64 (2.7.6-3ubuntu0.2) ...
Removing grilo-plugins-0.3-base:amd64 (0.3.5-1ubuntu1) ...
Removing gstreamer1.0-gtk3:amd64 (1.14.5-0ubuntu1~18.04.1) ...
Removing libcmis-0.5-5v5 (0.5.1+git20160603-3build2) ...
Removing libboost-date-time1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Removing libboost-filesystem1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Removing libboost-iostreams1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Removing libboost-locale1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Removing libcdr-0.1-1:amd64 (0.1.4-1build1) ...
Removing libclucene-contribs1v5:amd64 (2.3.3.4+dfsg-1) ...
Removing libclucene-core1v5:amd64 (2.3.3.4+dfsg-1) ...
Removing lp-solve (5.5.0.15-4build1) ...
Removing libcolamd2:amd64 (1:5.1.2-2) ...
Removing libdazzle-1.0-0:amd64 (3.28.1-1) ...
Removing libe-book-0.1-1:amd64 (0.1.3-1) ...
Removing libedataserverui-1.2-2:amd64 (3.28.5-0ubuntu0.18.04.2) ...
Removing libeot0:amd64 (0.01-5) ...
Removing libepubgen-0.1-1:amd64 (0.1.0-2ubuntu1) ...
Removing libetonyek-0.1-1:amd64 (0.1.7-3) ...
Removing libevent-2.1-6:amd64 (2.1.8-stable-4build1) ...
Removing libgexiv2-2:amd64 (0.10.8-1) ...
Removing libexiv2-14:amd64 (0.25-3.1ubuntu0.18.04.5) ...
Removing libfreerdp-client2-2:amd64 (2.0.0~git20170725.1.1648deb+dfsg1-7ubuntu0.1) ...
Removing libfreerdp2-2:amd64 (2.0.0~git20170725.1.1648deb+dfsg1-7ubuntu0.1) ...
Removing libfwup1:amd64 (12-3bionic2) ...
Removing libgc1c2:amd64 (1:7.4.2-8ubuntu1) ...
Removing libgee-0.8-2:amd64 (0.20.1-1) ...
Removing libgom-1.0-0:amd64 (0.3.3-4) ...
Removing libgpgmepp6:amd64 (1.10.0-1ubuntu2) ...
Removing libgpod-common (0.8.3-11) ...
Removing libgpod4:amd64 (0.8.3-11) ...
Removing liblangtag1:amd64 (0.6.2-1) ...
Removing liblangtag-common (0.6.2-1) ...
Removing liblirc-client0:amd64 (0.10.0-2) ...
Removing liblua5.3-0:amd64 (5.3.3-1ubuntu0.18.04.1) ...
Removing libmediaart-2.0-0:amd64 (1.9.4-1) ...
Removing libmspub-0.1-1:amd64 (0.1.4-1) ...
Removing libodfgen-0.1-1:amd64 (0.1.6-2) ...
Removing libqqwing2v5:amd64 (1.3.4-1.1) ...
Removing libraw16:amd64 (0.18.8-1ubuntu0.3) ...
Removing librevenge-0.0-0:amd64 (0.0.4-6ubuntu2) ...
Removing libsgutils2-2 (1.42-2ubuntu1.18.04.1) ...
Removing libssh-4:amd64 (0.8.0~20170825.94fa1e38-1ubuntu0.5) ...
Removing libsuitesparseconfig5:amd64 (1:5.1.2-2) ...
Removing libvncclient1:amd64 (0.9.11+dfsg-1ubuntu1.1) ...
Removing libwayland-egl1-mesa:amd64 (19.2.8-0ubuntu0~18.04.3) ...
Removing libwinpr2-2:amd64 (2.0.0~git20170725.1.1648deb+dfsg1-7ubuntu0.1) ...
Removing libxapian30:amd64 (1.4.5-1ubuntu0.1) ...
Removing libxmlsec1-nss:amd64 (1.2.25-1build1) ...
Removing libxmlsec1:amd64 (1.2.25-1build1) ...
Removing media-player-info (23-1) ...
Removing python3-mako (1.0.7+ds1-1) ...
Removing python3-markupsafe (1.0-1build1) ...
Removing syslinux (3:6.03+dfsg1-2) ...
Removing syslinux-common (3:6.03+dfsg1-2) ...
Removing syslinux-legacy (2:3.63+dfsg-2ubuntu9) ...
Processing triggers for udev (237-3ubuntu10.39) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for dbus (1.12.2-1ubuntu1.1) ...
Processing triggers for fontconfig (2.12.6-0ubuntu2) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
esak@esak-VirtualBox:~$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete 
Digest: sha256:fc6a51919cfeb2e6763f62b6d9e8815acbf7cd2e476ea353743570610737b752
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

esak@esak-VirtualBox:~$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   617  100   617    0     0    714      0 --:--:-- --:--:-- --:--:--   713
100 16.3M  100 16.3M    0     0  2555k      0  0:00:06  0:00:06 --:--:-- 3944k
esak@esak-VirtualBox:~$ sudo chmod +x /usr/local/bin/docker-compose
esak@esak-VirtualBox:~$ docker-compose --version
docker-compose version 1.25.4, build 8d51620a
esak@esak-VirtualBox:~$ 

### To Fix the Issue in Docker 
## Issue - Permission Denied 
```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denied
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ sudo chmod 666 /var/run/docker.sock
[sudo] password for esak: 
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ 


```

## Running the Hello World 

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```



### INstalling the required Packages 
```
Django>=2.1.3,<2.2.0
djangorestframework>=3.11.0,<3.12.0
```

  docker build .

it will start Building the docker images 

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker build .
Sending build context to Docker daemon  65.54kB
Step 1/10 : FROM python:3.7-alpine
 ---> a5d195bb2a63
Step 2/10 : MAINTAINER London App Developer Ltd.
 ---> Using cache
 ---> 032c9cbef7d1
Step 3/10 : ENV PYTHONUNBUFFERED 1
 ---> Using cache
 ---> 015137370c04
Step 4/10 : COPY ./requirements.txt /requirements.txt
 ---> 66daf4010948
Step 5/10 : RUN pip install -r /requirements.txt
 ---> Running in a65190b04f3c
Collecting Django<2.2.0,>=2.1.3
  Downloading Django-2.1.15-py3-none-any.whl (7.3 MB)
Collecting djangorestframework<3.12.0,>=3.11.0
  Downloading djangorestframework-3.11.0-py3-none-any.whl (911 kB)
Collecting pytz
  Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
Installing collected packages: pytz, Django, djangorestframework
Successfully installed Django-2.1.15 djangorestframework-3.11.0 pytz-2019.3
Removing intermediate container a65190b04f3c
 ---> fb85bb5d89ae
Step 6/10 : RUN mkdir /app
 ---> Running in dec1282f4638
Removing intermediate container dec1282f4638
 ---> 80ed8eb012dd
Step 7/10 : WORKDIR /app
 ---> Running in 99b1a96bdffc
Removing intermediate container 99b1a96bdffc
 ---> fef56abfd6fa
Step 8/10 : COPY ./app/ /app
 ---> 14d91d94fc13
Step 9/10 : RUN adduser -D user
 ---> Running in a30b90590ba6
Removing intermediate container a30b90590ba6
 ---> d59190cc1797
Step 10/10 : USER user
 ---> Running in b2e5b0b849a8
Removing intermediate container b2e5b0b849a8
 ---> f46feff95f07
Successfully built f46feff95f07

```

## Creating Docker-compose File 
```
version: "3"

services: 
    app:
        build:
            context: .
        ports:
            - "8000:8000"
        volumes: 
            - "./app:/app"

        command: >
          sh -c "python manage.py runserver 0.0.0.0:8000"

```

we are mapping the port 8000 from docker port to the local machine port 
we are maping the volumes , which means code available inside the /app folder is reflected in the docker image as well 
we are running the django server using the commad manage.py command 

  docker-compose build 

output looks like 

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker-compose build
Building app
Step 1/10 : FROM python:3.7-alpine
 ---> a5d195bb2a63
Step 2/10 : MAINTAINER London App Developer Ltd.
 ---> Using cache
 ---> 032c9cbef7d1
Step 3/10 : ENV PYTHONUNBUFFERED 1
 ---> Using cache
 ---> 015137370c04
Step 4/10 : COPY ./requirements.txt /requirements.txt
 ---> 4bcbcba72249
Step 5/10 : RUN pip install -r /requirements.txt
 ---> Running in 96441ced8e7a
Collecting Django<2.2.0,>=2.1.3
  Downloading Django-2.1.15-py3-none-any.whl (7.3 MB)
Collecting djangorestframework<3.12.0,>=3.11.0
  Downloading djangorestframework-3.11.0-py3-none-any.whl (911 kB)
Collecting pytz
  Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
Installing collected packages: pytz, Django, djangorestframework
Successfully installed Django-2.1.15 djangorestframework-3.11.0 pytz-2019.3
Removing intermediate container 96441ced8e7a
 ---> 1096f3674c68
Step 6/10 : RUN mkdir /app
 ---> Running in 6c0249560177
Removing intermediate container 6c0249560177
 ---> ea1373a0659d
Step 7/10 : WORKDIR /app
 ---> Running in 0946d12a9a06
Removing intermediate container 0946d12a9a06
 ---> 42be0943c077
Step 8/10 : COPY ./app/ /app
 ---> e71fd8e23a9f
Step 9/10 : RUN adduser -D user
 ---> Running in 9de511c3a377
Removing intermediate container 9de511c3a377
 ---> 788d91774bd5
Step 10/10 : USER user
 ---> Running in 602fe202ccc8
Removing intermediate container 602fe202ccc8
 ---> d973f62fb030
Successfully built d973f62fb030
Successfully tagged receipe-app-api_app:latest
```

Docker Image created 

  Successfully built d973f62fb030
  Successfully tagged receipe-app-api_app:latest


## Djamgo Project 
Create a New project 

**Docker Command "docker-compose run sh -c "django-admin.py startproject app ." "**

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker-compose run app sh -c "django-admin.py startproject app ."
Creating network "receipe-app-api_default" with the default driver

```


### CI / CD 

 when ever we push a chnage to travis, it will spin a python server , it will install the docker image on that server and it will run these test and flake8 

 if its failed to , a mail will be triggered 



 ### Unit Test 

 # writing our first Testcase 

we are creating a simple file callled `tests.py` and we are adding our testcases in there 
we are using the django TestCase class , a simple test case look like as below 
test name should also startes with test `test_add_numbers`

 ```
 class calcTest(TestCase):
    
    def test_add_numbers(self):
        """ Test That add two Numbers Together"""
        self.assertEqual(add(3,7), 10)
 ```
 # Running our First Test case 
    docker-compose run app sh -c "python manage.py test"

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker-compose run app sh -c "python manage.py test"
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...

```

## Unit Testing Using test Driven Framework 

docker-compose run app sh -c "python manage.py test"
docker-compose run app sh -c "python manage.py test && flake8"

```
esak@esak-VirtualBox:~/mycodespace/Receipe-app-api$ docker-compose run app sh -c "python manage.py test"
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK
Destroying test database for alias 'default'...

```