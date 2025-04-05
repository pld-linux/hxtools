Summary:	Collection of day-to-day tools
Summary(pl.UTF-8):	Zbiór narzędzi codziennego użytku
Name:		hxtools
Version:	20250309
Release:	1
License:	MIT, BSD, LGPL v2.1+, GPL v2+
Group:		Applications
Source0:	https://inai.de/files/hxtools/%{name}-%{version}.tar.zst
# Source0-md5:	a442cbcb481ff34425aaf904ebfc169a
URL:		https://inai.de/projects/hxtools/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libHX-devel >= 3.17
BuildRequires:	libmount-devel >= 2.19
# -std=gnu++17
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxcb-devel >= 1
BuildRequires:	pciutils-devel >= 3
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.31
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	zstd
Requires:	libHX >= 3.17
Obsoletes:	hxtools-data
Obsoletes:	hxtools-noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and scripts that have accumulated over the
years, and each of which seems to be too small to warrants its own
project.

%description -l pl.UTF-8
Zbiór narzędzi i skryptów, które nazbierały się w ciągu lat, a każde
jest za małe, aby zasługiwał na własny projekt.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_datadir}/%{name} \
	--disable-silent-rules \
	--with-kbddatadir=/lib/kbd \
	--with-x11fontdir=%{_datadir}/fonts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# tools removed before release
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/extract_f3pod.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/xfs_irecover.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.MIT LICENSES.txt NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/aumeta
%attr(755,root,root) %{_bindir}/bin2c
%attr(755,root,root) %{_bindir}/bsvplay
%attr(755,root,root) %{_bindir}/checkbrack
%attr(755,root,root) %{_bindir}/cwdiff
%attr(755,root,root) %{_bindir}/declone
%attr(755,root,root) %{_bindir}/extract_d3pkg
%{_bindir}/extract_dfqshared.pm
%attr(755,root,root) %{_bindir}/extract_dxhog
%attr(755,root,root) %{_bindir}/extract_qupak
%attr(755,root,root) %{_bindir}/fxterm
%attr(755,root,root) %{_bindir}/gh-trim-workflowruns
%attr(755,root,root) %{_bindir}/git-author-stat
%attr(755,root,root) %{_bindir}/git-blame-stats
%attr(755,root,root) %{_bindir}/git-forest
%attr(755,root,root) %{_bindir}/git-logsortbychgsize
%attr(755,root,root) %{_bindir}/git-revert-stats
%attr(755,root,root) %{_bindir}/git-track
%attr(755,root,root) %{_bindir}/gpsh
%attr(755,root,root) %{_bindir}/gxxdm
%attr(755,root,root) %{_bindir}/hcdplay
%attr(755,root,root) %{_bindir}/make_qupak
%attr(755,root,root) %{_bindir}/man2html
%attr(755,root,root) %{_bindir}/mkvappend
%attr(755,root,root) %{_bindir}/mod2opus
%attr(755,root,root) %{_bindir}/ofl
%attr(755,root,root) %{_bindir}/pcmdiff
%attr(755,root,root) %{_bindir}/pcmmix
%attr(755,root,root) %{_bindir}/pegrep
%attr(755,root,root) %{_bindir}/pesubst
%attr(755,root,root) %{_bindir}/pmap_dirty
%attr(755,root,root) %{_bindir}/proc_iomem_count
%attr(755,root,root) %{_bindir}/proc_stat_parse
%attr(755,root,root) %{_bindir}/qpdecode
%attr(755,root,root) %{_bindir}/qplay
%attr(755,root,root) %{_bindir}/qtar
%attr(755,root,root) %{_bindir}/rot13
%attr(755,root,root) %{_bindir}/selective-preprocess
%attr(755,root,root) %{_bindir}/spec-beautifier
%attr(755,root,root) %{_bindir}/ssa2srt
%attr(755,root,root) %{_bindir}/su1
%attr(755,root,root) %{_bindir}/sysinfo
%attr(755,root,root) %{_bindir}/tailhex
%attr(755,root,root) %{_bindir}/wktimer
%attr(755,root,root) %{_bindir}/xcp
%attr(755,root,root) %{_bindir}/xmlformat
%dir %{_libexecdir}/hxtools
%attr(755,root,root) %{_libexecdir}/hxtools/clock_info
%attr(755,root,root) %{_libexecdir}/hxtools/diff2php
%attr(755,root,root) %{_libexecdir}/hxtools/doxygen-kerneldoc-filter
%attr(755,root,root) %{_libexecdir}/hxtools/fd0ssh
%attr(755,root,root) %{_libexecdir}/hxtools/hxnetload
%attr(755,root,root) %{_libexecdir}/hxtools/ldif-duplicate-attrs
%attr(755,root,root) %{_libexecdir}/hxtools/ldif-leading-spaces
%attr(755,root,root) %{_libexecdir}/hxtools/logontime
%attr(755,root,root) %{_libexecdir}/hxtools/mailsplit
%attr(755,root,root) %{_libexecdir}/hxtools/paddrspacesize
%attr(755,root,root) %{_libexecdir}/hxtools/peicon
%attr(755,root,root) %{_libexecdir}/hxtools/proc_stat_signal_decode
%attr(755,root,root) %{_libexecdir}/hxtools/psthreads
%attr(755,root,root) %{_libexecdir}/hxtools/recursive_lower
%attr(755,root,root) %{_libexecdir}/hxtools/rezip
%attr(755,root,root) %{_libexecdir}/hxtools/sourcefuncsize
%attr(755,root,root) %{_libexecdir}/hxtools/vcsaview
%{_datadir}/hxtools
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hxloginpref.conf
%{_mandir}/man1/aumeta.1*
%{_mandir}/man1/bin2c.1*
%{_mandir}/man1/bsvplay.1*
%{_mandir}/man1/checkbrack.1*
%{_mandir}/man1/clock_info.1*
%{_mandir}/man1/cwdiff.1*
%{_mandir}/man1/declone.1*
%{_mandir}/man1/diff2php.1*
%{_mandir}/man1/extract_d3pkg.1*
%{_mandir}/man1/extract_dxhog.1*
%{_mandir}/man1/extract_qupak.1*
%{_mandir}/man1/fd0ssh.1*
%{_mandir}/man1/fxterm.1*
%{_mandir}/man1/git-author-stat.1*
%{_mandir}/man1/git-forest.1*
%{_mandir}/man1/git-revert-stats.1*
%{_mandir}/man1/git-track.1*
%{_mandir}/man1/gpsh.1*
%{_mandir}/man1/hcdplay.1*
%{_mandir}/man1/ldif-duplicate-attrs.1*
%{_mandir}/man1/mailsplit.1*
%{_mandir}/man1/man2html.1*
%{_mandir}/man1/mod2opus.1*
%{_mandir}/man1/ofl.1*
%{_mandir}/man1/pcmdiff.1*
%{_mandir}/man1/pcmmix.1*
%{_mandir}/man1/pegrep.1*
%{_mandir}/man1/peicon.1*
%{_mandir}/man1/pesubst.1*
%{_mandir}/man1/psthreads.1*
%{_mandir}/man1/qplay.1*
%{_mandir}/man1/qtar.1*
%{_mandir}/man1/recursive_lower.1*
%{_mandir}/man1/rezip.1*
%{_mandir}/man1/rot13.1*
%{_mandir}/man1/sourcefuncsize.1*
%{_mandir}/man1/spec-beautifier.1*
%{_mandir}/man1/ssa2srt.1*
%{_mandir}/man1/sysinfo.1*
%{_mandir}/man1/tailhex.1*
%{_mandir}/man1/wktimer.1*
%{_mandir}/man1/xcp.1*
%{_mandir}/man7/hxtools.7*
%{_mandir}/man8/hxnetload.8*
%{_mandir}/man8/logontime.8*
%{_mandir}/man8/vcsaview.8*

#%files kbd?
/lib/kbd/consolefonts/A1.fnt
/lib/kbd/consolefonts/B1.fnt
/lib/kbd/consolefonts/E1.fnt
/lib/kbd/consolefonts/neuropol.fnt
/lib/kbd/consolefonts/uefi.psf
/lib/kbd/keymaps/i386/qwerty/us_jng.map
/lib/kbd/keymaps/i386/qwerty/us_jng_vaiou3.map
/lib/kbd/keymaps/i386/qwertz/de_jng.map
/lib/kbd/unimaps/cp437AB.uni
/lib/kbd/unimaps/cp437x.uni
