import ntplib
import os
from time import ctime

c = ntplib.NTPClient()

server = os.getenv("NTPServer","0.debian.pool.ntp.org")

resp = c.request(server, version=3)


server = os.getenv("NTPServer","Warning!! No NTPServer define in env")
output={"server" : server,
        "date": ctime(resp.tx_time),
        "offset" : resp.offset,
        "stratum" : resp.stratum,
        "root-server" : ntplib.ref_id_to_text(resp.ref_id)
        }

print(output)
