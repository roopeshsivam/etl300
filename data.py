#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import serial
import StringIO

DB_hostname = 'localhost'
DB_username = 'etl_ps_user'
DB_password = 'etl_ps_user'
DB_name = 'etldata'
con = psycopg2.connect(host=DB_hostname, user=DB_username, password=DB_password, dbname=DB_name)
cur = con.cursor()
serialIn = serial.Serial()
serialIn.baudrate = 9600
serialIn.timeout = 2
serialIn.port = '/dev/ttyUSB0'
serialIn.open()
serialIn.write(b'@#T2\r')
stInput = serialIn.read(99999)  				## Read upto 9999 lines from serial
stReplace = stInput.replace("\r\r", "\n")		## Replace EOL
#print streplace
lineBuffer = StringIO.StringIO(stReplace)		# Pass to line buffer
#bufout = buf.getvalue()
#print bufout
for singleLine in lineBuffer.readlines():		## Read single lines
	singleLine = singleLine.strip()				## Strip EOL
	singleLine = singleLine.split(";")			## Line to list seperated by ;
	if len(singleLine) >1:						## Condition for NoData Lines
		dateChange = singleLine[0]				## Date Change for postgre timestamp 
		dateChange = dateChange.split( "-" )	## Split date to list
		dateNew = "20" + dateChange[2] + "-" + dateChange[1] + "-" + dateChange[0] + " " + singleLine[1] + ":00" + " +4:00" "
		print dataNew
		print singleLine
		cursor.execute("INSERT INTO etlview_serindata ( name, AGE) VALUES (%s, %s)",("leo", 26))
	else:
		print singleLine[0]						## NoData Lines (for test only)
lineBuffer.close()								## Close Line buffer
serialIn.close()								## Close Serial
con.close()
