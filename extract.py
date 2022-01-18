import os

try:
    os.mkdir('input_rom')
    os.mkdir('extracted_roms')
except:
    pass

for rom in os.listdir("input_rom/"):
    gameid=rom.split('.')[0]
    os.system('wit extract input_rom/'+rom+' --dest extracted_roms/'+gameid)