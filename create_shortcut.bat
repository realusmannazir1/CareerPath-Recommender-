@echo off
REM Create shortcut to run the app
REM This script creates a Windows shortcut that launches the app

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\CareerPath Recommender.lnk'); $Shortcut.TargetPath = 'D:\UET\3rd Semester\Introduction to Data Science\Project\CareerPath_Recommender\run_app.bat'; $Shortcut.WorkingDirectory = 'D:\UET\3rd Semester\Introduction to Data Science\Project\CareerPath_Recommender'; $Shortcut.IconLocation = 'C:\Windows\System32\cmd.exe'; $Shortcut.Save()"

echo Shortcut created on Desktop: "CareerPath Recommender.lnk"
pause
