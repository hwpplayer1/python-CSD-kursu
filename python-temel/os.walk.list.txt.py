import os

try:
    f = open('list.txt', 'w')
    for root, dirs, files in os.walk('/home/hwpplayer1/Documents'):
        f.write(root + '\n')
    f.close()
except:
    print('file cannot open!')
