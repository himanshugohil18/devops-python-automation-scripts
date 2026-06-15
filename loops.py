list_of_cloud = ["aws","azure","gcp","digital ocean","utho","alibaba"]
cloud = "aws"

print(list_of_cloud)

#add new cloud 

list_of_cloud.append("ibm")
list_of_cloud.append("oracle")
print(list_of_cloud)

list_of_cloud.insert(2,"heroku")
print(list_of_cloud)

print(len(list_of_cloud))

list_of_cloud.insert(0,"hello cloud")
print(list_of_cloud)



#loop

for cloud in list_of_cloud:
    print(" ")
    print(cloud)