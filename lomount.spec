Summary:	lomount - utility to mount partitions in a hard disk image
Name:		lomount
Version:	0
Release:	0.2
License:	BSD-like
Group:		Applications/System
Source0:	%{name}.c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to mount partitions in a hard disk image.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build
%{__cc} %{rpmcflags} -W -Wall -D_FILE_OFFSET_BITS=64 %{rpmldflags} lomount.c -o lomount

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install lomount $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/lomount
