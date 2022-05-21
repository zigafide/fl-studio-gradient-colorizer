# fl-studio-gradient-colorizer
Python script that basically colorizes folders and files in FL Studio using NFO files.

![a](https://i.imgur.com/pHR1ExE.png)

# Setup
1. Download the zip from the releases section and extract it.
2. Open the "settings.txt" file
3. set the "drumkit_folder" variable to your desired folder to colorize
4. Right bewow that, you can cusotmize the colors that are used. The script will create a gradient between these colors.

-- You can also set different colors for files and folders if you want to.

-- Colors are in web format. To find the value of colors to use, go on google and type in "hex color picker", and copy the hex value into the settings file.

The last option is "ignore_sub_folders", which is default false.

If set to true, the script will not dig down into subdirectories. This is only useful if you are colorizing ALOT of folders/files.

For just a drumkit, leave this option as "false"
Make sure to save your changes to "settings.txt"

# Running the script
Now that you have your options sorted, you can now run the script.

Upon running the file, it will prompt you asking if your options are correct.

If they are, press enter and the colorizing will happen.

That should be all there is to it!



# Using as script instead of EXE file
Ignore this section unless you really wanna run the script instead of using the compiled EXE.

This script was written in python 3.10

This script requires the "colour" and "configparser" libraries.

If you have all this, you can run the script by typing "py main.py" in a CMD window.
