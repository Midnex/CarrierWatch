export = open('VendorNotes.csv','w')

vndNumLast = ''
count = 0

with open('2019.04.11-cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vndNum = line[0:7].replace(' ','')
        vndNotes = line[289:].replace('ú', '~').replace('"','\'').upper()

        if count == 0:
            export.write('"Vndr#","Vendor Notes"\n')
            count += 1
        elif count > 3:
            if vndNum == '': # if vndNum is empty
                if '|' in vndNotes:
                    for note in vndNotes.split('|'):
                        note = note.replace('\n','')
                        output = '"{}","{}"\n'.format(vndNumLast, note)
                        export.write(output)
                        count += 1
                else:
                    vndNotes = vndNotes.replace('\n','')
                    output = '"{}","{}"\n'.format(vndNumLast, vndNotes)
                    export.write(output)
                    count += 1
            else: # if vndNum is not empty
                if '|' in vndNotes:
                    for note in vndNotes.split('|'):
                        note = note.replace('\n', '')
                        output = '"{}","{}"\n'.format(vndNum, note)
                        export.write(output)
                        count += 1
                else:
                    vndNotes = vndNotes.replace('\n', '')
                    output = '"{}","{}"\n'.format(vndNum, vndNotes)
                    export.write(output)
                    count += 1
                vndNumLast = vndNum
        else:
            count += 1