@echo off
rem ---------------------------------------------------------
rem convert .ui to .py
rem output filename will be the same but with .py extension.
rem ---------------------------------------------------------

set infolder=c:\dev\ws-py\QPos\ui
set outfolder=c:\dev\ws-py\QPos\qpos\view
set pyuicpath=c:\dev\qtdesigner\.venv\scripts

rem input file required
IF "%1"=="" (
  echo syntax: convert input-file
  exit /b 1
)

rem if input file has no extension then append .ui into it
IF "%~x1"=="" set infile=%1.ui

set outfile=%~n1_ui.py
rem -x parameter generate extra code to test and display the class
%pyuicpath%\pyuic6 -x %infolder%\%infile% -o %outfolder%\%outfile%

rem if input file uses/references resource icon/image
py findreplace.py null null %outfolder%\%outfile%
