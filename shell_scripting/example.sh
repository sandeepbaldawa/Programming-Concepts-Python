'''
There is a log file with writes processes details in the below mentioned format . 
--- 
Process_Name - RID(MB) - Time 
--- 
It is updated every second. write bash script to report processes which is having RID greater than 30. 
NB: Avoid reading the file line by line as it is very huge and updated every second
'''
-- logmonitor.sh --
#!/bin/sh

tail -f logfile.txt | awk '{if ($3 > 30) {print $0}}'
-- eof --

Test:

echo "PNAME - 31 - Time"| awk '{if ($3 > 30) {print $0}}'
