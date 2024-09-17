@echo off
echo Hello... I see you're here to install python. I'll let you continue.
@echo.
@echo.
@echo But first let's make sure you CAN install python.
powershell -Command "$progressPreference = 'silentlyContinue'; $latestWingetMsixBundleUri = $(Invoke-RestMethod https://api.github.com/repos/microsoft/winget-cli/releases/latest).assets.browser_download_url | Where-Object {$_.EndsWith('.msixbundle')}; $latestWingetMsixBundle = $latestWingetMsixBundleUri.Split('/')[-1]; Write-Output 'Downloading $latestWingetMsixBundle...'; Invoke-WebRequest -Uri $latestWingetMsixBundleUri -OutFile $latestWingetMsixBundle; Add-AppxPackage -Path $latestWingetMsixBundle"



cd %userprofile%\AppData\Local\Microsoft\WindowsApps
winget install -e --id Python.Python.3.11 --accept-source-agreements --accept-package-agreements

start Solara.py
