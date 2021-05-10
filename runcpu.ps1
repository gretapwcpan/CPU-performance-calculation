$results = @()
$MaxClockSpeed = (Get-CimInstance CIM_Processor).MaxClockSpeed
$ProcessorPerformance = (Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue
$CurrentClockSpeed = $MaxClockSpeed*($ProcessorPerformance/100)
Write-Host "Current Processor Speed: " -ForegroundColor Yellow -NoNewLine
While($true){
     $ProcessorPerformance = (Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue
     $CurrentClockSpeed = $MaxClockSpeed*($ProcessorPerformance/100)

     Write-Host "Current Processor Speed: " -ForegroundColor Yellow -NoNewLine
     Write-Host $CurrentClockSpeed
     $results += New-Object PSObject -Property $CurrentClockSpeed

     Sleep -Seconds 1
 }
$results | export-csv -Path c:\Users\nxf33342\Desktop\pycpu\so.csv -NoTypeInformation
