export = open('VendorNotes.csv','w')

vndNumLast = ''
count = 0

with open('2019.04.18-cardump.txt','r') as txt_in_file:
    for line in txt_in_file:
        vndNum = line[0:7].replace(' ','')
        vndMC = line[222:228]
        vndDOT = line[244:252]
        vndNotes = line[289:].replace('ú', '~').replace('"','\'').upper()

        if count == 0:
            export.write('"Vndr#","Docket Number","DOT Number","Vendor Notes"\n')
            count += 1
        elif count > 3:
            if vndNum == '': # if vndNum is empty
                if '|' in vndNotes:
                    for note in vndNotes.split('|'):
                        note = note.replace('\n','')
                        output = f'"{vndNumLast}", "{vndMC}", "{vndDOT}", "{note}"\n'
                        export.write(output)
                        count += 1
                else:
                    vndNotes = vndNotes.replace('\n','')
                    output = f'"{vndNumLast}", "{vndMC}", "{vndDOT}", "{vndNotes}"\n'
                    export.write(output)
                    count += 1
            else: # if vndNum is not empty
                if '|' in vndNotes:
                    for note in vndNotes.split('|'):
                        note = note.replace('\n', '')
                        output = f'"{vndNum}", "{vndMC}", "{vndDOT}", "{note}"\n'
                        export.write(output)
                        count += 1
                else:
                    vndNotes = vndNotes.replace('\n', '')
                    output = f'"{vndNum}", "{vndMC}", "{vndDOT}", "{vndNotes}"\n'
                    export.write(output)
                    count += 1
                vndNumLast = vndNum
        else:
            count += 1