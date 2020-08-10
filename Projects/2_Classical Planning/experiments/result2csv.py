import csv
import os
import sys

def result2csv(target):
    csv_columns = ['P','S','Actions', 'Expansions', 'Goal Tests', 'New Nodes', 'Plan length', 'Time elapsed in seconds']
    dict_data = []

    files = os.listdir(target)
    for file in files:
        filename, ext = os.path.splitext(file)
        problem, solution = filename.split('_')

        dict_item = {}
        dict_item['P'] = problem
        dict_item['S'] = solution
        with open (os.path.join(target, file), "r") as f:
            data=f.readlines()
            result_line0 = data[4].split()
            result_line1 = data[6].split()
            dict_item['Actions'] = result_line0[0]
            dict_item['Expansions'] = result_line0[1]
            dict_item['Goal Tests'] = result_line0[2]
            dict_item['New Nodes'] = result_line0[3]
            dict_item['Plan length'] = result_line1[2]
            dict_item['Time elapsed in seconds'] = result_line1[7]

        dict_data.append(dict_item)

    csv_file = target + ".csv"
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
        print(csv_file)
    except IOError:
        print("I/O error")

if __name__ == '__main__':
    target = "workstation"
    if len(sys.argv) < 2:
        print('usage : python result2csv.py $target')
    else:
        target = sys.argv[1]
    result2csv(target)