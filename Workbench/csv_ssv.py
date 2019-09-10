import csv

with open('csv_gaming.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # if you want to skip the header
    # next(csv_reader)

    with open('new_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)