#-*-coding:utf-8-*-
import os
import base64
import zlib

def CMD(str):
	os.system("%s"%str)

def encStr(str0):
	return zlib.compress(base64.b64encode(str0.encode('utf-8')))
	
def decStr(str0):
	if not str0:
		return ""
	return str(base64.b64decode(zlib.decompress(str0)),'utf-8')

def configMpv():
	global globalCmd
	for i in range(100):
		CMD("cls&@echo.")
		if os.path.exists(configPath):
			if os.path.exists(os.path.join(configPath,'std-mpv.exe')):
				path=configPath
			else:
				# print("Error: %s   std-mpv.exe文件已被修改"%configPath)
				path=input("重新配置路径: ").strip()
				print("[按1]退出")
		else:
			path=input("配置路径: ").strip()
			print("[按1]退出")
		
			
		if path=="1":
			break
		try:
			if path[0] == "\"" and path[-1] == "\"" or path[0] + path[-1] == "\'\'":
				path = path[1:-1]
		except:
			pass
		if isDirFile(path)==1:
			cmdConfig="set path=%%path%%;%s"%path
			if isDirFile(os.path.join(path,'std-mpv.exe'))==-1:
			
				if path==configPath:
					globalCmd=cmdConfig
					return
				
				try:
					CMD(cmdConfig)
					print("\n配置成功")
				except:
					print("\n配置失败")
				break
			else:
				print("\n识别该路径可能有误")
				try:
					CMD(cmdConfig)
					print("\n已配置")
				except:
					print("\n配置失败")
			break
		print("[按1]退出")

			

	
def getList(str,list0):
	length=len(list0)
	lengthStr=["%s"%(i+1) for i in range(length)]
	CMD("cls&@echo. &@echo. &@echo %s:"%(" "*(pre-4)+str))
	
	for i in range(length):
		print(" "*pre,i+1,":  ",list0[i])
	while length:
		oth=input("\n%s选中："%(" "*(pre-4))).strip()
		if oth in lengthStr:
			return int(oth)-1
		else:
			print("\n错误输入，请重输:")
		
def isDirFile(path):
	if not os.path.exists(path):
		print("无效路径")
		return 0
	if os.path.isdir(path):
		return 1
	else:
		return -1
		
def func_get_filePath_fileName_fileExt(path):
    (filepath,tempfilename) = os.path.split(path);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension

def player(path):
	while True:
		if isDirFile(path)==1:
			list1=os.listdir(path)
			
			oth=getList(str=os.path.split(path)[1],list0=list1)
			path=os.path.join(path,list1[oth])
		elif isDirFile(path)==-1:
			fn=func_get_filePath_fileName_fileExt(path)
			CMD("cls&@title %s &@echo %s is on the air now..."%(fn[1],fn[1]+fn[-1]))
			try:
				if globalCmd:
					if "&" not in path and " " not in path:
						CMD("@%s&@std-mpv %s"%(globalCmd,path))
					else:
						CMD("@title error&@echo.")
						print("\n\n%s\n\n路径中不能包含空格\" \"与\"&\"字符"%path)
						input("")
						main()
				else:
					CMD("std-mpv %s"%path)
			except:
				CMD("cls&@title failed")
				print("\n未经授权的错误配置")
			break
		elif isDirFile(path)==0:
			break
			
def _str_(string,oth=''):
	#error for "str"[string_variable_name]
	return str(string)

def otherFiles():
	CMD("cls&title otherFiles")
	path=input("\n\n路径： ").strip()
	try:
		if path[0] == "\"" and path[-1] == "\"" or path[0] + path[-1] == "\'\'":
			path = path[1:-1]
	except:
		pass
	player(path)
	input("\n...")
	main()
	return
	
def URLs():
	CMD("cls&title URLs")
	url=input("\n\nURL： ").strip()
	try:
		if url[0] == "\"" and url[-1] == "\"" or url[0] + url[-1] == "\'\'":
			url = url[1:-1]
	except:
		pass
	print("\n准备就绪 尝试播放...")
	try:
		if globalCmd:
			if "&" not in path and " " not in path:
				CMD("@%s&@std-mpv %s"%(globalCmd,url))
			else:
				CMD("@title error&@echo.")
				print("\n\n%s\n\n路径中不能包含空格\" \"与\"&\"字符"%path)
				input("")
				main()
		else:
			CMD("std-mpv %s"%url)
	except:
		print("404")
	input("\n...")
	main()
	return
	
def getDictStr():
	if not os.path.exists(path):
		if not os.path.exists(os.path.split(path)[0]):
			os.makedirs(os.path.split(path)[0])
		with open(path,'wb')as f:
			f.write(b'')
	else:
		with open(path,'rb')as f:
			dict1=f.read().strip()
		if dict1=="":
			return dict1
		else:
			return decStr(dict1)

def writeDictStr(str):
	global path
	if not os.path.exists(path):
		if not os.path.exists(os.path.split(path)[0]):
			os.makedirs(os.path.split(path)[0])
		with open(path,'wb')as f:
			f.write(b'')
	with open(path,'wb')as f:
			f.write(encStr(str))
	
def printDict():
	CMD("cls&title #&echo.")
	dictStr=getDictStr()
	if dictStr:
		dict0=eval(dictStr)
	else:
		print("#空列表")
		pause=input("\n按任意键返回主界面...")
		main()
		return 	
	index=0
	str='\n'
	dictLink=linkDict(dict0)
	for i in dictLink:
		index+=1
		str+="%s[%s]%s%s:%s\n"%(" "*pre,index," "*6,dictLink["%s"%index],dict0[dictLink["%s"%index]])
	print(str)
	input("")
	main()
	
def removeList():
	dictStr=getDictStr()
	if dictStr:
		dict0=eval(dictStr)
	else:
		print("空列表|无可移除项")
		pause=input("\n按任意键返回主界面...")
		main()
		return 
		
	index=0
	str='\n'
	dictLink=linkDict(dict0)
	for i in dictLink:
		index+=1
		str+="%s[按%s]%s移除%s列表...\n"%(" "*pre,index," "*6,dictLink["%s"%index])
		
	str+="%s[按其它键]%s退出\n"%(" "*pre," "*1)
	
	print(str)
	
	dict1=dict0
	
	for i in dictLink:
		list0=input("%s选中： "%(" "*(pre))).strip()
		
		if list0 in dictLink:
			
			dict1.pop(dictLink[list0],'此项已删除')
			#print(dict1)
		
			try:
				if dict1=={}:
					str1=''
				else:
					str1=_str_(dict1)
				writeDictStr(str1)
				print("删除%s成功"%dictLink[list0])
			except:
				print("删除%s失败"%dictLink[list0])
			
		else:
			print(0)
			break
	input("\n：")
	main()
	return
		
	
def addList():
	dictStr=getDictStr()
	if dictStr:
		dict0=eval(dictStr)
	else:
		dict0={}
	for i in range(100):
		listName=input("列表名： ").strip()
		listPath=input("路径： ").strip()
		try:
			if listPath[0] == "\"" and listPath[-1] == "\"" or listPath[0] + listPath[-1] == "\'\'":
				listPath = listPath[1:-1]
		except:
			pass
		
		dict0[listName]=listPath
		str0=_str_(dict0)
		writeDictStr(str0)
		try:
			str0=_str_(dict0)
			writeDictStr(str0)
			if not os.path.exists(listPath):
				print("{提示: 无效路径}\n")
			print("\n%s: %s\n配置成功\n"%(listName,listPath))
		except:
			print("\n%s: %s\n配置失败.\n"%(listName,listPath))
		print("\n\n")
		print("%s[*]   退出\n"%(" "*pre))
		print("%s[1]   继续\n"%(" "*pre))
		oth=input("%s选中: "%(" "*pre)).strip()
		if oth=="1":
			CMD("cls&@echo.")
			continue
		else:
			break
	input("\n...")
	main()
	return
		
def defaultDict():
	for i in range(100):
		CMD("cls&title adjust the list &@echo.")
		try:
			print("%s[0]%sremove\n"%(" "*pre," "*4))
			print("%s[1]%sadd\n"%(" "*pre," "*4))
			Tail = input("%s选中： "%(" "*(pre))).strip()
			if Tail=="lsw":
				printDict()
				return
			Tail=int(Tail)
			if Tail==0 or Tail==1:
				break
			else:
				print("输入有误")
		except:
			print("输入有误")
		if i == 99:
			print("error")
			exit()
	if Tail == 0:
		CMD("cls&title #Remove&@echo.")
		removeList()
	else:
		CMD("cls&title #Add&@echo.")
		addList()

def linkDict(dict0):
	index=0
	dict1={}
	for i in dict0:
		index+=1
		dict1["%s"%index]=i
	return dict1
		
def makePrint(dictLink,dict0):
	index=0
	str0='\n'
	dict1={}
	
	for i in dictLink:
		index+=1
		str0+="%s[按%s]%s进入%s列表...\n"%(" "*pre,index," "*space,dictLink["%s"%index])
		dict1[i]=dict0[dictLink[i]]
	
	
	index+=1
	dict1["%s"%index]=otherFiles
	str0+="%s[按%s]%s选取文件播放...\n"%(" "*pre,index," "*space)
	
	index+=1
	dict1["%s"%index]=URLs
	str0+="%s[按%s]%s选取URL播放...\n"%(" "*pre,index," "*space)
	
	index+=1
	dict1["%s"%index]=defaultDict
	str0+="%s[按%s]%s调整列表\n"%(" "*pre,index," "*space)
	
	index+=1
	dict1["%s"%index]=help
	str0+="%s[按%s]%s获取帮助\n"%(" "*pre,index," "*space)
	
	str0+="%s[按其它键]%s退出\n"%(" "*pre," "*(space-5))
	
	print(str0)
	return dict1

def help():
	CMD("title help&@echo.")
	dictHelp={"按键":"效果","Enter":"   ","RIGHT":"前进 5 秒","LEFT":"后退 5 秒","UP":"前进 60 秒","DOWN":"后退 60 秒","[":"0.9091 倍速播放",
	"]":"1.1 倍速播放","{":"0.5 倍速播放","}":"2.0 倍速播放","Backspace":"还原到 1.0 倍速","Space/p":"播放/暂停",".":"下一帧",",":"上一帧","9//":"音量 -2",
	"0/*":"音量 +2","1":"对比度 -1","2":"对比度 +1","3":"亮度 -1","4":"亮度 +1","5":"Gamma 值 -1","6":"Gamma 值 +1","7":"饱和度 -1","8":"饱和度 +1",
	"l":"设置/清除 A-B 循环点","j|J":"选择字幕","#":"切换声道","q":"退出","Enter":"   ","[路径:]":"{可通过拖拽文件至此输入}","[注意事项]":"{路径中不能包含\"&\"与\" \"字符}","[配置路径]":"{D:\std: std-conf.dll{std-mpv|.conf}}"}
	
	for i in dictHelp:
		if "路径"in i or "注意" in i:
			str="%s%s%s%s"%(' '*pre,i,' '*(space-len(i)),dictHelp[i])
		elif i=="Enter":
			str="\n"
		else:
			str="%s%s%s%s"%(' '*pre,i,' '*(space*3-len(i)),dictHelp[i])
		print(str)
		
	input("")
	main()

	
def main():
	print("欢迎回来")
	CMD("title welcome Lo")
	
	configMpv()
	
	dictStr=getDictStr()
	if dictStr:
		dict0=eval(dictStr)
	else:
		dict0={}
		
	dictLink=linkDict(dict0)
	dict1=makePrint(dictLink=dictLink,dict0=dict0)
	
	list0=input("\n%s选中： "%(" "*(pre+8))).strip()
	
	if list0=="lsw":
		CMD("title feedback")
		print("\n\n**: ***")
		input("..")
		main()
		
		
	if list0 in dict1:
		try:
			dict1[list0]()
		except:
			player(dict1[list0])
		input("..")
		main()
	else:
		exit()

space=10
pre=20
path=r"D:\std\std-conf.dll"
configPath=r"D:\std"
globalCmd=0
for i in range(1000):
	try:
		main()
	except:
		print(i+1)
	