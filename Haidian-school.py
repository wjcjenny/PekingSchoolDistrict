
#-*- coding: UTF-8 -*-
# import urllib2  # the lib that handles the url stuff

# region_names ={'yfd':'羊坊店学区', 'wsl': '万寿路学区','ydl': '永定路学区','zzy':'紫竹院学区','blz':'八里庄学区',
# 'sjq':'四季青学区',
# 'btpz':'北太平庄学区',
# 'hyl':'花园路学区',
# 'hd_new':'海淀学区',
# 'zgc':'中关村学区',
# 'qlq':'青龙桥学区',
# 'sd':'上地学区',
# 'xyl':'学院路学区',
# 'qh':'清河学区',
# 'xsq':'西三旗学区',
# 'sz':'上庄西北旺学区', 
# 'wq':'温泉苏家坨学区'}



# #link = "http://edu.bjhd.gov.cn/dhgc/xx/blz/"

# def print_name(link):
# 	data = urllib2.urlopen(link) # it's a file like object and works just like a file
# 	flag = 0 # switch
# 	for line in data: # files are iterable
# 	    if flag == 1:
# 	        school_name_start = line.find('title=')
# 	        if school_name_start > 0:
# 	            school_name_end = line.find('>', school_name_start)
# 	            if school_name_end > 0:
# 	                print "   ", line[school_name_start+7 : school_name_end-1]
# 	    xqListBox = line.find('xqListBox')
# 	    if xqListBox > 0:
# 	        flag = 1
# 	    sumBox = line.find('sumBox')
# 	    if sumBox > 0:
# 	        flag = 0
# 	data.close()

# link = "http://edu.bjhd.gov.cn/dhgc/xx/"

# for key in region_names:
#     print key
#     print region_names[key]
#     link = link + key
#     print_name(link)

# #print_name(link)



# import schedule
# import time
import urllib2
# import json
# from csvkit.unicsv import UnicodeCSVDictWriter, UnicodeCSVDictReader

city_names = ['yfd', 'wsl','ydl','zzy','blz','sjq','btpz','hyl','hd_new','zgc','qlq','sd','xyl','qh','xsq','sz', 'wq']
# 高中变化：海淀为hdnew
# city_names = ['yfd', 'wsl','ydl','zzy','blz','sjq','btpz','hyl','hdnew','zgc','qlq','sd','xyl','qh','xsq','sz', 'wq']
base_url = "http://edu.bjhd.gov.cn/dhgc/cz/{0}"
region_names ={'yfd':'羊坊店学区', 'wsl': '万寿路学区','ydl': '永定路学区','zzy':'紫竹院学区','blz':'八里庄学区',
'sjq':'四季青学区',
'btpz':'北太平庄学区',
'hyl':'花园路学区',
'hd_new':'海淀学区',
# 'hdnew':'海淀学区',
'zgc':'中关村学区',
'qlq':'青龙桥学区',
'sd':'上地学区',
'xyl':'学院路学区',
'qh':'清河学区',
'xsq':'西三旗学区',
'sz':'上庄西北旺学区', 
'wq':'温泉苏家坨学区'}



def download_city_data(city_name):
	url = base_url.format(city_name)
	data = urllib2.urlopen(url)
	flag = 0
	for line in data: # files are iterable
	    if flag == 1:
	        school_name_start = line.find('title=')
	        if school_name_start > 0:
	            school_name_end = line.find('>', school_name_start)
	            if school_name_end > 0:
	                print "   ", line[school_name_start+7 : school_name_end-1]
	    xqListBox = line.find('xqListBox')
	    if xqListBox > 0:
	        flag = 1
	    sumBox = line.find('sumBox')
	    if sumBox > 0:
	        flag = 0


	
def get_city_data():
	for city_name in city_names:
		print region_names[city_name]
		download_city_data(city_name)
		
		

def main():
	get_city_data()

	
if __name__ == '__main__':
	main()