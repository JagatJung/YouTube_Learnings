#===============import libraries, some are custom installled=================
import json
from typing import Any
import pandas as pd
import streamlit as st
import yfinance as yf
import numpy as np
import bs4 as bs

#========================side bar code=-========================
st.sidebar.header("Chose a coin name")
coin_list=['RSX', 'VXX', 'UVXY', 'VIXY', 'IEFA', 'ITB', 'ITA', 'USMV', 'FLOT', 'ARKG', 'SVXY', 'GOVT', 'USHY', 'EFV', 'ICSH', 'INDA', 'EZU', 'IGV', 'REM', 'JPST', 'IDV', 'PICK', 'NOBL', 'PAVE', 'DNOV', 'QUAL', 'MOAT', 'COWZ', 'FCPI', 'IEO', 'RYLD', 'TAIL', 'ESGV', 'HFGO', 'OILK', 'ARKQ', 'EFAV', 'ACWV', 'SLVP', 'XBTF', 'MTUM', 'VLUE', 'UFEB', 'ARKX', 'VUSB', 'BBEU', 'IGE', 'HYD', 'VNM', 'DIVB', 'VSGX', 'EEMV', 'FBCV', 'BBUS', 'GVAL', 'NJUL', 'TOKE', 'PTLC', 'FMIL', 'ITM', 'TMFC', 'IFRA', 'BBAX', 'BBJP', 'ICF', 'AAAU', 'FBCG', 'RSXJ', 'CBOE', 'SMDV', 'HEFA', 'BBIN', 'EFG', 'EMHY', 'NEAR', 'BUFF', 'ECH', 'IGHG', 'VIXM', 'NULV', 'REGL', 'BBRE', 'SYLD', 'BFEB', 'WUGI', 'FDG', 'IYJ', 'VOTE', 'PRNT', 'IYZ', 'KWT', 'GTIP', 'IZRL', 'CALF', 'PJUL', 'PAWZ', 'EMGF', 'BBCA', 'IYT', 'FGRO', 'VFVA', 'JEMA', 'FMAG', 'OMFL', 'PTMC', 'BUFT', 'ACIO', 'TMFM', 'CNYA', 'NULG', 'PBUS', 'DRSK', 'FSMO', 'ESML', 'PTNQ', 'TMFG', 'BUFG', 'JCPB', 'FPRO', 'FRDM', 'TTAI', 'FJAN', 'IBHC', 'SMIN', 'FCTR', 'ALFA', 'CSM', 'PTEU', 'OUSA', 'NUSC', 'DALT', 'NURE', 'IETC', 'CEFS', 'VFMV', 'VXZ', 'ICVT', 'GCOW', 'PSMM', 'IAGG', 'QVAL', 'JMST', 'DDLS', 'WBAT', 'PMAR', 'CEMB', 'GVI', 'IQDG', 'JBBB', 'DJAN', 'PAUG', 'DJUL', 'NUMV', 'DFNL', 'EYLD', 'DUSA', 'AFIF', 'SMI', 'PMAY', 'ADME', 'IBMN', 'PFEB', 'FRNW', 'HYDB', 'LVHI', 'PJAN', 'BUFD', 'SMMV', 'SHYD', 'FCLD', 'FLQM', 'LKOR', 'FLDR', 'HYHG', 'CTRU', 'JPHY', 'PNOV', 'AMER', 'DAUG', 'KNG', 'OSCV', 'HEGD', 'EFNL', 'HSRT', 'IBHE', 'SMB', 'MLN', 'SVAL', 'FLHY', 'IEFN', 'FOCT', 'FLQL', 'FDEC', 'VFMO', 'PBTP', 'PEX', 'VFQY', 
'IYLD', 'ALTS', 'DDWM', 'XJH', 'XJR', 'BALT', 'ESG', 'PWS', 'FDEM', 'QTJL', 'FDRV', 'OUSM', 'GMOM', 'DWLD', 'EPRF', 'PBSM', 'NOCT', 'FFEB', 'ESCR', 'BBSA', 'MOTI', 'GCLN', 'HELX', 'BMAR', 'ATMP', 'VCEB', 'GSEW', 'XTJL', 'FPFD', 'HEEM', 'TYA', 'NETZ', 'WDNA', 'PUNK', 'IGEB', 'LEAD', 'ZECP', 'DMAR', 'IVAL', 'DFEB', 'FAUG', 'PAPR', 'OMFS', 'NUMG', 'DURA', 'FLBL', 'ENOR', 'MSTB', 'PBND', 'EAOA', 'LYFE', 'FDEV', 'DUDE', 'LUXE', 'OGIG', 'SMMD', 'EWGS', 'IDHD', 'KNGS', 'IMOM', 'LQDI', 'EFAD', 'TMFS', 'XSHD', 'MAGA', 'IEIH', 'XVV', 'GAA', 'VFMF', 'MINN', 'OEUR', 'XSHQ', 'XMPT', 'DFND', 'BMAY', 'FUNL', 'CLSE', 'DFHY', 'GDMN', 'GLDB', 'KOCT', 'TRTY', 'VAMO', 'EDEN', 'BUFR', 'SATO', 'EMTL', 'BUYZ', 'DINT', 'IAUF', 'BLKC', 'BJAN', 'EWUS', 'SEPZ', 'IEHS', 'TTAC', 'BJUL', 'IBHD', 'VMOT', 'POCT', 'VWID', 'MRGR', 'USMF', 'WIL', 'IGRO', 'PSEP', 'HYXU', 'IVDG', 'STLG', 'GSUS', 'EGIS', 'VIRS', 'ADFI', 'ESEB', 'ESHY', 'HYIN', 'IECS', 'LIV', 'IEDI', 'NUDV', 'PSMG', 'FDHT', 'FYLD', 'IBMM', 'ESGG', 'FIBR', 'IVRA', 'IVSG', 'NUDM', 'TDV', 'UJAN', 'UOCT', 'WFHY', 'WTAI', 'BOB', 'HYMU', 'TMAT', 'AGT', 'IQM', 'BAPR', 'GSID', 'QDEC', 'XTJA', 'FJUL', 'PDEC', 'SHAG', 'EUDV', 'FEDX', 'IBML', 'IBMP', 'IDME', 'JPIB', 'AESR', 'BOSS', 'DFRA', 'MBCC', 'IBHF', 'IEME', 'FLIA', 'GSEE', 'IBMO', 'IMFL', 'IVLC', 'MSVX', 'NJAN', 'QCON', 'SFIG', 'TSJA', 'WFIG', 'APXH', 'AVDG', 'BAUG', 'BDEC', 'BJUN', 'BLDG', 'BOCT', 'BSEP', 'DDEC', 'EOPS', 'EURZ', 'FFTI', 'FLV', 'FMAR', 'FMAY', 'FOMO', 'FSEP', 'GEMD', 'GHYG', 'GOVZ', 'HCRB', 'IBHB', 'ICOW', 'JMUB', 'MEAR', 'MOTG', 'NUEM', 'PSFO', 'PSMB', 'PSMC', 'PSMD', 'PSMO', 'QMOM', 'QTAP', 'RODE', 'THY', 'TILT', 'TSOC', 'VFLQ', 'XDAP', 'XTOC', 'YPS', 'ACSI', 'APRZ', 'ARCM', 'AUGZ', 'AVDR', 'BGLD', 'BNOV', 'BUFB', 'CFCV', 'CVAR', 'DAPR', 'DBJA', 'DBOC', 'DECZ', 'DFNV', 'DJUN', 'DMAY', 'DOCT', 'DSEP', 'DSJA', 'DSOC', 'EAOK', 'EAOM', 'EAOR', 'EMDV', 'EMSH', 'EUCG', 'FAIL', 'FAPR', 
'FEBZ', 'FFHG', 'FFSG', 'FFTG', 'FJUN', 'FLQS', 'FLTN', 'FNOV', 'FPAG', 'FUT', 'GHTA', 'GPAL', 'GSST', 'HEET', 'HSUN', 
'HYBL', 'IBHG', 'IBMQ', 'IGLD', 'IMLP', 'ISVL', 'JANZ', 'JULZ', 'JUNZ', 'KAPR', 'KJAN', 'KJUL', 'MAAX', 'MAMB', 'MARZ', 'MAYZ', 'MBBB', 'MBND', 'MDEV', 'MFUL', 'MIG', 'MOHR', 'MOTE', 'MPRO', 'MRSK', 'MSMR', 'NAPR', 'NOVZ', 'NULC', 'OBND', 'OCTZ', 'PBDM', 'PBEE', 'PJUN', 'PLRG', 'PLTL', 'PSCJ', 'PSCQ', 'PSCW', 'PSCX', 'PSFD', 'PSFF', 'PSFJ', 'PSFM', 'PSMJ', 'PSMR', 'PXUS', 'QJUN', 'QLC', 'QMAR', 'QPFF', 'QSPT', 'QTJA', 'QTOC', 'RDFI', 'REC', 'RESD', 'RESE', 'RODI', 'ROMO', 'RSEE', 'RTAI', 'RULE', 'SECT', 'SPMV', 'STLV', 'STOT', 'TBJL', 'TCTL', 'TFJL', 'TMDV', 'TRDF', 'UAPR', 'UAUG', 'UDEC', 'UJUL', 'UJUN', 'UMAR', 'UMAY', 'UNOV', 'USEP', 'USEQ', 'WLDR', 'XBAP', 'XBJA', 'XBJL', 'XBOC', 'XDAT', 'XDEC', 'XDJA', 'XDJL', 'XDOC', 'XDQQ', 'XDSQ', 'XJUN', 'XTAP', 'YDEC', 'YJUN', 'YMAR', 'YSEP', '', '']
coin_list=np.unique(coin_list)
selected_comp=st.sidebar.selectbox('Company', coin_list )

#===============Writing headers===============
#here ** is used too make text bold and # is used to make text header
st.write("""
# Simple stock price app
Shown are the stock **closing prices** and value of google!
""")

if selected_comp=="":
    selected_comp="IBMQ"
#===========we make a dataframe which collects all the data
tickerData = yf.Ticker(selected_comp)

#collect the data 
tickerDf=tickerData.history()


#==========data showing from the json returned by tickerData
st.header(tickerData.info['longName'])

#printing the highest data
highest_price= tickerData.info['dayHigh']
new_title = 'The highest price today was: <p style="font-family:sans-serif; color:Green; font-size: 18px;">'+str(highest_price)+'</p>'
st.markdown(new_title, unsafe_allow_html=True)

#printing the lowest data
lowest_price= tickerData.info['dayLow']
new_title = 'The lowest price today was: <p style="font-family:sans-serif; color:red; font-size: 18px;">'+str(lowest_price)+'</p>'
st.markdown(new_title, unsafe_allow_html=True)



res=np.std(tickerDf.High) - np.std(tickerDf.Low)
if(res>0):
    new_title = '<p style="font-family:sans-serif; color:green; font-size: 18px;"> You shall buy the stocks</p>'
    st.markdown(new_title, unsafe_allow_html=True)
else:
    new_title = '<p style="font-family:sans-serif; color:red; font-size: 18px;">You shall not buy stocks</p>'
    st.markdown(new_title, unsafe_allow_html=True)


st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)

