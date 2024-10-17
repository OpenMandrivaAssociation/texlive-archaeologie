Name:		texlive-archaeologie
Version:	68476
Release:	1
Summary:	A citation-style which covers rules of the German Archaeological Institute
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/archaeologie
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This citation-style covers the citation and bibliography rules
of the German Archaeological Institute (DAI). Various options
are available to change and adjust the outcome according to
one's own preferences.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/archaeologie
%{_texmfdistdir}/tex/latex/archaeologie
%{_texmfdistdir}/bibtex/bib/archaeologie
%doc %{_texmfdistdir}/doc/latex/archaeologie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
