@echo off
setlocal

:: Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed. Installing Git...
    :: Install Git
    choco install git -y
    if %errorlevel% neq 0 (
        echo Error: Failed to install Git.
        exit /b 1
    )
)

:: Clone or update the repository
set repository_url=https://github.com/vortexsys/artemis.git
set target_folder=artemis

if not exist %target_folder% (
    echo Cloning the repository...
    git clone %repository_url% %target_folder%
    if %errorlevel% neq 0 (
        echo Error: Failed to clone the repository.
        exit /b 1
    )
) else (
    echo Updating the repository...
    cd %target_folder%
    :: Clean everything in the folder except update_project.bat
    for /f %%i in ('dir /b ^| find /v /i "update_project.bat"') do (
        rd /s /q "%%i" 2>nul
        del /q "%%i" 2>nul
    )
    git pull
    if %errorlevel% neq 0 (
        echo Error: Failed to update the repository.
        exit /b 1
    )
    cd ..
)

echo Repository has been updated successfully.
exit /b 0
