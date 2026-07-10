%global tl_name archaeologie
%global tl_revision 79585

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5.1
Release:	%{tl_revision}.1
Summary:	A citation-style which covers rules of the German Archaeological Institute
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/archaeologie
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archaeologie.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This citation-style covers the citation and bibliography rules of the
German Archaeological Institute (DAI). Various options are available to
change and adjust the outcome according to one's own preferences.

