# ntpserver-test
Use this script for test "NTPd" (synced , stratum and reference server) 

# Requirements
python3  
ntplib  

# Installing
> pip install -r requirements.txt

# Running
Pointing to server over environment variable called "NTPServer"  like this

> NTPServer=0.ubuntu.pool.ntp.org python3 run.py
