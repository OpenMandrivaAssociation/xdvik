Summary:	An X viewer for DVI files
Name:		xdvik
Version:	22.84.14
Release:	%mkrel 2
Url: 		http://xdvi.sourceforge.net/
# encodings.c is GPLv2+ and LGPL and MIT
# read-mapfile.c tfmload.c are from dvips
# remaining is MIT
License:        GPLv2+
Group: 		Publishing
Source0: 	http://puzzle.dl.sourceforge.net/sourceforge/xdvi/%{name}-%{version}.tar.gz
Source1: 	icons-xdvi.tar.bz2
# Fedora patch
# Fix handling of the 0 key. See:
# http://sourceforge.net/tracker/index.php?func=detail&aid=2067614&group_id=23164&atid=377580
# https://bugzilla.redhat.com/show_bug.cgi?id=470942
# Fixed upstream post 22.84.14 ?
Patch0:		xdvik-22.84.14-zerofix.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Conflicts: 	tetex-xdvi
Conflicts: 	xdvi
BuildRequires: 	libt1lib >= 5.0.2
BuildRequires: 	X11-devel

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

It is based on the regular (non-k) xdvi of the same version number, and is
part of the texk project (deployed e.g. in teTeX).

%prep
%setup -q
%patch0 -p1 -b .zerofix

%build
%configure --with-system-t1lib
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall texmf=%{buildroot}%_datadir/texmf

rm -fr %{buildroot}%{_datadir}/texmf

mkdir -p %{buildroot}%{_iconsdir}

tar xjvf %SOURCE1 -C %{buildroot}%{_iconsdir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDvi
Comment=DVI files viewer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Office;Publishing;Viewer;
MimeType=application/x-dvi;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES README_maintainer TODO release-tetex-src.txt
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/dvi.png
%{_liconsdir}/dvi.png
%{_miconsdir}/dvi.png

