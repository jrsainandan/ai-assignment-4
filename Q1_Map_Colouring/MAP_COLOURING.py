states=['WA','NT','Q','SA','NSW','V','T']

neighbors={
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'Q':['NT','SA','NSW'],
    'SA':['WA','NT','Q','NSW','V'],
    'NSW':['Q','SA','V'],
    'V':['SA','NSW'],
    'T':[]
}

colours=['Red','Green','Blue']

def isValid(state,color,assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor]==color:
            return False
    return True

def backTrack(assignment):
    if len(assignment)==len(states):
        return assignment

    unassigned=None
    for s in states:
        if s not in assignment:
            unassigned=s
            break

    for color in colours:
        if isValid(unassigned,color,assignment):
            assignment[unassigned]=color
            result=backTrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

def main():
    print("Colour Mapping-(CSP Algorithm).")
    print()
    print("STATES:", end=" ")
    print(*states,sep=",")

    print("COLOURS:", end=" ")
    print(*colours,sep=",")

    startState=input("Enter state: ")
    startColour=input("Enter color: ")

    if startState not in states or startColour not in colours:
        print("No solution")
        return

    assignment={}
    assignment[startState]=startColour

    if not isValid(startState,startColour,assignment):
        print("No solution")
        return

    solution=backTrack(assignment)

    if solution:
        for s in states:
            print(s,":",solution[s])
    else:
        print("No solution")

if __name__=="__main__":
    main()
