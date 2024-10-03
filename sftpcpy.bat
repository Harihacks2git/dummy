@echo off
setlocal enabledelayedexpansion

set ip=192.168.1.200

:: Define the IDs you want to skip
set skip_ids=2022103038 2022103040 2022103045

for /l %%i in (2022103031, 1, 2022103044) do (
    :: Check if current ID is in the skip list
    set skip=0
    for %%s in (%skip_ids%) do (
        if %%i==%%s (
            echo Skipping %%i...
            set skip=1
        )
    )

    :: If skip is set to 1, skip the current ID
    if !skip! equ 1 (
        continue
    )

    echo Trying s%%i@%ip% ...
    
    :: Create the SFTP batch command file
    echo mkdir cp_try > sftp_script.txt
    echo put -r wk09 cw9 >> sftp_script.txt
    echo bye >> sftp_script.txt

    :: Execute the SFTP command with the batch file
    sftp -b sftp_script.txt s%%i@%ip%

    :: Check if SFTP succeeded
    if %errorlevel% equ 0 (
        echo Copied to %%i successfully!
    ) else (
        echo Failed to copy to %%i.
    )

    del sftp_script.txt
)

endlocal
