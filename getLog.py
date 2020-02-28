import os
import json

#oc login
os.system('sh script.sh $(oc whoami -t)')

#range rangeForLogLine * 10.000 = LogLine
rangeForLogLine = 40


for i in range(rangeForLogLine):
  with open('log.json') as f:
    data = json.load(f)
  f = open("log.txt", "a")
  for a in range(9999):
    msg = str(data.get("hits").get("hits")[a].get("_source").get("@timestamp")) + ":" + str(data.get("hits").get("hits")[a].get("_source").get("message"))
    f.write(msg)
  f.close()
  print("-------------------------")
  os.system('sh cont.sh $(oc whoami -t) '+data.get("_scroll_id"))
