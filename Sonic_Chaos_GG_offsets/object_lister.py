
from pathlib import Path


CONST_ROM_FILESYSTEM_DATA = {
    "sc":  {
        "rom_dir": "E:\\EMU\\GENESIS",
        "rom_files": {
            "gg": "Sonic Chaos (USA, Europe, Brazil).gg",
            "sms": "Sonic Chaos (EB) [!].sms"
        },
        "Levels": {
            "THZ1":  0x705AE,
            "THZ2":  0x7078C,
            "THZ3":  0x708FE,
            "GPZ1":  0x70959,
            "GPZ2":  0x70B7F,
            "GPZ3":  0x70DAE,
            "SEZ1":  0x70DF7,
            "SEZ2":  0x70F57,
            "SEZ3":  0x71081,
            "MGHZ1": 0x710C1,
            "MGHZ2": 0x711F4,
            "MGHZ3": 0x71378,
            "APZ1":  0x713C1,
            "APZ2":  0x714FD,
            "APZ3":  0x7160C,
            "EEZ1":  0x71631,
            "EEZ2":  0x716DD,
            "EEZ3":  0x71819
        }
    },
    "stt": {}
}

ROM_SELECTION    = "sc"
SYSTEM_SELECTION = "gg"
LEVEL_SELECTION  = ["THZ1","THZ2","THZ3","GPZ1","GPZ2","GPZ3","SEZ1","SEZ2","SEZ3","MGHZ1","MGHZ2","MGHZ3","APZ1","APZ2","APZ3","EEZ1","EEZ2","EEZ3"]
OUTPUT_FILEPATH   = Path(__file__).resolve().parent / "combined_object_list.csv"
ROM_DIR       = Path("./")
ROM_FILEPATH  = None

class AspectObject:
    def __init__(self,hexData: bytearray,level:int,idx:int,offset:str):
        self.address = offset
        self.type = hexData[0]
        self.x    = {"macro": hexData[1], "micro": hexData[2]}
        self.y    = {"macro": hexData[3], "micro": hexData[4]}
        self.flags = hexData[5]
        self.params = hexData[6]
        self.tiles  = {"normal": hexData[7], "reversed": hexData[8]}
        if level != None:
            self.level = level
        else:
            self.level = "Unset"
        if idx != None:
            self.index = idx
        else:
            self.index = "Unset"

    def print(obj):
        typ = f"{obj.type:02x}".upper()
        xMacro = f"{obj.x['macro']:02x}".upper()
        yMacro = f"{obj.y['macro']:02x}".upper()
        xMicro = f"{obj.x['micro']:02x}".upper()
        yMicro = f"{obj.y['micro']:02x}".upper()
        flags = f"{obj.flags:02x}".upper()
        params = f"{obj.params:02x}".upper()
        tilesNormal = f"{obj.tiles['normal']:02x}".upper()
        tilesReversed = f"{obj.tiles['reversed']:02x}".upper()
        
        print(f"Level: {obj.level} Index: {obj.index}")
        print(f"Aspect Object: {typ} Hex Values:")
        print(f" -  X Macro: {xMacro} Micro: {xMicro}")
        print(f" -  Y Macro: {yMacro} Micro: {yMicro}")
        print(f" -  Flags: {flags}")
        print(f" -  Params: {params}")
        print(f" -  Tiles Normal: {tilesNormal} Reversed: {tilesReversed}")

    def create_csv_record(obj):
        typ           = f"{obj.type:02x}".upper()
        xMacro        = f"{obj.x['macro']:02x}".upper()
        yMacro        = f"{obj.y['macro']:02x}".upper()
        xMicro        = f"{obj.x['micro']:02x}".upper()
        yMicro        = f"{obj.y['micro']:02x}".upper()
        flags         = f"{obj.flags:02x}".upper()
        params        = f"{obj.params:02x}".upper()
        tilesNormal   = f"{obj.tiles['normal']:02x}".upper()
        tilesReversed = f"{obj.tiles['reversed']:02x}".upper()
        return f"{obj.level},{obj.index},{obj.address},{typ},{xMacro},{xMicro},{yMacro},{yMicro},{flags},{params},{tilesNormal},{tilesReversed}"

def findRomData(selected_rom):
    global ROM_DIR,ROM_FILEPATH
    print ("------ Finding ROM Data ------")
    print (" ")
    ROM_DIR      = Path(CONST_ROM_FILESYSTEM_DATA[selected_rom]["rom_dir"])
    ROM_FILEPATH = ROM_DIR / CONST_ROM_FILESYSTEM_DATA[selected_rom]["rom_files"][SYSTEM_SELECTION]
    ROM_FILEPATH = ROM_FILEPATH.resolve()
    print(f"Using ROM Filepath: {ROM_FILEPATH}")

def loadRomData(selected_rom, level_selection):
    global ROM_DIR,ROM_FILEPATH
    findRomData(selected_rom)

    rom_data = None
    fopen = open(ROM_FILEPATH, "rb")
    rom_data = fopen.read()
    fopen.close()
    rom_data = bytearray(rom_data)
    print(f"ROM Data Loaded: {len(rom_data)} bytes")



    print ("------ Reading Object Data from Object List at: 705AE ------")
    start_offset = hex(CONST_ROM_FILESYSTEM_DATA[ROM_SELECTION]["Levels"][level_selection])[2:].upper()
    current_offset = start_offset
    bytes_to_read = 9;
    first_hex = "00"
    object_index = 0
    object_list = []
    while first_hex != "FF" and object_index < 100:  # Limiting to 100 objects for safety
        start_idx = int(current_offset, 16)
        end_idx = start_idx + bytes_to_read;
        current_block = rom_data[start_idx:end_idx]
        first_hex = current_block[0:1].hex().upper()
        if first_hex != "FF":
            #print(f"Current Block: {current_block.hex(' ').upper()}")
            new_object = AspectObject(current_block, level_selection, object_index,current_offset)
            object_list.append(new_object)
            object_index += 1
            current_offset = hex(end_idx)[2:].upper()
            
    if first_hex == "FF":
        print ("------ End of Object List Reached due to ending character ------")
    else:
        print ("------ Object List Limit Reached due to 100 limit ------")

    print ("------ Writing Object Data to CSV File ------")
    csv_file_path =  Path(__file__).resolve().parent / f"{level_selection}_object_list.csv"
    with open(csv_file_path, "w") as f:
        f.write("Level,Object Index,Address,Type,X Macro,X Micro,Y Macro,Y Micro,Flags,Params,Tiles Normal,Tiles Reversed\n")
        for obj in object_list:
            f.write(obj.create_csv_record() + "\n")

    with open(OUTPUT_FILEPATH, "a") as f:
        for obj in object_list:
            f.write(obj.create_csv_record() + "\n")

def main():
    with open(OUTPUT_FILEPATH, "w") as f:
        f.write("Level,Object Index,Address,Type,X Macro,X Micro,Y Macro,Y Micro,Flags,Params,Tiles Normal,Tiles Reversed\n")
        f.close()

    for level in LEVEL_SELECTION:
        loadRomData(ROM_SELECTION, level)

if __name__ == "__main__":
    print ("---------------------------")
    print ("------ Object Lister ------")
    print ("---------------------------")
    print (" ")
    main()