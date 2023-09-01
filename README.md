# Requirements

Windows 10. Other Windows versions might work but have not been tested against.

Tesseract windows binary. Can be found at https://github.com/UB-Mannheim/tesseract/wiki

Built using version w64 5.3.0 but later versions should work.

# Installation

## Downloading the prepackaged binary

Head over to [releases](https://github.com/natsukashiixo/OCRAutomation/releases/tag/binary), download the .zip and extract it. Install the Tesseract binary and then launch OCRAutomation.exe

The archive contains a manual in Swedish. Feel free to run it through a translation service.

## Building your own binary

Install git using Winget in your terminal.

`winget install -e --id Git.Git`

Clone the repo.

`git clone https://github.com/natsukashiixo/OCRAutomation.git`

Change directory to the repo.

`cd OCRAutomation`

Set up a Python virtual environment. Python 3.10.6 is recommended. Because of Pythons various ways to set this up, I recommend researching how to do it yourself if you don't already know how to do it.

Once done, activate your environment.

Install prerequisites using pip.

`pip install -r requirements.txt`

Change directory to app/src.

`cd app/src`

Build using pyinstaller and the preconfigured build_specs.spec file. Replace the `./build` with the folder where you want the .exe file to end up. Its recommended to not build in the same folder as this repository.

`pyinstaller --noconfirm --clean --log-level DEBUG --distpath ./build build_specs.spec`

Copy the `app/assets` folder and its contents into the same folder you built to. For instance, if you built to `./build` the final folder structure should be `./build/app/assets`

Install the Windows Tesseract binary.

Launch OCRAutomation.exe, on first startup it might take a while because it needs to set up the expected folder structure.

# Worth noting:

This project is hardcoded to use the best swedish language model combined with latin script data. If you need to change this you have to edit `app/src/modules/run_tesseract.py`

This project won't be maintained, it was built for one specific purpose at a workplace. Feel free to fork it for whatever reason though!

This is my first project ever, when I started I didn't know how to print `hello world` in any language. It may be inflexible, inefficient and slow. But it is my firstborn and therefore I think it is beautiful. 
