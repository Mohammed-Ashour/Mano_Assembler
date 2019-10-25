from grammer import LANG_DICT
from helpers import convert_to_hex, construct_output, out_file

import json
config = ""

with open("config.json", "r") as f: config = json.load(f)
print(config)
mode = config["mode"]

mem_ref_inst = LANG_DICT["MEM_REF"].keys()
reg_inst = LANG_DICT["REG_INST"].keys()
io_inst = LANG_DICT["IO"].keys()
LC = 0
locs = {}
final_code = ""
num_systems = ["DEC", "BIN", "HEX"]

def read_input(inp_file_location):
    with open(inp_file_location, 'r') as f:
        data = f.read().splitlines()
        return data



def make_memory(loc_line, index):
    loc_name = loc_line.split(",")[0]
    value = convert_to_hex(loc_line.split(",")[1])
    return {loc_name : {"value": value, "index": str(index) }}

def read_from_memory(pesudo):
    return locs[pesudo]["value"]

def memory_ref_interpreter(inst_line):
    if "/" in inst_line:
        inst_line = inst_line.split(" /")[0]
    line = inst_line.split(" ")
    inst = line[0]
    m_inst = ""
    if len(line) > 3:
        print("heeeey" + inst_line)
        inst = line[1]
        m_inst =  LANG_DICT["MEM_REF"][inst]["1"] #TODO handle LOP (test2)
    else:
        m_inst = LANG_DICT["MEM_REF"][inst]["0"]
    m_inst = m_inst.replace("XXX", locs[line[1]]["index"])
    return m_inst



def simple_converter(data):
    global LC, final_code
    cur_index = 0
    for i in data:
        cur_index += 1
        if "ORG" in i: 
            LC = int(i.split(" ")[1])
            cur_index = LC - 1  # as that location is the next instruction location
        elif "," in i:
            locs.update(make_memory(i, cur_index))
    
    for i in data:
        cur_index += 1
        inst = i.split(" ")[0]
        if  inst in mem_ref_inst:
            print(memory_ref_interpreter(i))
            final_code = construct_output(final_code, str(cur_index) + " " + memory_ref_interpreter(i))
        elif inst in reg_inst:
            print(LANG_DICT["REG_INST"][inst])
            final_code = construct_output(final_code, str(cur_index) + " " + LANG_DICT["REG_INST"][inst])
        elif inst in io_inst:
            final_code = construct_output(final_code, str(cur_index) + " " + LANG_DICT["IO"][inst])
            print(LANG_DICT["IO"][inst])
        else:
            if inst == "ORG":
                LC = int(i.split(" ")[1])
                cur_index = LC - 1
            elif inst == "END":
                break
            elif inst in num_systems:
                print(i)
            else:
                final_code =  construct_output(final_code,str(cur_index) + " " + read_from_memory(i.split(",")[0]) )




x = read_input("test2.inp.txt")
simple_converter(x)
out_file(final_code, "out.out")
print(locs)

 
