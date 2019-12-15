import requests
import random
APICode = '''
{% extends "base.html" %}

{% block content %}
 <div>
'''
CodeEnd = '''
</div>
{% endblock content %}
'''
base = 'https://docs.google.com/document/d/'
APCode = ""
numblock = []
buffer2 = 1
listrange = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ--_'
num = ""
for i in range(1):
    for i in range(44):  
      num = num + str(random.choice(listrange))
      while True:
        if num in numblock:
            num = str(random.choice(listrange))
        else:
            break
    link = 'https://docs.google.com/document/d/' + num +'/edit?usp=sharing'
    req = requests.get(link)
    print(num)
    numblock.append(num)
    if req.status_code == 404:
      while True:
        num = ""
        for i in range(44):  
          num = num + str(random.choice(listrange))
        print(num)
        if num in numblock:
          num = ""
          for i in range(44):  
            num = num + str(random.choice(listrange))
        link = 'https://docs.google.com/document/d/' + num +'/edit?usp=sharing'
        req = requests.get(link)
        if req.status_code == 200:
          break
    if buffer2 == 3:
      APCode = APCode + ' <a href ="' + link + '">        ' + 'docs' + '</a><br>\n'
    else:
      APCode = APCode + ' <a href ="' + link + '">        ' + 'docs' + '</a>\n'
    buffer2 = buffer2 + 1

    buffer2 = buffer2 + 1
homehtml = open("templates/main/index.html", "w")
homehtml.write(APICode + APCode + CodeEnd)
homehtml.close()