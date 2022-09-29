# On Ubunt 20.4 LTS
# Analyze /var/log/syslog
# find all lines with ERROR word
import os
from funcAnalyzer import error_finder

targetFile = "/var/log/syslog"
searchingphrase = "ERROR"
openedTargetFile = open(targetFile,'r')
error_finder(openedTargetFile,searchingphrase)
openedTargetFile.close()