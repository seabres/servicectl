%define name	servicectl
%define release	1.el7
%define version	1.0.1

Summary:	Control services (daemons) for systemd in chroot environment
License:	MIT
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System Environment/Base
BuildRoot:	%{_topdir}/BUILDROOT
BuildArch:	noarch
Vendor:		Alexander Sobolevskiy
Packager:	rainer.brestan@gmx.net
Requires:	bash,coreutils,filesystem,setup,systemd,psmisc

%description
Control services (daemons) for systemd in chroot environment.

%prep
# empty, because nothing to do

%build
# empty, because nothing to do

%install
# first empty the install root
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/servicectl
cp -p ../servicectl $RPM_BUILD_ROOT/usr/lib/servicectl
cp -p ../serviced $RPM_BUILD_ROOT/usr/lib/servicectl
cp -p ../LICENSE.txt $RPM_BUILD_ROOT/../../BUILD
cp -p ../README.md $RPM_BUILD_ROOT/../../BUILD

%files
%defattr(-,root,root)
/usr/lib/*
%doc LICENSE.txt README.md

%changelog
* Mon May 13 2019 Alexander Sobolevskiy - 1.0.0-1
* Mon Nov 11 2019 Rainer Brestan <rainer.brestan@gmx.net> - 1.0.1-1
- Added environment handling to servicectl
