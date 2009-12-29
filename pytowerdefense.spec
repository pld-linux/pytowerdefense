Summary:	An Open-Source Tower Defense Game
Name:		pytowerdefense
Version:	0.4.6
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/pytowerdefense/%{name}%{version}.zip
# Source0-md5:	d14676a78622362dfc3b28a697ad0b29
Source1:	%{name}
URL:		http://sourceforge.net/projects/pytowerdefense/
Requires:	python-pygame >= 1.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Open-Source Tower Defense Game.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/images}
install *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -r images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
