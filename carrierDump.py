#   TODO: If row is blank it needs to append to the previous
#   TODO: Vendor Notes now delimited by pipe |

export = open('cardump.csv','w')
count = 0

header = '"Vnd#","Type","Status","Attached","Last Used","Vendor Name","Add","City","St","Zip","Phone","Email","Fax","Air","MC#","InsExpDate","Cmp.","DOT#","E I No","TTL.INV","Vendor Notes"'

with open('cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vnd = line[0:7].strip().upper() # Vendor #
        carrierType = line[8:20].strip().upper() # Vendor Type
        status = line[21:30].strip().upper() # Status
        attached = line[31:39].strip().upper() # Docs Attached
        lastused = line[40:49].strip().upper().replace('.','/') # Last Used
        vndname = line[50:90].strip().upper() # Vendor Name
        add = line[91:124].strip().upper() # Vendor Address
        city = line[125:144].strip().upper() # Vendor City
        st = line[145:147].strip().upper() # Vendor State
        zipCode = line[148:158].strip().upper() # Vendor Zip
        phone = line[159:171].strip().upper().replace('-','').replace(' ','') # Vendor Phone
        email = line[172:202].strip().upper() # Vendor Email
        fax = line[203:215].strip().upper().replace('-','').replace(' ','') # Vendor Fax
        air = line[216:220].strip().upper() # UNLOCODE Airport (minus US prefix)
        mcnum = line[221:228].strip().upper() #MC Number
        insExpDate = line[229:239].strip().upper() # Insurance Expiration Date
        cmp = line[240:244].strip().upper() # ?
        dotNum = line[245:252].strip().upper() # DOT Number
        eino = line[253:265].strip().upper()  # E I Number
        ttlinv = line[266:279].strip().upper().replace(',','') # Total invoiced
        # date = line[279:283].upper().strip() # Follow Up Date, Change to flag.
        vndnotes = line[288:].strip().upper().replace(',','~').replace('Ú','~').replace('|','~').replace('~~','~') # Vendor Notes

        # fixs for Excel dropping zeros.
        if dotNum == '':
            dot = ''
        else:
            dotNum = f"'{dotNum}"

        if mcnum == '':
            mcnum == ''
        else:
            mcnum = f"'{mcnum}"

        if count == 0:
            export.write(header)
            export.write('\n')
        elif count > 4:
            newHeader = f'"{vnd}","{carrierType}","{status}","{attached}","{lastused}","{vndname}","{add}","{city}","{st}","{zipCode}","{phone}","{email}","{fax}","{air}","{mcnum}","{insExpDate}","{cmp}","{dotNum}","{eino}","{ttlinv}","{vndnotes}" \n'

            export.write(newHeader)
        count += 1
print('Done exporting cardump.csv')
