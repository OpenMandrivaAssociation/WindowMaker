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
Version:	0.95.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
URL:		http://www.windowmaker.info/

# git clone git://repo.or.cz/wmaker-crm.git
# cd wmaker-crm
# git archive --prefix WindowMaker-0.95.0/ wmaker-0.95.0-crm | bzip2 > WindowMaker-0.95.0.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
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

Requires:	desktop-common-data
Requires:	mandriva-theme
Requires:	xdg-compliance-menu
Requires:	wmcalclock
Obsoletes:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common
Provides:	windowmaker windowmaker-libs WindowMaker-kde WindowMaker-gnome WindowMaker-common

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxft-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxmu-devel
BuildRequires:	fontconfig-devel
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	tiff-devel
BuildRequires:  imagemagick

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
Obsoletes:	%{mklibname wraster 3 -d -s}

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
Provides:	%{mklibname WindowMaker %{WINGs_major}}
Obsoletes:	%{mklibname WindowMaker 0 -d}
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
