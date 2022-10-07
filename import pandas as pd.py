
import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('/home/pi/Desktop/NDP/cpu_temp_without_heatsink.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "CPU INTERNAL TEMPERATURE DATA")
  
plt.xticks(rotation = 25)
plt.xlabel('Time')
plt.ylabel('Temperature(°C)')
plt.title('CPU INTERNAL TEMPERATURE REPORT', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
plt.savefig('CPU_TEMP_WITHOUT_HEATSINK')