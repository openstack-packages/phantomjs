Name:           phantomjs
Version:        1.9.7
Release:        1%{?dist}
Summary:        Scriptable Headless WebKit

License:        BSD
URL:            http://phantomjs.org/
Source0:        https://github.com/ariya/phantomjs/archive/1.9.7/phantomjs-1.9.7.tar.gz

BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  ruby
BuildRequires:  openssl-devel
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libicu-devel
BuildRequires:  sqlite-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

%description
PhantomJS is a headless WebKit scriptable with a JavaScript API. It has fast and
native support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG.

%prep
%setup -q


%build
./build.sh --confirm --jobs 4

%install
mkdir -p %{buildroot}%{_bindir}
cp bin/phantomjs %{buildroot}%{_bindir}
chrpath -d %{buildroot}%{_bindir}/phantomjs


%files
%attr(755, root, root) %{_bindir}/phantomjs


%changelog
* Wed Jul 29 2015 Graeme Gillies <ggillies@redhat.com - 1.9.7-1
- Initial Packaging
