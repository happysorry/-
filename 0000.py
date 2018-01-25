# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:30:08 2018

@author: owowowowo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import csv
import os


with open('2330.csv','w',newline='') as f:
    w = csv.writer(f)#writer
    r=csv.reader(f)#reader

list1=[1101,1102,1103,1104,1108,1109,1110];#水泥
lsit2=[1201,1203,1210,1213,1215,1216,1217,1218,1219,1220,1225,1227,1229,1231,1232,1233,1234,1235,1236,1256,1702,1737];#食品

#jd=json.loads({"item_shop_ids":[{"itemid":22091130,"campaignid":74457,"shopid":2101724,"adsid":74457,"ads_keyword":"google home","logisticid":[30006,30007,30005,39303],"deduction_info":"Zno2amFpY2xhdm1mMXk5cDBpyhODDJjdjzqwb12kJuIkrl2VoBrOGQ7wqMRZGxtP96tjSF5a2YMHa0fsjUpQDQ=="},{"itemid":250305654,"campaignid":81686,"shopid":3330566,"adsid":81686,"ads_keyword":"google","logisticid":[30006,30007,39304,30005],"deduction_info":"Zno2amFpY2xhdm1mMXk5cD2T1pnSb7+nzrCY8gcYl/GH6L1OY9AXe9RR3ehySQWuKs7Yp2vnu+KN38iiKH3n2w=="},{"itemid":142351852,"campaignid":54395,"shopid":3672206,"adsid":54395,"ads_keyword":"home","logisticid":[30006,30007,30005,30001,39304,39303],"deduction_info":"Zno2amFpY2xhdm1mMXk5cD2T1pnSb7+nzrCY8gcYl/Et8vkQd9CNVBtM5gQrjbs+DUjkCcx4ZGbxejkBaHp/Ag=="},{"itemid":5372602,"campaignid":229365,"shopid":1879236,"adsid":229365,"ads_keyword":"home","logisticid":[30005,30001,30006,30007,39304],"deduction_info":"Zno2amFpY2xhdm1mMXk5cMDWPYgfBDQdB6BqN/FsEKLXsgHvTxlq40Bs1MJDb8N/"},{"itemid":654313342,"shopid":761154,"logisticid":[30005,30001,30006,30007,39304]},{"itemid":730819759,"shopid":1069515,"logisticid":[30006,30007,39304,30005]},{"itemid":795792818,"shopid":9067107,"logisticid":[30006,30007,39304,30005]},{"itemid":713799584,"shopid":15170056,"logisticid":[30001,30005,30006,30007]},{"itemid":806008932,"shopid":4088231,"logisticid":[30007,39304,30005,30001,30006]},{"itemid":858268760,"shopid":7442378,"logisticid":[30005,30006,39304]},{"itemid":841518682,"shopid":2816163,"logisticid":[30006,30005]},{"itemid":839456614,"shopid":4088231,"logisticid":[30001,30006,30007,39304,30005]},{"itemid":828344202,"shopid":6440668,"logisticid":[39304]},{"itemid":827092829,"shopid":3237388,"logisticid":[39303,30006,30007,30005]},{"itemid":802111558,"shopid":46361503,"logisticid":[30006,30007,30005]},{"itemid":801746448,"shopid":2381469,"logisticid":[30006,30007,30005,39303,30001]},{"itemid":795266402,"shopid":4619374,"logisticid":[30006,30007,30005,39303,30001]},{"itemid":768357042,"shopid":3744104,"logisticid":[30007,39304,30001,30005]},{"itemid":757474738,"shopid":20242721,"logisticid":[39304]},{"itemid":757465992,"shopid":20242721,"logisticid":[39304]},{"itemid":755688631,"shopid":704241,"logisticid":[39304]},{"itemid":754919054,"shopid":829427,"logisticid":[30005,30006,39304]},{"itemid":751716314,"shopid":9465666,"logisticid":[39304,30005,30006]},{"itemid":751460856,"shopid":5911876,"logisticid":[30006,30007,39304,30005]},{"itemid":748586417,"shopid":1972077},{"itemid":727304246,"shopid":4924534,"logisticid":[30006,30001,30005]},{"itemid":723217974,"shopid":8224199,"logisticid":[30005,30006]},{"itemid":696894550,"shopid":7938247,"logisticid":[39303,30006,30007,30005]},{"itemid":695614709,"shopid":30417764,"logisticid":[30006,39304,30005]},{"itemid":674473974,"shopid":6191704,"logisticid":[30005,30006,30007,39303,39304]},{"itemid":626888252,"shopid":22292982,"logisticid":[30006,30007,30005,39304,39303]},{"itemid":609046821,"shopid":5748532,"logisticid":[39304]},{"itemid":600148602,"shopid":4395608,"logisticid":[30005,39303,30006,30007]},{"itemid":600081120,"shopid":4395608,"logisticid":[39303,30006,30007,30005]},{"itemid":571038317,"shopid":9878337,"logisticid":[38012,38011]},{"itemid":466446027,"shopid":18184908,"logisticid":[39304]},{"itemid":393153772,"shopid":119078,"logisticid":[39303,30001,30005]},{"itemid":368976870,"shopid":25996915,"logisticid":[30005,30006]},{"itemid":315255719,"shopid":18595310,"logisticid":[30006,30007,39304,30005,39303]},{"itemid":169091765,"shopid":2828023,"logisticid":[30001,39304,39303,30006,30007,30005]},{"itemid":43393642,"shopid":2828023,"logisticid":[30001,39304,39303,30006,30007,30005]},{"itemid":715965736,"shopid":10337254,"logisticid":[30006,30007,39304,30005]},{"itemid":785846139,"shopid":6086651,"logisticid":[30006,39304]},{"itemid":805688132,"shopid":7442378,"logisticid":[39304,30005,30006]},{"itemid":373007295,"shopid":4395608,"logisticid":[30005,39303,30006,30007]},{"itemid":805687405,"shopid":7442378,"logisticid":[30006,39304,30005]},{"itemid":805686724,"shopid":7442378,"logisticid":[39304,30005,30006]},{"itemid":805685966,"shopid":7442378,"logisticid":[30006,39304,30005]},{"itemid":858264468,"shopid":7442378,"logisticid":[30006,39304,30005]},{"itemid":755651249,"shopid":704241,"logisticid":[39304]}]})
i=2330
i=str(i)
url = 'http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID='+i+'&SYEAR=2017&SSEASON=3&REPORT_ID=C'
table=pd.read_html(url)[1]
#print(table);
table.to_csv("2330.csv", encoding = "utf-8");#寫入CSV
table = pd.read_html(url)[2]#1~27個表格
#table = table.drop(table.columns[[0,1,2,3,4]],axis=0)
#table = table.drop(table.columns[9:296],axis=1)
#print(table)
#f.write(table);
t=pd.read_csv("2330.csv", encoding = "utf-8");
print(t);

f.close();
