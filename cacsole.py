from luandoan import *
import requests
from bs4 import BeautifulSoup
class Lichvannien():
    def __init__(self,url):
        self.url = url
    def connect(self):
        return requests.get(f"{self.url}")
    def soup(self):
        return BeautifulSoup(self.connect().content,'lxml')
url ='http://ngaydep.com/lich-van-nien.html'
data = Lichvannien(url)
def ngayam():
    dulieungay = data.soup().find(class_='ngayam')
    ngayam = dulieungay.find("a")
    for am in ngayam:
        return am
def thangam():
    dulieuthang = data.soup().find(class_="ngayduong font1")
    thangam = dulieuthang.find("b")
    for thang in thangam:
        return thang[6:7]

print("Hôm nay là ngày {} tháng {} Năm 2016 Âm lịch".format(ngayam(),thangam()))
print("----------------------------------")
print("""Giờ muốn xem khởi hành vui lòng chọn theo tính 12h kể đêm vào ngày:"
      1.Chọn a nếu xuất hành giờ từ 11h đến 1h 
      2.Chọn b nếu xuất hành chọn giờ từ 1h đến 3 h
      3.Chọn c nếu xuất hành giờ từ 3h đến 5 h
      4.Chọn d nếu xuất hành giờ từ 5h đến 7 h
      5.Chọn e nếu xuất hành giờ từ 7 h đến 9 h
      6. Chọn f xuất hành nếu giờ 9 đến 11 """)
khacche = input("Thành tâm nghĩ tới nó >>> nhập vd 'a' :")
khac = {1: "11,12,1a", 2: "1,2,3b", 3: "3,4,5c", 4: "5,6,7d", 5: "7,8,9e", 6: "9,10,11f"}
def socantim():
    for a,v in khac.items():
        if khacche == khac[a][-1:]:
            return a
socantims = int(socantim())
# print(socantims)
ketqualuan = (int(thangam())+ int(ngayam())+ socantims)-2
# print(ketqualuan)
boi = ketqualuan % 6

# print(boi)
if boi == 1:
 print(daian)
elif boi ==2:
    print(luunien)
elif boi == 3:
    print(tochi)
elif boi == 4:
    print(xichkhau)
elif boi == 5:
    print(tieucat)
elif boi == 6:
    print(khongvong)
else:
    print("VUI LÒNG NHẬP NHƯ HƯỚNG DẪN")
