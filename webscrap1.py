import requests
import bs4

result = requests.get("https://info.bbdc.sg/members-login/")
result.text
soup = bs4.BeautifulSoup(result.text, 'lxml')
answer = soup.select('#popup-inner1')[0].getText()
answer2 = soup.select('#popup-inner2')[0].getText()
answer3 = soup.select('#popup-inner3')[0].getText()
print(answer + '\n\n' + answer2 + '\n\n' + answer3)
input()
