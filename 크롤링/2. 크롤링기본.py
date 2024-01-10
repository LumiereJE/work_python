from bs4 import BeautifulSoup

# ''' -> 파이썬에서 주석을 다는 문법, 전체가 문자열로 구분 됨
# 파싱하면 서버로부터 HTML이 이 형태로 들어오게 됨
html = ''' 
<html>
    <table border=1> 
        <tr>
            <td> 항목 </td> 
            <td> 2013 </td> 
            <td> 2014 </td> 
            <td> 2015 </td>
        </tr> 
        <tr>
            <td> 매출액 </td> 
            <td> 100 </td> 
            <td> 200 </td>
            <td> 300 </td>
        </tr> 
    </table>
</html> 
'''
# html을 이용해서 html.parser에 의해 들어오게 됨
soup = BeautifulSoup(html, 'html.parser')
print(soup)
result = soup.select('td')
print(result)

# 각 태그의 텍스트만 가져오기
for val in result :
    print(val.text)