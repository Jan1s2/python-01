import re

def getPass() -> str:
    """
        Gets and checks the password from user
    """
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
    """
        Gets the proxy server for connections
    """
    proxy:str = input("Zadejte proxy: ")
    print("Použitý proxy server: {proxy}".format(proxy = proxy))
    return proxy

def getRepo() -> int:
    """
        Asks user for repository
    """
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
    """
        Allows user to input groups
    """
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
    """
        Test for C-like output formatting
    """
    probability:float = float(input("Zadejte pravděpodobnost chyby: "))
    print("Pravděpodobnost: %3.2f" %probability)
    return probability

def calculate() -> None:
    """
        Calculates the input
    """
    form:str = input("DEBUG: Zadejte matematický výraz: ")
    # Checks whether the untrusted input actually is in base format
    if(re.match(r"^\d+ ?[+*/\-] ?\d+$", form) != None):
        print("Výsledek: ", eval(form))
    else:
        print("Nevalidní vstup")

password:str = getPass()
proxy:str = getProxy()
repo:int = getRepo()
groups:list[str] = getGroups()
prob:float = getProbability()
calculate()
