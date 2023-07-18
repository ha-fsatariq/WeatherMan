# Imports:
import os
import glob
import sys
import calendar
from Utils import ExtractFileData

# GETTING AND DISPLAYING YEARLY DATA:


def getYearData(directory, year):
    filesOfTargetedYear = os.path.join(
        directory, f'*{year}*')  # making the required pattren
    # selecting the required columns from the txt file
    target_col = [0, 1, 3, 7]
    # getting all the file paths that matches the defined pattren
    file_paths = glob.glob(filesOfTargetedYear)
    # getting required data from the txt file
    return ExtractFileData(file_paths, target_col)


# Getting max min and max humidity for the year
def yearlyWeatherSummary(year_information):
    # intializing the values of the variables:
    max_temp = float('-inf')
    min_temp = float('inf')
    max_humidity = float('-inf')

    for day in year_information:
        if (day[1].isdigit()):  # checking if the data is empty or not
            if int(day[1]) > max_temp:  # finding the max value
                max_temp = int(day[1])
                max_temp_day = day[0]
        if (day[2].isdigit()):
            if int(day[2]) < min_temp:
                min_temp = int(day[2])
                min_temp_day = day[0]
        if (day[3].isdigit()):
            if int(day[3]) > max_humidity:
                max_humidity = int(day[3])
                max_humidity_day = day[0]

    # spliting the date to get the month and day
    max_temp_day = max_temp_day.split('-')
    # Result Print statements:
    print('Highest: '+str(max_temp)+'C on ' +
          calendar.month_name[int(max_temp_day[1])]+' '+max_temp_day[2])
    min_temp_day = min_temp_day.split('-')
    print('Lowest: '+str(min_temp)+'C on ' +
          calendar.month_name[int(min_temp_day[1])]+' '+min_temp_day[2])
    max_humidity_day = max_humidity_day.split('-')
    print('Humid: '+str(max_humidity)+'% on ' +
          calendar.month_name[int(max_humidity_day[1])]+' '+max_humidity_day[2])


# GETTING AND PRINTING MONTLY WEATHER SUMMARY:
def getMonthlyData(directory, year, month):
    TargetedMonth = os.path.join(directory, f'*{year}*{month}*')
    target_col = [0, 2, 8, 1, 3]
    file_paths = glob.glob(TargetedMonth)
    return ExtractFileData(file_paths, target_col)


# Getting max min and max humidity for the year
def monthlyWeatherSummary(month_information):
    max_avg_temp = float('-inf')
    min_avg_temp = float('inf')
    avg_humidity = 0
    no_of_days = 0

    for day in month_information:
        no_of_days += 1
        if (day[1].isdigit()):
            if int(day[1]) > max_avg_temp:
                max_avg_temp = int(day[1])
            if int(day[1]) < min_avg_temp:
                min_avg_temp = int(day[1])
        if (day[1].isdigit()):
            avg_humidity = avg_humidity+int(day[2])

    avg_humidity = avg_humidity/no_of_days

    print('Higest Average:' + str(max_avg_temp)+'C')
    print('Lowest Average: '+str(min_avg_temp)+'C')
    print('Average Humidity: '+str(int(avg_humidity))+'%')


# VISUALLY DISPLAYING THE MONTHLY DATA:
def displayMonthlyData(month_information):
    getMonth = month_information[0][0].split('-')
    print(calendar.month_name[int(getMonth[1])]+' '+getMonth[0])
    red = '\033[91m'
    blue = '\033[94m'
    RESET = '\033[0m'

    for Day in month_information:
        date = Day[0].split('-')
        if (Day[3].isdigit()):
            max_temp = int(Day[3])
            chart1 = '+' * max_temp + f" {max_temp}C"
            print(f"{date[2]}{' '}{red}{chart1}{RESET}")

        if (Day[4].isdigit()):
            min_temp = int(Day[4])
            chart2 = '+' * min_temp + f" {min_temp}C"
            print(f"{date[2]}{' '}{blue}{chart2}{RESET}")


if __name__ == "__main__":
    try:
        # if block to chcek if the number of arguments added are correct or not and then getting values from the args
        if ((len(sys.argv) == 4 or len(sys.argv) == 5)):
            if (sys.argv[2].lower() == 'dubai'):
                directory = 'Dubai_weather'
            elif (sys.argv[2].lower() == 'lahore'):
                directory = 'lahore_weather'
            elif (sys.argv[2].lower() == 'murree'):
                directory = 'Murree_weather'
            year = sys.argv[3]

            if (sys.argv[1] == '-e' and len(sys.argv) == 4):
                yearly_data = getYearData(directory, year)
                yearlyWeatherSummary(yearly_data)
            elif (sys.argv[1] == '-a' or sys.argv[1] == '-c' and len(sys.argv) == 5):
                if (len(sys.argv) == 5 and (int(sys.argv[4]) > 0 and int(sys.argv[4]) < 13)):
                    month = int(sys.argv[4])
                    monthName = calendar.month_name[month]
                    monthName = monthName[:3].capitalize()
                    if (sys.argv[1] == '-a'):
                        monthly_data = getMonthlyData(
                            directory, year, monthName)
                        monthlyWeatherSummary(monthly_data)
                    elif (sys.argv[1] == '-c'):
                        monthly_data = getMonthlyData(
                            directory, year, monthName)
                        displayMonthlyData(monthly_data)

                else:
                    raise EOFError('Correct Month number is required.')

            else:
                raise EOFError(
                    'Incorrent Command.Accepted commands are -e,-a,-c. HINT: Incase of -e only 3 yet in case of -a,-c only 4 arguments are allowed.')

        else:
            raise ValueError(
                "Incorrect number of arguments. Expected 4 or 5 arguments.")
    except (ValueError, EOFError) as e:
        print(e)
