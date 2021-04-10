# logbisect
python library to search huge log files quickly

This library works on datestamped, ordered files of arbitrary size

pass in:
1. file handle
2. regex to sort the date out of the log file
3. target date to search

cli:

    logbisect -f data/bisectable -r "^\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}" -t "2021-04-08 15:46:01" -n 4


as library:

    with open("data/bisectable", "r") as fh:
        pos = bisect(fh, "^\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}", "2021-04-08 15:46:01")
        # pos is the numerical position of the fh pointer
        # file handle is now in the correct position to read from the discovered line
        print(fh.readline().strip())

example data:

    Apr  8 15:48:24 templar named[317]: client @0x7f0d98029298 10.3.0.106#43556 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d8c06e4d8 10.3.0.106#61766 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d94047e88 10.3.0.106#49621 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d98029298 10.3.0.106#54996 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d98029298 10.3.0.106#62061 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d8c06e4d8 10.3.0.106#60412 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:24 templar named[317]: client @0x7f0d94047e88 10.3.0.106#46876 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied 
    Apr  8 15:48:29 templar named[317]: client @0x7f0d900382c8 10.3.0.106#36796 (pubads.g.doubleclick.net): query 'pubads.g.doubleclick.net/A/IN' denied
