from datetime import datetime
def ExtractFileData(file_paths,target_col):
    information=[]
    for path in file_paths:
        with open(path, 'r') as file:
            file.readline()
            for line in file:
                try:
                    date_str = line.split(',')[0]
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    continue
                data = (line.strip().split(','))
                data = [data[i] for i in target_col]
                information.append(data)
    return information