custom_data = open("C:\\Users\\Paul\Documents\\Advent of Code\\Day 6\\data.txt","r")

# Load data into a raw_batch_file
raw_batch_file= []

content = custom_data.read()
content = content.split('\n\n')


raw_batch_file.append([x.replace('\n','') for x in content])
raw_batch_file = raw_batch_file[0]

vAffirmativeResponse = []
vAffirmativeCountByGroup = []

def fnCollectResponses(group_response):
    for response in group_response:
        if response not in vAffirmativeResponse:
            vAffirmativeResponse.append(response)

    vCountAffirmative = len(vAffirmativeResponse)
    

    return vCountAffirmative   

for i in raw_batch_file:
    vAffirmativeCountByGroup.append(fnCollectResponses(i))
    vAffirmativeResponse = []

print(sum(vAffirmativeCountByGroup))