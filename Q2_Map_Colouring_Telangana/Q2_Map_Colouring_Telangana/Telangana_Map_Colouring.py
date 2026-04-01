import json

def isValid(state,color,assignment,neighbors):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor]==color:
            return False
    return True

def backTrack(assignment,states,colours,neighbors):
    if len(assignment)==len(states):
        return assignment

    unassigned=None
    for s in states:
        if s not in assignment:
            unassigned=s
            break

    for color in colours:
        if isValid(unassigned,color,assignment,neighbors):
            assignment[unassigned]=color
            result=backTrack(assignment,states,colours,neighbors)
            if result:
                return result
            del assignment[unassigned]

    return None

def main():
    print("Colour Mapping Telangana-(CSP Algorithm).")
    print()
    with open("TelanganaMap.json") as f:
        data=json.load(f)

    states=data["states"]
    edges=data["edges"]
    colours=data["colours"]

    neighbors={}
    for s in states:
        neighbors[s]=[]

    for a,b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    print("STATES:", end=" ")
    print(*states,sep=",")
    print("COLOURS:", end=" ")
    print(*colours,sep=",")

    startStates=input("Enter state: ")
    startColour=input("Enter color: ")

    if startStates not in states or startColour not in colours:
        print("No solution")
        return

    assignment={}
    assignment[startStates]=startColour

    if not isValid(startStates,startColour,assignment,neighbors):
        print("No solution")
        return

    solution=backTrack(assignment,states,colours,neighbors)

    if solution:
        for s in states:
            print(s,":",solution[s])
    else:
        print("No solution")

if __name__=="__main__":
    main()
