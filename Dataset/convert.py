import csv, re, os

def createcsv(file):
    rawfile = open(file, 'r')
    name = file.replace('.' + file.split('.')[-1], '') + '.csv'

    with open('../csvfiles/'+ name, 'w') as csvfile:
        writer = csv.writer(csvfile)

        for row in rawfile:
            csvrow = []
            #print("raw row: ", row)

            for elem in re.split("\s|,", row):
                #print(elem)
                try:
                    float(elem)
                    csvrow.append(float(elem))
                except:
                    #print("oomb", elem, '.')
                    pass

            writer.writerow(csvrow)
            #print("csvrow: ",csvrow)
    rawfile.close()

if __name__ == "__main__":
    files = os.listdir('.')
    print("select file to convert", files)
    createcsv(files[int(input())])
    print("converted Succefully \n File should be located in the Dataset Folder")
