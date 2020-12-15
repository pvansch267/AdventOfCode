# ****************************************************************************************************** #
# Open file and create dictionary                                                                        #
# Dictionary format: Key - Instruction ID : Value - Instruction                                          #
# ****************************************************************************************************** #
instruction_batch_data = open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 8\\data.txt",'r')
instructions_cleaned_data = instruction_batch_data.read().strip().split('\n')
instructions_dict = dict(enumerate(line.strip() for line in instructions_cleaned_data))
instructions_frequency_dict = {x: 0 for x in instructions_dict}
instructions_switch_dict = {x: 0 for x in instructions_dict}

# print(instructions_dict)
# print(instructions_frequency_dict)

accumulator = 0
instruction = 0
inst_acc_values = [0,0]

count_inctructions = len(instructions_dict)

instruction = accumulator

# 1. Get Instruction
def fnGetInstruction(instruction):
    vTmpInstruction = instructions_dict[instruction]

    fnUpdateFrequencyDict(instruction, instructions_frequency_dict)


    return vTmpInstruction

# 2. Apply Instruction
def fnApplyInstruction(tmpInstruction,inst_acc_values):
    instruction = inst_acc_values[0]
    accumulator = inst_acc_values[1]

    print('Instruction ',instruction)
    print('Accumulator ',accumulator)

    vInstructionType = tmpInstruction.split(' ')[0]
    vInstructionDirection = tmpInstruction.split(' ')[1][0]
    vInstructionValue = tmpInstruction.split(' ')[1][1:]

    if vInstructionDirection == '+':
        vInstructionValue = int(vInstructionValue)
    else:
        vInstructionValue = int(vInstructionValue)*-1

    print('Instruction ',vInstructionType)
    print('Direction ',vInstructionDirection)
    print('Value ',vInstructionValue)

    if vInstructionType == 'nop':
        accumulator = fnSetNopInstruction(accumulator)
        instruction = fnIncrementInstruction(instruction)
    elif vInstructionType == 'acc':
        accumulator = fnSetAccInstruction(accumulator,vInstructionValue)
        instruction = fnIncrementInstruction(instruction)
    elif vInstructionType == 'jmp':
        instruction = fnSetJmpInstruction(instruction, vInstructionValue)

    print('Next Instruction:', instruction)
    print('Accumulator Value:', accumulator)

    return [instruction,accumulator]

def fnIncrementInstruction(instruction):
    instruction += 1

    return  instruction

# 2.0 Update Instruction Frequency Dictionary
def fnUpdateFrequencyDict(accumulator, instructions_frequency_dict):
    instructions_frequency_dict[accumulator] += 1
#    print(instructions_frequency_dict)

    return instructions_frequency_dict

# 2.1 No Operation Function
def fnSetNopInstruction(accumulator):
    accumulator += 0

    return  accumulator


# 2.2 Accumulate Function
def fnSetAccInstruction(accumulator, value):
    accumulator = accumulator + value

    return accumulator

# 2.3 Jump Function
def fnSetJmpInstruction(instruction, value):
    instruction = instruction + value

    return instruction

# Trigger Endless Loop
while inst_acc_values[0] < count_inctructions:

    vTmpInstruction = fnGetInstruction(inst_acc_values[0])

   
    print('Instruction:', vTmpInstruction)

    if instructions_frequency_dict[inst_acc_values[0]] == 2:
        print('Accumulator: ', inst_acc_values[1])
        break
    else:
        inst_acc_values = fnApplyInstruction(vTmpInstruction,inst_acc_values)

