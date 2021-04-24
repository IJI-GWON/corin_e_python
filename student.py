import requests
import os

sessioin = requests.Session()

for i in range(2016, 2017):
    if not os.path.isdir(str(i)):
        os.makedirs(str(i))

    for j in range(10000, 13500):
        studentnumber = str(i) + str(j).zfill(5)
        response = sessioin.get("http://kutis.kyonggi.ac.kr/webkutis/TransferImageStream.do?hakbun=" + studentnumber)

        if response.content:
            f = open(str(i) + "/" + studentnumber + ".jpg", 'wb')
            f.write(response.content)
            f.close()
