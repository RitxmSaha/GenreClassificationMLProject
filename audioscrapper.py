import time
import os
import sys
import subprocess
idArr = [9272650142,8719338602]

p = subprocess.Popen(["python","-u",r"C:\Users\ritam\DeepLearningNotebooks\chimera-main\main.py"],stdin=subprocess.PIPE,stdout=None,stderr=None, bufsize=1)

p.stdin.write("login\n".encode())
time.sleep(1)
p.stdin.write("2\n".encode())
time.sleep(1)
p.stdin.write("311dde2b3700b0ab90eab49de7196e993284b0c66a52f58dd5c3a1ba1883b3dda154d6328a10edd739244ea08cc38b7160e3931d36b451daa3b62a5087415b42304a160d571ef2529d80e38a1fbedb10a88c60f4dc01ba2df32a5abb1f1e02a1\n".encode())

for i in range(1): # repeat several times to show that it works
    p.stdin.write("grab playlist 8719338602\n".encode()) # write input
p.communicate("exit".encode())[0]