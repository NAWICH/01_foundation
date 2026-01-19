def usd_npr(usd):
    print("The USD in NPR is: ")
    return float(usd) * 145.28

def usd_inr(usd):
    print("The USD in INR is: ")
    return float(usd) * 90.87

def usd_cad(usd):
    print("The USD in CAD is: ")
    return float(usd) * 1.39

def choose(num,usd):
    if int(num) == 1:
        return usd_npr(usd)
    elif int(num) == 2:
        return usd_inr(usd)
    elif int(num) == 3:
        return usd_cad(usd)
    else :
        print("invalid entry")

converter = input("choose one \n 1.USD to NPR \n 2.USD to INR \n 3.USD to CAD\n")
usd = input("Enter amount of USD: ")
if __name__ == "__main__":
    print(choose(converter, usd))
