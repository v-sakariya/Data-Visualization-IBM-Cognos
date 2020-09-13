import pandas as pd



readcsv = pd.read_csv('sales_data_sample.csv', encoding="latin1")
readcsv['PRICEEACH'] = round(readcsv['PRICEEACH'], 2)
readcsv['SALES'] = round(readcsv['SALES'], 2)


readcsv['PHONE'] = readcsv['PHONE'].str.replace('.', '')
readcsv['PHONE'] = readcsv['PHONE'].str.replace('+', '')
readcsv['PHONE'] = readcsv['PHONE'].str.replace('-', '')
readcsv['PHONE'] = readcsv['PHONE'].str.replace('(', '')
readcsv['PHONE'] = readcsv['PHONE'].str.replace(')', '')
readcsv['PHONE'] = readcsv['PHONE'].str.replace(' ', '')


readcsv['ORDERDATE'] = readcsv['ORDERDATE'].str.split(" ",1,expand = True)
df = readcsv.fillna({
'ADDRESSLINE2' : 'NA',
'STATE' : 'NA',
'POSTALCODE' : 'NA',
'TERRITORY' : 'NA'

})

mywrite = pd.DataFrame(df, columns=['ORDERNUMBER','QUANTITYORDERED','PRICEEACH',
                                          'ORDERLINENUMBER','SALES','ORDERDATE','STATUS',
                                          'QTR_ID','MONTH_ID','YEAR_ID','PRODUCTLINE',
                                          'MSRP',
                                          'PRODUCTCODE','CUSTOMERNAME','PHONE',
                                          'ADDRESSLINE1',
                                          'ADDRESSLINE2','CITY','STATE','POSTALCODE',
                                          'COUNTRY',
                                          'TERRITORY','CONTACTLASTNAME',
                                          'CONTACTFIRSTNAME',
                                          'DEALSIZE'])

# Writing all rows to csv file
mywrite.to_csv('AllCleanedDataFile.csv', index=False)
print("All Cleaned Data File has been created")


newreadcsv = pd.read_csv('AllCleanedDataFile.csv', encoding="latin1")

orderDetails = pd.DataFrame(newreadcsv, columns=['ORDERNUMBER','ORDERDATE', 'DEALSIZE'])

od = orderDetails.drop_duplicates(subset='ORDERNUMBER',keep="first")
od.insert(0, 'ORDERLINEID', range(101, 101 + len(od)))

#print(od)
fodList = []

dfodlist = od.values.tolist()

orderlist = orderDetails.values.tolist()
orderlist.sort()

#for f in dfodlist:
#    print(f)

#for fo in orderlist:
#    print(fo)

for d in dfodlist:
    for o in orderlist:
        if o[0] == d[1]:
            fodList.append(d)



orderDetailsDf = pd.DataFrame(fodList, columns=['ORDERLINEID', 'ORDERNUMBER',
                                                'ORDERDATE', 'DEALSIZE'])

orderDetailsDf.to_csv("ORDERDETAILS.csv", index=False)
print("ORDERDETAILS.csv has been created")

# TIME INFO

time = pd.DataFrame(newreadcsv, columns=['QTR_ID','MONTH_ID','YEAR_ID'])

t = time.drop_duplicates(subset='MONTH_ID',keep="first")
t.insert(0, 'TIMEID', range(5900, 5900 + len(t)))

#print(t)

tList = []

dftlist = t.values.tolist()


timelist = time.values.tolist()
timelist.sort()


for d in dftlist:
    for o in timelist:
        if o[1] == d[2]:
            tList.append(d)



timeDf = pd.DataFrame(tList, columns=['TIMEID','QTR_ID','MONTH_ID','YEAR_ID'])

timeDf.to_csv("TIME.csv", index=False)
print("TIME.csv has been created")


# STATUS

status = pd.DataFrame(newreadcsv, columns=['STATUS'])

stat = status.drop_duplicates(subset='STATUS',keep="first")
stat.insert(0, 'STATUSID', range(1, 1 + len(stat)))

statList = []

dfstatlist = stat.values.tolist()


statlist = status.values.tolist()
statlist.sort()


for d in dfstatlist:
    for o in statlist:
        if o[0] == d[1]:
            statList.append(d)



statusdf = pd.DataFrame(statList, columns=['STATUSID', 'STATUS'])

statusdf.to_csv("STATUS.csv", index=False)
print("STATUS.csv has been created")

# PRODUCT INFO

productDetails = pd.DataFrame(newreadcsv, columns=['PRODUCTCODE', 'MSRP'])

pro = productDetails.drop_duplicates(subset='PRODUCTCODE',keep="first")
pro.insert(0, 'PRODUCTLINEID', range(80000, 80000 + len(pro)))



proList = []

dfprolist = pro.values.tolist()

productlist = productDetails.values.tolist()
productlist.sort()


#for fo in orderlist:
#    print(fo)

for d in dfprolist:
    for o in productlist:
        if o[0] == d[1]:
            proList.append(d)



productDetailsDf = pd.DataFrame(proList, columns=['PRODUCTLINEID', 'PRODUCTCODE', 'MSRP'])

productDetailsDf.to_csv("PRODUCT.csv", index=False)
print("PRODUCT.csv has been created")

# CUSTOMER DETAILS


custDetails = pd.DataFrame(newreadcsv, columns=['CUSTOMERNAME','PHONE'])

tem = custDetails.drop_duplicates(subset='CUSTOMERNAME',keep="first")

tem.insert(0, 'CUSTOMERID', range(82825, 82825 + len(tem)))
tem.insert(0, 'CONTACTID', range(94130, 94130 + len(tem)))


finalList = []

dflist = tem.values.tolist()


custlist = custDetails.values.tolist()
custlist.sort()


for d in dflist:
    for c in custlist:
        if c[0] == d[2]:
            finalList.append(d)



customerDf = pd.DataFrame(finalList, columns=['CONTACTID','CUSTOMERID'
                                              ,'CUSTOMERNAME', 'PHONE'])

customerDf.to_csv("CUSTOMERDETAILS.csv", index=False)
print("CUSTOMERDETAILS.csv has been created")


# ADDRESS DETAILS



addressDetails1 = pd.DataFrame(newreadcsv, columns=['ADDRESSLINE1','ADDRESSLINE2',
                                                'POSTALCODE'])


addressDetails = addressDetails1.fillna({
'ADDRESSLINE2' : 'NA',
'STATE' : 'NA',
'POSTALCODE' : 'NA',
'TERRITORY' : 'NA'

})

add = addressDetails.drop_duplicates(subset='POSTALCODE',keep="first")


add.insert(0, 'CITYID', range(88480, 88480 + len(add)))
add.insert(0, 'ADDRESSID', range(85650, 85650 + len(add)))


addList = []

dfaddlist = add.values.tolist()


addlist = addressDetails.values.tolist()
addlist.sort()


for d in dfaddlist:
    for c in addlist:
        if c[2] == d[4]:
            addList.append(d)



addressDf = pd.DataFrame(addList, columns=['ADDRESSID', 'CITYID','ADDRESSLINE1',
                                              'ADDRESSLINE2',
                                              'POSTALCODE'])




addressDf.to_csv("ADDRESS.csv", index=False)
print("ADDRESS.csv has been created")

# STATE INFO

stateinfodf = pd.read_csv("CITY.csv", encoding="latin1")
stateid = pd.DataFrame(stateinfodf, columns=['STATEID'])
stateName = pd.DataFrame(newreadcsv, columns=['STATE'])
co = pd.DataFrame(newreadcsv, columns=['COUNTRY'])
co = co.drop_duplicates(subset='COUNTRY',keep="first")



stateName = stateName.drop_duplicates(subset='STATE',keep="first")
stateid = stateid.drop_duplicates(subset='STATEID',keep="first")
stateid = stateid[:-2]


L1 = stateid.values.tolist()
L2 = stateName.values.tolist()

L = []

for i in range(len(L1)):
    temp = []
    temp.append(L1[i][0])
    temp.append(L2[i][0])
    L.append(temp)


merged_df = pd.DataFrame(L, columns=['STATEID', 'STATE'])


merged_df.insert(0, 'COUNTRYID', range(99785, 99785 + len(merged_df)))

stateList = []

dfstatelist = merged_df.values.tolist()


statelist = stateName.values.tolist()
#statelist.sort()


for d in dfstatelist:
    for c in statelist:
        if c[0] == d[2]:
            stateList.append(d)


stateDf = pd.DataFrame(stateList, columns=['COUNTRYID', 'STATEID', 'STATE'])

stateDf.to_csv("STATE.csv", index=False)
print("STATE.csv has been created")


# COUNTRY INFO

countryinfodf = pd.read_csv("STATE.csv", encoding="latin1")
countryid = pd.DataFrame(countryinfodf, columns=['COUNTRYID'])
countryName = pd.DataFrame(newreadcsv, columns=['COUNTRY'])
countryName = countryName.drop_duplicates(subset='COUNTRY',keep="first")

terri = pd.DataFrame(readcsv, columns=['TERRITORY'])
terri = terri.drop_duplicates(subset='TERRITORY',keep="first")


countryName = countryName[:-3]


L1 = countryid.values.tolist()
L2 = countryName.values.tolist()

L = []

for i in range(len(L1)):
    temp = []
    temp.append(L1[i][0])
    temp.append(L2[i][0])
    L.append(temp)


merged_df = pd.DataFrame(L, columns=['COUNTRYID', 'COUNTRY'])


#merged_df.insert(0, 'COUNTRYID', range(99785, 99785 + len(merged_df)))

countryList = []

dfcountrylist = merged_df.values.tolist()


countrylist = countryName.values.tolist()
countrylist.sort()



for d in dfcountrylist:
    for c in countrylist:
        if c[0] == d[1]:
            countryList.append(d)


countryDf = pd.DataFrame(countryList, columns=['COUNTRYID', 'COUNTRY'])

countryDf.to_csv("COUNTRY.csv", index=False)
print("COUNTRY.csv has been created")

# Fact Table

customerDim = pd.read_csv("CUSTOMERDETAILS.csv", encoding="latin1")
mycusdim = customerDim.drop_duplicates(subset='CUSTOMERID',keep="first")
mycusdim.to_csv("FINAL_CUSTOMERDETAILS.csv", index = False)

productcodeDim = pd.read_csv("PRODUCT.csv", encoding="latin1")
myprocodedim = productcodeDim.drop_duplicates(subset='PRODUCTCODE',keep="first")
myprocodedim.to_csv("FINAL_PRODUCT.csv", index = False)

timeDim = pd.read_csv("TIME.csv", encoding="latin1")
mytimedim = timeDim.drop_duplicates(subset='TIMEID',keep="first")
mytimedim.to_csv("FINAL_TIME.csv", index = False)

ordernumberDim = pd.read_csv("ORDERDETAILS.csv", encoding="latin1")
myorderdim = ordernumberDim.drop_duplicates(subset='ORDERNUMBER',keep="first")
myorderdim.to_csv("FINAL_ORDERDETAILS.csv", index = False)

statusDim = pd.read_csv("STATUS.csv", encoding="latin1")
mystatusdim = statusDim.drop_duplicates(subset='STATUSID',keep="first")
myorderdim.to_csv("FINAL_STATUS.csv", index = False)

addressDim = pd.read_csv("ADDRESS.csv", encoding="latin1")
myadddim = addressDim.drop_duplicates(subset='ADDRESSID',keep="first")
myadddim.to_csv("FINAL_ADDRESS.csv", index = False)


#priceeachDim = pd.read_csv("AllCleanedDataFile.csv", encoding="latin1")


# FACT TABLE

AllCleanedFile = pd.read_csv("AllCleanedDataFile.csv", encoding="latin1")

#customerDim = pd.read_csv("FINAL_CUSTOMERDETAILS.csv", encoding="latin1")
#productcodeDim = pd.read_csv("FINAL_PRODUCT.csv", encoding="latin1")
#timeDim = pd.read_csv("FINAL_TIME.csv", encoding="latin1")
#salesDim = pd.read_csv("AllCleanedDataFile.csv", encoding="latin1")
#ordernumberDim = pd.read_csv("FINAL_ORDERDETAILS.csv", encoding="latin1")
#statusDim = pd.read_csv("FINAL_STATUS.csv", encoding="latin1")
#priceeachDim = pd.read_csv("AllCleanedDataFile.csv", encoding="latin1")
#addressDim = pd.read_csv("FINAL_ADDRESS.csv", encoding="latin1")

#print(customerDim['CUSTOMERID'])

L1 = mycusdim.iloc[:,1].values.tolist()
L2 = myprocodedim.iloc[:,1].values.tolist()
L3 = mytimedim.iloc[:,0].values.tolist()
#L4 = salesDim.iloc[:,4].values.tolist()
L5 = myorderdim.iloc[:,1].values.tolist()
L6 = mystatusdim.iloc[:,0].values.tolist()
#L7 = priceeachDim.iloc[:,2].values.tolist()
L8 = myadddim.iloc[:,0].values.tolist()

print(L1)

BigList = []
FactTable = pd.DataFrame()


