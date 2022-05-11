@echo off

cls
if _%4_ equ __  goto :usage

setlocal

set patdir=%1
if _%1_ equ _._  set patdir=%cd%

set sluser=%3
if _%3_ equ _._  set sluser=%USERNAME%@snaplogic.com

:. python t:\tools\modpatcat.py %patdir% %2 %sluser% %4
:. python T:\tools\__pycache__\modpatcat.cpython-310.pyc %patdir% %2 %sluser% %4
python t:\tools\modpatcat.pyc %patdir% %2 "%sluser%" %4

endlocal
goto :eof

:usage
echo.
echo USAGE: %0 path/to/files stage/elastic/endpointUrl username password
