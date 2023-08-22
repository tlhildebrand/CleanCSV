# Python script takes in a csv file and removes any embedded double quotations
# testfile.csv - test file with embedded quotes
# cleanfile.csv - output file with double quotes removed
import csv

def clean_csv(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                cleaned_row = [field.replace('"', '') for field in row]
                writer.writerow(cleaned_row)

if __name__ == "__main__":
    input_csv_file = "testfile.csv" # input file
    output_csv_file = "cleanfile.csv" # output file
    clean_csv(input_csv_file, output_csv_file)
    print("CSV file cleaned and saved.") 
