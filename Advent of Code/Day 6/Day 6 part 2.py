import collections

custom_data = open("C:\\Users\\Paul\Documents\\Advent of Code\\Day 6\\data.txt","r")

# Load data into a raw_batch_file
raw_batch_file= []

content = custom_data.read()
content = content.split('\n\n')


raw_batch_file.append([x.replace('\n',' ') for x in content])
raw_batch_file = raw_batch_file[0]

# vAffirmativeResponse = []
vAffirmativeCountByGroup = []
vSumAllAffirmative = 0

def fnCollectResponses(group_response):
    for response in group_response:
        if response not in vAffirmativeResponse:
            vAffirmativeResponse.append(response)

    vCountAffirmative = len(vAffirmativeResponse)
    

    return vCountAffirmative   

def fnIdentifyGroupedAffirmativeCount(response):
    response = response.strip()
    vAffirmativeResponse = []

    vCountGroupMembers = response.count(' ') + 1
    response = response.replace(' ','')
    
    counter = collections.Counter(response)
    vCommonResponses = counter.most_common(26)
    
    for groupedAnswers in vCommonResponses:
        if groupedAnswers[1] == vCountGroupMembers:
            vAffirmativeResponse.append(groupedAnswers[0])
    
    print('Members in group:', vCountGroupMembers)
    print('Answers of group:', counter)
    print('Simplified responses', response)
    print('Most common responses', vCommonResponses)
    print('All answered yes:', vAffirmativeResponse)

    vCountAffirmative = len(vAffirmativeResponse)

    print(vCountAffirmative)

    return vCountAffirmative

for response in raw_batch_file:
    vSumAllAffirmative =  vSumAllAffirmative + fnIdentifyGroupedAffirmativeCount(response)

#print(sum(vAffirmativeCountByGroup))

#print(fnIdentifyGroupedAffirmativeCount('se u j se',vSumAllAffirmative))

print(vSumAllAffirmative)    



#    vAffirmativeResponse = []

#rint(sum(vAffirmativeCountByGroup))