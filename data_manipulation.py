import os
from xml.etree.ElementInclude import include
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True

def does_file_exist(file_path):
    return os.path.exists(file_path)

print(does_file_exist("nonsense"))
print(does_file_exist("AirQuality.csv"))

# Purpose: get the contents of a given file and return them; if the file cannot be found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()

def get_file_contents(filename):
    if does_file_exist(filename):
        with open(filename, "r") as file:
            return file.read()  # Return the entire file content as a string
    else:
        return "Not found"


# print(get_file_contents("AirQuality.csv"))
# print(get_file_contents("nonsense"))

# Fetch 25th December air quality data rows and if boolean argument "include_header_row" is True, return first header row (if False, omit)

# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# should use get_file_contents() - N.B. as should any subsequent functions you write, using anything previously built if and where necessary

def christmas_day_air_quality(filename, include_header_row):
    contents = get_file_contents(filename)
    lines = contents.splitlines()
    header = lines[0] if lines else ""



    # contents = get_file_contents(filename)
    # if contents == "Not found":
    #     return "Not Found"
    
    # lines = contents.splitlines()
    # header = lines[0] if lines else ""
    # christmas_rows = [line for line in lines if line.startswith("25/12")]

    # if include_header_row and header:
    #     return f"{header}\n" + "\n".join(christmas_rows)
    # else:
    #     return "\n".join(christmas_rows)


#print(christmas_day_air_quality("AirQuality.csv", True))
#print(christmas_day_air_quality("AirQuality.csv", False))


# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    pass

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    pass

# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    pass

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    pass