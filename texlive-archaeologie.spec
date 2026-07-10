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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This citation-style covers the citation and bibliography rules of the
German Archaeological Institute (DAI). Various options are available to
change and adjust the outcome according to one's own preferences.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bib
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bib/archaeologie
%dir %{_datadir}/texmf-dist/doc/latex/archaeologie
%dir %{_datadir}/texmf-dist/source/latex/archaeologie
%dir %{_datadir}/texmf-dist/tex/latex/archaeologie
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-bibancient.bib
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-bibcorpora.bib
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-examples.bib
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-lstabbrv.bib
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-lstlocations.bib
%{_datadir}/texmf-dist/bibtex/bib/archaeologie/archaeologie-lstpublishers.bib
%doc %{_datadir}/texmf-dist/doc/latex/archaeologie/README.md
%doc %{_datadir}/texmf-dist/doc/latex/archaeologie/archaeologie.pdf
%doc %{_datadir}/texmf-dist/source/latex/archaeologie/Makefile
%doc %{_datadir}/texmf-dist/source/latex/archaeologie/archaeologie.dtx
%{_datadir}/texmf-dist/tex/latex/archaeologie/archaeologie.bbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/archaeologie.cbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/archaeologie.dbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/english-archaeologie.lbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/french-archaeologie.lbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/german-archaeologie.lbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/italian-archaeologie.lbx
%{_datadir}/texmf-dist/tex/latex/archaeologie/spanish-archaeologie.lbx
