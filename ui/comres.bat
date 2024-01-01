@echo off

rem ----------------------------------------------------
rem compile qrc resource file into py
rem Note: customize it for your own dev environment
rem ----------------------------------------------------

set infolder=c:\dev\ws-py\QPos\qpos\asset
set outfolder=%infolder%
set rccpath=C:\dev\qtdesigner\.venv\Lib\site-packages\qt6_applications\Qt\bin

IF "%DEVENV%" == "HOME" (
  set infolder=e:\dev\ws-py\QPos\qpos\asset
  set outfolder=e:\dev\ws-py\QPos\qpos\asset
  set rccpath=C:\dev\ws-py\design\.venv\Lib\site-packages\qt6_applications\Qt\bin
)

rem input file required
IF "%1"=="" (
  echo syntax: comres input-file[.qrc]
  exit /b 1
)

rem if input file has no extension then append .qrc into it
IF "%~x1"=="" (set infile=%1.qrc) ELSE (set infile=%1)

set outfile=%~n1_rc.py

rem -x parameter generate extra code to test and display the class
%rccpath%\rcc -g python %infolder%\%infile% -o %outfolder%\%outfile%

rem replace PySide6 with PyQt6
py findreplace.py PySide6 PyQt6 %outfolder%\%outfile%