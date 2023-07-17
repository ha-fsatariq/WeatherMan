from datetime import datetime
import os
import glob
import sys

#months dictionary
months = {
        '1': "January",
        '2': "February",
        '3': "March",
        '4': "April",
        '5': "May",
        '6': "June",
        '7': "July",
        '8': "August",
        '9': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }


#GETTING AND DISPLAYING YEARLY DATA
def getYearData():
    if(sys.argv[2]=='dubai'):
        directory='Dubai_weather'
    elif(sys.argv[2]=='lahore'):
        directory='lahore_weather'
    elif(sys.argv[2]=='murree'):
        directory='Murree_weather'
    
    year=sys.argv[3]
    year_information = []
    # Create a file path pattern to match files with the specific number in their path
    filesOfTargetedYear = os.path.join(directory, f'*{year}*')
    target_col=[0,1,3,7]

    # Use glob to get a list of file paths matching the pattern
    file_paths = glob.glob(filesOfTargetedYear)
    for path in file_paths:
        with open(path, 'r') as file:
            # Assuming the file contains one value per line (e.g., numbers)
            file.readline()
            for line in file:
                try:
                    date_str = line.split(',')[0] 
                    date = datetime.strptime(date_str, '%Y-%m-%d')  
                except ValueError:
                    continue  
                data = (line.strip().split(',')) 
                data=[data[i] for i in target_col]
                year_information.append(data)
                
                    

    return year_information


#Getting max min and max humidity for the year
def yearlyWeatherSummary(year_information):
    max_temp=float('-inf')    
    min_temp=float('inf')
    max_humidity=float('-inf')

    for day in year_information:
        if(day[1].isdigit()):
             if  int(day[1])>max_temp:
                 max_temp=int(day[1])
                 max_temp_day=day[0]
        if(day[2].isdigit()):
             if int(day[2])< min_temp:
                 min_temp=int(day[2])
                 min_temp_day=day[0]
        if(day[3].isdigit()):
             if int(day[3])>max_humidity:
                 max_humidity=int(day[3])
                 max_humidity_day=day[0]
        
    max_temp_day=max_temp_day.split('-')
    print('Highest: '+str(max_temp)+'C on '+months.get(max_temp_day[1])+' '+max_temp_day[2])
    min_temp_day=min_temp_day.split('-')
    print('Lowest: '+str(min_temp)+'C on '+months.get(min_temp_day[1])+' '+min_temp_day[2])
    max_humidity_day=max_humidity_day.split('-')
    print('Humid: '+str(max_humidity)+'% on '+months.get(max_humidity_day[1])+' '+max_humidity_day[2])


#GETTING AND PRINTING MONTLY WEATHER SUMMARY:
def getMonthlyData():

    if(sys.argv[2]=='dubai'):
        directory='Dubai_weather'
    elif(sys.argv[2]=='lahore'):
        directory='lahore_weather'
    elif(sys.argv[2]=='murree'):
        directory='Murree_weather'
    year=sys.argv[3]
    month=sys.argv[4]
    month_information = []
    # Create a file path pattern to match files with the specific number in their path
    TargetedMonth = os.path.join(directory, f'*{year}*{month}*')
    target_col=[0,2,8,1,3]
    # Use glob to get a list of file paths matching the pattern
    file_path = glob.glob(TargetedMonth)
    print(file_path)
    with open(file_path[0], 'r') as file:
        file.readline()
        for line in file:
            try:
                    date_str = line.split(',')[0] 
                    date = datetime.strptime(date_str, '%Y-%m-%d')  
            except ValueError:
                    continue  
            data = (line.strip().split(',')) 
            data=[data[i] for i in target_col]
            month_information.append(data)
    return month_information


#Getting max min and max humidity for the year
def monthlyWeatherSummary(month_information):
    max_avg_temp=float('-inf')    
    min_avg_temp=float('inf')
    avg_humidity=0
    no_of_days=0

    for day in month_information:
        no_of_days+=1
        if(day[1].isdigit()):
             if  int(day[1])>max_avg_temp:
                 max_avg_temp=int(day[1])
             if int(day[1])< min_avg_temp:
                 min_avg_temp=int(day[1])
        if(day[1].isdigit()):
            avg_humidity=avg_humidity+int(day[2])
        
    avg_humidity=avg_humidity/no_of_days

    print('Higest Average:'+ str(max_avg_temp)+'C')
    print('Lowest Average: '+str(min_avg_temp)+'C')
    print('Average Humidity: '+str(int(avg_humidity))+'%')

#VISUALLY DISPLAYING THE MONTHLY DATA:
def displayMonthlyData(month_information):
    getMonth=month_information[0][0].split('-')
    print(months.get(getMonth[1])+' '+getMonth[0])
    red='\033[91m'
    blue='\033[94m'
    RESET = '\033[0m'
    
    for Day in month_information:
        date=Day[0].split('-')
        if(Day[3].isdigit()):
            max_temp = int(Day[3])
            chart1 = '+' * max_temp + f" {max_temp}C"
            print(f"{date[2]}{' '}{red}{chart1}{RESET}")

        if(Day[4].isdigit()):
            min_temp = int(Day[4])
            chart2 = '+' * min_temp + f" {min_temp}C"
            print(f"{date[2]}{' '}{blue}{chart2}{RESET}")
            



if __name__ == "__main__":
    if(sys.argv[1]=='-e'):
        yearly_data=getYearData()
        yearlyWeatherSummary(yearly_data)
    elif(sys.argv[1]=='-a'):
        monthly_data=getMonthlyData()
        monthlyWeatherSummary(monthly_data)
    elif(sys.argv[1]=='-c'):
        monthly_data=getMonthlyData()
        displayMonthlyData(monthly_data)

