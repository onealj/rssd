###############################################################################
### Rohde & Schwarz Automation for demonstration use.
### Date   : mclim.2020.05.12
###############################################################################
SMW_IP      = '192.168.1.114'
FSW_IP      = '192.168.1.109'
CMP_IP      = '192.168.1.160'
UserDir     = '2020.05.12-CMPEval'
FSW_Rx      = True
freqArry    = [24e9, 26e9, 28e9, 39e9]
pwrArry     = range(-40,10,1)                                       #Power Array

###############################################################################
### Overhead
###############################################################################
from rssd.VSG.NR5G_K144     import VSG                              #pylint: disable=E0611,E0401
from rssd.VSA.NR5G_K144     import VSA                              #pylint: disable=E0611,E0401
from rssd.RCT.NR5G_KM601    import RCT                              #pylint: disable=E0611,E0401
from rssd.FileIO            import FileIO                           #pylint: disable=E0611,E0401
import timeit

OFile = FileIO().makeFile(__file__)
SMW = VSG().jav_Open(SMW_IP)                                        #Create SMW Object
if FSW_Rx:
    FSW = VSA().jav_Open(FSW_IP)                                    #Create FSW Object
else:
    CMP = RCT().jav_Open(CMP_IP)                                    #Create CMP Object

class dataClass():
    pass

def ReadSMW_Settings():
    NR5G.freq               = SMW.Get_Freq()
    NR5G.Direction          = SMW.Get_5GNR_Direction()
    NR5G.NR_FreqRng         = SMW.Get_5GNR_FreqRange()
    NR5G.NR_ChBW            = SMW.Get_5GNR_ChannelBW()
    NR5G.NR_TF              = SMW.Get_5GNR_TransPrecoding()
    NR5G.NR_SubSp           = SMW.Get_5GNR_BWP_SubSpace()
    NR5G.NR_RB              = SMW.Get_5GNR_BWP_ResBlock()
    NR5G.NR_RBO             = SMW.Get_5GNR_BWP_ResBlockOffset()
    NR5G.NR_Ch_RB           = SMW.Get_5GNR_BWP_Ch_ResBlock()
    NR5G.NR_Ch_RBO          = SMW.Get_5GNR_BWP_Ch_ResBlockOffset()
    NR5G.NR_Ch_DMRS_Config  = SMW.Get_5GNR_BWP_Ch_DMRS_Config()
    NR5G.NR_Ch_DMRS_1st     = SMW.Get_5GNR_BWP_Ch_DMRS_1stDMRSSym()
    NR5G.NR_Ch_DMRS_AddPost = SMW.Get_5GNR_BWP_Ch_DMRS_AddPosition()
    NR5G.NR_Ch_DMRS_Mapping = SMW.Get_5GNR_BWP_Ch_DMRS_Mapping()
    NR5G.NR_Ch_DMRS_MSymbL  = SMW.Get_5GNR_BWP_Ch_DMRS_MSymbLen()
    NR5G.NR_Ch_DMRS_RelPwr  = SMW.Get_5GNR_BWP_Ch_DMRS_RelPwr()
    NR5G.NR_Ch_DMRS_SGMeth  = SMW.Get_5GNR_BWP_Ch_DMRS_SeqGenMeth()
    NR5G.NR_Ch_DMRS_SGSeed  = SMW.Get_5GNR_BWP_Ch_DMRS_SeqGenSeed()
    NR5G.NR_Mod             = SMW.Get_5GNR_BWP_Ch_Modulation()

def Rx_Init():
    if FSW_Rx:
        FSW.Init_5GNR()
    else:
        CMP.Init_5GNR()

def Rx_5GNR_Config():
    if FSW_Rx:
        FSW.Set_Freq(NR5G.freq)
        FSW.Set_5GNR_Direction(NR5G.Direction)
        FSW.Set_5GNR_FreqRange(NR5G.NR_FreqRng)
        FSW.Set_5GNR_ChannelBW(NR5G.NR_ChBW)
        FSW.Set_5GNR_TransPrecoding(NR5G.NR_TF)
        FSW.Set_5GNR_BWP_SubSpace(NR5G.NR_SubSp)
        FSW.Set_5GNR_BWP_ResBlock(NR5G.NR_RB)
        FSW.Set_5GNR_BWP_ResBlockOffset(NR5G.NR_RBO)
        FSW.Set_5GNR_BWP_Ch_ResBlock(NR5G.NR_Ch_RB)
        FSW.Set_5GNR_BWP_Ch_ResBlockOffset(NR5G.NR_Ch_RBO)
        FSW.Set_5GNR_BWP_Ch_Modulation(NR5G.NR_Mod)
        FSW.Set_5GNR_BWP_Ch_DMRS_Config(NR5G.NR_Ch_DMRS_Config)
        # FSW.Set_5GNR_BWP_Ch_DMRS_1stDMRSSym(NR5G.NR_Ch_DMRS_1st)
        FSW.Set_5GNR_BWP_Ch_DMRS_AddPosition(NR5G.NR_Ch_DMRS_AddPost)
        FSW.Set_5GNR_BWP_Ch_DMRS_Mapping(NR5G.NR_Ch_DMRS_Mapping)
        FSW.Set_5GNR_BWP_Ch_DMRS_MSymbLen(NR5G.NR_Ch_DMRS_MSymbL)
        FSW.Set_5GNR_BWP_Ch_DMRS_RelPwr(NR5G.NR_Ch_DMRS_RelPwr)
        # FSW.Set_5GNR_BWP_Ch_DMRS_SeqGenMeth(NR5G.NR_Ch_DMRS_SGMeth)
        # FSW.Set_5GNR_BWP_Ch_DMRS_SeqGenSeed(NR5G.NR_Ch_DMRS_SGSeed)
    else:
        CMP.Set_5GNR_Freq(NR5G.freq)

def Meas_EVM():
    if FSW_Rx:
        FSW.Set_Autolevel()
        FSW.Get_5GNR_Params_EVM()
    else:
        pass
###############################################################################
### Code Start
###############################################################################
LoopParam   = 'State,Model,SMW_Fre,SMW_Pwr'
WaveParam   = 'ChBW,SubSp,RB,Mod,TF'
SwpParam    = FSW.Get_Params_Sweep(1)
AttnParam   = FSW.Get_Params_Amp(1)
EVMParam    = FSW.Get_5GNR_Params_EVM(1)
TimeParam   = 'AlTime,MeasTime,TotalTIme'
Header      = f'{LoopParam},{WaveParam},{AttnParam},{EVMParam},{TimeParam}'
OFile.write(Header)

### Instr Init
NR5G        = dataClass()
SMW.Set_OS_Dir(UserDir)
saveArry = SMW.Get_OS_FileList('savrcltxt')
Rx_Init()

for saveState in saveArry:
    SMW.Set_Setting(f'{UserDir}/{saveState}')
    ReadSMW_Settings()
    Rx_5GNR_Config()
    for freq in freqArry:
        SMW.Set_Freq(freq)
        for pwr in pwrArry:
            SMW.Set_RFPwr(pwr)
            tick = timeit.default_timer()                       #Tick Begin meas
            EVM = Meas_EVM
            tockA = timeit.default_timer()                      #Tick Auto Lev
            tockB    = timeit.default_timer()                   #Tick Meas
            ALTime   = (tockA-tick)
            TotTime  = (tockB-tick)
            TestTime = TotTime - ALTime

            ### Log Data
            CurrFreq    = FSW.Get_5GNR_CC_Freq()
            LoopParam   = f'{saveState},{FSW.Model},{freq},{pwr:3d}'
            NR5GParam   = f'{NR5G.NR_ChBW},{NR5G.NR_RB},{NR5G.NR_SubSp},{NR5G.NR_Mod},{NR5G.NR_TF}'
            AttnParam   = FSW.Get_Params_Amp()
            OutStr      = f'{LoopParam},{NR5GParam},{AttnParam},{EVM},{TimeParam}'
            OFile.write(OutStr)

