#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen

Summary:	A C++ binding of GtkSourceView2
Summary(pl.UTF-8):	Wiązania C++ dla GtkSourceView2
Name:		gtksourceviewmm2
Version:	2.10.3
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtksourceviewmm/2.10/gtksourceviewmm-%{version}.tar.xz
# Source0-md5:	89d75c441ceeb071943acad1fe48d973
URL:		http://www.gnome.org/projects/gtksourceviewmm/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gtkmm-devel >= 2.12.1
BuildRequires:	gtksourceview2-devel >= 2.10.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtkmm >= 2.12.1
Requires:	gtksourceview2 >= 2.10.0
Obsoletes:	libgtksourceviewmm2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceViewMM2 is a C++ binding of GtkSourceView2, an extension to
the text widget included in GTK+ 2.x adding syntax highlighting and
other features typical for a source file editor.

%description -l pl.UTF-8
GtkSourceViewMM2 to wiązania C++ dla GtkSourceView2 - rozszerzenia
tekstowego widgetu będącego częścią GTK+ 2.x, dodającego kolorowanie
składni oraz inne właściwości typowe dla edytora kodu źródłowego.

%package devel
Summary:	Header files for GtkSourceViewMM2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GtkSourceViewMM2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.12.1
Requires:	gtksourceview2-devel >= 2.10.0
Obsoletes:	libgtksourceviewmm2-devel

%description devel
Header files for GtkSourceViewMM2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GtkSourceViewMM2.

%package static
Summary:	Static GtkSourceViewMM2 library
Summary(pl.UTF-8):	Statyczna biblioteka GtkSourceViewMM2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libgtksourceviewmm2-static

%description static
Static GtkSourceViewMM2 library.

%description static -l pl.UTF-8
Statyczna biblioteka GtkSourceViewMM2.

%package apidocs
Summary:	GtkSourceViewMM2 API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkSourceViewMM2
Group:		Documentation
Obsoletes:	libgtksourceviewmm2-apidocs
BuildArch:	noarch

%description apidocs
GtkSourceViewMM2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkSourceViewMM2.

%prep
%setup -q -n gtksourceviewmm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-documentation \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtksourceviewmm-2.0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-2.0.so
%{_libdir}/gtksourceviewmm-2.0
%{_includedir}/gtksourceviewmm-2.0
%{_pkgconfigdir}/gtksourceviewmm-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceviewmm-2.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/gtksourceviewmm-2.0
%{_docdir}/gtksourceviewmm-2.0
%endif
