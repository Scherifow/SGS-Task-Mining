# import re
#
# with open(f"log1.mxml", 'r', encoding='utf-8') as f:
#     all_string = f.read()
#     data = re.findall(r"<Data>.*?</Data>", all_string)
#     with open(f"try.txt", 'w', encoding='utf-8') as file:
#         for date in data:
#             file.write(data + '\n')
#     print(all_string)
#     print(data)

import re
import csv
import pandas as pd

regex0 =r'<ProcessInstance.*?</ProcessInstance>'
regex = r'<Data>.*?</Data>'
regex1 = '(?<=attribute name=").*(?=</attribute>)'
clean_values = []
n = str(1)
batch = []
headers = []


with open(f"log8.mxml", 'r', encoding='utf-8') as f:
    all_string = f.read()

matches = re.findall(regex0, all_string, re.DOTALL)

with open(f"try.txt", 'w', encoding='utf-8') as file:
    for match in matches:
        file.write(match)

with open(f"try.txt", 'r', encoding='utf-8') as f:
    all_string = f.read()
matches = re.findall(regex, all_string, re.DOTALL)
# print(matches)

with open(f"try1.txt", 'w', encoding='utf-8') as file:
    for match in matches:
        file.write(match)

with open(f"try1.txt", 'r', encoding='utf-8') as f1:
    all_string1 = f1.read()


matches1 = re.findall(regex1, all_string1)


for match1 in matches1:
    cleaned_value = re.sub(r'">', ';', match1)
    clean_values.append(cleaned_value)
    splited_words = cleaned_value.split(';')
    if splited_words[0] not in headers:
        headers.append(splited_words[0])
    if splited_words[1] == n:
        n = str(int(n) + 1)

        with open("result8.csv", "a", encoding='utf-8', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow(batch)
            print(batch)
            batch = []
            batch.append(splited_words[1])

    else:
        batch.append(splited_words[1])

print(headers)










#         for date in data:
#             file.write(data + '\n')


# for matchNum, match in enumerate(matches, start=1):
#
#     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
#                                                                         end=match.end(), match=match.group()))
#
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
#
#         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
#                                                                         start=match.start(groupNum),
#                                                                         end=match.end(groupNum),
#                                                                         group=match.group(groupNum)))




    #     with open(f"justInfo{n}.txt", 'w', encoding='utf-8') as file:
    #         for log in info_log:
    #             file.write(log + '\n')
    #
    #     x = re.sub(r'\n.{14}Info {"message".*"logType":"User".*"}', '', all_string)
    #     print(x)
    # with open(f"2021-08-1{n}_Execution.log", 'w', encoding='utf-8') as file:
    #     file.write(x)
