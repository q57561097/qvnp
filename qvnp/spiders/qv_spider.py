from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest
class QvSpider(Spider):
    name = "qvp"
    start_urls=["http://weibo.com/aigenxing/home?topnav=1&wvr=6&mod=logo",]
    BG = "QN99=8210; QN1=eIQiPViQYhGj8o2C5rGeAg==; QunarGlobal=10.86.213.173_7004b050_159f3f71a39_-57f3|1485857299674; QN269=30FDF410E79D11E69769FA163E1273DD; QN48=tc_70ba7d56c34a9e95_159f3ff2418_83e1; PHPSESSID=68i1d68ud8npjkb3hr2mq22bh3; QN25=a4753b0a-0f2f-4ed1-86e9-02516794572a-9f992f90; QN271=be57ad30-8cca-4a6c-bb92-2fe178f45057; QN43=2; QN42=txgh4095; _q=U.tozcxxt2928; _t=24876057; csrfToken=REnt1h0tLe9awatSmSdVFuNJjrmrqfae; _s=s_F6TNXWXMNSEJK7Q3JNAIMKF3SU; _v=GdhFpb0ZuwQN-AFmviIVFdFRx1PrtD9ued7RJ-LfBaalY7wOvcB96ftb60Q2RCed0ym_LAXWo8YxC2BwPVwEhYIiL5pL93CF9J62Tp8kyE8E0MBVeKrWLJsaQ2zJBhtFFtmPXivTqsdaM56pduvZ2bfMpAJR3A205DxILcX_XzPA; QN6=auto_4e0d874a; QN163=0; Hm_lvt_75154a8409c0f82ecd97d538ff0ab3f3=1485849665,1485994605; Hm_lpvt_75154a8409c0f82ecd97d538ff0ab3f3=1485998385; QN268=|1485998391947_f90251ba3ff7ff09; JSESSIONID=925B4DE417ABC945E8908B06B388EB15; QN44=tozcxxt2928; _i=ueHd8ZQwpbYubXlAPZxBzRLZQTYX; _vi=eHBefuu8HrtP1oboQpa58GXy-j5lyUryn03CeK7AcC487Okni8bzhZNlq1MfR_5dug9ICCA82e8-wOqlNpIFSeN9PEt0N-NxGy57naU5LklzsCs4NgnXbdcTZL3Lj3j6gu3anNjvUIjruKNBW4ZdZb-F1aM0PuLGul5Gp60pruu2"
    FG = BG.split(';')
    cook = {}
    for i in FG:
        NB = i.split('=', 1)
        cook[NB[0]] = NB[1]

    headers = {
       "Host":"user.qunar.com",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding":"gzip, deflate",
        #"Referer":"http://order.qunar.com/",
        "Connection":"keep-alive",
        #"Cache-Control":"max-age=0",
        #"Cookie":"QN99=6034; QN1=eIQiPliPB70oCYpTd1t8Ag==; csrfToken=gDgYXwguGupdAiwWEfrgGtBJhfaNEdsg; QunarGlobal=192.168.31.100_-1048beaf_159eeb146a7_-6e27|1485768639979; _i=RBTjeLzySXRVuFyRsaAS-S0jdAUx; QN269=C4B7CC50E6CE11E6994FFA163EBE0F8B; Hm_lvt_75154a8409c0f82ecd97d538ff0ab3f3=1485767830; QN48=tc_82cd2e89e5d52b0a_159eeb6532f_e478; QN25=5893ef66-f2c6-4d09-ba74-56ee1f574002-9f992f90; _vi=EcSxtJPFT8h2KdOK8XDO5OO5B5tbrNf-ypyexHQvx4jHYU8va3LSlsqWXRak4lkH8TQi408vSregFxDP4lidTto22nq0uxnwQnePXJWsqe7awIEk1myoJU-hfKJzr9s--2qZjCOU4znZ2AEUabFLmY3bvETV76jb2587neF7B1t3; QN271=a7331ab9-3bc5-417c-8508-acc7b22149be; QN43=2; QN42=txgh4095; _q=U.tozcxxt2928; _t=24873312; _s=s_L5HEYMLU7LK6NOJNOXBHXCHGJU; _v=8zCcRkbfkWz4QNwkSeL0Z1RyOrsejKLzovYsn9bSlI9_bqdlI6EMjLlOgXD9UyTlEL8kC9iow7dwzEIL6_ECp9AKcGxr6qdmfboZOwsrZimyOBsPQJPHWgWpdqgZQ4GIaZiJyHTyKx7EmWQsrPd8r-88fnZaUJKXQzKOTi7At9t3; JSESSIONID=839A9D31B1C27A8C1F4542BD53A3C937; QN44=tozcxxt2928; PHPSESSID=palcf8pob5a2od0c658vkrekm1; QN268=|1485832403329_31eb0c007a6bd698"

    }

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url, cookies=self.cook,callback=self.parse_gh,headers=self.headers)
    def parse_gh(self, response):
        with open('/home/zyh/dkl.txt','a') as f:
            f.write(response.body)
