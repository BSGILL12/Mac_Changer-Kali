import subprocess

inteja=input("Enter Iterface:")
n_mja=input("Enter MAC you want:")

print("Changing MAC from-")



subprocess.call(["ifconfig",inteja,"down"])
subprocess.call(["ifconfig",inteja,"hw","ether",n_mja])
subprocess.call(["ifconfig",inteja,"up"])