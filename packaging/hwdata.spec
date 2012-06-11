Name:           hwdata
Version:        0.232
Release:        1
License:        GPL-2.0+
Summary:        Hardware identification and configuration data
Group:          System/Base
Source:         %{name}-%{version}.tar.bz2
Url:            http://git.fedorahosted.org/git/hwdata.git
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q

%build
# nothing to build

%install
%make_install

%files
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
