#-*- coding:utf-8 -*-
import os,zipfile

def touch(path):
    pdir = os.path.dirname(path)
    if not os.path.exists(pdir):
        os.makedirs(pdir)
    with open(path, 'a'):
        os.utime(path, None)

def joinConfigPath(index):
    path=os.path.join(index+':\\',std)
    configPath=os.path.join(path,conf)
    return path,configPath

def getConfigPath_():
    winDr=['D','E','F','C']
    for index in winDr:
        path,configPath=joinConfigPath(index)
        if os.path.exists(configPath):
            return path,configPath
    for index in winDr:
        try:
            path,configPath=joinConfigPath(index)
            touch(configPath)
            return path,configPath
        except:
            pass
    index=os.getcwd()[0]
    path,configPath=joinConfigPath(index)
    touch(configPath)
    return path,configPath

def getConfigPath():
    try:
        path,configPath=getConfigPath_()
        return path,configPath
    except Exception as e:
        print("\n\n    throws: %s\n\n"%e)  

def unzip_file(zip_src, winDr):
    if zipfile.is_zipfile(zip_src):     
        zipR = zipfile.ZipFile(zip_src, 'r')
        for file in zipR.namelist():
            zipR.extract(file, winDr)      

std='std'
conf='%s-conf.dll'%std

soL=['std.std','std-temp.std']
exeStr='std.std'

configPath,path=getConfigPath()        
scrPath=os.path.join(configPath,'mpv.conf')  

cwd=os.getcwd()
os.system("@title stdInstaller&@cls&@echo.")


for i in soL:
    thePath=os.path.join(cwd,i)
    if not os.path.exists(thePath):
        print("\n\n\n%s文件缺失: [%s]"%(' '*8,thePath))
        input("\n\n%s安装失败"%(' '*8))
        exit()
    else:
        if i==exeStr:
            unzip_file(thePath,cwd)
        else:
            unzip_file(thePath,configPath[0]+':\\')
        try:
            os.remove(thePath)
        except:
            pass

with open(scrPath,'a',encoding='utf-8')as f:
    scrAdd="#脚本\n--script=\"%s\"  #播完后续播"%path
    f.write(scrAdd)
 
try:
    os.system('\"%s\"'%os.path.join(cwd,'std.exe'))
except:
    pass 
    
input("\n\n\n%sdone%s"%(' '*8))    
    
    