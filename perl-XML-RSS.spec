Name:           perl-XML-RSS
Version:        1.45
Release:        2%{?dist}
Summary:        Perl module for managing RDF Site Summary (RSS) files

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/XML-RSS/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/XML-RSS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::Manifest)
BuildRequires:  perl(Test::Pod), perl(Test::More)
BuildRequires:	perl(HTML::Entities)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.


%prep
%setup -q -n XML-RSS-%{version}
chmod 644 Changes README TODO
find examples -type f -exec chmod 644 {} ';'
find examples -type d -exec chmod 755 {} ';'


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README TODO examples
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::RSS.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.45-2
- rebuild against perl 5.10.1

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.45-1
- update to 1.45

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-1
- update to 1.44

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.43-1
- update to 1.43

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.31-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.31-2
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.31-1
- bump to 1.31
- license tag fix

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-1
- bump to 1.22
- add new BR for building and testing

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10-2
- bump for FC-6

* Mon Mar 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.10-1
- 1.10.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.05-2
- rebuilt

* Sat Aug 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.05-0.fdr.1
- Update to 1.05, patches applied upstream.

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.04-0.fdr.2
- Bring up to date with current fedora.us Perl spec template.

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.04-0.fdr.1
- Update to 1.04.
- Reduce directory ownership bloat.

* Fri Nov 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.02-0.fdr.2
- Eliminate some spurious test warnings.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.02-0.fdr.1
- First build.
