import os

try:
    os.mkdir('output_rom')
except:
    pass

gameid=input("Enter your Game ID: ")
os.system('wit copy extracted_roms/'+gameid+' --dest output_rom/'+gameid+'.wbfs')