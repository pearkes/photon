Summary:	Build tool
Name:		pkg-config
Version:	0.28
Release:	1
License:	GPLv2+
URL:		http://www.freedesktop.org/wiki/Software/pkg-config
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: Photon
Source0:		http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
%description
Contains a tool for passing the include path and/or library paths
to build tools during the configure and make file execution.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--with-internal-glib \
	--disable-host-tool \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_bindir}/pkg-config
%{_datadir}/aclocal/pkg.m4
%{_docdir}/pkg-config-0.28/pkg-config-guide.html
%{_mandir}/man1/pkg-config.1.gz
%changelog
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 0.28-1
-	Initial build. First version
