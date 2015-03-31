'''
Created on 10/01/2015

@author: myxomaZ
'''
import os.path, sys
import re

def get_my_string():
    """Returns the file inputFn"""

    inputFn = ""+os.path.dirname(__file__) + "\RawTextStatementFormatter_Input\mStatement.txt"

    try:
        with open(inputFn) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        sys.stderr.write( "[myScript] - Error: Could not open %s\n" % (inputFn) )
        sys.exit(-1)

def get_general_statement_info(mSInput):
    Date_Info_Searchkey = "FROM LAST STATEMENT DATED"
    Date_Info = ""
    Total_Page_Searchkey ="Page 1 of "
    Total_Page = ""
    for item in mSInput.split("\n"):
        if Date_Info_Searchkey in item:
            Date_Info =  item.strip()
            break
    for item in mSInput.split("\n"):
        if Total_Page_Searchkey in item:
            Total_Page =  item.strip()[-1]
            break        
    return Date_Info, Total_Page

def Strip_NonTables_Strings(mSInput):
    x = mSInput.find("Page 3 of")
    return x
#mS = unicode(get_my_string())
mS = get_my_string()

#print mS
get_general_statement_info(mS)
#TextOutput = re.sub('\((.*?)\)[:](.*?)(<br />)', "<br />", TextOutput)
print mS[Strip_NonTables_Strings(mS):]