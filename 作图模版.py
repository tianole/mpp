import matplotlib.pyplot as plt
import numpy as np
##x=y=np.linspace(0,1000,1000)
##X,Y=np.meshgrid(x,y)
##z=((30*(X/80))**2-(30*(Y/80))**2)**1/2/100
##x=plt.axes(projection='3d')
##x.plot_surface(X,Y,z)
x=np.linspace(0,50,100)
y=x-np.sqrt(5*x)
z=x+np.sqrt(5*x)
plt.plot(x,y)
plt.plot(x,z)

plt.axis('equal')
plt.show()











##import requests
##import re
##data=requests.get(f"http://www.weather.com.cn/weather1d/101250101.shtml")
##air_quality=re.findall("\"od28\":\"[0-9]{0,3}\"",data.text)
##for i in range(0,len(air_quality)):
##    air_quality[i] = re.sub(r'"', "", air_quality[i])
##    index=air_quality[i].index(':')
##    air_quality[i]=air_quality[i][index+1:]
##    if(air_quality[i]==''):
##        air_quality[i]='数据缺失'
##    else:
##        air_quality[i]=int(air_quality[i])
##print(air_quality)

##import requests
##import re
##url=requests.get("http://www.weather.com.cn/weather1d/101250101.shtml")
##url.encoding="utf-8"
##source=url.text
##data=re.findall('(?<="od28":")\d+',source)
##lst=[int(i) for i in data]
##print(lst)
##try:
##    print(2/'0')
##except ZeroDivisionError:
##    print('AAA')
##except:
##    b='abc'
##    print(b)
