file_Name= raw_input("Enter the name of the file read the Gcode from: ")

txt_file=open(file_Name,"r") #opening file
txt_string=txt_file.read()
print("Reading from file")
txt_file.close()#closing text file to save memory

list=txt_string.split()
length=len(list)

#index variable for looping
i=0
#output each "word" onto console
while i<length:
    print(list[i])
    i += 1
i=0
#variables storing info for instruction, initially just all zeros
endX=0
endY=0
feedRate=0
offsetX=0
offsetY=0

#functions for getting info
def getEndPos(param):
    if param.startswith('X'):
        endX=int(param.lstrip('X'))
        print('End X: '+str(endX))
    elif param.startswith('Y'):
        endY=int(param.lstrip('Y'))
        print('End Y: '+str(endY))
    else:
        print('Error instruction')
def getFeed(param):
    if param.startswith('F'):
       feedRate=int(param.lstrip('F'))
       print('Feed rate: '+ str(feedRate))
    else:
        print('Error instruction')
def getOffset(param):
    if param.startswith('I'):
        offsetX=int(param.lstrip('I'))
        print('X Offset: ' + str(offsetX))
    elif param.startswith('J'):
        offsetY=int(param.lstrip('J'))
        print('Y Offset: ' + str(offsetY))
    else:
        print('Error in instruction')
    
#loop for going through instructions
while i<length:
    if list[i]=='M04': #pen up
        print('Pen Up')
    elif list[i]=='M03': #pen down
        print('Pen Down')
    elif list[i]=='M02': #end of program
        print('End of program')
    elif list[i]=='G28': #return home
        print('Return Home')
    elif list[i]=='G00': #Rapid Position
        print('Rapid Position')
        i+=1
        getEndPos(list[i])
        i+=1
        getEndPos(list[i])
        
    elif list[i]=='G01': #Linear Interpolation
        print('Linear interpolation')
        i+=1
        getEndPos(list[i])
        i+=1
        getEndPos(list[i])
        i+=1
        getFeed(list[i])
    elif list[i]=='G02': #Circ Interpol CW
        print('Circ Interpol CW')
        i+=1
        getEndPos(list[i])
        i+=1
        getEndPos(list[i])
        i+=1
        getOffset(list[i])
        i+=1
        getOffset(list[i])
    elif list[i]=='G03': #Circ Interpol CCW
        print('Circ Interpol CCW')
        i+=1
        getEndPos(list[i])
        i+=1
        getEndPos(list[i])
        i+=1
        getOffset(list[i])
        i+=1
        getOffset(list[i])
    else: #in case of error
        print('Error instruction')
    i+=1 #move on to next instruction
