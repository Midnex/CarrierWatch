export = open('VendorNotes.csv','w')

vndLast = ''
count = 0


with open('2019.04.08-cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vnd = line[0:7].replace(' ','')
        vndnotes = line[288:]

        if count == 0:
            export.write('"Vndr#","Vendor Notes"\n')
        if count > 3:
            if vnd == '':
                if '|' in vndnotes:
                    for i in vndnotes.split('|'):
                        # output = '"' + vndLast + '","' + i.replace('\n','') + '"\n'
                        output = '"{}",""{}"\n'.format(vndLast,i.replace('\n',''))
                        export.write(output.replace('ú',' ').upper())
                else:
                    # output = '"' + vndLast + '","' + vndnotes.replace('\n','') + '"\n'
                    output = '"{}","{}"\m'.format(vndLast,vnd.replace('\n',''))
                    export.write(output.replace('ú',' ').upper())
            else:
                if '|' in vndnotes:
                    for i in vndnotes.split('|'):
                        # output = '"' + vnd + '","' + i.replace('\n','') + '"\n'
                        output = '"{}","{}"\n'.format(vndLast,i.replace('\n',''))
                        export.write(output.replace('ú',' ').upper())
                else:
                    # output = '"' + vndLast + '","' + vndnotes.replace('\n','') + '"\n'
                    output = '"{}","{}"\n'.format(vndLast,vnd.replace('\n',''))
                    export.write(output.replace('ú',' ').upper())
        vndLast = vnd
        count += 1
