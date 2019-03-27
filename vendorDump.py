import pyperclip


#   TODO: get length of each item, and store in list. run through list and print exactly that but remove spaces, \t and other items that are not needed.
#   TODO: If row is blank it needs to append to the previous

with open('cardump.txt','r') as txt_in_file:
    rowArrayLen = []
    count = 1
    for textRow in txt_in_file:
        rowArray = []
        if count == 1:
            for rowCol in textRow.split('. '):
                if 'Attached' in rowCol:
                    rowArrayLen.append(len('Attached'))
                    rowArray.append('Attached')
                    rowArrayLen.append(len('Last Used'))
                    rowArray.append('Last Used')
                    rowArrayLen.append(len(rowCol[rowCol.find('Vendor Name'):]))
                    rowArray.append(rowCol[rowCol.find('Vendor Name'):])
                if 'St Zip' in rowCol:
                    rowArrayLen.append(len('St'))
                    rowArray.append('St')
                    rowArrayLen.append(len('Zip'))
                    rowArray.append('Zip')
                if 'InsExpDate Cmp' in rowCol:
                    rowArrayLen.append(len('InsExpDate'))
                    rowArray.append('InsExpDate')
                    rowArrayLen.append(len('Cmp'))
                    rowArray.append('Cmp')
                if 'Ind E I No' in rowCol:
                    rowArrayLen.append(len('Ind'))
                    rowArray.append('Ind')
                    rowArrayLen.append(len('E I No'))
                    rowArray.append('E I No')
                else:
                    rowArrayLen.append(len(rowCol)+1)
                    rowArray.append(rowCol + '.')
                    print(rowArray)
        else:
            print(rowArray)
            break
        count += 1
