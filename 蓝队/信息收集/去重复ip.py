# -*- coding:utf-8 -*-
def cleanCLRFspace(content):
    noCLContext = content.replace('\n','')
    noSpaceCLRFcontext = noCLContext.strip()
    return noSpaceCLRFcontext

def cleanDup(f):
    contextSet = set()
    contexts = f.readlines()
    for content in contexts:
        cleanContet = cleanCLRFspace(content)
        if cleanContet != '':
            contextSet.add(cleanContet)
            okContext = list(contextSet)
            okContext.sort()
    return okContext
 
def saveContext(s):
    wfile = open('./ip.txt','w')
    for i in s:
        wfile.write(i+'\n')
    wfile.close()

def main():
    f = open('./ip2.txt','r')
    contextSet = cleanDup(f)
    saveContext(contextSet)
    f.close()

if __name__ == '__main__':
    main()
