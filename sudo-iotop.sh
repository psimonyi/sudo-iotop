# In interactive shells, use sudo for iotop automatically.
# Copied bits from colorls.sh.  Why do their alias lines do 2>/dev/null?

# Skip all for noninteractive shells.
[ -z "$PS1" ] && return

alias iotop='sudo iotop'
