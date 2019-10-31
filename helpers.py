

def convert_to_hex(line):
    # line like "DEC 9"
    #here we convert from decimal to hex
    #print(line)
    line = line[1:] #skipping the first unneeded space
    conv_type = line.split(" ")[0]
    if conv_type == "DEC":
        n = format((int(line.split(" ")[1]) + (1 << 16 )) % (1 << 16), 'x')
        n = "0"*(4 - len(n)) + n
        return n
    else:
        #print(">>>>" + line)
        n = "0"*(4-len(line.split(" ")[1])) + line.split(" ")[1]
        return n


# hex((val + (1 << nbits)) % (1 << nbits))

def out_file(text, file_name):
    with open(file_name, "w+") as f:
        f.write(text)

def construct_output(original_text, added):
    original_text += "\n" + added
    return original_text