%define major			3
%define libwraster		%mklibname wraster %major
%define libwrasterdev		%mklibname wraster -d
%define libwrasterstatic	%mklibname wraster -d -s

%define	wmcalclock	wmCalClock-1.25
%define version		0.92.0
%define rel     	15
%define mdkrelease	%mkrel %rel
%define _pixdir		%_datadir/pixmaps
%define gnustepdir	%_prefix/GNUstep

%define wmmajor		0
%define libnamedev	%mklibname %name -d
%define libnamestatic	%mklibname %name -s -d

Summary:	A window manager for the X Window System
Name:		WindowMaker
Version:	%{version}
Release:	%{mdkrelease}
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
URL:		http://www.windowmaker.info/

Source0:	ftp://windowmaker.org/pub/source/release/%name-%version.tar.bz2
Source1:	WindowMaker-data.tar.bz2
Source2:	WindowMaker-%{wmcalclock}.tar.bz2
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

# Matthias: NET_WM_NAME patch by Marcelo E. Magallon <mmagallo@debian.org>
Patch0:		WindowMaker-0.91.0-NET_WM_NAME.patch.bz2

# gcc 4.x build patch for asm stuff by Vladimir Nadvornik <nadvornik@suse.cz>
Patch10:	WindowMaker-0.92.0-asm-gcc4.patch.bz2

Patch11:	WindowMaker-0.92.0-fix-x86_64.patch.bz2

# fix a bogus buffer length for a snprintf call in SendHelperMessage
Patch12:	WindowMaker-0.92.0-setWorkspaceSpecificBack.patch

# include the xdg menu (do not replace the original menu since it contains windowmaker-specific commands)
Patch13:	WindowMaker-0.92.0-applications-menu.patch

# 3 next patches from https://bugzilla.redhat.com/show_bug.cgi?id=267041
Patch14:	181001-Substitute-polling-with-kernel-s-dnotify-mechanism.patch
Patch15:	181041-Remove-timer-which-calls-delayedAction.patch
Patch16:	181061-Remove-useless-timer.patch

# This patch fixes a nasty bug switching virtual consoles when the
# Composite extension is enabled but default depth is not 24
Patch17:	WindowMaker-0.92.0-specify-visual-id-to-avoid-composite-corruption.patch

Requires:	gcc-cpp
Requires:	desktop-common-data
Requires:       mandriva-theme
Obsoletes:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common
Provides:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common

BuildRoot:	%_tmppath/%name-%version-%release-root

BuildRequires:	automake1.4
BuildRequires:	libxft-devel libxinerama-devel
BuildRequires:	gcc-cpp
BuildRequires:	libhermes-devel libjpeg-devel
BuildRequires:	libpng-devel libtiff-devel libungif-devel
BuildRequires:	libxpm-devel mawk rpm-build
BuildRequires:	libPropList-devel
BuildRequires:  ImageMagick

%description
Window Maker is a X11 window manager which emulates the look and feel of the
NeXTSTEP (TM) graphical user interface. It is relatively fast, feature rich and
easy to configure and use. Window Maker is part of the official GNU project,
which means that Window Maker can interoperate with other GNU projects, such as
GNOME.

Window Maker allows users to switch themes 'on the fly,' to place favorite
applications on either an application dock, similar to AfterStep's Wharf or on
a workspace dock, a 'clip' which extends the application dock's usefulness.


%package -n %{libwraster}
Summary:	Window Maker Raster Graphics Library
Group:		Graphical desktop/WindowMaker
Provides:	libwraster
Conflicts:	libwraster2

%description -n %{libwraster}
Also known as libwraster, it is WindowMaker's core graphics and image
processing system. libwraster is an optimized, fast, lightweight image library.
It takes advantage of MMX optimizations (on systems that have support for it)
to accelerate rendering. You can load a picture from a file easily with
libwraster, and it has support for .gif, .jpg, .png, .xpm, .ppm, and .tiff at
the moment. Support for other image formats can be added in the future.


This package contains a shared library needed if you wish use WindowMaker.


%package -n	%{libwrasterdev}
Summary:	Window Maker Raster Graphics Library development files	
Group:		Development/C
Requires:	%{libwraster} = %version
Provides:	libwraster-devel
Conflicts:	libwraster2-devel
Obsoletes:	%{mklibname wraster 3 -d}

%description -n %{libwrasterdev}
This package allows building applications using the libwraster library.


%package -n %{libwrasterstatic}
Summary:	Libwraster - Static library
Group:		Development/C
Requires:	%{libwrasterdev} = %version
Provides:	libwraster-static-devel
Conflicts:	libwraster2-static-devel
Obsoletes:	%{mklibname wraster 3 -d -s}

%description -n %{libwrasterstatic}
This package contains a static library used to build statically linked 
applications against libwraster.


%package -n %{libnamedev}
Summary:	Libraries and header files for WindowMaker
Group:		Development/C
Requires:	%{libwrasterdev} = %version
Obsoletes:	%{mklibname WindowMaker 0 -d}
Obsoletes:	windowmaker-devel, WindowMaker-devel
Provides:	windowmaker-devel, WindowMaker-devel

%description -n %{libnamedev}
Window Maker is an X11 window manager which emulates the look and feel of the
NeXTSTEP (TM) graphical user interface. It is relatively fast, feature rich and
easy to configure and use. Window Maker is part of the official GNU project,
which means that Window Maker can interoperate with other GNU projects, such as
GNOME.

Window Maker allows users to switch themes 'on the fly,' to place favorite
xapplications on either an application dock, similar to AfterStep's Wharf or on
a workspace dock, a 'clip' which extends the application dock's usefulness.

This package contains headers needed for development.


%package -n %{libnamestatic}
Summary:	Static libraries and header files for WindowMaker
Group:		Development/C
Requires:	%{libnamedev} = %{version}
Obsoletes:	%{mklibname WindowMaker 0 -d -s}
Obsoletes:	WindowMaker-static-devel
Provides:	WindowMaker-static-devel

%description -n %{libnamestatic}
Window Maker is an X11 window manager which emulates the look and feel of the
NeXTSTEP (TM) graphical user interface. It is relatively fast, feature rich and
easy to configure and use. Window Maker is part of the official GNU project,
which means that Window Maker can interoperate with other GNU projects, such as
GNOME.

Window Maker allows users to switch themes 'on the fly,' to place favorite
xapplications on either an application dock, similar to AfterStep's Wharf or on
a workspace dock, a 'clip' which extends the application dock's usefulness.

This package contains static libraries needed for development.


%prep
%setup -q -a 1 -a 2 -a 20
%patch0 -p0

%patch10 -p0
%patch11 -p1 -b .fix_compile_x86_64
%patch12 -p1 -b .setWorkspaceSpecificBack
%patch13 -p1 -b .xdg
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
# protect the WPrefs.app location for unclean build envs with gnustep-make installed
unset GNUSTEP_LOCAL_ROOT

autoconf

LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko nl no pl pt ro ru sk sv tr zh_CN zh_TW"
export LINGUAS
%configure2_5x --prefix=%_prefix \
		--sysconfdir=%_sysconfdir/X11 \
		--with-nlsdir=%_datadir/locale \
		--enable-sound  \
		--with-pixmapdir=%_pixdir \
                --with-gnustepdir=%gnustepdir \
		--enable-xinerama \
		--enable-usermenu \
		--with-pic \
		--with-x

make

## wmCalClock (default clock)
pushd wmCalClock-1.25/Src
make
popd


%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
%makeinstall_std

install -d 644 %buildroot/%_pixdir
install -m 644 WindowMaker-data/pixmaps/* %buildroot/%_pixdir


# Install wmCalClock (default clcok)
pushd wmCalClock-1.25/Src
install -s -m 0755 wmCalClock %buildroot/%_bindir
install -m 0644 wmCalClock.1 %buildroot/%_mandir/man1/
popd

# Config files: Auto installation
install -m 755 %SOURCE8 %buildroot/%_bindir/startwindowmaker

install -d -m 755 %buildroot/%_sysconfdir/X11/WindowMaker
install -m 644 %SOURCE6 %buildroot/%_sysconfdir/X11/WindowMaker/WindowMaker
install -m 644 %SOURCE7 %buildroot/%_sysconfdir/X11/WindowMaker/WMWindowAttributes
install -m 644 %SOURCE15 %buildroot/%_sysconfdir/X11/WindowMaker/WMState
install -m 644 %SOURCE22 %buildroot/%_sysconfdir/X11/WindowMaker/WMGLOBAL

# Better terminal launched in Dock
install -m 755 %SOURCE10 %buildroot/%_bindir


# Menu support

install -d %{buildroot}/%{_menudir}
install -m 755 %SOURCE23 %{buildroot}/%{_menudir}/%{name}

# Icons
mkdir -p $RPM_BUILD_ROOT{%_iconsdir,%_miconsdir,%_liconsdir}
convert -geometry 48x48 %name/Icons/GNUstepGlow.tiff $RPM_BUILD_ROOT%{_liconsdir}/%name.png
convert -geometry 32x32 %name/Icons/GNUstepGlow.tiff $RPM_BUILD_ROOT%{_iconsdir}/%name.png
convert -geometry 16x16 %name/Icons/GNUstepGlow.tiff $RPM_BUILD_ROOT%{_miconsdir}/%name.png

# Some documentation for WMCalClock
install -d 755 $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/BUGS $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/CHANGES $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/COPYING $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/HINTS $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/README $RPM_BUILD_ROOT%_docdir/%{wmcalclock}
install -m 644 %{wmcalclock}/TODO $RPM_BUILD_ROOT%_docdir/%{wmcalclock}

install -m 644 *.1x $RPM_BUILD_ROOT/%_mandir/man1/


# Dadou - 0.62.1-18mdk - Make auto-login happy
install -m 755 %SOURCE13 %buildroot/%_bindir/wmaker.inst

# Matthias - 0.91.0-3mdk - change font in WM standard themes to Sans to
# make non-western users happy
for i in %buildroot/%_datadir/%name/Themes/*.style
do
	sed s/Trebuchet\ MS\,Luxi\ //g $i > $i.tmp && mv -f $i.tmp $i;
	sed s/Arial,Luxi\ //g $i > $i.tmp && mv -f $i.tmp $i;
	sed s/Verdana/Sans/g $i > $i.tmp && mv -f $i.tmp $i;
done

# Matthias - 0.90.0.02mdk - Install Galaxy theme
# (made default in startwindowmaker script)
bzcat %SOURCE21 > %buildroot/%_datadir/%name/Themes/Galaxy.style

# wmsession support
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d/
cat << EOF > %buildroot/%_sysconfdir/X11/wmsession.d/03WindowMaker
NAME=WindowMaker
ICON=wmaker-wmsession.xpm
EXEC=%_bindir/startwindowmaker
DESC=Window manager which emulates the look and feel of the NeXTSTEP (TM) graphical user interface
SCRIPT:
exec %_bindir/startwindowmaker
EOF

%find_lang WPrefs
%find_lang WindowMaker
%find_lang WINGs
cat WPrefs.lang >> WindowMaker.lang
cat WINGs.lang >> WindowMaker.lang


%clean
rm -fr %buildroot


%post
%update_menus
%make_session

%postun
%clean_menus
%make_session

%post -n %{libwraster} -p /sbin/ldconfig
%postun -n %{libwraster} -p /sbin/ldconfig


%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGFORM BUGS ChangeLog COPYING.WTFPL FAQ FAQ.I18N MIRRORS NEWS README* TODO
%doc %_docdir/%{wmcalclock}

%dir %_sysconfdir/X11/WindowMaker/
%config(noreplace) %_sysconfdir/X11/WindowMaker/*
%{_menudir}/%{name}
%config(noreplace) %_sysconfdir/X11/wmsession.d/*

%_bindir/*

%gnustepdir/Applications/WPrefs.app/

%doc %_mandir/man1/*
%lang(sk) %doc %_mandir/sk/man1/*

%dir %_datadir/WindowMaker/
%_datadir/WindowMaker/*

%dir %_datadir/WINGs/
%_datadir/WINGs/*.tiff
%_datadir/WINGs/*.xpm

%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%_pixdir/*.png


%files -n %{libwraster}
%defattr(-,root,root,-)
%_libdir/libwraster.so.*


%files -n %{libwrasterdev}
%defattr(-,root,root)
%_includedir/wraster.h
%_libdir/libwraster.so
%_libdir/libwraster.la


%files -n %{libwrasterstatic}
%defattr(-,root,root,-)
%_libdir/libwraster.a


%files -n %{libnamedev}
%defattr(-,root,root,-)
%_includedir/WMaker.h

%dir %_includedir/WINGs/
%_includedir/WINGs/*.h
%_libdir/pkgconfig/*.pc

%files -n %{libnamestatic}
%defattr(-,root,root,-)
%_libdir/libE*.a
%_libdir/libW*.a
