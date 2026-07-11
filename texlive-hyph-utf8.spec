%global tl_name hyph-utf8
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Hyphenation patterns expressed in UTF-8
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyph-utf8
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Modern native UTF-8 engines such as XeTeX and LuaTeX need hyphenation
patterns in UTF-8 format, whereas older systems require hyphenation
patterns in the 8-bit encoding of the font in use (such encodings are
codified in the LaTeX scheme with names like OT1, T2A, TS1, OML, LY1,
etc). The present package offers a collection of conversions of existing
patterns to UTF-8 format, together with converters for use with 8-bit
fonts in older systems. Since hyphenation patterns for Knuthian-style
TeX systems are only read at iniTeX time, it is hoped that the UTF-8
patterns, with their converters, will completely supplant the older
patterns.

