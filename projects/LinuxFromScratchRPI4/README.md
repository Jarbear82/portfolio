# Overview

This is my attepmt at compiling linux from scratch. Currently, it's still a work in progress, as while I was finishing manually compiling each package,
I messed up when I compiled gcc and didn't find out until much later when I tried to build OpenSSL. I did create a backup, but it was after the initial
mistake was made, so I had to restart completely. On this second pass through, I am using the provided build scripts and executing one section at a time
in order to watch for errors.

The goal of this project is to learn the nitty gritty details of linux. So far, I've learned how to create a filesystem, add users, change permissions, change file
ownership, chroot, build packages, test packages, run builds in parallel, and extrace and manage files from the command line. 

As it stands, I still need to rebuild all of the package, then I can finish configuring the filesystem and make it bootable. On a Raspberry Pi, it is a little bit
different because you need to add an eeprom file and you don't use grub.


[Current Demo Video](https://youtu.be/R5spLRaFxxY)

# Development Environment

Hardware:
- Raspberry Pi 4 (8GB RAM)

Software:
- Raspberry Pi OS
- Terminal Emulator
- Bash Shell

Useful Commands (not exhaustive):
- Administration: su, passwd, chroot
- File management commands: cd, chown, mkdir, mv, tar, rm
- Build commands: ./configure, make, make check, make test, make install, -j4 option for building in parallel

# Useful Websites

- https://www.linuxfromscratch.org/lfs/
- https://intestinate.com/pilfs/guide.html

# Future Work

- Rebuild Packages
- Finish Configuration
- Make Bootable
- Add GUI (Beyond Linux From scratch)
