#!/bin/sh
py_module=wmaker
curl "https://github.com/window-maker/wmaker/releases/" 2>/dev/null |grep "tag/" |sed -e 's,.*>wmaker-,,;s,<.*,,;' |head -n1

