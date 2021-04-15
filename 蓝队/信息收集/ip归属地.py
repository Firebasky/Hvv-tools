# -*- coding: utf-8 -*-
'''
@fucntion: 使用纯真ip数据库qqwry.dat批量查询txt内ip的归属地
'''
from qqwry import QQwry
from IPy import IP

def batch_query_and_print():
    county = set()
    vps = set()
    ip = set()
    q = QQwry()
    q.load_file('qqwry.dat')
    with open('ip1.txt') as f:
        ip_list = f.read().splitlines()
        for read_content in ip_list:
            try:
                IP(read_content)
            except:
                print("有不符合规范的IP地址，请检查后重新运行")
                exit(0)
    address_list = [q.lookup(ip) for ip in ip_list]
    for i, j in zip(ip_list, address_list):
        query_results = i+" "+j[0]+" "+j[1]
        county.add(j[0])
        vps.add(j[1])
        ip.add(i)
        print(len(ip),len(county),len(vps))
        with open("query_results.txt", 'a', encoding='utf-8') as f:
            f.writelines(query_results+"\n")
        print(query_results)
if __name__ == "__main__":
    batch_query_and_print()
    
    
