Summary:	Background browser and setter for X
Name:		nitrogen
Version:	1.5.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://projects.l3ib.org/nitrogen/files/%{name}-%{version}.tar.gz
# Source0-md5:	dd779a252a222eb9d329d74b809cfe73
Patch0:		%{name}-libs.patch
URL:		http://projects.l3ib.org/nitrogen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gdk-pixbuf-rsvg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nitrogen is a background browser and setter for X windows.

%prep
%setup -q

# /usr/bin/ld: SetBG.o: undefined reference to symbol 'XFreeStringList'
# /usr/bin/ld: note: 'XFreeStringList' is defined in DSO /usr/lib64/libX11.so.6 so try adding it to the linker command line
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nitrogen
%{_iconsdir}/hicolor/*/apps/nitrogen.png
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/devices/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.png
%{_mandir}/man1/nitrogen.1*

