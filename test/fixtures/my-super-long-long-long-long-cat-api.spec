%define name my-super-long-long-long-long-cat-api
%define version 1.0.0
%define release 1
%define buildroot %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Name: %{name}
Version: %{version}
Release: %{release}
Summary: my-super-long-long-long-long-cat-api

Group: Installation Script
License: MIT
Source: %{name}.tar.gz
BuildRoot: %{buildroot}
Requires: nodejs
BuildRequires: nodejs
AutoReqProv: no

%description
My Super Long Long Long Long Cat API

%prep
%setup -q -c -n %{name}

%build
npm prune --production
npm rebuild

%pre
getent group my-super-long-long-long-long-cat >/dev/null || groupadd -r my-super-long-long-long-long-cat
getent passwd my-super-long-long-long-long-cat >/dev/null || useradd -r -g my-super-long-long-long-long-cat -G my-super-long-long-long-long-cat -d / -s /sbin/nologin -c "my-super-long-long-long-long-cat" my-super-long-long-long-long-cat

%install
mkdir -p %{buildroot}/etc/systemd/system/my-super-long-long-long-long-cat-api
cp -r ./ %{buildroot}/etc/systemd/system/my-super-long-long-long-long-cat-api
mkdir -p %{buildroot}/var/log/my-super-long-long-long-long-cat-api

%post
systemctl enable /etc/systemd/system/my-super-long-long-long-long-cat-api/my-super-long-long-long-long-cat-api.service

%clean
rm -rf %{buildroot}

%files
%defattr(644, my-super-long-long-long-long-cat, my-super-long-long-long-long-cat, 755)
/etc/systemd/system/my-super-long-long-long-long-cat-api
/var/log/my-super-long-long-long-long-cat-api
