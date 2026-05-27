resp = {'n': 0, 'y': 1, 'r': 2, 'e': 10, 'm': 11, 'h': 12}

def getTextInput(msg:str, opts:set[int])->int:
    while True:
        rtn:str = input(msg).lower()
        if rtn in resp:
            if (x := resp[rtn]) in opts:
                return x
        print(f"Response: '{rtn}' is not an accepted response")

def getCoordInput(msg:str)->tuple[int, int]:
    while True:
        rtn:str = input(msg)
        if len(rtn) == 3:
            a, b = int(rtn[0]), int(rtn[2])
            if a or b <= 3 and a or b >= 1:
                return a, b
            else:
                print("Column and row designation is 1-based and must be in range 1-3")
        else:
            print(f"Response: '{rtn}' is not an accepted response. Response must be in the form (column#,row#)")
