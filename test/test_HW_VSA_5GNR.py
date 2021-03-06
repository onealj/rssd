###############################################################################
### Purpose: rssd.VSA.NR5G_K144 test
###              _   ___        __  _____         _
###             | | | \ \      / / |_   _|__  ___| |_
###             | |_| |\ \ /\ / /    | |/ _ \/ __| __|
###             |  _  | \ V  V /     | |  __/\__ \ |_
###             |_| |_|  \_/\_/      |_|\___||___/\__|
###             Please connect instrument prior 2 test
###############################################################################
### User Entry
###############################################################################
host = '192.168.1.109'                              #Get local machine name

###############################################################################
### Code Start
###############################################################################
import unittest
from rssd.VSA.NR5G_K144     import VSA

class TestGeneral(unittest.TestCase):
    def setUp(self):                                #run before each test
        self.FSW = VSA().jav_OpenTest(host)
        self.FSW.Init_5GNR()

    def tearDown(self):                             #Run after each test
        self.assertEqual(self.FSW.jav_Error()[0],'0')
        self.FSW.jav_Close()

###############################################################################
### <Test>
###############################################################################
    def test_FSW_5GNR_Direction(self):
        self.FSW.Set_5GNR_Direction('UL')
        getVal = self.FSW.Get_5GNR_Direction()
        if self.FSW.connected: self.assertEqual(getVal,'UL')
        self.FSW.Set_5GNR_Direction('DL')
        getVal = self.FSW.Get_5GNR_Direction()
        if self.FSW.connected: self.assertEqual(getVal,'DL')

    def test_FSW_5GNR_Ex_Meas_Multi_CC(self):
        self.FSW.Init_5GNR_Meas('EVM')
        # Configure setup
        self.FSW.Set_5GNR_CellID(1)
        self.FSW.Set_5GNR_SubFrameCount(2)
        self.FSW.Set_5GNR_Result_View('ALL')        # Multi CC results
        self.FSW.Set_5GNR_EVMUnit('DB')
        self.FSW.Get_5GNR_Params_EVM()

    def test_FSW_5GNR_Ex_SEM(self):
        self.FSW.Init_5GNR_SEM()
        self.FSW.Set_5GNR_SEM_Freq(20e9)
        self.FSW.Set_5GNR_SEM_SubBlockNum(1)
        self.FSW.Get_5GNR_SEM()

    def test_FSW_5GNR_FreqRange(self):
        self.FSW.Set_5GNR_Direction('UL')
        self.FSW.Set_5GNR_FreqRange('LOW')
        getVal = self.FSW.Get_5GNR_FreqRange()
        if self.FSW.connected: self.assertEqual(getVal,'LOW')

        self.FSW.Set_5GNR_FreqRange('MIDD')
        getVal = self.FSW.Get_5GNR_FreqRange()
        if self.FSW.connected: self.assertEqual(getVal,'MIDD')

        self.FSW.Set_5GNR_FreqRange('HIGH')
        getVal = self.FSW.Get_5GNR_FreqRange()
        if self.FSW.connected: self.assertEqual(getVal,'HIGH')

    def test_FSW_5GNR_Get_DL(self):
        self.FSW.Set_5GNR_Direction('DL')
        nullVal = self.FSW.Get_5GNR_CC_Freq()
        nullVal = self.FSW.Get_5GNR_Direction()
        nullVal = self.FSW.Get_5GNR_FreqRange()
        nullVal = self.FSW.Get_5GNR_RefA()
        nullVal = self.FSW.Get_5GNR_ChannelBW()
        nullVal = self.FSW.Get_5GNR_TransPrecoding()
        nullVal = self.FSW.Get_5GNR_PhaseCompensate()
        nullVal = self.FSW.Get_5GNR_SSB_SubSpace()
        nullVal = self.FSW.Get_5GNR_BWP_SubSpace()
        nullVal = self.FSW.Get_5GNR_BWP_Count()
        nullVal = self.FSW.Get_5GNR_BWP_ResBlock()
        nullVal = self.FSW.Get_5GNR_BWP_ResBlockOffset()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_Modulation()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_ResBlock()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_ResBlockOffset()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_SymbNum()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_SymbOff()
        if self.FSW.connected: nullVal = self.FSW.Get_5GNR_BWP_Center()
        ### "=DMRS="
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_Config()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_Mapping()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_1stDMRSSym()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_AddPosition()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_MSymbLen()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_SeqGenMeth()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_SeqGenSeed()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_RelPwr()
        ### "=PTRS=")
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_State()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_L()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_K()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_Pow()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_RE_Offset()

    def test_FSW_5GNR_Get_PTRS(self):
        self.FSW.Set_5GNR_Direction('DL')
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_State()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_L()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_K()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_Pow()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_RE_Offset()

    def test_FSW_5GNR_Get_Misc(self):
        self.FSW.Get_5GNR_ACLR()
        self.FSW.Get_5GNR_BWP_SlotNum()
        self.FSW.Get_5GNR_CC_Offset()
        self.FSW.Get_5GNR_Meas_ACLR()


    def test_FSW_5GNR_Get_UL(self):
        self.FSW.Set_5GNR_Direction('UL')
        nullVal = self.FSW.Get_5GNR_CC_Freq()
        nullVal = self.FSW.Get_5GNR_Direction()
        nullVal = self.FSW.Get_5GNR_FreqRange()
        nullVal = self.FSW.Get_5GNR_RefA()
        nullVal = self.FSW.Get_5GNR_ChannelBW()
        nullVal = self.FSW.Get_5GNR_TransPrecoding()
        nullVal = self.FSW.Get_5GNR_PhaseCompensate()
        nullVal = self.FSW.Get_5GNR_SSB_SubSpace()
        ### "=User="
        nullVal = self.FSW.Get_5GNR_BWP_SubSpace()
        nullVal = self.FSW.Get_5GNR_BWP_Count()
        nullVal = self.FSW.Get_5GNR_BWP_ResBlock()
        nullVal = self.FSW.Get_5GNR_BWP_ResBlockOffset()
        ### "==Ch=="
        nullVal = self.FSW.Get_5GNR_BWP_Ch_Modulation()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_ResBlock()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_ResBlockOffset()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_SymbNum()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_SymbOff()
        if self.FSW.connected: nullVal = self.FSW.Get_5GNR_BWP_Center()
        ### "=DMRS="
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_Config()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_Mapping()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_1stDMRSSym()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_AddPosition()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_MSymbLen()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_SeqGenMeth()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_SeqGenSeed()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_DMRS_RelPwr()
        ### "=PTRS=")
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_State()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_L()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_K()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_Pow()
        nullVal = self.FSW.Get_5GNR_BWP_Ch_PTRS_RE_Offset()

    def test_FSW_5GNR_InstrState(self):
        self.FSW.Get_5GNR_TM_Cat()
        self.FSW.Set_5GNR_TM('NR-FR1-TM1_1__FDD_15MHz_30kHz')
        self.FSW.Set_5GNR_savesetting('test')
        self.FSW.Set_5GNR_AllocFile('test')         #mmm
        self.FSW.Set_5GNR_AllocFileSave('test')     #mmm

    def test_FSW_5GNR_Set_DL(self):
        self.FSW.Set_5GNR_Direction('DL')
        self.FSW.Set_5GNR_CC_Num(1)
        self.FSW.Set_5GNR_TransPrecoding('OFF')
        self.FSW.Set_5GNR_PhaseCompensate('ON')
        self.FSW.Set_5GNR_PhaseCompensate_Freq(1e6)
        self.FSW.Set_5GNR_FreqRange('HIGH')
        self.FSW.Set_5GNR_ChannelBW(100)
        self.FSW.Set_5GNR_BWP_SubSpace(120)
        self.FSW.Set_5GNR_BWP_ResBlock(66)
        self.FSW.Set_5GNR_BWP_ResBlockOffset(0)
        self.FSW.Set_5GNR_BWP_Ch_ResBlock(66)
        self.FSW.Set_5GNR_BWP_Corset_ResBlock(66)
        self.FSW.Set_5GNR_BWP_Ch_ResBlockOffset(0)
        self.FSW.Set_5GNR_BWP_Ch_Modulation('QPSK')
        # self.FSW.Set_5GNR_SSB()

    def test_FSW_5GNR_Set_DMRS(self):
        self.FSW.Set_5GNR_BWP_Ch_DMRS_1stDMRSSym(2)
        self.FSW.Set_5GNR_BWP_Ch_DMRS_AddPosition(0)
        self.FSW.Set_5GNR_BWP_Ch_DMRS_Config(1)
        self.FSW.Set_5GNR_BWP_Ch_DMRS_Mapping('A')
        self.FSW.Set_5GNR_BWP_Ch_DMRS_MSymbLen(1)
        self.FSW.Set_5GNR_BWP_Ch_DMRS_RelPwr(0)
        self.FSW.Set_5GNR_BWP_Ch_DMRS_SeqGenMeth('NICD')
        self.FSW.Set_5GNR_BWP_Ch_DMRS_SeqGenSeed(0)

    def test_FSW_5GNR_Set_UL(self):
        self.FSW.Set_5GNR_Direction('UL')
        self.FSW.Set_5GNR_CC_Num(1)
        self.FSW.Set_5GNR_TransPrecoding('OFF')
        self.FSW.Set_5GNR_PhaseCompensate('OFF')
        self.FSW.Set_5GNR_FreqRange('HIGH')
        self.FSW.Set_5GNR_ChannelBW(100)
        self.FSW.Set_5GNR_BWP_SubSpace(120)
        self.FSW.Set_5GNR_BWP_ResBlock(66)
        self.FSW.Set_5GNR_BWP_ResBlockOffset(0)
        self.FSW.Set_5GNR_BWP_Ch_ResBlock(66)
        self.FSW.Set_5GNR_BWP_Corset_ResBlock(66)
        self.FSW.Set_5GNR_BWP_Ch_ResBlockOffset(0)
        self.FSW.Set_5GNR_BWP_Ch_Modulation('QPSK')

###############################################################################
### </Test>
###############################################################################
if __name__ == '__main__':
#coverage run -a -m unittest -b -v test_HW_VSA_5GNR
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneral)
    unittest.TextTestRunner(verbosity=2).run(suite)
