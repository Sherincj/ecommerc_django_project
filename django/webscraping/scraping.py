import requests
from bs4 import BeautifulSoup as bs

# res=requests.get('https://expertzlab.com/contact')
# val=bs(res.text)
# new=val.findAll('div',attrs={'class':"contact-info"})
# print(new[2].text)

# with open('data.txt','w') as f:
#     f.write(new[2].text)


# res=requests.get('https://expertzlab.com/index')
# val=bs(res.text)
# data=val.findAll('div',attrs={'class':"course"})
# for i in data:
#     print(i.h4.a.text)


# with open('course.text','w') as b:
#     for course in data:
#         b.write(course.h4.a.text)
