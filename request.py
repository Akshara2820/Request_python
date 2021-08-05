import requests
import json
from pprint import pprint
import time
tttt=True
while tttt:

    Data=requests.get("http://saral.navgurukul.org/api/courses")
    data1=json.loads(Data.text)

    with open("course.json","w") as data:
        json.dump(data1,data,indent=4)

    store=data1["availableCourses"]
    id=[]
    name=[]
    logo=[]

    for i in range(len(store)):
        time.sleep(0.1)
        print(i,store[i]["name"],end=" ----")

        print(store[i]["id"])

        id.append(store[i]["id"])

        name.append(store[i]["name"])
    print()

    print("******-- id --********")

    print()

    # print(id)
    print()

    n=int(input("enter which id you want--"))
    i=0
    v=0
    z=0
    l=len(id)
    while i<n:
        v=id[i]
        z=name[i]
        i+=1
    print(v)
    print("* parents exercise*")
    print()

    child_url=requests.get("http://saral.navgurukul.org/api/courses/"+id[n]+"/exercises")

    child_data=json.loads(child_url.text)

    with open("child_data1.json","w")as data:

        json.dump(child_data,data,indent=4)

    child_file=open("child_data1.json","r")

    child_ex=json.load(child_file)

    s=child_ex["data"]


    #
    l=len(s)
    i=0
    p=0
    zx=[]
    while i<l:

        print(i,s[i]['name'])
        

        zx.append(s[i]['slug'])
        
        i+=1
    print("********up_dawn*********")
    kk = input("Enter 'up' or exercise no.: ") 
    if kk == "up": 
        continue
    else:
        kk=int(kk)

    child_url=requests.get("http://saral.navgurukul.org/api/courses/"+id[n]+"/exercise/getBySlug?slug="+(zx[kk]))
    child_data=json.loads(child_url.text)


    with open("child_data1.json","w")as data:

        json.dump(child_data,data,indent=4)

    child_file=open("child_data1.json","r")

    child_ex=json.load(child_file)

    print(child_ex['content'])
    break
print("******next*****previous*******")

ku=0
while True:
    next_p=input("enter 'n' for next or 'p' for previous or c to close------")
    if next_p=='n' and kk==len(zx)-1:
        break
    elif next_p=='p' and kk==0:
        break
    
    if next_p=='c':
        break
    elif next_p=="n":
        
        child_url=requests.get("http://saral.navgurukul.org/api/courses/"+id[n]+"/exercise/getBySlug?slug="+str(zx[kk]))
        child_data=json.loads(child_url.text)


        with open("child_data1.json","w")as data:

            json.dump(child_data,data,indent=4)

        child_file=open("child_data1.json","r")

        child_ex=json.load(child_file)
        print(child_ex['content'])
        kk+=1
    elif next_p=="p":
        
        child_url=requests.get("http://saral.navgurukul.org/api/courses/"+id[n]+"/exercise/getBySlug?slug="+str(zx[kk]))
        child_data=json.loads(child_url.text)


        with open("child_data1.json","w")as data:

            json.dump(child_data,data,indent=4)

        child_file=open("child_data1.json","r")

        child_ex=json.load(child_file)
        print(child_ex['content'])
        kk-=1

    else:
        print("not found")