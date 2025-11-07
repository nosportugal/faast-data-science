# VSCode Portable Setup Guide

This guide explains how to set up a portable version of VSCode 1.85.2 alongside your current VSCode installation. This is necessary for users who need to maintain connectivity to on-prem infrastructure that requires an older VSCode version.

## Why VSCode Portable?

Some on-prem infrastructure requires specific VSCode versions that are not compatible with the latest GitHub Copilot extensions. A portable installation allows you to:

- Keep your current VSCode setup intact
- Run an older VSCode version when needed for on-prem work
- Use both versions side-by-side without conflicts

## Setup Instructions

### 1. Download VSCode Portable

Download VSCode version 1.85.2 portable from the [official VSCode download page](https://code.visualstudio.com/updates/v1_85).

### 2. Extract the ZIP file

Extract the downloaded ZIP file to your preferred location. For example:
- `C:\Users\<your-username>\VSCode 1.85.2`
- `D:\Tools\VSCode-Portable`

### 3. Create the data folder

Inside the extracted folder, create a new folder called `data`. This makes VSCode run in portable mode.

Example path: `C:\Users\<your-username>\VSCode 1.85.2\data`

### 4. Transfer your extensions (optional)

If you want to use your existing VSCode extensions in the portable version:

1. Copy your extensions folder from your current VSCode installation:
   - Default location: `C:\Users\<your-username>\.vscode\extensions`
2. Paste it into the portable `data` folder:
   - Example: `C:\Users\<your-username>\VSCode 1.85.2\data\extensions`

### 5. Transfer your settings (optional)

If you want to use your current VSCode settings:

1. **First**, launch the portable VSCode at least once (this creates the necessary folder structure)
2. Copy your `settings.json` file from:
   - `%appdata%\Code\User\settings.json`
3. Paste it into:
   - `<portable-folder>\data\user-data\User\settings.json`

You can also copy `keybindings.json` if you have custom keyboard shortcuts.

### 6. Create a shortcut

Create a desktop or taskbar shortcut to the portable VSCode executable (`Code.exe`) and give it a distinctive name like "VSCode 1.85.2 Portable" to distinguish it from your regular VSCode installation.

### 7. Update your regular VSCode

You can now safely update your regular VSCode installation to the latest version without affecting your portable setup.

## Verifying the setup

1. Launch the portable VSCode using your shortcut
2. Open the Command Palette (Ctrl+Shift+P)
3. Type "About" and verify you're running version 1.85.2
4. Check that your extensions and settings are loaded correctly

## Installing GitHub Copilot

Once your portable VSCode is set up:

1. Open the Extensions view (Ctrl+Shift+X)
2. Search for "GitHub Copilot"
3. Install the compatible version for VSCode 1.85.2
4. Sign in with your GitHub account
5. Verify Copilot is working by opening a Python file and typing a comment

## Troubleshooting

**Extensions not showing up:**
- Verify the `data\extensions` folder exists and contains your extension folders

**Settings not applied:**
- Make sure you launched the portable VSCode at least once before copying settings
- Check that `settings.json` is in `data\user-data\User\`

**Can't find the portable VSCode:**
- Create a shortcut with a clear name to avoid confusion with your regular installation

**GitHub Copilot not working:**
- Ensure you're signed in with your GitHub account
- Check that your Copilot subscription is active
- Try restarting VSCode

## Need help?

If you encounter issues during setup, reach out to your mentor or check the progress tracking sheet for similar questions from other students.
