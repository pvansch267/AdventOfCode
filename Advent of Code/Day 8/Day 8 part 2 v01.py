# ****************************************************************************************************** #
# Open file and create dictionary                                                                        #
# Dictionary format: Key - Instruction ID : Value - Instruction                                          #
# ****************************************************************************************************** #
instruction_batch_data = open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 8\\data.txt",'r')
instructions_cleaned_data = instruction_batch_data.read().strip().split('\n')
instructions_dict = dict(enumerate(line.strip() for line in instructions_cleaned_data))
instructions_switch_dict = {x: 0 for x in instructions_dict}

vGlobalAccumulateScore = 0
vGlobalTerminateFlag = False

def fnSetScoreVariables():
    inst_acc_values = [0,0]

    return inst_acc_values

def fnSetFrequencyDict(instructions_frequency_dict):
    instructions_frequency_dict = {x: 0 for x in instructions_dict}

    return instructions_frequency_dict

# 1. Get Instruction
def fnGetInstruction(instruction):
    vTmpInstruction = instructions_dict[instruction]

    return vTmpInstruction

# 2. Apply Instruction
def fnApplyInstruction(tmpInstruction,inst_acc_values):
    instruction = inst_acc_values[0]
    accumulator = inst_acc_values[1]

#    print('Instruction ',instruction)
#    print('Accumulator ',accumulator)

    vInstructionType = tmpInstruction.split(' ')[0]
    vInstructionDirection = tmpInstruction.split(' ')[1][0]
    vInstructionValue = tmpInstruction.split(' ')[1][1:]

    if vInstructionDirection == '+':
        vInstructionValue = int(vInstructionValue)
    else:
        vInstructionValue = int(vInstructionValue)*-1

#    print('Instruction ',vInstructionType)
#    print('Direction ',vInstructionDirection)
#    print('Value ',vInstructionValue)

    if vInstructionType == 'nop':
        accumulator = fnSetNopInstruction(accumulator)
        instruction = fnIncrementInstruction(instruction)
    elif vInstructionType == 'acc':
        accumulator = fnSetAccInstruction(accumulator,vInstructionValue)
        instruction = fnIncrementInstruction(instruction)
    elif vInstructionType == 'jmp':
        instruction = fnSetJmpInstruction(instruction, vInstructionValue)

#    print('Next Instruction:', instruction)
#    print('Accumulator Value:', accumulator)

    return [instruction,accumulator]

# 2.0.1 Increment Instruction
def fnIncrementInstruction(instruction):
    instruction += 1

    return  instruction

# 2.0.2 Update Instruction Frequency Dictionary
def fnUpdateFrequencyDict(accumulator, instructions_frequency_dict):
    instructions_frequency_dict[accumulator] += 1

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
def fnTriggerApplication():
    global vGlobalAccumulateScore, vGlobalTerminateFlag

    inst_acc_values = fnSetScoreVariables()
    instructions_frequency_dict = {x: 0 for x in instructions_dict}

    count_inctructions = len(instructions_dict)

    flRuleChange = False

    vInstructionID = inst_acc_values[0]
    vAccumulatedScore = inst_acc_values[1]

    while vInstructionID < count_inctructions:
        if vGlobalTerminateFlag:
            return vGlobalTerminateFlag

        vTmpInstruction = fnGetInstruction(vInstructionID)
    
        instructions_frequency_dict = fnUpdateFrequencyDict(vInstructionID, instructions_frequency_dict)

        if not flRuleChange and instructions_switch_dict[vInstructionID] == 0:
            if vTmpInstruction.split(' ')[0] == 'nop':
                vTmpInstruction = vTmpInstruction.replace('nop','jmp')
                instructions_switch_dict[vInstructionID] = 1    
                flRuleChange = True
            elif vTmpInstruction.split(' ')[0] == 'jmp':
                vTmpInstruction = vTmpInstruction.replace('jmp','nop')
                instructions_switch_dict[vInstructionID] = 1    
                flRuleChange = True           

        if instructions_frequency_dict[vInstructionID] == 2:
            fnTriggerApplication()
        else:
            inst_acc_values = fnApplyInstruction(vTmpInstruction,inst_acc_values)
            vInstructionID = inst_acc_values[0]
            vAccumulatedScore = inst_acc_values[1]


    print('Answer is: ',vAccumulatedScore)
    vGlobalTerminateFlag = True
    return vGlobalTerminateFlag

print(fnTriggerApplication())