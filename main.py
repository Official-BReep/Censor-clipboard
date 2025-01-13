import win32clipboard, re

modified = ""

# get clipboard data
win32clipboard.OpenClipboard()
data = str(win32clipboard.GetClipboardData()).splitlines()
win32clipboard.CloseClipboard()
for line in data:
    x = re.search(r"password\s*=\s*", line)
    if x:
        #print(line)
        string = re.findall(r"\".*\"", line)[0]
        modified += line.replace(string, f'\"{"*"*len(string)}\"') + "\n"
    else:
        modified += line + "\n"
print(modified)
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()

win32clipboard.SetClipboardText(modified)
win32clipboard.CloseClipboard()
