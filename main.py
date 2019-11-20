import requests
from lxml import etree

def main():
    base_url = 'https://movie.douban.com'
    url1 = 'https://movie.douban.com/people/VIELVET/wish'
    url2 ='https://movie.douban.com/people/62981626/wish'
    wl1 = generate_wl(url1, base_url)
    wl2 = generate_wl(url2, base_url)
    shared_wl = set(wl1) & set(wl2)
    for f in shared_wl:
        print (f)

def generate_wl(url, base_url):
    data = requests.get(url, headers={'User-Agent': 'Chrome'}).text
    s=etree.HTML(data)
    wl = s.xpath('//*[@class=\'title\']//em/text()')
    #check all remaining pages while next page is true
    while (s.xpath("//*[@class='next']/a/@href")):
        next = s.xpath("//*[@class='next']/a/@href")[0]
        next = requests.compat.urljoin(base_url, next)
        s=etree.HTML(requests.get(next, headers={'User-Agent': 'Chrome'}).text)
        wl.extend(s.xpath('//*[@class=\'title\']//em/text()'))
    return wl

if __name__ == "__main__":
    main ()


