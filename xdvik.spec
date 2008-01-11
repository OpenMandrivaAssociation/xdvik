%define name xdvik
%define version 22.84.10
%define release %mkrel 4

Summary:	An X viewer for DVI files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url: 		http://xdvi.sourceforge.net/
License: 	GPL
Group: 		Publishing
Source0: 	http://puzzle.dl.sourceforge.net/sourceforge/xdvi/%{name}-%{version}.tar.bz2
Source1: 	icons-xdvi.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Conflicts: 	tetex-xdvi
Conflicts: 	xdvi
BuildRequires: 	libt1lib >= 5.0.2
BuildRequires: 	X11-devel
# Makes it use www-browser by default
Patch0:		xdvik-www-browser.patch

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

It is based on the regular (non-k) xdvi of the same version number, and is
part of the texk project (deployed e.g. in teTeX).

%prep
%setup -q
%patch0 -p0

%build
%configure --with-system-t1lib
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
%makeinstall texmf=%buildroot%_datadir/texmf

rm -fr %buildroot%_datadir/texmf

mkdir -p %buildroot%_iconsdir

tar xjvf -C %buildroot%_iconsdir %SOURCE1

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDvi
Comment=DVI files viewer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Office-Publishing;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL README CHANGES README_maintainer TODO release-tetex-src.txt
%_bindir/*
%_mandir/man?/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/dvi.png
%_liconsdir/dvi.png
%_miconsdir/dvi.png


