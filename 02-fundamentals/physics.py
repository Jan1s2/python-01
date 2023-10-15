'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
GRAVITATIONAL_CONSTANT = 6.6743e-11
EARTH_MASS = 5.972e24

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def earth_to_moon(weight):
    '''Converts weight on earth to weight on the moon'''
    return earth_to_mass(weight) * MOON_GRAVITY

def moon_to_earth(weight):
    '''Converts weight on the moon to weight on earth'''
    return moon_to_mass(weight) * EARTH_GRAVITY

def earth_to_mass(weight):
    '''Calculates the mass from weight on earth'''
    return weight / EARTH_GRAVITY

def moon_to_mass(weight):
    '''Calculates the mass from weight on the moon'''
    return weight / MOON_GRAVITY

def gravity(mass_one:float, mass_two:float, distance:float):
    '''Gravity equation; all masses are in kg
    Params:
        constant (float) gravitational constant
        mass_one (float) mass of object one
        mass_two (float) mass of object two
        distance (float) distance between the centers of mass of the two objects (m)
        '''
    return (GRAVITATIONAL_CONSTANT * mass_one * mass_two) / distance ** 2

def earth_gravity(mass, distance:float=6378000):
    '''Calls gravity with earth in mind
    mass (float) mass of the object (kg)
    distance (float) distance between the object and earth - default is radius of earth (m)
    '''
    return gravity(EARTH_MASS, mass, distance)

def velocity_to_light(velocity:float) -> float:
    '''Compare velocity to speed of light'''
    return velocity / SPEED_OF_LIGHT

def velocity_to_sound(velocity:float) -> float:
    '''Compare velocity to speed of sound'''
    return velocity / SPEED_OF_SOUND

def velocity_all(velocity:float) -> tuple[float, float]:
    '''Compare velocity to speed of light and sound'''
    return velocity_to_light(velocity), velocity_to_sound(velocity)

if __name__ == "__main__":
    print(f"One 1 kg on moon equals {moon_to_earth(1)} kg on earth")
    print(f"One 1 kg on earth equals {earth_to_moon(1)} kg on moon")
    print(f"One 1 m/s equals {velocity_to_light(1)} of light and {velocity_to_sound(1)} of sound")
