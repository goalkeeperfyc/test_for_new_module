import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help="The csv file name, if any, input all")
args = parser.parse_args()

filename_list = args.file.split(",")

print(filename_list)

for filename in filename_list:
    print(filename)

