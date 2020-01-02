cd ..
curr=$(pwd)
cp -r "$curr/Cinfo" /usr/share/
cp "$curr/Cinfo/Cinfo.desktop" /usr/share/applications/
echo "Cinfo Installed, Please Check Your Application Launcher"
