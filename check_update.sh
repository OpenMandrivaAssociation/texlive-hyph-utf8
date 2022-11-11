#!/bin/sh
curl -L http://mirrors.ctan.org/systems/texlive/tlnet/archive/ 2>/dev/null |grep -E hyph-utf8.r[0-9]*\.tar |sed -e 's,.*hyph-utf8\.r,,;s,\.tar.*,,' |sort -V |tail -n1
