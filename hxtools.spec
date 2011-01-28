Summary:	Collection of day-to-day tools
Name:		hxtools
Version:	20100625
Release:	0.1
License:	GPL, Public Domain
Group:		Base
Source0:	http://jengelh.medozas.de/files/hxtools/%{name}-%{version}.tar.xz
# Source0-md5:	cd505cb8b83f170fc8c5614bc363302a
Patch0:		dl-libs.patch
URL:		http://jengelh.medozas.de/projects/hxtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libHX-devel >= 3.4
BuildRequires:	libcap-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xz
Obsoletes:	hxtools-data
Obsoletes:	hxtools-noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A big tool collection.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_datadir}/%{name} \
	--with-keymapdir=/lib/kbd/keymaps \
	--with-vgafontdir=/lib/kbd/consolefonts \
	--with-x11fontdir=%{_datadir}/fonts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	pkglibexecdir=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

# identical bins
ln -f $RPM_BUILD_ROOT%{_bindir}/{oplay,omixer}
ln -f $RPM_BUILD_ROOT%{_bindir}/{oplay,orec}

# don't know actually what to package, so drop all
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

# kbd keymaps and consolefonts
rm -rfv $RPM_BUILD_ROOT/lib/kbd

# fonts
rm -rf $RPM_BUILD_ROOT%{_datadir}/fonts/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/bsvplay
%attr(755,root,root) %{_bindir}/cctypeinfo
%attr(755,root,root) %{_bindir}/checkbrack
%attr(755,root,root) %{_bindir}/cwdiff
%attr(755,root,root) %{_bindir}/declone
%attr(755,root,root) %{_bindir}/diff2php
%attr(755,root,root) %{_bindir}/doxygen-kerneldoc-filter
%attr(755,root,root) %{_bindir}/extract_d3pkg
%attr(755,root,root) %{_bindir}/extract_dxhog
%attr(755,root,root) %{_bindir}/extract_f3pod
%attr(755,root,root) %{_bindir}/extract_qupak
%attr(755,root,root) %{_bindir}/fd0ssh
%attr(755,root,root) %{_bindir}/fduphl
%attr(755,root,root) %{_bindir}/filenameconv
%attr(755,root,root) %{_bindir}/flv2avi
%attr(755,root,root) %{_bindir}/flv2mka
%attr(755,root,root) %{_bindir}/fnt2bdf
%attr(755,root,root) %{_bindir}/fxterm
%attr(755,root,root) %{_bindir}/git-author-stat
%attr(755,root,root) %{_bindir}/git-blame-stats
%attr(755,root,root) %{_bindir}/git-export-patch
%attr(755,root,root) %{_bindir}/git-forest
%attr(755,root,root) %{_bindir}/git-lemon
%attr(755,root,root) %{_bindir}/git-new-root
%attr(755,root,root) %{_bindir}/git-revert-stats
%attr(755,root,root) %{_bindir}/git-track
%attr(755,root,root) %{_bindir}/graph-fanout
%attr(755,root,root) %{_bindir}/graph-lchain
%attr(755,root,root) %{_bindir}/htruncate
%attr(755,root,root) %{_bindir}/kps
%attr(755,root,root) %{_bindir}/logontime
%attr(755,root,root) %{_bindir}/mailsplit
%attr(755,root,root) %{_bindir}/man2html
%attr(755,root,root) %{_bindir}/mod2ogg
%attr(755,root,root) %{_bindir}/mpg2ogg
%attr(755,root,root) %{_bindir}/mpl
%attr(755,root,root) %{_bindir}/netload
%attr(755,root,root) %{_bindir}/newns
%attr(755,root,root) %{_bindir}/ofl
%attr(755,root,root) %{_bindir}/omixer
%attr(755,root,root) %{_bindir}/oplay
%attr(755,root,root) %{_bindir}/orec
%attr(755,root,root) %{_bindir}/paddrspacesize
%attr(755,root,root) %{_bindir}/pesubst
%attr(755,root,root) %{_bindir}/pmap_dirty
%attr(755,root,root) %{_bindir}/png2wx.pl
%attr(755,root,root) %{_bindir}/printcaps
%attr(755,root,root) %{_bindir}/proc_iomem_count
%attr(755,root,root) %{_bindir}/proc_stat_signal_decode
%attr(755,root,root) %{_bindir}/qplay
%attr(755,root,root) %{_bindir}/qtar
%attr(755,root,root) %{_bindir}/raregetty
%attr(755,root,root) %{_bindir}/recursive_lower
%attr(755,root,root) %{_bindir}/rpmdep.pl
%attr(755,root,root) %{_bindir}/sourcefuncsize
%attr(755,root,root) %{_bindir}/stxdb
%attr(755,root,root) %{_bindir}/su1
%attr(755,root,root) %{_bindir}/sysinfo
%attr(755,root,root) %{_bindir}/tailhex
%attr(755,root,root) %{_bindir}/testdl
%attr(755,root,root) %{_bindir}/utmp_register
%attr(755,root,root) %{_bindir}/vcsaview
%attr(755,root,root) %{_bindir}/vfontas
%attr(755,root,root) %{_bindir}/wavdiff
%attr(755,root,root) %{_bindir}/wktimer
%attr(755,root,root) %{_bindir}/xcp
%attr(755,root,root) %{_bindir}/xfs_irecover
%{_mandir}/man[178]/*.*
