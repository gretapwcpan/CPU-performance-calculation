#pip install py-cpuinfo instead of cpuinfo
from cpuinfo import *
import psutil
import subprocess
import sys

#comment: only obtain high-level CPU specification

info = get_cpu_info()
print(info["hz_actual_friendly"])

#still returns the same value after several attempts

frequency = psutil.cpu_freq()
print(frequency)


#solutions: combine powershell and python to retrive the timely cpu data

p = subprocess.Popen(['powershell.exe', 'C:\\Users\\nxf33342\\Desktop\\runcpu.ps1'])
#stdout=sys.stdout.fileno() will cause UnsupportedOperation: fileno, so lets ps1 file output log
p.communicate()



# =============================================================================
# 
# def run(cmd):
#     completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
#     return completed
# 
# ps_command = '''$MaxClockSpeed = (Get-CimInstance CIM_Processor).MaxClockSpeed
# 
# While($true){
#     $ProcessorPerformance = (Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance").CounterSamples.CookedValue
#     $CurrentClockSpeed = $MaxClockSpeed*($ProcessorPerformance/100)
# 
#     Write-Host "Current Processor Speed: " -ForegroundColor Yellow -NoNewLine
#     Write-Host $CurrentClockSpeed
# 
#     Sleep -Seconds 2
# }'''
# ps_info = run(cmd = ps_command)
# if ps_info.returncode != 0:
#     print("An error occured: %s", ps_info.stderr)    
#     print("-------------------------")
#     
# bad_syntax_command = "Write-Hst 'Incorrect syntax command!'"
# bad_syntax_info = run(bad_syntax_command)
# if bad_syntax_info.returncode != 0:
#     print("An error occured: %s", bad_syntax_info.stderr)
# else:
#    print("Bad syntax command executed successfully!")
# =============================================================================
