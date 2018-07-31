# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 14:11
# @Author  : buf
# @Email   : niuxinzan@cennavi.com.cn
# @File    : RTIC.py
# @Software: PyCharm
class Rtic(object):
    def __init__(self,data_line):
        dataArr=str(data_line).split(",")
        self.__areaId=dataArr[0]
        self.__mapVersion=dataArr[1]
        self.__timeStamp=dataArr[2]
        self.__meshID=dataArr[3]
        self.__number = dataArr[4]
        self.__layer = dataArr[5]
        self.__rticKind = dataArr[6]
        self.__rricTravelTime = dataArr[7]
        self.__LOS = dataArr[8]
        self.__sectionCount = dataArr[9]
    @property
    def areaId(self):
        return  self.__areaId
    @areaId.setter
    def areaId(self,areaId):
        self.__areaId=areaId

    @property
    def mapVersion(self):
        return  self.__mapVersion
    @mapVersion.setter
    def mapVersion(self,mapVersion):
        self.__mapVersion=mapVersion
    @property
    def timeStamp(self):
        return  self.__timeStamp
    @timeStamp.setter
    def timeStamp(self,timeStamp):
        self.__timeStamp=timeStamp
    @property
    def meshID(self):
        return  self.__meshID
    @meshID.setter
    def meshID(self,meshID):
        self.__meshID=meshID
    @property
    def number(self):
        return  self.__number
    @number.setter
    def number(self,number):
        self.__number=number
    @property
    def layer(self):
        return  self.__layer
    @layer.setter
    def layer(self,layer):
        self.__layer=layer
    @property
    def rticKind(self):
        return  self.__rticKind
    @rticKind.setter
    def rticKind(self,rticKind):
        self.__rticKind=rticKind
    @property
    def rricTravelTime(self):
        return  self.__rricTravelTime
    @rricTravelTime.setter
    def rricTravelTime(self,rricTravelTime):
        self.__rricTravelTime=rricTravelTime
    @property
    def LOS(self):
        return  self.__LOS
    @LOS.setter
    def LOS(self,LOS):
        self.__LOS=LOS
    @property
    def sectionCount(self):
        return  self.__sectionCount
    @sectionCount.setter
    def sectionCount(self,sectionCount):
        self.__sectionCount=sectionCount
    def __str__(self):
        return self.areaId+','+self.rticKind+','+self.meshID+","+self.number
