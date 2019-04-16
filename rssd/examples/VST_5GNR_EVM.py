##########################################################
### Rohde & Schwarz Automation for demonstration use.
###
### Title  : Timing SCPI Commands Example
### Author : mclim
### Date    : 2018.05.24
### Steps  : 
###
##########################################################
### User Entry
##########################################################
SMW_IP      = '192.168.1.114'
FSW_IP      = '192.168.1.108'
FreqArry    = [6e9]
pwrArry     = [-5]
pwrArry     = range(-50,8,1)
NR_Dir      = 'UL'
NR_ChBW     = 100
NR_RB       = 132               #100:060:132  200:060:264  <Not Appli>
subCarr     = [60]            #100:120:066  200:120:132  400:120:264
waveparam   =[[100,60,132],
              [100,120,66]]
subFArry    = [1]
modArry     = ['QPSK', 'QAM64'] #QPSK; QAM16; QAM64; QAM256; PITB
numMeas     = 10
AutoLvl     = 1                #0:AutoEVM 1:AutoLevel
DFT_S_OFDM  = 'OFF'

##########################################################
### Code Overhead: Import and create objects
##########################################################
from datetime               import datetime     #pylint: disable=E0611,E0401
from rssd.FileIO            import FileIO       #pylint: disable=E0611,E0401
from rssd.VST_5GNR_K144     import VST          #pylint: disable=E0611,E0401
import time
import ctypes  # An included library with Python install.   
OFile = FileIO().makeFile(__file__)

##########################################################
### Code Start
##########################################################
NR5G = VST().jav_Open(SMW_IP,FSW_IP,OFile)
NR5G.NR_TF      = DFT_S_OFDM
NR5G.NR_Dir     = NR_Dir
NR5G.Freq       = FreqArry[0]

##########################################################
### Measure Time
##########################################################
#sDate = datetime.now().strftime("%y%m%d-%H:%M:%S.%f") #Date String
OFile.write('Iter,Freq,K144Crest,K144Pwr,EVM,ChBW,Waveform,SubSp,Mod,Pwr,SubFram,Attn,Preamp,RefLvl,AutoLvl,AlTime,CrestF,P10_00,P01_00,P00_10,P00_01,CmdTime')

NR5G.FSW.Init_5GNR()
NR5G.FSW.Set_5GNR_EVMUnit('DB')
NR5G.FSW.Set_Trig1_Source('EXT')
NR5G.FSW.Set_SweepCont(0)
NR5G.FSW.Init_CCDF()
NR5G.FSW.Set_YIG(0)
NR5G.FSW.Set_CCDF_BW(120e6)
NR5G.FSW.Set_CCDF_Samples(2e6)
NR5G.FSW.Set_Trig1_Source('IMM')
NR5G.FSW.Set_SweepCont(0)

for i in range(numMeas):                                        #Loop: Measurements
    for mod in modArry:                                         #Loop: Modulation
        for param in waveparam:                                    #Loop: Subcarrier
            NR5G.NR_ChBW    = param[0]
            NR5G.NR_SubSp   = param[1]
            NR5G.NR_Mod     = mod
            NR5G.NR_RB      = param[2]
            for freq  in FreqArry:                              #Loop: Frequency
                NR5G.Freq     = FreqArry[0]
                NR5G.Set_5GNR_All()                             #[[[Make Waveform]]]
                NR5G.FSW.Init_CCDF()
                NR5G.FSW.Set_InitImm()
                ccdf = NR5G.FSW.Get_CCDF()
                print(f'Freq:{freq} RFBW:{NR5G.NR_ChBW} SubC:{NR5G.NR_SubSp} Mod:{NR5G.NR_Mod}')
                #ctypes.windll.user32.MessageBoxW(0, "Verify", "Please Verify Waveform", 1)
                for pwr in pwrArry:                             #Loop: Power
                    NR5G.FSW.Init_5GNR()
                    NR5G.SMW.Set_RFPwr(pwr)
                    tickA = datetime.now()
                    if AutoLvl == 1:
                        NR5G.FSW.Set_Autolevel()
                    else:
                        NR5G.FSW.Set_5GNR_AutoEVM()
                    ALTime = datetime.now() - tickA
                    for subFram in subFArry:                    #Loop: Subframe
                        NR5G.FSW.Set_SweepTime((subFram)*1.1e-3)
                        NR5G.FSW.Set_5GNR_SubFrameCount(subFram)
                        tick = datetime.now()
                        NR5G.FSW.Init_5GNR()
                        NR5G.FSW.Set_SweepCont(0)
                        NR5G.FSW.Set_InitImm()
                        EVM = NR5G.FSW.Get_5GNR_EVMParams()
                        Attn = NR5G.FSW.Get_AmpSettings()
                        d = datetime.now() - tick
                        OutStr = f'{i},{freq},{EVM},{NR5G.NR_ChBW},{NR5G.NR_TF},{NR5G.NR_SubSp},{NR5G.NR_Mod},{pwr:3d},{subFram},{Attn},{AutoLvl},{ALTime.seconds:3d}.{ALTime.microseconds:06d},cf:{ccdf},{d.seconds:3d}.{d.microseconds:06d}'
                        OFile.write (OutStr)

##########################################################
### Cleanup Automation
##########################################################
NR5G.jav_Close()