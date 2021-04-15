# coding=utf-8
import urllib.request
import urllib.error

f = open("tar.txt")
url = []

for line in f.readlines():
    tmp = line.replace('\n','')
    url.append(tmp)
f.close()
for tmpurl in url:
    try:
        req = urllib.request.Request(tmpurl)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
        resp = urllib.request.urlopen(req,timeout=2)
        code = resp.getcode()
        if code==200:
            with open("query_results.txt", 'a', encoding='utf-8') as f:
                f.writelines(tmpurl+"\n")
        #print(tmpurl,":",code)
    except urllib.error.URLError as e:
        print(tmpurl,":",e.reason)
    except urllib.error.HTTPError as e:
        print(e.code,":",e.reason)
