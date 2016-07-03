# `sudo-iotop` package

Unlike `top`, `iotop` requires root privileges (or the `NET_ADMIN` capability).
That's inconvenient when you're trying to use it quickly.

This package lets administrators run `iotop` easily by making `iotop` an alias
for `sudo iotop` and adding a sudo rule so that users in the `wheel` and
`iotop` groups don't need to enter their password to run it.

Security note: iotop allows the user to ionice any thread.

## Installation
    dnf copr enable psimonyi/sudo-iotop
    dnf install sudo-iotop
