def getPass() -> str:
    pass_ready:str = ""
    while(pass_ready == ""):
        password:str = input("Zadej heslo: ")
        password_chk:str = input("Znovu zadej heslo: ")
        if password != password_chk:
            print("Hesla se nechodují!")
        else:
            pass_ready = password
    return pass_ready

def getProxy() -> str:
    proxy = input("Zadejte proxy: ")
    print("Použitý proxy server: {proxy}".format(proxy = proxy))
    return proxy

def getRepo() -> int:
    print("""
          Repozitáře:
          1 - cz
          2 - us
          3 - de
          """)
    repo = input("Repozitář: ")
    if int(repo) < 1 or int(repo) > 3:
        print("Invalid repo!")
        return 0
    print("Repo: ", repo)
    return int(repo)

def getGroups() -> list[str]:
    print("""
          Skupiny:
          """)
    groups:list[str] = []
    groups[0] = input("Napište primární skupinu: ")
    groups[1] = input("Napište sekundární skupinu: ")
    print("""
          Primární skupina: {2}
          Sekundární skupina: {1}
          """.format(groups[1], groups[0]))
    return groups

def getProbability() -> float:
    probability:float = float(input("Zadejte pravděpodobnost chyby: "))
    print("Pravděpodobnost: f4.2" %probability)
    return probability


'''
Note: eval() not implemented -> __import__("os").system("echo A")
'''
password = getPass()
proxy = getProxy()
repo = getRepo()
groups = getGroups()
prob = getProbability()
