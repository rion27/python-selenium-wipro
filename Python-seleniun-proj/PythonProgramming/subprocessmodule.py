#subprocess module-
#execute external system commands
#interact with os processes
#capture output, error and return codes
#control the process execution
# run os level commands- Linux, macos, windows
import subprocess
#subprocess.run() - run command and wait
#subprocess.Popen() - run process asynchronously
#subprocess.PIPE - capture the output
#subprocess.CompleteProcess - result
#subprocess.TimeoutExpired - Time outexpction
#subprocess.CalledProcessError - command failure

result=subprocess.run("dir",shell=True, capture_output=True, text=True)
print(f"{result}")
#print(result.stdout)

result=subprocess.run("ipconfig",shell=True, capture_output=True, text=True)
print(f"{result}")
#print(result.stdout)

result=subprocess.run("python --version",shell=True, capture_output=True, text=True)
print(result.stdout)
print(result.stdout)


