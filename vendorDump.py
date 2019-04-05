#   TODO: If row is blank it needs to append to the previous

export = open('carddump.csv','w')
count = 0

header = 'Vnd#, Type, Status, Attached, Last Used, Vendor Name, Add, City, St, Zip, Phone, Email, Fax, Air, MC#, InsExpDate, Cmp., Ind, E I No, TTL.INV, Vendor Notes'

with open('cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vnd = line[0:7].strip().upper()
        type = line[8:20].strip().upper()
        status = line[21:30].strip().upper()
        attached = line[31:39].strip().upper()
        lastused = line[40:49].strip().upper().replace('.','/')
        vndname = line[50:90].strip().upper()
        add = line[91:124].strip().upper()
        city = line[125:144].strip().upper()
        st = line[145:147].strip().upper()
        zip = line[148:158].strip().upper()
        phone = line[159:171].strip().upper().replace('-','').replace(' ','')
        email = line[172:202].strip().upper()
        fax = line[203:215].strip().upper().replace('-','').replace(' ','')
        air = line[216:220].strip().upper()
        mcnum = line[221:227].strip().upper()
        insExpDate = line[228:238].strip().upper()
        cmp = line[239:243].strip().upper()
        ind = line[244:247].strip().upper()
        eino = line[248:260].strip().upper()
        ttlinv = line[261:274].strip().upper().replace(',','')
        # date = line[275:283].upper().strip() #not used currently
        vndnotes = line[284:].strip().upper().replace(',','~').replace('Ú','~')

        fileHeader = vnd, type, status, attached, lastused, vndname, add, city, st, zip, phone, email, fax, air, mcnum, insExpDate, cmp, ind, eino, ttlinv, vndnotes

        if count == 0:
            export.write(header)
        elif count > 0:
            newHeader = '"' + vnd + '","' + type + '","' + status + '","' + attached + '","' + lastused + '","' + vndname + '","' + add + '","' + city + '","' + st + '","' + zip + '","' + phone + '","' + email + '","' + fax + '","' + air + '","' + mcnum + '","' + insExpDate + '","' + cmp + '","' + ind + '","' + eino + '","' + ttlinv + '","' + vndnotes + '"\n'
            export.write(str(newHeader))
        count += 1
print('done')
