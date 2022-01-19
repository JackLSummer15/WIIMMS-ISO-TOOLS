import os

try:
    os.mkdir('output_rom')
except:
    pass

wiidir=input("Enter your extracted Wii directory: ")
os.system('wit copy extracted_roms/'+wiidir+' --dest output_rom/'+wiidir+'.wbfs')
