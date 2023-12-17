@echo off
rem ---------------------------------------------------------
rem convert .ui to .py
rem output filename will be the same but with .py extension.
rem ---------------------------------------------------------

set outfolder=e:\dev\ws-py\QPos\qpos\ui

rem input file required
IF "%1"=="" GOTO noparam

rem if input file has no extension then append .ui into it
IF "%~x1"=="" set infile=%1.ui

set outfile=%~n1.py
rem -x parameter generate extra code to test and display the class
.venv\scripts\pyuic6 -x %infile% -o %outfolder%\%outfile%
goto end

:noparam
echo syntax: convert input-file

:end
