#-----------------------------------------------------------------------------#
#
#                 Script for handling https://power.dat.com tsv files
#
#-----------------------------------------------------------------------------#
#       Owner: llanerost+gtsi@gmail.com
#       Version: 20190220
#
#       TODO:   Cargo authority this is a tough one
#                Got 1 part done, need to figure out how else to tell.
#       TODO:   DOT expired to be worked on, working on, i hate dates!
#       TODO:   first to expire, needs fixed for dates 22xx.
#       TODO:   set more of the code up as functions.
#       TODO:   Set a config file in json or something else for easier changes
#       TODO:   Limits can be tuples.
#
#
#-----------------------------------------------------------------------------#
#                              Required Modules
#-----------------------------------------------------------------------------#
import csv, datetime, time
from datetime import datetime
from datetime import date


#-----------------------------------------------------------------------------#
#                                 Variables
#-----------------------------------------------------------------------------#
# DO NOT CHANGE
stamp = datetime.now().strftime('%Y%m%d%H%M%S-')
logStamp = datetime.now().strftime('%m-%d-%Y')
currDate = time.strptime(str(datetime.now().strftime('%m/%d/%Y')), '%m/%d/%Y')


# CONFIGURABLE
fileIn = 'download.tsv'
fileOutGM = stamp + 'DAT_UPLOAD.csv'
fileOutCSV = stamp + 'download.csv'
failLogFile = 'failed_log.csv'

auto_ins_min = 100000
cargo_ins_min = 100000
general_ins_min = 1000000


# WILL NEED TO BE MONITORED TO ENSURE WE ALWAYS ACCOUNT FOR ALL POSSIBILITES
auto_limits = ['Combined Single Limit (Each Accident)', 'ANY ONE OCCURENCE CSL', 'CSL']
cargo_limits = ['Limit', 'PER OCC', 'PER OCCUR', 'PER OCCURENCE', 'PER OCCURRANCE', 'PER OCCURRENCE', 'PER TRAILER', 'PER TRUCK', 'Per Vehicle', 'ANY 1 LOSS', 'ANY ONE LOAD', 'ANY ONE LOSS', 'ANY ONE OCC', 'ANY ONE OCCURENCE', 'ANY ONE OCCURRENCE', 'EACH OCCURRENCE', 'EACH OCCURRENCE LIMIT', 'PER DIA', 'PER DISASTER', 'PER LOAD', 'PER LOSS', 'PER SHIPMENT']
general_limits = ['Each Occurrence']


#-----------------------------------------------------------------------------#
#                           FUNCTION: Menu System
#-----------------------------------------------------------------------------#
def menuSystem():
    menuItem = input('Choose a number\n1 - Straight Convert\n2 - GM Convert\n3 - Exit\n')
    if menuItem == '1':
        straightConvert()
        print('File has been converted to csv.\nExiting...')
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
# basic function to convert the file from tsv to csv. Eventually do this to Excel.
def straightConvert():
    with open(fileIn, 'r') as csv_file_in:
        tsv_reader = csv.reader(csv_file_in, delimiter='\t')
        with open(fileOutCSV, 'w', newline='') as csv_file_out:
            csv_writer = csv.writer(csv_file_out, delimiter=',',quoting=csv.QUOTE_ALL)
            for row in tsv_reader:
                csv_writer.writerow(row)
        csv_file_out.close()
    csv_file_in.close()


#-----------------------------------------------------------------------------#
#               FUNCTION: Check File Format for GM Convert
#-----------------------------------------------------------------------------#
def checkFormat(columnName):
    if len(columnName) == 139:
        return True
    else:
        return False


#-----------------------------------------------------------------------------#
#               FUNCTION: Checks DOT Expiration Date
#-----------------------------------------------------------------------------#
# http://www.part380.com/blog/2014/03/11/biennial-update-mcs-150-registration-renewal/

# Requires exporting dot profile regardless. So use built in dates?
# does not function correctly yet.
def checkDOTExpiration(DOT,MCS150):
    if MCS150 != '':
        year = date.now().year()
        month = date.now().month()
        yearMCS = str(time.strptime(MCS150, '%m/%d/%Y'))
        monthMCS = str(time.strptime(MSC150))
        return DOT[-2],DOT[-1], MCS150, month, year
    else:
        return False

#-----------------------------------------------------------------------------#
#                 FUNCTION: Append Errors to a log.
#-----------------------------------------------------------------------------#
# logs all errors to a file.

def logErrorsToFile(issue):
    with open(failLogFile, 'a', newline='') as fail_log_file:
        csv_writer = csv.writer(fail_log_file, delimiter=',', quoting=csv.QUOTE_ALL)
        errorInfo = (logStamp, issue, 'DOES NOT HAVE A MC # AND WAS NOT EXPORTED')
        csv_writer.writerow(errorInfo)
        print(issue, 'DOES NOT HAVE A MC # AND WAS NOT EXPORTED - ', 'Error logged to', failLogFile)
        fail_log_file.close()


#-----------------------------------------------------------------------------#
#                 FUNCTION: Check Insurance Levels
#-----------------------------------------------------------------------------#
# checks insurance type against types of insurance that are covered and then checks if the value meets or exceeds min limit. - Really want to clean this up more. Possibly build a new function for if '~' and else: pulling ins type.
def check(ins_type,input):
    status = set()

    # Auto limit check versus min
    if ins_type == 'auto_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace('\t','').replace(',','').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in auto_limits:
                    if term == item:
                        if value >= auto_ins_min:
                            status.add(True)
                        elif value <= auto_ins_min:
                            status.add(False)
        else:
            newList = input.replace('\t','').replace(',','').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in auto_limits:
                if term == item:
                    if int(value) >= auto_ins_min:
                        status.add(True)
                    elif int(value) <= auto_ins_min:
                        status.add(False)

    # Cargo limit check versus min
    elif ins_type == 'cargo_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace('\t','').replace(',','').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in cargo_limits:
                    if term == item:
                        if value >= cargo_ins_min:
                            status.add(True)
                        elif int(value) <= cargo_ins_min:
                            status.add(False)
        else:
            newList = input.replace('\t','').replace(',','').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in cargo_limits:
                if term == item:
                    if int(value) >= cargo_ins_min:
                        status.add(True)
                    elif int(value) <= cargo_ins_min:
                        status.add(False)

    # General limit check versus min
    elif ins_type == 'general_limits':
        if '~' in input:
            for row in input.split('~'):
                newList = row.replace('\t','').replace(',','').strip()
                term = newList.split(' $')[0].strip()
                value = int(newList.split(' $')[1].strip().replace(' ',''))
                for item in general_limits:
                    if term == item:
                        if value >= general_ins_min:
                            status.add(True)
                        elif int(value) <= general_ins_min:
                            status.add(False)
        else:
            newList = input.replace('\t','').replace(',','').strip()
            term = newList[:newList.find('$')-1]
            value = newList[newList.find('$')+1:]
            for item in general_limits:
                if term == item:
                    if int(value) >= general_ins_min:
                        status.add(True)
                    elif int(value) <= general_ins_min:
                        status.add(False)
    if True in status:
        return True
    elif False in status:
        return False


#-----------------------------------------------------------------------------#
#                 FUNCTION: Convert for Upload to Global Main
#-----------------------------------------------------------------------------#
def gmConvert():
#-----------------------------------------------------------------------------#
# Reads CarrierWatch Export file - currently no integrity checks
    with open(fileIn, 'r') as csv_file_in:
        tsv_reader = csv.DictReader(csv_file_in, delimiter='\t')
        next(tsv_reader, None)
        if checkFormat(tsv_reader.fieldnames) == True:


#-----------------------------------------------------------------------------#
# Checks info against company policy and prints out csv file for upload
            with open(fileOutGM, 'w', newline='') as csv_file_out:
                csv_writer = csv.writer(csv_file_out, delimiter=',', quoting=csv.QUOTE_ALL)
                header = ['COMP_DOCKET_NUMBER','COMP_NAME','COMP_DOT','FIRST_TO_EXPIRE_DATE','NOTES','STATUS']
                csv_writer.writerow(header)
                for row in tsv_reader:


#-----------------------------------------------------------------------------#
# DEFAULT VARIABLES FOR FILEIN
                    status = set()
                    status.add('ACTIVE')
                    final_status = ''
                    notes = ''


#-----------------------------------------------------------------------------#
# Check if DBA, and if so move legal to notes.
                    if row['COMP_DBA_NAME'] != '':
                        notes += '~LEGAL NAME ' + row['COMP_LGL_NAME']


#-----------------------------------------------------------------------------#
# DOT Expired/Exist
                    if row['COMP_DOT'] == '':
                        notes += '~NO DOT NUMBER LISTED'
                        status.add('INACTIVE')
                        # checkDOTExpiration(row['COMP_DOT'],row['MCS150_DATE'])
                        # if checkDOTExpiration(row['COMP_DOT'],row['MCS150_DATE']) == False:
                        #     print(row['COMP_DOT'],checkDOTExpiration(row['COMP_DOT'],row['MCS150_DATE']),'INACTIVE')


#-----------------------------------------------------------------------------#
# Safety Rating Check
                    if row['SAFE_RATE'] == 'C':
                        notes += '~SAFETY RATING CONDITIONAL'
                        status.add('INACTIVE')


#-----------------------------------------------------------------------------#
# Check for Carrier Authority - still needs more checks, other ways to be inactive
                    if row['AUTH_COM'] == '' and row['AUTH_CONT'] == '' and row['AUTH_BRK'] == '':
                        status.add('INACTIVE')
                        notes += '~CARRIER AUTHORITY NOT ACTIVE'


#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Limit Check
# Remove, code not working atm. working on new code.
                    # print(row['COMP_DOCKET_NUMBER'])
                    if check('auto_limits',row['AUTO_LIMITS']) == False:
                        notes += '~AUTO INSURANCE TO LOW'
                        status.add('INACTIVE')
                    elif check('auto_limits',row['AUTO_LIMITS']) == True:
                        status.add('ACTIVE')
                    if check('cargo_limits',row['CARGO_LIMITS']) == False:
                        notes += '~CARGO INSURANCE TO LOW'
                        status.add('INACTIVE')
                    elif check('cargo_limits',row['CARGO_LIMITS']) == True:
                        status.add('ACTIVE')
                    if check('general_limits',row['GENERAL_LIMITS']) == False:
                        notes += '~GENERAL INSURANCE TO LOW'
                        status.add('INACTIVE')
                    elif check('general_limits',row['GENERAL_LIMITS']) == True:
                        status.add('ACTIVE')


#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Expiration Check
                    first_to_expire = (0,0,0,0,0,0,0,0,0)

                    if row['CARGO_EXP_DATE'] != '': # working
                        if time.strptime(row['CARGO_EXP_DATE'], '%m/%d/%Y') < currDate:
                            notes += '~CARGO INS EXPIRED ' + row['CARGO_EXP_DATE']
                            status.add('INACTIVE')
                        first_to_expire = time.strptime(row['CARGO_EXP_DATE'], '%m/%d/%Y')
                    else:
                        notes += '~CARGO INS NOT LISTED'
                        status.add('INACTIVE')

                    if row['GENERAL_EXP_DATE'] != '': # working
                        if time.strptime(row['GENERAL_EXP_DATE'], '%m/%d/%Y') < currDate:
                            notes += '~GENERAL INS EXPIRED ' + row['GENERAL_EXP_DATE']
                            status.add('INACTIVE')
                        if first_to_expire < time.strptime(row['GENERAL_EXP_DATE'], '%m/%d/%Y'):
                            first_to_expire = time.strptime(row['GENERAL_EXP_DATE'], '%m/%d/%Y')
                    else:
                        notes += '~GENERAL INS NOT LISTED'
                        status.add('INACTIVE')

                    if row['AUTO_EXP_DATE'] != '': # working
                        if time.strptime(row['AUTO_EXP_DATE'], '%m/%d/%Y') < currDate:
                            notes += '~AUTO INS EXPIRED ' + row['AUTO_EXP_DATE']
                            status = 'INACTIVE'
                        if first_to_expire < time.strptime(row['AUTO_EXP_DATE'], '%m/%d/%Y'):
                            first_to_expire = time.strptime(row['AUTO_EXP_DATE'], '%m/%d/%Y')
                    else:
                        notes += '~AUTO INS NOT LISTED'
                        status.add('INACTIVE')

                    first_to_expire = str(first_to_expire[1]) + '/' + str(first_to_expire[2]) + '/' + str(first_to_expire[0])
                    if first_to_expire == '0/0/0':
                        first_to_expire = ''


#-----------------------------------------------------------------------------#
# Authorized Broker Check
                    if row['ENTITY_TYPE'] == 'BROKER':
                        notes += '~VENDOR IS A BROKER, NO ASSETS'
                        status.add('INACTIVE')
                    elif 'BROKER' in row['ENTITY_TYPE']:
                        notes += '~VENDOR IS A BROKER, TENDER TO CARRIER ASSET ONLY'
                        status.add('ACTIVE')


#-----------------------------------------------------------------------------#
# Docket Prefix Check
                    if row['COMP_DOCKET_PREFIX'] != 'MC':
                        if row['COMP_DOCKET_PREFIX'] != '':
                            notes += '~' + row['COMP_DOCKET_PREFIX'] + row['COMP_DOCKET_NUMBER']


#-----------------------------------------------------------------------------#
# Checks if Intrastate versus Interstate
                    if row['OPER_TYPE'] == 'Intrastate Only (Non-HM)':
                        notes += '~INTRASTATE ONLY (NON-HM)'


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
                            newLine = row['COMP_DOCKET_NUMBER'], row['COMP_DBA_NAME'], row['COMP_DOT'], first_to_expire, notes[1:], final_status
                        else:
                            newLine = row['COMP_DOCKET_NUMBER'], row['COMP_LGL_NAME'], row['COMP_DOT'], first_to_expire, notes[1:], final_status
                    else:
                        logErrorsToFile(row['COMP_DOT'])


#-----------------------------------------------------------------------------#
# Prints to row
                    csv_writer.writerow(newLine)
                csv_file_in.close()
            csv_file_out.close()
            print('File has been converted to GM import file.\nExiting...')
        else:
            print('''
===========WARNING INVALID FORMAT============
    Ensure the following is selected
    Tab-delimited from the drop down menu
    Include Header bullet selected as Yes
    DOT Authority is checked
    DOT Insurance is checked)
    Cargo Insurance is checked
    Auto Insurance is checked
    General Insurance is checked
    Safety is checked
    DOT Profile & Commodities
===========WARNING INVALID FORMAT============

Convert canceled''')


#-----------------------------------------------------------------------------#
#                    CALLS MENU FUNCTION FOR USER SELECTION
#-----------------------------------------------------------------------------#

menuSystem()
