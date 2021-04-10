# logbisect
python library to search huge log files quickly

cli:
    logbisect -f data/bisectable -r "^\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}" -t "2021-04-08 15:46:01" -n 4


as library:
    with open("data/bisectable", "r") as fh:
        pos = bisect(fh, "^\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}", "2021-04-08 15:46:01")
        # pos is the numerical position of the fh pointer
        # file handle is now in the correct position to read from the discovered line
        print(fh.readline().strip())
    
