Name:           sudo-iotop
Version:        2
Release:        1%{?dist}
Summary:        Allow administrators to run iotop without a sudo password

License:        Public Domain
URL:            https://github.com/psimonyi/sudo-iotop
Source0:        iotop.sudoers
Source1:        sudo-iotop.sh

BuildArch:      noarch
Requires:       iotop
# setup owns /etc/profile.d
Requires:       setup

%description
Unlike top, iotop requires root privileges (or the NET_ADMIN cap).  That's
inconvenient when you're trying to use it quickly.

This package lets administrators run iotop easily by aliasing iotop to use sudo
and adding a sudo rule to let that happen without a password for users in the
wheel or iotop group.

Security note: iotop allows the user to ionice any thread.

%prep
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/{sudoers,profile}.d
cp -p iotop.sudoers %{buildroot}%{_sysconfdir}/sudoers.d/iotop
cp -p sudo-iotop.sh %{buildroot}%{_sysconfdir}/profile.d/sudo-iotop.sh

%files
%config(noreplace) %{_sysconfdir}/sudoers.d/iotop
%config(noreplace) %{_sysconfdir}/profile.d/sudo-iotop.sh

%changelog
* Wed May 11 2016 Peter Simonyi <pts@petersimonyi.ca> - 2
- Restrict the sudo permission to the wheel and iotop groups
* Wed Jan 27 2016 Peter Simonyi <pts@petersimonyi.ca> - 1
- First version
