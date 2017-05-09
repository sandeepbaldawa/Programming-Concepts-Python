import os
def List(pathname):
    fname = os.listdir(pathname)
    for each in fname:
        if os.path.isdir(each):
            List(each)
        else:
            print os.path.join(pathname, each)

List("/home/sandeep")
