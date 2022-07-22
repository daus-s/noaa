import os
import token

url = input("Enter url:") #this will be relaced with importing urlbulder

exe = 'curl -H "token:{}" "{}" | jq'


os.system(exe.format(token.token, url))


print("\nclose")
