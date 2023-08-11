

import pyulog
import pandas as pd

#location of ulog file
ulog_file = r"C:\Users\Rahul\OneDrive\Desktop\ENORD\ulogtocsv\log100.ulog"

data = pyulog.ULog(ulog_file)
data_list = []

for d in data.data_list:
    if d.name == 'sensor_combined':  # Adjust the topic name as per your ulog file
        field_names = [field.field_name for field in d.field_data]
        for i in range(len(d.data['timestamp'])):
            row = [d.data[field][i] for field in field_names]
            data_list.append(row)



df = pd.DataFrame(data_list, columns=field_names)
#locaiton of output file
csv_file = r"C:\Users\Rahul\OneDrive\Desktop\ENORD\ulogtocsv\output.csv"
df.to_csv(csv_file, index=False)

