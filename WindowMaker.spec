%define snapshot		1

%define wraster_major		3
%define libwraster		%mklibname wraster %{wraster_major}
%define libwraster_devel	%mklibname wraster -d
%define libwraster_static_devel	%mklibname wraster -d -s

%define WINGs_major		2
%define libWINGs		%mklibname WINGs %{WINGs_major}
%define libWINGs_devel		%mklibname WINGs -d
%define libWINGs_static_devel	%mklibname WINGs -d -s

%define gnustepdir		%{_prefix}/GNUstep

Summary:	A window manager for the X Window System
Name:		WindowMaker
Version:	0.95.2
Release:	3
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
URL:		http://www.windowmaker.info/
Source0:	http://windowmaker.org/pub/source/release/%{name}-%{version}.tar.gz
Source1:	WindowMaker-data.tar.bz2
Source4:	WindowMaker-menumethod
Source6:	WindowMaker-WindowMaker
Source7:	WindowMaker-WMWindowAttributes
Source8:	WindowMaker-startwindowmaker
Source10:	WindowMaker-Terminal
Source13:	WindowMaker-wmaker.inst
Source15:	WindowMaker-WMState
Source20:	WindowMaker-0.80.1-man-pages.tar.bz2
Source21:	WindowMaker-Galaxy.style.bz2
Source22:	WindowMaker-WMGLOBAL
Source23:	WindowMaker
Source24:	03WindowMaker

# Matthias: NET_WM_NAME patch by Marcelo E. Magallon <mmagallo@debian.org>
Patch0:		WindowMaker-0.95.0-NET_WM_NAME.patch

# include the xdg menu (do not replace the original menu since it contains windowmaker-specific commands)
Patch1:		WindowMaker-0.95.0-applications-menu.patch

# correct focus not set on some qt windows, usually "About Qt"
Patch2:		WindowMaker-0.95.0-qt_popup.patch

# Mageia patches
Patch3:		windowmaker-0.95.2-mga-fix-paths-in-german-plmenu.patch
Patch4:		windowmaker-0.95.2-mga-stop-using-old-X11R6-directory.patch
Patch5:		windowmaker-0.95.2-mga-patch-WMState-to-use-old-Mageia-configuration.patch
Patch6:		wmaker-0.94.0-net_wm_moveresize.patch

Patch7:		WindowMaker-automake-1.13.patch

Requires:	desktop-common-data
Requires:	mandriva-theme
Requires:	xdg-compliance-menu
Requires:	wmcalclock
Obsoletes:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common
Provides:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	tiff-devel
BuildRequires:	imagemagick

%description
Window Maker is a X11 window manager which emulates the look and feel of the
NeXTSTEP (TM) graphical user interface. It is relatively fast, feature rich and
easy to configure and use. Window Maker is part of the official GNU project,
which means that Window Maker can interoperate with other GNU projects, such as
GNOME.

Window Maker allows users to switch themes 'on the fly,' to place favorite
applications on either an application dock, similar to AfterStep's Wharf or on
a workspace dock, a 'clip' which extends the application dock's usefulness.

%files -f WindowMaker.lang
%doc AUTHORS BUGFORM BUGS ChangeLog COPYING.WTFPL FAQ FAQ.I18N NEWS README* TODO
%dir %{_sysconfdir}/X11/WindowMaker/
%config(noreplace) %{_sysconfdir}/X11/WindowMaker/*
%{_sysconfdir}/menu.d/WindowMaker
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*

%{_bindir}/*

%{gnustepdir}/Applications/WPrefs.app/

%doc %{_mandir}/man1/*
%lang(cs) %doc %{_mandir}/cs/man1/*
%lang(sk) %doc %{_mandir}/sk/man1/*
%lang(ru) %doc %{_mandir}/ru/man1/*

%{_datadir}/WindowMaker

%{_datadir}/WINGs

%{_iconsdir}/WindowMaker.png
%{_liconsdir}/WindowMaker.png
%{_miconsdir}/WindowMaker.png

%{_datadir}/pixmaps/*.png

#-----------------------------------------------------------------------
%package	-n %{libwraster}
Summary:	Window Maker Raster Graphics Library
Group:		Graphical desktop/WindowMaker
Provides:	libwraster
Conflicts:	libwraster2

%description	-n %{libwraster}
Also known as libwraster, it is WindowMaker's core graphics and image
processing system. libwraster is an optimized, fast, lightweight image library.
It takes advantage of MMX optimizations (on systems that have support for it)
to accelerate rendering. You can load a picture from a file easily with
libwraster, and it has support for .gif, .jpg, .png, .xpm, .ppm, and .tiff at
the moment. Support for other image formats can be added in the future.

This package contains a shared library needed if you wish use WindowMaker.

%files		-n %{libwraster}
%{_libdir}/libwraster.so.*

#-----------------------------------------------------------------------
%package	-n %{libwraster_devel}
Summary:	Window Maker Raster Graphics Library development files	
Group:		Development/C
Requires:	%{libwraster} = %version
Provides:	libwraster-devel
Conflicts:	libwraster2-devel
Obsoletes:	%{mklibname wraster 3 -d}

%description	-n %{libwraster_devel}
This package allows building applications using the libwraster library.

%files		-n %{libwraster_devel}
%{_includedir}/wraster.h
%{_libdir}/libwraster.so
%{_libdir}/pkgconfig/wrlib.pc

#-----------------------------------------------------------------------
%package	-n %{libwraster_static_devel}
Summary:	Libwraster - Static library
Group:		Development/C
Requires:	%{libwraster_devel} = %{EVRD}
Provides:	libwraster-static-devel
Conflicts:	libwraster2-static-devel
Obsoletes:	%{mklibname wraster 3 -d -s} < %{EVRD}

%description	-n %{libwraster_static_devel}
This package contains a static library used to build statically linked 
applications against libwraster.

%files -n %{libwraster_static_devel}
%{_libdir}/libwraster.a

#-----------------------------------------------------------------------
%package	-n %{libWINGs}
Summary:	WINGs Is Not GNUstep
Group:		Graphical desktop/WindowMaker
Provides:	libWINGs = %{EVRD}
Provides:	%{mklibname WindowMaker %{WINGs_major}} = %{EVRD}
Obsoletes:	%{mklibname WindowMaker 0 -d} < %{EVRD}
Requires:	%{libwraster_devel} = %{EVRD}

%description	-n %{libWINGs}
WINGs is a small widget set with the N*XTSTEP look and feel. It's API
is inspired in OpenStep and it's implementation borrows some ideas
from Tk. It has a reasonable set of widgets, sufficient for building
small applications (like a CDPlayer or hacking something like rxvt). It
also has other functions that are usefull for applications, like a
User Defaults alike configuration manager and a notification system.

%files		-n %{libWINGs}
%{_libdir}/libWINGs.so.*
%{_libdir}/libWUtil.so.*

#-----------------------------------------------------------------------
%package	-n %{libWINGs_devel}
Summary:	WINGs Is Not GNUstep
Group:		Development/C
Provides:	%{mklibname WindowMaker -d}
Requires:	%{libWINGs} = %{EVRD}
%rename WindowMaker-devel
%rename windowmaker-devel

%description	-n %{libWINGs_devel}
This package allows building applications using the libWINGs library.

%files		-n %{libWINGs_devel}
%{_includedir}/WINGs
%{_libdir}/pkgconfig/WINGs.pc
%{_libdir}/libWINGs.so
%{_libdir}/libWUtil.so

#-----------------------------------------------------------------------
%package	-n %{libWINGs_static_devel}
Summary:	WINGs Is Not GNUstep
Group:		Development/C
Provides:	%{mklibname WindowMaker -d -s}
Requires:	%{libWINGs_devel} = %{EVRD}
%rename WindowMaker-static-devel

%description	-n %{libWINGs_static_devel}
This package allows building applications using the libWINGs library.

%files		-n %{libWINGs_static_devel}
%{_libdir}/libWINGs.a
%{_libdir}/libWUtil.a

#-----------------------------------------------------------------------
%prep
%setup -q -a 1 -a 20
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1 -b .am113~

%if %{snapshot}
sh ./autogen.sh
%else
autoreconf -fi
%endif

#-----------------------------------------------------------------------
%build
# protect the WPrefs.app location for unclean build envs with gnustep-make installed
unset GNUSTEP_LOCAL_ROOT

LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko nl no pl pt ro ru sk sv tr zh_CN zh_TW"
export LINGUAS
%configure	--sysconfdir=%{_sysconfdir}/X11 \
		--with-nlsdir=%{_datadir}/locale \
		--enable-sound  \
		--with-pixmapdir=%{_datadir}/pixmaps \
                --with-gnustepdir=%{gnustepdir} \
		--enable-xinerama \
		--enable-usermenu \
		--with-pic \
		--with-x

make

#-----------------------------------------------------------------------
%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

install -d 644 %{buildroot}/%{_datadir}/pixmaps
install -m 644 WindowMaker-data/pixmaps/* %{buildroot}/%{_datadir}/pixmaps

# Config files: Auto installation
install -m 755 %{SOURCE8} %{buildroot}/%{_bindir}/startwindowmaker

install -d -m 755 %{buildroot}/%{_sysconfdir}/X11/WindowMaker
install -m 644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/X11/WindowMaker/WindowMaker
install -m 644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/X11/WindowMaker/WMWindowAttributes
install -m 644 %{SOURCE15} %{buildroot}/%{_sysconfdir}/X11/WindowMaker/WMState
install -m 644 %{SOURCE22} %{buildroot}/%{_sysconfdir}/X11/WindowMaker/WMGLOBAL

# Better terminal launched in Dock
install -m 755 %{SOURCE10} %{buildroot}/%{_bindir}


# Menu support

install -d %{buildroot}/%{_sysconfdir}/menu.d
install -m 755 %{SOURCE23} %{buildroot}/%{_sysconfdir}/menu.d/%{name}

# Icons
mkdir -p %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -geometry 48x48 %{name}/Icons/GNUstepGlow.tiff %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 %{name}/Icons/GNUstepGlow.tiff %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 %{name}/Icons/GNUstepGlow.tiff %{buildroot}%{_miconsdir}/%{name}.png

install -m 644 *.1x %{buildroot}/%{_mandir}/man1/


# Dadou - 0.62.1-18mdk - Make auto-login happy
install -m 755 %{SOURCE13} %{buildroot}/%{_bindir}/wmaker.inst

# Matthias - 0.91.0-3mdk - change font in WM standard themes to Sans to
# make non-western users happy
for i in %{buildroot}/%{_datadir}/%{name}/Themes/*.style
do
	sed s/Trebuchet\ MS\,Luxi\ //g $i > $i.tmp && mv -f $i.tmp $i;
	sed s/Arial,Luxi\ //g $i > $i.tmp && mv -f $i.tmp $i;
	sed s/Verdana/Sans/g $i > $i.tmp && mv -f $i.tmp $i;
done

# Matthias - 0.90.0.02mdk - Install Galaxy theme
# (made default in startwindowmaker script)
bzcat %{SOURCE21} > %{buildroot}/%{_datadir}/%{name}/Themes/Galaxy.style

# wmsession support
install -D %{SOURCE24} %{buildroot}/%{_sysconfdir}/X11/wmsession.d/03WindowMaker

%find_lang WPrefs
%find_lang WindowMaker
%find_lang WINGs
%find_lang wmgenmenu
cat WPrefs.lang >> WindowMaker.lang
cat WINGs.lang >> WindowMaker.lang
cat wmgenmenu.lang >> WindowMaker.lang


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.95.2-1
+ Revision: 778412
- Update to latest upstream release.
- Add Mageia patches.

* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.95.0-3
+ Revision: 768166
- added unpkgd find_lang wmgenmenu
- removed all .la files
- removed dup lang files
- added requires for wmcalclock
- split out wmcalclock to its own package

* Fri Dec 02 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.95.0-2
+ Revision: 737330
- Correct logic to load menu.xdg when using pt localization.

* Fri Dec 02 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.95.0-1
+ Revision: 737302
- Update to wmaker-0.95.0-crm git tag.

* Sun Oct 23 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92.0-26
+ Revision: 705716
- Correct build with png 1.5.

  + Oden Eriksson <oeriksson@mandriva.com>
    - attempt to relink against libpng15.so.15

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 0.92.0-25
+ Revision: 672102
- cleanup br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Tue Feb 15 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.92.0-24
+ Revision: 637851
- Require xdg-compliance-menu (moved from desktop-common-data)

* Mon Sep 28 2009 Olivier Blin <blino@mandriva.org> 0.92.0-23mdv2010.0
+ Revision: 450403
- use autoreconf (from Arnaud Patard)

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.92.0-22mdv2010.0
+ Revision: 416608
- rebuilt against libjpeg v7

* Thu May 21 2009 Christiaan Welvaart <spturtle@mandriva.org> 0.92.0-21mdv2010.0
+ Revision: 378321
- fix arguments order in format patch
- add changes from CVS, taken from fedora
  o fixes QT4 menu problem (bug #50255)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - run libtoolize before building to update libtool files to the latest version
    - add patch to fix wformat errors

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.92.0-20mdv2009.1
+ Revision: 300996
- rebuilt against new libxcb

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.92.0-19mdv2009.0
+ Revision: 194806
- Fix #39677. Thanks to Carlos R. Mafra for the patch and analysis of
  the problem.

* Mon Mar 31 2008 Antoine Ginies <aginies@mandriva.com> 0.92.0-18mdv2008.1
+ Revision: 191244
- use the /etc/menu.d directory to store the WM's script to generate the xdg menu

* Thu Mar 27 2008 Antoine Ginies <aginies@mandriva.com> 0.92.0-17mdv2008.1
+ Revision: 190613
- fix empty Application menu

* Thu Feb 28 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.92.0-16mdv2008.1
+ Revision: 176383
- Bump release for submit as release 15 is stuck in build system.
- Attempt to fix failure to upload package by renaming menu file to
  package name, as this is the only difference with a package that seems
  to work.
- Install menu in %%{_menudir}, not in %%{_sysconfdir}/menu.d.
- This patch fixes a nasty bug switching virtual consoles when the
  Composite extension is enabled but default depth is not 24.
- Fix "Reduce Window Maker wakeups to zero" (#37978)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 24 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.92.0-14mdv2008.1
+ Revision: 111794
- increase release number
- fix stdout redirection
- remove debian menu support
- package all menu files from upstream
- also patch german and french menu files for xdg menu

  + Thierry Vignaud <tv@mandriva.org>
    - fix URL

* Mon Nov 19 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.92.0-12mdv2008.1
+ Revision: 110555
- put the XDG menu in menu.xdg and include it from the WindowMaker applications menu

* Mon Sep 24 2007 Adam Williamson <awilliamson@mandriva.org> 0.92.0-11mdv2008.0
+ Revision: 92660
- rebuild to restore libwraster3, which seems to have gone AWOL
- new -devel policy
- minor cleanups to old conditionals and requirements
- new license policy

* Mon May 28 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.92.0-10mdv2008.0
+ Revision: 31957
- fix buildrequires
- patch12: fix handling of setWorkspaceSpecificBack configuration item
- Import WindowMaker




* Thu Aug 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.92.0-9mdv2007.0
- fix buggy requires for libproplist for x86_64
- fix mklibification on x86_64
- fix abuse of prereq (not justified by %%post)
- fix requires-on-release
- misc other rpmlint fixes (I didn't fix the
  update-menus-without-menu-file-in-%%post{,un} errors because they might be
  needed in order to run the newly installed WM menu method)

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 0.92.0-8mdv2007.0
- Allow package to be installed on 2007.0, don't ship old menu method 
  for 2007.0 and later

* Thu Jul 27 2006 Jerome Soyer <saispo@mandriva.org> 0.92.0-7mdv2007.0
- Fix startwindomaker script
- Close #23616

* Mon Nov 28 2005 Laurent MONTEL <lmontel@mandriva.com> 0.92.0-5mdk
- Add patch11: fix compile on x86_64

* Mon Nov 28 2005 Laurent MONTEL <lmontel@mandriva.com> 0.92.0-4mdk
- Don't use Mandrake (Bug found by Helene Durosini)

* Sat Aug 06 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.92.0-3mdk
- fix buildrequires (upstream used automake 1.4)

* Mon Aug 01 2005 Guillaume Bedot <littletux@mandriva.org> 0.92.0-2mdk
- thanks to Udo Rader: use --with-gnustepdir for a correct Wprefs.app 
 location, and reenable mmx asm  with SuSE patch (Patch10).
- removed %%_datadir/WPrefs/ from packaged files (no more file in there)
- use mkrel

* Sun Jul 31 2005 Guillaume Bedot <littletux@mandriva.org> 0.92.0-1mdk
- New release 0.92.0
- disabled mmx asm
- added %%_datadir/WPrefs/ to packaged files
- removed WPrefs.app (no more there...)

* Mon Apr 18 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.91.0-6mdk
- Fix for X86-64.

* Tue Mar 22 2005 Matthias Debus <psic4t@netbands.de> 0.91.0-5mdk
- sanitize requires
- add conflicts: libwraster2

* Fri Jan 13 2005 Matthias Debus <psic4t@netbands.de> 0.91.0-4mdk
- patch0: fix NET_WM_NAME property

* Fri Dec 10 2004 Matthias Debus <psic4t@netbands.de> 0.91.0-3mdk
- change menu encoding to UTF-8 (Thanks to Michael Scherer!)
- use Sans font in WM default themes to make non-western users happy
- Galaxy theme: Use switch panel image

* Sun Nov 28 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.91.0-2mdk
- fix the WPrefs.app location before the build

* Thu Nov 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91.0-1mdk
- fix WPrefs.app location
- disable parrallel build (broken for now)
- Matthias Debus <psic4t@netbands.de>:
  o new version
  o relocate in /usr
  o remove WMMail from core package
  o set NLSDIR in startwindowmaker script and remove locale patch
  o remove all old patches (merged)
  o Source22: provide WMGLOBAL file to use system standard font in WINGs
  o Galaxy theme: use system standard font
  o remove wm_mdk_dir/WindowMaker (clueless)
  o spec file cleanup

* Mon Sep 13 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040826.2mdk
- fix WPrefs location in default menu

* Thu Aug 31 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040826.1mdk
- new snapshot from wm2 branch
- fixes #9697
- remove patches 2-7 (NETWM support): merged

* Wed Aug 04 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040627.6mdk
- change Mandrakelinux.png -> default.png in Galaxy theme

* Wed Aug 04 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040627.5mdk
- update Galaxy theme to use new path to Mandrakelinux wallpaper

* Fri Jul 16 2004 Michael Scherer <misc@mandrake.org> 0.90.0-0.4cvs20040627.4mdk
- use correct Requires on mandrakelinux-theme

* Fri Jul 02 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040627.3mdk
- really remove CJK style

* Fri Jul 01 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040627.2mdk
- patch12: don't crash with 16-bit color depth (fixes bug #10145)
- use ImageMagick to convert icons
- only ship with Galaxy and default themes (remove CJK style)

* Thu Jul  1 2004 Nicolas Planel <nplanel@mandrakesoft.com> 0.90.0-0.4cvs20040627.1mdk
- snapshot 20040627.
- merge stable and devel spec file.

* Fri Jun 18 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.90.0-0.4cvs20040502.4mdk
- re-add BuildRequires: libPropList-devel
- use specific versions of autotools

* Tue May 18 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040502.3mdk
- convert more icons to png (WM standard and WM-data)
- remove WindowMaker-extras from sources list (not used)
- no rpmlint errors anymore (use mklibname macro)
- remove libPropList requirement

* Wed May 12 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040502.2mdk
- patch10: make localisation working
- patch11: reduce minimize animation speed on fast boxes or with kernel 2.6

* Fri May 07 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.4cvs20040502.1mdk
- From Christiaan Welvaart <cjw@daneel.dyndns.org>:
	- new snapshot
	- patch9: Try to fix xlib in WMMail
	- replace cd's by popd/pushd
- patches 2-7: enable NETWM2 support (removed old NETWM patch)
- make rpmlint happier (use configure macro)
- make guys at windowmaker.org happier (clearer cvs version naming)
- requires libwraster
- change default WMMail config (fixes bug #4473)
- add xvt argument passing (fixes bug #457)
- adjust workspace display fontsize in Galaxy theme
- set NLSDIR to /usr/share (but localisation still isn't working)

* Sat Apr 24 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.90.0-0.3mdk
- patch7: add basic NETWM (gnome2) support

* Wed Apr 21 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.2mdk
- make new Galaxy theme the default 
	- needs bitstream vera fonts
	- changes in startwindowmaker script
	- use setstyle for default theme
- patch8: vera fonts (not arial) in WINGs apps
- disable NETWM support (patch7; not working)
- patch1 (zh locale fix): backed out (needs to be regenerated) 
- patch2 (window levels): removed (merged)
- patch3 (windows switch menu): backed out (merged/buggy) 
- patch4 (single WINGs): removed (merged)
- patch6 (xinerama fixes): removed (merged)
- remove some non-existant icon/pixmap paths
- change some icons in WMWindowAttributes

* Tue Apr 13 2004 Matthias Debus <psic4t@netbands.de> 0.90.0-0.1mdk
- new cvs snapshot with XFT support (yes!)
- back out patch1,2,3,4 and 6: need to be regenerated
- patch7 - enable NETWM2 support

* Thu Sep 04 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.80.2-5mdk
- Fix buildrequires

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.80.2-4mdk
- rebuild

* Wed Jan 21 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 0.80.2-2mdk
- English correction of menu entry (proofreading by Stew Benedicts)

* Tue Nov 12 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.2-1mdk
- new release
- remove patch 7 (merged upstream)

* Tue Nov 12 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.1-2mdk
- source 20 : add new man pages : WPrefs.1x.bz2, WindowMaker.1x.bz2
- patch 2 : fix some invalid pointer dereferences
- patch 3 : fix windows list window / windows switch
- patch 4 : ensure simple WINGs
- patch 5 : add autoscale option
- patch 6 : fix some xinerama bugs
- patch 7 : fix buffer overflow

* Fri Jul 12 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.1-2mdk
- %%lang non english man pages

* Tue Jul 02 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.1-1mdk
- new release
- add source Url
- regenerate configure (IF needed)
- require newer mandrake_desk
- fix zh translation (patch1)

* Thu Feb 28 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.80.0-5mdk
- Really don't depend on aterm (sorry for the missing fix).

* Wed Feb 27 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.80.0-4mdk
- Use xvt so we don't explicitly depend on aterm.
- Put the libwraster la file in -devel.

* Wed Feb 20 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.80.0-3mdk
- Fix description length
- Do not modify _prefix macro
- Replace Wine with Red Wine entry (to prevent translation errors with Wine package)

* Thu Jan 10 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.0-2mdk
- further spec clean

* Wed Jan 09 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.80.0-1mdk
- sanitize macros use
- new release

* Tue Dec  4 2001 Stefan van der Eijk <stefan@eijk.nu> 0.70.0-2mdk
- Removed %%dir %%_pixdir/ (owned by filesystem)
- Removed redundant BuildRequires

* Tue Nov 08 2001 David BAUDENS <baudens@mandrakesoft.com> 0.70.0-1mdk
- 0.70.0
- various rpmlint fixes (Titi)
- s!wundowmaker!windowmaker!g (Titi)
- s!windowmkaer!windowmaker!g (Titi)

* Tue Oct 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.65.1-6mdk
- rebuild against new libpng

* Tue Oct 02 2001 David BAUDENS <baudens@mandrakesoft.com> 0.65.1-5mdk
- Fix Provides/Requires/PreReq
- Clean spec
- Remove old KDE support
- Move static libraries in static-devel packages
- Put includes in right packages
- Solve locales inclusion problem

* Wed Aug 29 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.65.1-4mdk
- switched to manual dependencies to avoid depending upon gnome-libs
- the default paths for icons and pixmaps in WPrefs.app/Paths.c has been
  altered to reflect our own locations
- added --enable-shm
- removed executable flag from source 4 8 10 to make rpmlint happy
- added the 48x48 menu icon

* Fri Aug 24 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.65.1-3mdk
- added a symlink for wmCalClock so that old conf will not be broken
- added two alternative rpms with or without gnome/kde  

* Wed Aug 08 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.65.1-2mdk
- nothing much, I have added scaled and tiled modes for the background picture
  in /usr/lib/menu/WindowMaker

* Wed Aug 01 2001 David BAUDENS <baudens@mandrakesoft.com> 0.65.1-1mdk
- 0.65.1
- Changed background color
- Close bug #2325

* Wed Jun 20 2001 Matthias Badaire <mbadaire@mandrakesoft.com> 0.65.0-4mdk
- add ia64 compliant

* Fri Jun 08 2001 David BAUDENS <baudens@mandrakesoft.com> 0.65.0-3mdk
- Add Conflicts: tag to stop "Rebuild to replace packages lost by crazy bot" song

* Tue Jun 05 2001 David BAUDENS <baudens@mandrakesoft.com> 0.65.0-2mdk
- Rebuild to replace packages lost by crazy bot

* Fri May 18 2001 David BAUDENS <baudens@mandrakesoft.com> 0.65.0-1mdk
- 0.65.0

* Sun Apr 15 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-8mdk
- Display WMMail applet only if /var/spool/mail/$USER exist and is readable
- Add missing locales for WMPrefs

* Thu Apr 12 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-7mdk
- Rebuild to replace packages lost by crazy bot

* Mon Mar 26 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.64.0-6mdk
- rebuild to get a binary RPM in Cooker

* Sat Mar 24 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-5mdk
- BuildRequires: egcs for architectures which don't use GCC-2.95.3 as
  default compiler

* Wed Mar 21 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-4mdk
- Rebuild to have packages lost by crazy bot

* Tue Mar 20 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-3mdk
- Fix crash when X run in 16 bit (buggy, buggy gcc...)

* Mon Feb 12 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-2mdk
- Re-upload 0.64.0 replaced by crazy bot
- Merge Alex DU modifications for Chinese

* Mon Feb 12 2001 David BAUDENS <baudens@mandrakesoft.com> 0.64.0-1mdk
- 0.64.0

* Tue Feb 08 2001 David BAUDENS <baudens@mandrakesoft.com> 0.63.1-1mdk
- 0.63.1

* Thu Feb 08 2001 Alex DU <dxiaoming@mandrakesoft.com> 0.62.1-21mdk
- Add support for CJK (multibytes chars) user.
- Add a new theme Default.CJK.style and make change of WindowMaker-wmaker.inst.

* Wed Dec 13 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-20mdk
- Libdification

* Fri Nov 10 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-19mdk
- Build with glibc-2.2 & gcc-2.96

* Tue Sep 19 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-18mdk
- Make auto-login happy

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-17mdk
- Fix wmsession

* Wed Aug 30 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-16mdk
- Fix "I kill the X server"

* Sun Aug 13 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-15mdk
- New clock (wmCalClock)
- New config files
- Modify Window Maker specific menu entries
- Spec clean up
- Patch for wmsetbg
- Add Packager tag
- New wmsession support

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.62.1-14mdk
- automatically added BuildRequires

* Fri May 12 2000 dam's <damien@mandrakesoft.com> 0.62.1-13mdk
- corrected workspace menus.

* Wed May 10 2000 dam's <damien@mandrakesoft.com> 0.62.1-12mdk
- corrected wmaker.inst text script

* Tue May 09 2000 dam's <damien@mandrakesoft.com> 0.62.1-11mdk
- corrected wmaker test script.

* Mon May  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.62.1-10mdk
- remove asclock which conflicts with AfterStep-APPS
- added url

* Tue May  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.62.1-9mdk
- really add menu support

* Fri Apr 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.62.1-8mdk
- added fndSession call

* Thu Apr 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix wmconfig crash

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-6mdk
- Requires mandrake_desk >= 1.0.3-9mdk

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-5mdk
- Add the binary :/ and put it in the right PATH

* Fri Apr 21 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-4mdk
- Relocate in /usr/X11R6
- Menu support
- Fix crazy obsoletes

* Thu Apr 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.62.1-3mdk
- fix a very old bug : when ~/GNUstep doesn't exists, exec wmaker.inst
  else the end user won't be able to launch WindowMaker

* Tue Apr 04 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-2mdk
- Split in 2 packages (devel & normal)
- Fix Group

* Tue Apr 04 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.1-1mdk
- 0.62.1

* Fri Mar 31 2000 David BAUDENS <baudens@mandrakesoft.com> 0.62.0-1mdk
- 0.62.0
- Release for impatients
- Use new Groups
- Use %%{_tmppath} for BuildRoot

* Sun Mar 05 2000 David BAUDENS <baudens@mandrakesoft.com> 0.61.1-17mdk
- Fix duplicate screen saver
- French translations and adapatations

* Wed Jan 05 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61.1-16mdk: new icon
- 0.61.1-15mdk: back to /usr for some directories 
- 0.61.1-14mdk: fix PATH in /etc/X11/WindowMaker 
- 0.61.1-13mdk: fix a typo in WMDrake
- 0.61.1-12mdk: requires mandrake_desk >= 1.0.1-11mdk

* Tue Jan 04 2000 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61.1-11mdk: new icon
- 0.61.1-10mdk: better MandrakeSoft customization

* Mon Jan 03 2000 - David BAUDENS <baudens@mandrakesoft.com>
- Enable WMDrake
- Fix typos

* Mon Dec 27 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix display version

* Tue Dec 21 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix WMDrake

* Wed Dec 15 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Cleanup spec
- Back to original sources
- (Re) Fix cpp problem

* Wed Dec 09 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Build release

* Tue Dec 08 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Add some apps in wmdrake

* Fri Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Initial wmdrake

* Fri Nov 20 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 0.61
- Add some patches from package of Ryan Weaver <ryanw@infohwy.com>

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Various patch syncronised with package from Ryan Weaver <ryanw@infohwy.com>
- Added diff from cvs 'WindowMaker-0.61.0-19990922cvs.diff.bz2'
- fixes seg fault at exit among other things including the following.
- fixed problem with window shortcut assignment from the menu
- fixed problem with fonts in WINGs (Masahide -mac- NODA
- WindowMaker-0.61.0-po.patch.bz2

* Tue Sep 21 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 0.61.0
- fix compilation
- redo Mandrake adaptions

* Tue Jul 20 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description from Gregus <gregus@etudiant.net>
- fix a typo

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update URL.

* Mon May 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix include problem with /usr/bin/cpp (need /lib/cpp).

* Sat May 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake Adaptations.

* Mon Apr 19 1999 Preston Brown <pbrown@redhat.com>
- fixed up default config (dock was empty...)

* Thu Apr 15 1999 Cristian Gafton <gafton@redhat.com>
- version 0.52.0

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- fixed problem with running wmaker.inst in batch mode (forgot comma)

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- fixed icon problems
- run wmaker.inst in batch mode if no ~/GNUstep/Library/WindowMaker dir exists

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Thu Apr 01 1999 Cristian Gafton <gafton@redhat.com>
- requires cpp

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Mar 17 1999 Cristian Gafton <gafton@redhat.com>
- make sure we get the full distribution
- run ldconfig in the post script

* Mon Feb 15 1999 The Rasterman <raster@redhat.com>
- added gnome winhints areas support fix.

* Tue Feb 02 1999 Cristian Gafton <gafton@redhat.com>
- version 0.51.0
