Name:		texlive-cprotectinside
Version:	63833
Release:	2
Summary:	Use cprotect arbitrarily nested
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cprotectinside
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotectinside.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cprotectinside.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends the cprotect package to allow users to use
verbatim-like commands inside arbitrary parameters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cprotectinside
%doc %{_texmfdistdir}/doc/latex/cprotectinside

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
