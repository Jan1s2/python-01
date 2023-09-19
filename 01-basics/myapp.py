def getPass() -> str:
    pass_ready:str = ""
    while(pass_ready == ""):
        password:str = input("Zadej heslo: ")
        password_chk:str = input("Znovu zadej heslo: ")
        if password != password_chk:
            print("Hesla se neschodují!")
        else:
            pass_ready = password
    return pass_ready

def getProxy() -> str:
    proxy:str = input("Zadejte proxy: ")
    print("Použitý proxy server: {proxy}".format(proxy = proxy))
    return proxy

def getRepo() -> int:
    print("""
          Repozitáře:
          1 - cz
          2 - us
          3 - de
          """)
    repo:int = int(input("Repozitář: "))
    if repo < 1 or repo > 3:
        print("Invalid repo!")
        return 0
    print("Repo: ", repo)
    return repo

def getGroups() -> list[str]:
    print("""
          Skupiny:
          """)
    groups:list[str] = []
    groups.append(input("Napište primární skupinu: "))
    groups.append(input("Napište sekundární skupinu: "))
    print("""
          Primární skupina: {1}
          Sekundární skupina: {0}
          """.format(groups[1], groups[0]))
    return groups

def getProbability() -> float:
    probability:float = float(input("Zadejte pravděpodobnost chyby: "))
    print("Pravděpodobnost: %3.2f" %probability)
    return probability


'''
Note: eval() not implemented -> __import__("os").system("hostname")
'''
password:str = getPass()
proxy:str = getProxy()
repo:int = getRepo()
groups = getGroups()
prob = getProbability()
