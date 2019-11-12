##########################################################
### Rohde & Schwarz Automation for demonstration use.
###
### Title  : Direct Digital Modulation Example
### Author : mclim
### Date   : 2019.11.12
###
##########################################################
### User Entry
##########################################################
FSW_IP   = '192.168.1.109'
Freq     = 28e9
ChBW     = 100
numMeas  = 10

##########################################################
### Code Overhead: Import and create objects
##########################################################
from rssd.VSA.VSA_K70       import VSA

FSW = VSA().jav_Open(FSW_IP)  #Create FSW Object

##########################################################
### Code Start
##########################################################
FSW.Init_VSA()
FSW.Set_Freq(Freq)
FSW.Set_VSA_Filter_Type('RC')
FSW.Set_VSA_Symbol_Rate(123456)
FSW.Set_VSA_Filter_Alpha(0.30)
FSW.Set_VSA_Mod_Type('QAM')
FSW.Set_VSA_Mod_QAM(64)
FSW.Set_VSA_Capture_Length(4000)

##########################################################
### Cleanup Automation
##########################################################
FSW.jav_Close()
