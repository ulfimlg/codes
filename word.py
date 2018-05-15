fo = open('beneficiary.txt','r')
message = fo.read()
with open('beneficiary.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)
