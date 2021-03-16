///
Author: Md. Shamsujjoha, Prof. John Grundy, Dr. Li Li, Dr. Qinghua Lu and Dr. Hourieh Khalajzade
Python Version: 3.7 or later
S.B.: Please download the latest.csv with request from  https://androzoo.uni.lu "AndroZoo: Collecting Millions of Android Apps for the Research Community" and put it in the same folder as this python code. Also put the chabada_appID_versionCode.csv file in same folder as python code. 
///
import csv
i=0
CSV1L = [] CSV2L = []

csvfile1 = open('latest.csv')
readCSV1 = csv.reader(csvfile1, delimiter=',')
for m_row in readCSV1:
    CSV1L.append(m_row)

f1 = open('outSHA256.txt', 'w+', encoding="utf8")
csvfile2 = open('chabada_appID_versionCode.csv')
readCSV2 = csv.reader(csvfile2, delimiter=' ')
for row in readCSV2:
    CSV2L.append(row)

for row in CSV2L:
    flag = 1
    for m_row in CSV1L:
        if ((row[0] == m_row[5]) and (row[1] == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) + 1) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) - 1) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) + 2) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) - 2) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) + 3) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) - 3) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) + 4) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) - 4) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) + 5) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5]) and (str(int(row[1]) - 5) == m_row[6])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

        elif ((row[0] == m_row[5])):
            print(m_row[5], "\t", m_row[6], "\t", m_row[0], file=f1)
            flag = 2
            break

    if (flag == 1):
        print("Not Found")
