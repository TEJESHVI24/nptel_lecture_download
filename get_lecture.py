import requests
from os import path

nptel_base_url = 'https://nptel.ac.in/content/storage2/MP4/106105220/mod'

names = []
v_class = 1
for v_chapter in range(1,8):
    for num_of_classes in range(1,3):
        v_class += 1
        names.append((v_chapter,v_class))


for (x,y) in names:
    filename = "/Users/san/Downloads/lecture" + y + ".mp4"
    if not (path.exists(filename)):
        try:
            url = nptel_base_url + '0' + str(x) + 'lec' + y + '.mp4'
            print("====== Started for {} ====== {}".format(filename, url))
            r = requests.get(url)
            with open(filename, "wb") as f:
                f.write(r.content)
            print("====== Ended for ====== ", filename)
        except:
            continue
    else:
        print("==== File already exists ===", filename)

