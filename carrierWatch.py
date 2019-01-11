#-----------------------------------------------------------------------------#
#
#                 Script for handling https://power.dat.com tsv files
#
#-----------------------------------------------------------------------------#
#       Owner: llanerost+gtsi@gmail.com
#       Version: 20190110
#
#       TODO:   Cargo authority this is a tough one
#               Auto, Cargo, & General Limit Check (working, but...)
#
#
#-----------------------------------------------------------------------------#
#                              Required Modules
#-----------------------------------------------------------------------------#
import csv, datetime, time
from datetime import datetime



#-----------------------------------------------------------------------------#
#                                 Variables
#-----------------------------------------------------------------------------#
# DO NOT CHANGE
stamp = datetime.now().strftime('%Y%m%d%H%M%S-')
logStamp = datetime.now().strftime('%m-%d-%Y')
currDate = time.strptime(str(datetime.now().strftime('%m/%d/%Y')), "%m/%d/%Y")

# CONFIGURABLE
fileIn = 'download.tsv'
fileOutGM = stamp + 'DAT_UPLOAD.csv'
fileOutCSV = stamp + 'download.csv'
failLogFile = 'failed_log.csv' # no code written yet, will write in append mode.

# auto_ins_min = 100000
# cargo_ins_min = 100000
# general_ins_min = 1000000
auto_ins_min = 1
cargo_ins_min = 1
general_ins_min = 1

# WILL NEED TO BE MONITORED TO ENSURE WE ALWAYS ACCOUNT FOR ALL POSSIBILITES
auto_limits = ['Combined Single Limit (Each Accident)', 'ANY ONE OCCURENCE CSL', 'CSL']
cargo_limits = ['Limit', 'PER OCC', 'PER OCCUR', 'PER OCCURENCE', 'PER OCCURRANCE', 'PER OCCURRENCE', 'PER TRAILER', 'PER TRUCK', 'Per Vehicle', 'AGG', 'AGGREGATE', 'ANY 1 LOSS', 'ANY ONE LOAD', 'ANY ONE LOSS', 'ANY ONE OCC', 'ANY ONE OCCURENCE', 'ANY ONE OCCURRENCE', 'EACH OCCURRENCE', 'EACH OCCURRENCE LIMIT', 'PER DIA', 'PER DISASTER', 'PER LOAD', 'PER LOSS', 'PER SHIPMENT']
general_limits = ['Each Occurrence', 'General Aggregate']



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
    if len(columnName) == 102:
        return True
    else:
        return False



#-----------------------------------------------------------------------------#
#                 FUNCTION: Append Errors to a log.
#-----------------------------------------------------------------------------#
# logs all errors to a file, would like to only append issue, but for now writes all issues with append mode. Doesn't write to file, fix later, less important

def logErrorsToFile(issue):
    with open(failLogFile, 'a', newline='') as fail_log_file:
        csv_writer = csv.writer(fail_log_file, delimiter=',',quoting=csv.QUOTE_ALL)
        errorInfo = (logStamp, issue, 'DOES NOT HAVE A MC # AND WAS NOT EXPORTED')
        csv_writer.writerow(errorInfo)
        print(issue, 'DOES NOT HAVE A MC # AND WAS NOT EXPORTED - ', 'Error logged to',failLogFile)
        fail_log_file.close()


#-----------------------------------------------------------------------------#
#                 FUNCTION: Check Insurance Levels
#-----------------------------------------------------------------------------#
# Semi working in cw_scrap_paper.py, but needs additional checks
def check(ins_type,input):

    status = ['ACTIVE']
    notes = 'MONITORED IN CARRIER WATCH'
    final_status = 'ACTIVATE'

    # if ins_type == 'auto_limits':
    #     for row in input.split('~'):
    #         for item in auto_limits:
    #             if row[0:len(item)] == item:
    #                 listed_auto_ins_min = int(row[len(item)+2:].replace(',',''))
    #                 if listed_auto_ins_min < auto_ins_min:
    #                     if 'AUTO INSURANCE TO LOW' not in notes:
    #                         notes += '~AUTO INSURANCE TO LOW'
    #                     status.append('DEACTIVE')
    #                 else:
    #                     final_status = 'ACTIVE'
    #                     return final_status

    if ins_type == 'auto_limits':
        for row in input.split('~'):
            for item in auto_limits:
                newList = row.replace('\t',"").replace(',',"")
                term = newList[:newList.find('$')-1]
                value = newList[newList.find('$')+1:]
                if term == item:
                    if int(value) <= auto_ins_min:
                        final_status = 'ACTIVE'
                        return final_status
                    else:
                        if 'AUTO INSURANCE TO LOW' not in notes:
                            notes += '~AUTO INSURANCE TO LOW'
                        status.append('DEACTIVE')

    elif ins_type == 'cargo_limits':
        for row in input.split('~'):
            for item in cargo_limits:
                newList = row.replace('\t',"").replace(',',"")
                term = newList[:newList.find('$')-1]
                value = newList[newList.find('$')+1:]
                if term == item:
                    if int(value) <= cargo_ins_min:
                        final_status = 'ACTIVE'
                        return final_status
                    else:
                        if 'CARGO INSURANCE TO LOW' not in notes:
                            notes += '~CARGO INSURANCE TO LOW'
                        status.append('DEACTIVE')

    elif ins_type == 'general_limits':
        for row in input.split('~'):
            for item in general_limits:
                newList = row.replace('\t',"").replace(',',"")
                term = newList[:newList.find('$')-1]
                value = newList[newList.find('$')+1:]
                if term == item:
                    if int(value) <= general_ins_min:
                        final_status = 'ACTIVE'
                        return final_status
                    else:
                        if 'GENERAL INSURANCE TO LOW' not in notes:
                            notes += '~GENERAL INSURANCE TO LOW'
                        status.append('DEACTIVE')



#-----------------------------------------------------------------------------#
#                 FUNCTION: Convert for Upload to Global Main
#-----------------------------------------------------------------------------#
def gmConvert():
#-----------------------------------------------------------------------------#
# Reads CarrierWatch Export file, currently no integrity checks
    with open(fileIn, 'r') as csv_file_in:
        tsv_reader = csv.DictReader(csv_file_in, delimiter='\t')
        next(tsv_reader, None)
        if checkFormat(tsv_reader.fieldnames) == True:

#-----------------------------------------------------------------------------#
# Checks info against company policy and prints out csv file for upload
            # debugCounter = 1
            with open(fileOutGM, 'w', newline='') as csv_file_out:
                csv_writer = csv.writer(csv_file_out, delimiter=',', quoting=csv.QUOTE_ALL)
                header = ['COMP_DOCKET_NUMBER','COMP_LGL_NAME','COMP_DBA_NAME','COMP_DOT','FIRST_TO_EXPIRE_DATE','NOTES','STATUS']
                csv_writer.writerow(header)
                for row in tsv_reader:

#-----------------------------------------------------------------------------#
# DEFAULT VARIABLES FOR FILEIN
                    status = ['ACTIVE']
                    final_status = ''
                    notes = 'MONITORED ON CARRIER WATCH' # working

#-----------------------------------------------------------------------------#
# Safety Rating Check
                    if row['SAFE_RATE'] == 'C':
                        notes += '~SAFETY RATING CONDITIONAL'
                        status.append('DEACTIVE')

#-----------------------------------------------------------------------------#
# Check for Cargo/Carrier Authority

#
# if entity_status == 'I': # not working yet
#     notes += '~DOT NUMBER ' + comp_dot + ' IS INACTIVE'
#     status.append('DEACTIVE')

#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Limit Check
# Needs finished
                    # print(row['AUTO_LIMITS'])
                    check('auto_limits',row['AUTO_LIMITS'])
                    check('cargo_limits',row['CARGO_LIMITS'])
                    check('general_limits',row['GENERAL_LIMITS'])


#-----------------------------------------------------------------------------#
# Auto, Cargo, & General Expiration Check
                    first_to_expire = (0,0,0,0,0,0,0,0,0)

                    if row['CARGO_EXP_DATE'] != '': # working
                        if time.strptime(row['CARGO_EXP_DATE'], "%m/%d/%Y") < currDate:
                            notes += '~CARGO INS EXPIRED ' + row['CARGO_EXP_DATE']
                            status.append('DEACTIVE')
                        first_to_expire = time.strptime(row['CARGO_EXP_DATE'], "%m/%d/%Y")

                    else:
                        notes += '~CARGO INS NOT LISTED ON CARRIER WATCH'
                        status.append('DEACTIVE')

                    if row['GENERAL_EXP_DATE'] != '': # working
                        if time.strptime(row['GENERAL_EXP_DATE'], "%m/%d/%Y") < currDate:
                            notes += '~GENERAL INS EXPIRED ' + row['GENERAL_EXP_DATE']
                            status.append('DEACTIVE')
                        if first_to_expire < time.strptime(row['GENERAL_EXP_DATE'], "%m/%d/%Y"):
                            first_to_expire = time.strptime(row['GENERAL_EXP_DATE'], "%m/%d/%Y")
                    else:
                        notes += '~GENERAL INS NOT LISTED'
                        status.append('DEACTIVE')

                    if row['AUTO_EXP_DATE'] != '': # working
                        if time.strptime(row['AUTO_EXP_DATE'], "%m/%d/%Y") < currDate:
                            notes += '~AUTO INS EXPIRED ' + row['AUTO_EXP_DATE']
                            status = 'DEACTIVE'
                        if first_to_expire < time.strptime(row['AUTO_EXP_DATE'], "%m/%d/%Y"):
                            first_to_expire = time.strptime(row['AUTO_EXP_DATE'], "%m/%d/%Y")
                    else:
                        notes += '~AUTO INS NOT LISTED'
                        status.append('DEACTIVE')

                    first_to_expire = str(first_to_expire[1]) + '/' + str(first_to_expire[2]) + '/' + str(first_to_expire[0])
                    if first_to_expire == '0/0/0':
                        first_to_expire = ''

#-----------------------------------------------------------------------------#
# Checks for DOT Number
                    if row['COMP_DOT'] == '':
                        notes += '~NO DOT NUMBER LISTED'
                        status.append('DEACTIVE')

#-----------------------------------------------------------------------------#
# Authorized Broker Check
                    if row['AUTH_BRK'] == 'A':
                        notes += '~VENDOR IS A BROKER, TENDER TO CARRIER ASSET ONLY'

#-----------------------------------------------------------------------------#
# Docket Prefix Check
                    if row['COMP_DOCKET_PREFIX'] != 'MC':
                        if row['COMP_DOCKET_PREFIX'] != '':
                            notes += '~' + row['COMP_DOCKET_PREFIX'] + row['COMP_DOCKET_NUMBER']

#-----------------------------------------------------------------------------#
# Check for DEACTIVE status, otherwise keep status Active
                    if 'DEACTIVE' in status:
                        final_status = 'DEACTIVE'
                    else:
                        final_status = 'ACTIVE'

#-----------------------------------------------------------------------------#

# Docket Number Length Check
                    if len(row['COMP_DOCKET_NUMBER']):
                        newLine = row['COMP_DOCKET_NUMBER'], row['COMP_LGL_NAME'], row['COMP_DBA_NAME'], row['COMP_DOT'], first_to_expire, notes, final_status
                    else:
                        logErrorsToFile(row['COMP_DOT'])


#-----------------------------------------------------------------------------#
# Prints to row
                    csv_writer.writerow(newLine)
                    # print('daCount:',debugCounter,row['COMP_DOT'])
                    # debugCounter += 1
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
===========WARNING INVALID FORMAT============

Convert canceled''')



#-----------------------------------------------------------------------------#
#                    CALLS MENU FUNCTION FOR USER SELECTION
#-----------------------------------------------------------------------------#

menuSystem()
