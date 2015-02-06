Summary:	An X viewer for DVI files
Name:		xdvik
Version:	22.84.16
Release:	3
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
Patch1:		xdvik-22.84.14-fix-str-fmt.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Conflicts: 	tetex-xdvi
Conflicts: 	xdvi
BuildRequires: 	libt1lib >= 5.0.2
BuildRequires: 	X11-devel
BuildRequires:  bison

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

It is based on the regular (non-k) xdvi of the same version number, and is
part of the texk project (deployed e.g. in teTeX).

%prep
%setup -q
%patch0 -p1 -b .zerofix
%patch1 -p0 -b .str

%build
%configure2_5x --with-system-t1lib
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



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 22.84.16-2mdv2011.0
+ Revision: 615523
- the mass rebuild of 2010.1 packages

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 22.84.16-1mdv2010.1
+ Revision: 462965
- fix buildrequires
- 22.84.16

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 22.84.14-4mdv2010.0
+ Revision: 445926
- rebuild

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 22.84.14-3mdv2009.1
+ Revision: 362029
- bump rel
- fix str fmt

* Fri Nov 28 2008 Frederik Himpe <fhimpe@mandriva.org> 22.84.14-2mdv2009.1
+ Revision: 307488
- Add Fedora patch to fix zero key handling
- SPEC file clean-ups
- Use freedesktop.org menu categories
- Add application/x-dvi MIME type to desktop file (bug #45991)

* Sat Aug 16 2008 Olivier Thauvin <nanardon@mandriva.org> 22.84.14-1mdv2009.0
+ Revision: 272490
- 22.84.14

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 22.84.10-7mdv2009.0
+ Revision: 262309
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 22.84.10-6mdv2009.0
+ Revision: 256774
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 22.84.10-4mdv2008.1
+ Revision: 148539
- rebuild
- do not use sub-shell, which just hides errors
- drop old menu

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 22.84.10-2mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 06 2006 Olivier Thauvin <nanardon@mandriva.org> 22.84.10-2mdv2007.0
+ Revision: 91849
- fix urls

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org> 22.84.10-1mdv2007.0
+ Revision: 55774
- fix menu
- 22.84.10
- xdg menu
- Import xdvik

* Sun Feb 12 2006 Eskild Hustvedt <eskild@mandriva.org> 22.84.8-4mdk
- Added patch0 (use www-browser)

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 22.84.8-3mdk
- Fix BuildRequires thanks to pterjan
- %%mkrel

* Fri Feb 25 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 22.84.8-2mdk
- fix conflicts with texmf

* Tue Jan 04 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 22.84.8-1mdk
- First mdk spec

