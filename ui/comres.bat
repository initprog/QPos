@echo off

rem ----------------------------------------------------
rem compile qrc resource file into py
rem ----------------------------------------------------

rem input file required
IF "%1"=="" (
  echo syntax: comres input-file[.qrc]
  exit /b 1
)

rem if input file has no extension then append .qrc into it
IF "%~x1"=="" set infile=%1.qrc

set infolder=c:\dev\ws-py\QPos\qpos\asset
set outfolder=%infolder%
set outfile=%~n1_rc.py

rem -x parameter generate extra code to test and display the class
C:\dev\qtdesigner\.venv\Lib\site-packages\qt6_applications\Qt\bin\rcc -g python %infolder%\%infile% -o %outfolder%\%outfile%
