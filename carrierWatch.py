#-----------------------------------------------------------------------------#
#
#             Script for handling https://power.dat.com tsv files
#
#-----------------------------------------------------------------------------#
#       Owner: llanerost@casyl.com
#       Version: 20190702

#               CRITICAL

#               BUGS
#       TODO:   first to expire, needs fixed for dates 22xx.
#       TODO:   Convert all time modules to datetime.timedelta

#               CLEANUP/FEATURES
#       TODO:   set more of the code up as functions.
#       TODO:   Set a config file in json or something else for easier changes
#       TODO:   function to clean up import file, read into memory, then export
#               or convert. This will remove a lot of code!
#       TODO:   Split into multiple functions.
#       TODO:   Convert to exe, create ini file for settings, or json.
#       TODO:   Switch straightConvert to convert to Excel.
#       TODO:   Build function to check files for limits, currently manually done!
#       TODO:   Build GUI interface


#-----------------------------------------------------------------------------#
#                              Required Modules
#-----------------------------------------------------------------------------#
import csv, time, os
from os import system
from datetime import datetime


#-----------------------------------------------------------------------------#
#                                Date Variables
#-----------------------------------------------------------------------------#
# DO NOT CHANGE
stamp = datetime.now().strftime('%Y%m%d%H%M%S')
logStamp = datetime.now().strftime('%m-%d-%Y')
currDate = datetime.now().strftime('%Y-%m-%d')


#-----------------------------------------------------------------------------#
#                                Other Settings
#-----------------------------------------------------------------------------#
logo = '''                                             ,
      -j|||||||"                           <|||
    {||"                                    "
  ,|||`         <T|||||T  ,|||T|| /|||||l i||{  ,j|,|||L  ,|||i||
  |||L             ,|||   |||" ` ,|||" ` /||| ,|||L,|||l  |||"
 ||||         s||F^|||L  i||/    |||L   ,|||  |||F**^"`  i||/
 }|||~,,,,~= W|||,|||l, /|||    i||{    |||L ||||x,-=sL /|||
  "*LLANE*"  *ll*"*l=*` ===    !===    ===*   *ROST^`   ===                                 T||{
                                           |||L    ,,,     +|/                             {||l
                                          ]|||    /|||    ||"             ,jT             ,|||
                                          ||||   |||||  ,||   <j|||||L ;||||||l ,<l||| |   ||il|| l
                                          !||j / /L||| /|/       /|||   |||`   {||"      i||{  |||{
                                          L|||{|" L|||||"   i||Fj|||`  L||L   L||/      ||||  /|||
                                          L|||l   L|||l     ||L,L||{, {|||,,- |||L,,,~ ,|||  ,|||
                                          lll"    Wll*     <|l*"!ll"` v|l=^`  "l|ll*'  Wll`  WllL'''

# CONFIGURABLE 
fileIn = 'download.tsv'
fileOutGM = f"{stamp}-DAT_UPLOAD.csv"
fileOutCSV = f"{stamp}-download.csv"
failLogFile = 'failed_log.csv'
fileInDelim = '\t'
fileOutDelim = ','
row_variables = ('COMP_DBA_NAME', 'COMP_LGL_NAME', 'COMP_DOT', 'ENTITY_STATUS',
                 'SAFE_RATE', 'AUTH_COM', 'AUTH_PEN_COM', 'AUTO_LIMITS', 
                 'CARGO_LIMITS', 'GENERAL_LIMITS', 'CARGO_EXP_DATE', 
                 'AUTO_EXP_DATE', 'GENERAL_EXP_DATE', 'ENTITY_TYPE', 
                 'COMP_DOCKET_PREFIX', 'OPER_TYPE', 'COMP_DOCKET_NUMBER')

# Insurance minimums, contact JS for updates Jan 1 each year, last checked 1/1/2019.
auto_ins_min = 100_000
cargo_ins_min = 100_000
general_ins_min = 1_000_000


# WILL NEED TO BE MONITORED TO ENSURE WE ALWAYS ACCOUNT FOR ALL POSSIBILITES, Check every quarter.
# Last Checked Date: 1/1/2019.
auto_limits = ('Combined Single Limit (Each Accident)', 'ANY ONE OCCURENCE CSL', 'CSL')
cargo_limits = ('PER OCC', 'PER OCCUR', 'PER OCCURENCE', 'PER OCCURRANCE', 'PER OCCURRENCE', 
                'PER TRAILER', 'PER TRUCK', 'Per Vehicle', 
                'ANY 1 LOSS', 'ANY ONE LOAD', 'ANY ONE LOSS', 
                'ANY ONE OCC', 'ANY ONE OCCURENCE', 'ANY ONE OCCURRENCE', 
                'EACH OCCURRENCE', 'EACH OCCURRENCE LIMIT', 'Limit',
                'PER DIA', 'PER DISASTER', 'PER LOAD', 'PER LOSS', 'PER SHIPMENT')
general_limits = ('Each Occurrence')


#-----------------------------------------------------------------------------#
#                           FUNCTION: Menu System
#-----------------------------------------------------------------------------#
def menuSystem():
    os.system('cls' if os.name == 'nt' else 'clear')
    system('color 0e')
    print(logo)
    menuItem = input('Choose a menu selection:\n  1. Convert to CSV\n  2. GM Upload\n  3. Exit\n> ')
    if menuItem == '1':
        straightConvert()
    elif menuItem == '2':
        gmConvert()
    elif menuItem == '3':
        print('Exiting...')
    else:
        print('Not a valid option.')
        menuSystem()


#-----------------------------------------------------------------------------#
#               FUNCTION: Convert to CSV File - Straight Convert
#-----------------------------------------------------------------------------#
# basic function to convert the file from tsv to csv.
def straightConvert():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Converting to CSV File.')
    with open(fileIn, 'r') as csv_file_in:
        tsv_reader = csv.reader(csv_file_in, delimiter=fileInDelim)
        with open(fileOutCSV, 'w', newline='') as csv_file_out:
            csv_writer = csv.writer(csv_file_out, delimiter=fileOutDelim,quoting=csv.QUOTE_ALL)
            for row in tsv_reader:
                csv_writer.writerow(row)
    print('File has been converted to csv.\nExiting...')
    input('')


#-----------------------------------------------------------------------------#
#               FUNCTION: Check File Format for GM Convert
#-----------------------------------------------------------------------------#
def checkFormat():
    count = 0
    with open(fileIn, 'r') as tsv_file_in:
        tsv_reader = csv.DictReader(tsv_file_in, delimiter=fileInDelim)
        for item in row_variables:
            if item not in tsv_reader.fieldnames:
                count += 1
    return True if count == 0 else False


#-----------------------------------------------------------------------------#
#                 FUNCTION: Append Errors to a log.
#-----------------------------------------------------------------------------#
# logs all errors to a file.
def logErrorsToFile(issue):
    with open(failLogFile, 'a', newline='') as fail_log_file:
        csv_writer = csv.writer(fail_log_file, delimiter=fileOutDelim, quoting=csv.QUOTE_ALL)
        errorInfo = f"{logStamp} {issue} DOES NOT HAVE A MC # AND WAS NOT EXPORTED"
        csv_writer.writerow(errorInfo)
        print(f"{issue} DOES NOT HAVE A MC # AND WAS NOT EXPORTED - Error logged to {failLogFile}")


#-----------------------------------------------------------------------------#
#                 FUNCTION: Changes date from mm/dd/yyyy to yyyy/mm/dd
#-----------------------------------------------------------------------------#
# Function just to change the date format cause i am being a goon and can't figure it out.
def convertDate(date):
    return f"{date[-4:]}-{date[:2]}-{date[3:5]}"


#-----------------------------------------------------------------------------#
#                 FUNCTION: Check Insurance Levels
#-----------------------------------------------------------------------------#
# checks insurance type against types of insurance that are covered and then checks if the value meets or exceeds min limit. - Really want to clean this up more. Possibly build a new function for if '~' and else: pulling ins type.
def check(ins_type,input):
    checkStatus = set()
    # Auto limit check versus min
    if ins_type == 'auto_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in auto_limits:
                    if term == item:
                        if value >= auto_ins_min:
                            checkStatus.add(True)
                        elif value <= auto_ins_min:
                            checkStatus.add(False)
        else:
            newList = input.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in auto_limits:
                if term == item:
                    if int(value) >= auto_ins_min:
                        checkStatus.add(True)
                    elif int(value) <= auto_ins_min:
                        checkStatus.add(False)

    # Cargo limit check versus min
    elif ins_type == 'cargo_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in cargo_limits:
                    if term == item:
                        if value >= cargo_ins_min:
                            checkStatus.add(True)
                        elif int(value) <= cargo_ins_min:
                            checkStatus.add(False)
        else:
            newList = input.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in cargo_limits:
                if term == item:
                    if int(value) >= cargo_ins_min:
                        checkStatus.add(True)
                    elif int(value) <= cargo_ins_min:
                        checkStatus.add(False)

    # General limit check versus min
    elif ins_type == 'general_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in general_limits:
                    if term == item:
                        if value >= general_ins_min:
                            checkStatus.add(True)
                        elif int(value) <= general_ins_min:
                            checkStatus.add(False)
        else:
            newList = input.replace(fileInDelim,'').replace(fileOutDelim,'').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in general_limits:
                if term == item:
                    if int(value) >= general_ins_min:
                        checkStatus.add(True)
                    elif int(value) <= general_ins_min:
                        checkStatus.add(False)
    if True in checkStatus:
        return True
    elif False in checkStatus:
        return False


#-----------------------------------------------------------------------------#
#                 FUNCTION: Convert for Upload to Global Main
#-----------------------------------------------------------------------------#
def gmConvert():
#-----------------------------------------------------------------------------#
# Reads CarrierWatch Export file - currently no integrity checks
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Converting to GM Upload file.')
    with open(fileIn, 'r') as tsv_file_in:
        tsv_reader = csv.DictReader(tsv_file_in, delimiter=fileInDelim)
        next(tsv_reader, None)
        if checkFormat() == True:


#-----------------------------------------------------------------------------#
# Checks info against company policy and prints out csv file for upload
            with open(fileOutGM, 'w', newline='') as csv_file_out:
                csv_writer = csv.writer(csv_file_out, delimiter=fileOutDelim, quoting=csv.QUOTE_ALL)
                header = ('VENDOR','COMP_DOCKET_NUMBER','COMP_NAME','COMP_DOT','FIRST_TO_EXPIRE_DATE','NOTES','STATUS')
                csv_writer.writerow(header)
                for row in tsv_reader:


#-----------------------------------------------------------------------------#
# DEFAULT VARIABLES FOR FILEIN
                    status = []
                    status.append('ACTIVE')
                    final_status = ''
                    notes = ''
                    first_to_expire = ''
                    first_expire = []
                    minDate = ''


#-----------------------------------------------------------------------------#
# Check if DBA, and if so move legal to notes.
                    if row['COMP_DBA_NAME'] != '':
                        notes += f"~LEGAL NAME {row['COMP_LGL_NAME']}"


#-----------------------------------------------------------------------------#
# Checks for missing DOT, and DOT Inactive
                    if row['COMP_DOT'] == '':
                        notes += '~NO DOT NUMBER LISTED'
                        status.append('INACTIVE')
                    if row['ENTITY_STATUS'] == 'I':
                        notes += '~DOT# INACTIVE'
                        status.append('INACTIVE')


#-----------------------------------------------------------------------------#
# Safety Rating Check
                    if row['SAFE_RATE'] == 'C':
                        notes += '~SAFETY RATING CONDITIONAL'
                        status.append('INACTIVE')


#-----------------------------------------------------------------------------#
# Check for Carrier Authority - still needs more checks, other ways to be inactive
                    if row['AUTH_COM'] != 'A':
                        if row['AUTH_CONT'] != 'A':
                            notes += '~CARRIER AUTHORITY NOT ACTIVE'
                            status.append('INACTIVE')
                    if row['AUTH_PEN_COM'] == 'Y':
                        notes += '~CARRIER AUTHORITY PENDING'
                        status.append('INACTIVE')


#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Limit Check
                    if check('auto_limits',row['AUTO_LIMITS']) == False:
                        notes += '~AUTO INSURANCE TO LOW'
                        status.append('INACTIVE')
                    elif check('auto_limits',row['AUTO_LIMITS']) == True:
                        status.append('ACTIVE')
                    if check('cargo_limits',row['CARGO_LIMITS']) == False:
                        notes += '~CARGO INSURANCE TO LOW'
                        status.append('INACTIVE')
                    elif check('cargo_limits',row['CARGO_LIMITS']) == True:
                        status.append('ACTIVE')
                    if check('general_limits',row['GENERAL_LIMITS']) == False:
                        notes += '~GENERAL INSURANCE TO LOW'
                        status.append('INACTIVE')
                    elif check('general_limits',row['GENERAL_LIMITS']) == True:
                        status.append('ACTIVE')


#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Expiration Check
                    if row['CARGO_EXP_DATE'] != '':
                        selectDate = convertDate(row['CARGO_EXP_DATE'])
                        if selectDate < currDate:
                            notes += f"~CARGO INS EXPIRED {row['CARGO_EXP_DATE']}"
                            status.append('INACTIVE')
                        first_expire.append(selectDate)
                    elif row['CARGO_EXP_DATE'] == '':
                        notes += '~CARGO INS NOT LISTED'
                        status.append('INACTIVE')
                    else:
                        notes += '~cargo checked'
                    if row['GENERAL_EXP_DATE'] != '':
                        selectDate = convertDate(row['GENERAL_EXP_DATE'])
                        if selectDate < currDate:
                            notes += f"~GENERAL INS EXPIRED {row['GENERAL_EXP_DATE']}"
                            status.append('INACTIVE')
                        first_expire.append(selectDate)
                    elif row['GENERAL_EXP_DATE'] == '':
                        notes += '~GENERAL INS NOT LISTED'
                        status.append('INACTIVE')
                    else:
                        notes += '~general checked'

                    if row['AUTO_EXP_DATE'] != '':
                        selectDate = convertDate(row['AUTO_EXP_DATE'])
                        if selectDate < currDate:
                            notes += f"~AUTO INS EXPIRED {row['AUTO_EXP_DATE']}"
                            status.append('INACTIVE')
                        first_expire.append(selectDate)
                    elif row['AUTO_EXP_DATE'] == '':
                        notes += '~AUTO INS NOT LISTED'
                        status.append('INACTIVE')
                    else:
                        notes += '~auto checked'

                    if first_expire != []:
                        minDate = max(first_expire)
                        first_to_expire = f"{minDate[5:7]}/{minDate[-2:]}/{minDate[:4]}"


#-----------------------------------------------------------------------------#
# Authorized Broker Check
                    if row['ENTITY_TYPE'] == 'BROKER':
                        notes += '~VENDOR IS A BROKER, NO ASSETS'
                        status.append('INACTIVE')
                    elif 'BROKER' in row['ENTITY_TYPE']:
                        notes += '~VENDOR IS A BROKER, TENDER TO CARRIER ASSET ONLY'
                        status.append('ACTIVE')


#-----------------------------------------------------------------------------#
# Docket Prefix Check
                    if row['COMP_DOCKET_PREFIX'] != 'MC':
                        if row['COMP_DOCKET_PREFIX'] != '':
                            notes += f"~{row['COMP_DOCKET_PREFIX']}{row['COMP_DOCKET_NUMBER']}"


#-----------------------------------------------------------------------------#
# Checks if Intrastate versus Interstate
                    if 'Only' in row['OPER_TYPE']:
                        notes += '~INTRASTATE ONLY'
                        status.append('INACTIVE')


#-----------------------------------------------------------------------------#
# Check for INACTIVE status, otherwise keep status Active
                    if 'INACTIVE' in status:
                        final_status = 'INACTIVE'
                    else:
                        final_status = 'ACTIVE'
                        notes = '~MONITORED ON CARRIER WATCH'


#-----------------------------------------------------------------------------#

# Docket Number Length Check
                    if len(row['COMP_DOCKET_NUMBER']):
                        if row['COMP_DBA_NAME'] != '':
                            newLine = row['COMP_ID'],
                            row['COMP_DOCKET_NUMBER'],
                            row['COMP_DBA_NAME'],
                            row['COMP_DOT'],
                            first_to_expire,
                            notes[1:],
                            final_status
                        else:
                            newLine = row['COMP_ID'],
                            row['COMP_DOCKET_NUMBER'],
                            row['COMP_LGL_NAME'],
                            row['COMP_DOT'],
                            first_to_expire,
                            notes[1:],
                            final_status
                    else:
                        logErrorsToFile(f"{row['COMP_ID']}-{row['COMP_DOT']}")


#-----------------------------------------------------------------------------#
# Prints to row
                    csv_writer.writerow(newLine)

            print('File has been converted to GM import file.\nExiting...')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
===========WARNING INVALID FORMAT============
    Ensure the following is selected
    Tab-delimited from the drop down menu
    Include Header bullet selected as Yes
    DOT Authority is checked
    DOT Insurance is checked
    Cargo Insurance is checked
    Auto Insurance is checked
    General Insurance is checked
    Safety is checked
    DOT Profile & Commodities
===========WARNING INVALID FORMAT============
Convert canceled, Press enter to return to menu''')
            input('')

#-----------------------------------------------------------------------------#
#                    CALLS MENU FUNCTION FOR USER SELECTION
#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    menuSystem()
