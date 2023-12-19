# Simple POS(Point-Of-Sale) Program

- A simple POS system written in Python with PyQt-based user interface and SQLite database.
- Fork from [PyQt POS System](https://github.com/copolio/PyQt-POS-System)

## Development Environment
- Python 3.12
- PyQt6
- [Qt Designer](#qt-designer-tips)
- Visual Studio Code

**For developers**
1. Create a virtual environment
```
py -m venv .venv
```
2. Activate the virtual environment
```
.venv\Scripts\activate
```
3. Install required packages
```
pip install -r requirements.txt
```
4. Run Visual Studio Code
```
code .
```
5. To run the application from command window
```
py -m qpos
```

## Qt Designer Tips
Qt Designer is on `pyqt-tools` package, separate from `pyqt6` package.
As of writing, `pyqt-tools` only support Python v3.9. Therefore if you plan to use different version of Python
than v3.9 you need to install multiple versions.

Create a link to `.venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe` and place it on your Desktop
to bring up the Designer window.

### Convert designer file (.ui) into .py
```
.venv\scripts\pyuic6 -x input-file -o output-file
```
When using resource file with the Designer, you need to append an import statement for the resource file in the 
generated file.
For example:
```
from qpos.asset import resource_rc
```

### Compile resource file (.qrc) to .py
Use `rcc.exe` that is bundled with Qt Designer to compile the file.
* Make sure to use **-g python** parameter
* Update the generated file and replace import **PySide** to **PyQt6**
  
```
.venv\Lib\site-packages\qt6_applications\Qt\bin\rcc -g python [qrc-file] -o output-file
```

## Introduction

![소프트웨어공학 2조 최종 발표_3](https://user-images.githubusercontent.com/55977034/96537162-95c2c800-12d0-11eb-874f-92e39723f541.jpg)
![소프트웨어공학 2조 최종 발표_6](https://user-images.githubusercontent.com/55977034/96537172-978c8b80-12d0-11eb-9654-9742604773de.jpg)

## Screenshots

![소프트웨어공학 2조 최종 발표_7](https://user-images.githubusercontent.com/55977034/96537258-c440a300-12d0-11eb-8455-5c5a08c69a31.jpg)

### - Login Form

![Login form](/qpos/asset/doc/login.jpg)

### - Basic UI

![basic_ui](https://user-images.githubusercontent.com/55977034/96537447-40d38180-12d1-11eb-9af3-e584d1fb965c.png)

### - Select Menu

![menu_choose](https://user-images.githubusercontent.com/55977034/96537495-5d6fb980-12d1-11eb-9381-79aba1157283.png)

### - Payment Method

![purchasemode](https://user-images.githubusercontent.com/55977034/96537537-74aea700-12d1-11eb-9e07-df382558af14.png)

### - Payment

![purchase](https://user-images.githubusercontent.com/55977034/96537575-9019b200-12d1-11eb-8011-3c9c5b6afcae.png)

### - Complete Payment

![puchase_complete](https://user-images.githubusercontent.com/55977034/96537613-a7589f80-12d1-11eb-94f3-ffa23d53e3c8.png)


## Self Evaluation

![소프트웨어공학 2조 최종 발표_9](https://user-images.githubusercontent.com/55977034/96537174-98252200-12d0-11eb-9bbe-60438f43c5b8.jpg)
![소프트웨어공학 2조 최종 발표_10](https://user-images.githubusercontent.com/55977034/96537177-98bdb880-12d0-11eb-8010-849ad4191409.jpg)
![소프트웨어공학 2조 최종 발표_11](https://user-images.githubusercontent.com/55977034/96537178-98bdb880-12d0-11eb-960b-42acbbf10d0d.jpg)
![소프트웨어공학 2조 최종 발표_12](https://user-images.githubusercontent.com/55977034/96537180-99564f00-12d0-11eb-8e84-757d447fc85d.jpg)
![소프트웨어공학 2조 최종 발표_13](https://user-images.githubusercontent.com/55977034/96537181-99564f00-12d0-11eb-8ded-64b1b70cffb1.jpg)
![소프트웨어공학 2조 최종 발표_14](https://user-images.githubusercontent.com/55977034/96537261-c4d93980-12d0-11eb-9e87-c6af554ad3b5.jpg)
![소프트웨어공학 2조 최종 발표_15](https://user-images.githubusercontent.com/55977034/96537182-99eee580-12d0-11eb-9465-8bfeef78d78e.jpg)
![소프트웨어공학 2조 최종 발표_16](https://user-images.githubusercontent.com/55977034/96537184-99eee580-12d0-11eb-9c45-0eb4e753c054.jpg)
![소프트웨어공학 2조 최종 발표_17](https://user-images.githubusercontent.com/55977034/96537185-9a877c00-12d0-11eb-9b94-a0ac06983dec.jpg)
