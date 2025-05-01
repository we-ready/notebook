---
id: 20250501_adidas_win11_install
title: Adidas Win11 Install & Setup
subtitle: PowerShell Scritp Automation
subject: DevOps
category: PowerShell Script
tags: 
keywords: PowerShell;Script
level: 200
cover: http://qiniuargus.weready.online/blog/desktop.jpg
authors: Chris Wei
created_when: 2025-05-01
updated_when: 2025-05-01
---

# Adidas Win11 OS Install & Setup

> USB Disk files

## Autorun.inf

> Autorun is forbidden in Win11

```
[AutoRun]
shellexecute=.\install.ps1
icon=ms_windows.ico
label=Win11 Setup
```

## install.ps1

```
$title    = 'Win11 Setup'
$question = 'Are you sure you want to proceed?'
$choices  = New-Object Collections.ObjectModel.Collection[Management.Automation.Host.ChoiceDescription]

$choices.Add((New-Object Management.Automation.Host.ChoiceDescription -ArgumentList '&Yes'))
$choices.Add((New-Object Management.Automation.Host.ChoiceDescription -ArgumentList '&No'))

$decision = $Host.UI.PromptForChoice($title, $question, $choices, 0)

if ($decision -eq 1) {

    Write-Host 'User abort!'
    Exit 0

}



Write-Host 'Processing ...'



# cmd.exe /c "printer.bat"
# cmd.exe /c "netdrive.bat"


Start-Process powershell.exe -ArgumentList "-File `"./fonts.ps1`""

# Get-ChildItem -Filter ./fonts/*.ttf | ForEach-Object { Add-Font $_ } 
# Get-ChildItem -Filter ./fonts/*.ttc | ForEach-Object { Add-Font $_ }
# Get-ChildItem -Filter ./fonts/*.otf | ForEach-Object { Add-Font $_ }
# Get-ChildItem -Filter ./fonts/*.fon | ForEach-Object { Add-Font $_ }


.\software\YoudaoDict_dict_web_banner.exe



Write-Host 'Done!'
Read-Host -Prompt "Press Enter to quit!"
```

## fonts.ps1

```
function Install-Font {
    param(
        [string]$fontPath
    )

    $shell = New-Object -ComObject Shell.Application
    $folder = $shell.Namespace(0x14)
    $folder.CopyHere($fontPath)
}

function Install-FontsInFolder {
    param(
        [string]$folderPath
    )

    Get-ChildItem -Path $folderPath -Recurse -File -Include *.ttf,*.ttc,*.fon,*.otf,*.woff,*.eot,*.woff2 | ForEach-Object {
        Install-Font -fontPath $_.FullName
    }
}

# Set the path to the folder containing the fonts
$fontFolderPath = "./fonts"

# Call the function to install the fonts
Install-FontsInFolder -folderPath $fontFolderPath

```

## netdrive.bat

```
%SystemRoot%\explorer "D:\"

REM net use O: "\\ap.adsint.biz\CN\Sales Office\ShangHai\Others"
REM net use S: "\\amznfsxhpqdx1pi.emea.adsint.biz\CNSHAAPFS10-Scan$"
```

## printer.bat

```
%SystemRoot%\explorer "D:\"

REM net use O: "\\ap.adsint.biz\CN\Sales Office\ShangHai\Others"
REM net use S: "\\amznfsxhpqdx1pi.emea.adsint.biz\CNSHAAPFS10-Scan$"
```
