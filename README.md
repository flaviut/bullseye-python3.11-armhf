# Overview
Build of python3.11 for Debian Bullseye on ARM.

## Build details

Done in `qemu-user-static-binfmt` chroot pulled from the SD card of an ARM board I have. Commands run were:

```
sudo rsync --archive --partial --inplace --progress -r /run/media/user/48c1e88a-b408-42ec-9d6c-9aaacd147312/* ./
sudo arch-chroot .
source /etc/profile
export TERM=xterm-256color
apt -y install git-buildpackage
git clone https://salsa.debian.org/cpython-team/python3.git
apt build-dep .
gbp export-orig --pristine-ta
debuild -b -uc -us
```

## Installation

```
dpkg --install python3.11-minimal_3.11.0-3_armhf.deb python3.11-dev_3.11.0-3_armhf.deb python3.11_3.11.0-3_armhf.deb libpython3.11_3.11.0-3_armhf.deb libpython3.11-dbg_3.11.0-3_armhf.deb libpython3.11-dev_3.11.0-3_armhf.deb libpython3.11-stdlib_3.11.0-3_armhf.deb libpython3.11-minimal_3.11.0-3_armhf.deb
```

Note that this package will be missing a bunch of necessary stuff, since it does not build `python3.11-pip` and related packages. This is fine if you are following best-practices of working in a virtualenv, because then the following can be done:

```
# for some reason, the -m venv method fails with `Error: name 'cmd' is not defined` and no stack trace
python3.11 -c 'import venv; venv.EnvBuilder().create(".")'
source bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
```

You can also install pip outside of a virtualenv by running it as root, but then you would be violating [DontBreakDebian](https://wiki.debian.org/DontBreakDebian/) and will run into issues down the road.

## Usage with OctoPrint

I made this package for use with OctoPrint. Additional commands needed in that case are:

```
# in the venv,
pip install OctoPrint
# https://github.com/OctoPrint/OctoPrint/issues/4488
pip install 'wrapt>=1.14,<1.15'
```
