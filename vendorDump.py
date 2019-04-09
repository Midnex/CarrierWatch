#   TODO: If row is blank it needs to append to the previous
#   TODO: Vendor Notes now delimited by pipe |

export = open('carddump.csv','w')
count = 0

header = 'Vnd#, Type, Status, Attached, Last Used, Vendor Name, Add, City, St, Zip, Phone, Email, Fax, Air, MC#, InsExpDate, Cmp., DOT#, E I No, TTL.INV, Vendor Notes'

with open('cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vnd = line[0:7].strip().upper() # Vendor #
        type = line[8:20].strip().upper() # Vendor Type
        status = line[21:30].strip().upper() # Status
        attached = line[31:39].strip().upper() # Docs Attached
        lastused = line[40:49].strip().upper().replace('.','/') # Last Used
        vndname = line[50:90].strip().upper() # Vendor Name
        add = line[91:124].strip().upper() # Vendor Address
        city = line[125:144].strip().upper() # Vendor City
        st = line[145:147].strip().upper() # Vendor State
        zip = line[148:158].strip().upper() # Vendor Zip
        phone = line[159:171].strip().upper().replace('-','').replace(' ','') # Vendor Phone
        email = line[172:202].strip().upper() # Vendor Email
        fax = line[203:215].strip().upper().replace('-','').replace(' ','') # Vendor Fax
        air = line[216:220].strip().upper() # UNLOCODE Airport (minus US prefix)
        mcnum = line[221:227].strip().upper() #MC Number
        insExpDate = line[228:238].strip().upper() # Insurance Expiration Date
        cmp = line[239:243].strip().upper() # ?
        dotNum = line[244:251].strip().upper() # DOT Number
        eino = line[252:264].strip().upper()  # E I Number
        ttlinv = line[265:278].strip().upper().replace(',','') # Total invoiced
        # date = line[275:283].upper().strip() # Follow Up Date
        vndnotes = line[288:].strip().upper().replace(',','~').replace('Ú','~') # Vendor Notes

        # fixs for Excel dropping zeros.
        if dotNum == '':
            dot = ''
        else:
            dotNum = '\'' + dotNum

        if mcnum == '':
            mcnum == ''
        else:
            mcnum = '\'' + mcnum

        fileHeader = vnd, type, status, attached, lastused, vndname, add, city, st, zip, phone, email, fax, air, mcnum, insExpDate, cmp, dotNum, eino, ttlinv, vndnotes

        if count == 0:
            export.write(header)
        elif count > 0:
            newHeader = '"' + vnd + '","' + type + '","' + status + '","' + attached + '","' + lastused + '","' + vndname + '","' + add + '","' + city + '","' + st + '","' + zip + '","' + phone + '","' + email + '","' + fax + '","' + air + '","' + mcnum + '","' + insExpDate + '","' + cmp + '","' + dotNum + '","' + eino + '","' + ttlinv + '","' + vndnotes + '"\n'
            export.write(str(newHeader))
        count += 1
print('done')
