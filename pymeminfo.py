import csv

# Open file
try:
    # Create input file with 'watch -n 1 'cat /proc/meminfo >> /run/media/nvme/meminfo.log && date >> /run/media/nvme/meminfo.log''

    # TODO: Get this value from the system
    MEMINFO_LEN = 50

    # TODO: Make this an argument
    #filepath = '/home/jarrodn/meminfo.log';
    #filepath = '/run/media/nvme/meminfo.log';
    filepath = './meminfo.log';
    #filepath = './test';
    fp = open(filepath, 'r')

    with open('output.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        # On first pass get column headers
        headers = []
        values = []

        for i in range(0, MEMINFO_LEN - 1):
            line = fp.readline()
            # Write each first word as header
            splitline = line.split();
            headers.append(splitline[0])

        # Create a header for date/time stamp
        line = fp.readline()
        headers.append('Time')

        # Write headers and values to CSV output
        csvwriter.writerow(headers)

        cnt = 0
        fp.seek(0)

        # For the remaining passes put each value into CSV under appropriate header
        for line in fp:
            splitline = line.split();

            # Add the time and then start a new row
            if cnt == MEMINFO_LEN - 1:
                values.append(splitline[3])
                csvwriter.writerow(values)
                # Reset count 
                cnt = 0
                # Clear values
                del values[:]
            else:
                values.append(splitline[1])
                cnt += 1

# Clean up
finally:
    fp.close()
