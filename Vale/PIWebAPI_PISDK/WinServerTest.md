# Testing For Vale

## Install Windows Server

VM Specs:

- RAM: 10240 MB
- Enable I/O APIC
- CPU: 4
- Enable PAE/NX
- Video RAM: 64 MB
- Graphic: VBoxSVGA
- Storage: 60 GB Pre-Allocated
- Use Host I/O Cache
- Network Mode: Bridged Adapter
- Bridged Target: wlan0
- Cable Connected
- Guest Addition Installed
- Skip unattended Installation
- Shared Folder: Automount
- Disabled:
    - Audio
    - Serial Port

## OS Install

Version to install: **Windows Server+GUI 2019 Standard x64**

After Install:
 - Install Firefox
 - Enable NetFX3 from CMD

```bat
dism /online /enable-feature /featurename:netfx3 /all /source:D:\sources\sxs\
```
    
 - Virtualbox Addition
 
**Note:** Restart rule -> **Other (Planned)**

## Config IPv4

**Notes:** Firewall disabled

Check IPv4

```bat
ipconfig /all
```

Manual config IPv4:
- Host: 192.168.1.5
- Guest: 192.168.1.6 (Gateway: 192.168.1.5)

## PI System Install

### Pre-requisites

**Note:** Everything installed as **Administrator**.

Install Sequences:
- NetFramework 4.8
    - Restart
- OSIprerequisites-standalone
- SQL2022 SSEI
    - Download Media only
- SQLEXPR_x64_ENU_2022
    - No Azure Instance 
    

### PI Server

Install PI Server 2018:
    - Online 
    - Select All

Some license headache:
- Got machine signature code (MSF) in Document or check from installer tooltips when asking **pilicense.dat**
- Register Trial License (Using a company format email) [here](https://registrations.osisoft.com/s/redeemtrial)
- Login to get exchange MSF with **pilicense.dat**

### Authentification

USERNAME: WIN-F04CA4DRVSA\<RoleThings>
PASSWORD: Qwerty123

### Install the Rest
- PI Vision 2023
- PI Web API 2023
    - Connect to PI Server internally
    - Restart
    

## Some Useful Server URLs

Note: Requires setup SSL in Databases

https://10.160.10.71/PIVision/
https://10.160.10.71/PIVision/Admin/
https://10.160.10.71/PIVision/Admin/Configuration/
https://10.160.10.71/piwebapi
https://10.160.10.71/pivision

