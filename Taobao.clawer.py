import urllib2, re, json

#headers = {'User-agent': '"Mozilla/5.0 \(X11; U; Linux i686\) Gecko/20071127 Firefox/2.0.0.11"'}
#req = urllib2.request('www.someurl.com', None, headers)
#html = urllib2.urlopen(req).read()

url = 'http://hstar-hi.alicdn.com/dream/ajax/getProjectList.htm?page=%d&pageSize=20&projectType=&type=6&status=&sort=&_ksTS=1419353702053_48&callback=jsonp49'
Jsonhash = {}
f = open('sample.json')
line = f.readlines()
#line = json.load(f)
f.close()




def ParseJson(line):
    delSign = re.compile('\r\n')
    tmphash = {}
    line = delSign.sub('',''.join(line[1:-1]).decode('gbk'))
    line = line[line.index('(')+1:]
    tmphash.update(eval(line))
    return tmphash
#Jsonhash = dict(line[line.index('(')+1:].encode('utf8'))
#print line[line.index('(')+1:line.index(')', -1)]
