Summary:	An Open-Source Tower Defense Game
Name:		pytowerdefense
Version:	0.5
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/pytowerdefense/%{name}%{version}.zip
# Source0-md5:	289fda19abb2cfa1f5cbc86f0d25e35d
Source1:	%{name}
Source2:	%{name}.desktop
URL:		http://sourceforge.net/projects/pytowerdefense/
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	python-pygame >= 1.9.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Open-Source Tower Defense Game.

%prep
%setup -q -n %{name}%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/images,%{_desktopdir}}
install *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -r images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
