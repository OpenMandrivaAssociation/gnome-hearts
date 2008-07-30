Summary:	Classic hearts card game for the GNOME desktop
Name:     	gnome-hearts
Version:	0.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	http://www.jejik.com/files/gnome-hearts/%name-%version.tar.gz
URL:		http://www.gnome-hearts.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel libglade2-devel gnomeui2-devel libgnome2-devel
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	scrollkeeper

%description
Hearts is an implementation of the classic card game for the GNOME
desktop, featuring configurable rulesets and editable computer opponents
to satisfy widely diverging playing styles. It features various rulesets
with configurable options, multiple computer opponents with differing
styles of play, drag and drop adding of new opponents, and easy creation
and modification of opponents through the Lua scripting language.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS README NEWS TODO ChangeLog
%{_bindir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_mandir}/man6/*
%{_datadir}/omf/%name
%{_datadir}/applications/*.desktop
