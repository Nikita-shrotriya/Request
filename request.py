import json
from textwrap import indent
import requests
a=requests.get('http://saral.navgurukul.org/api/courses')
print(a)
x=(a.json())
with open("courses.json","w") as y:
    json.dump(x,y,indent=4)
count=0
list=[]
for i in x["availableCourses"]:
    print(count,".",i["name"],".....",i["id"])
    list.append(i["id"])
    count=count+1
choose=int(input("enter the serial number:"))
r=0
k=requests.get("http://saral.navgurukul.org/api/courses/"+str(list[choose])+"/exercises")
m=k.json()
list2=[]
for i in m["data"]:
    print(r,i["slug"])
    list2.append(i["slug"])
    r=r+1
choose2=int(input("enter the slug number"))
n=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"exercises/getbyslug?slug="+list2[choose2])
o=n.json()
print(o)    


    


