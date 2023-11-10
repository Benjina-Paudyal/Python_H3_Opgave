# Her udleveres kode til løsning af opgave 1

def pace2velocity(p):

    """ 
    Omregner tempo til hastighed
    
    Parameters:
    p:pace
    
    returns:
    velocity
    """
    return (1000/60)/p

assert pace2velocity(10) == 1.666666666666666666

def v2p(v):
    return (1000/60)/v

assert v2p(1.666666666666666666) == 10

# Her udleveres kode til at løse opgave 2
# virker med stien når du har mappen `projektopgave` aktiv`

def indlaes_fra_fit(fname = "data/hok_klubmesterskab_2022/CA8D1347.FIT"):
    from fit_file import read
    points = read.read_points(fname)
    return points

punkter = indlaes_fra_fit()

print(f"Der er indlæst {len(punkter)} punkter fra filen")
print(punkter[300])

## -----------------------------------------------------------------

from geopy.distance import distance 

# afstand mellem punkter

# Ved at bruge enumarate får jeg både hvert element (`p`), og et index for hvert element (`i`), altid startende med 0 
# Jeg itereret over listen `punkter[1:]` hvor første element er slicet væk
#   inde i løkken henter jeg forrige punkt med index'et i 
#     Da i starter på nul, for jeg hvert punkt fra 0 til nedstsidste,
#     punktet p er hvert af punkterne fra andet til sidste

for i, p in enumerate(punkter[1:]):
    # previus point
    pp = punkter[i]

    dt = (p['timestamp'] - pp['timestamp']).seconds
    dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
    v = dd/dt
    print(f"p: {p}")
    print(f"pp: {pp}")
    print(f"dt: {dt}")
    print(f"dd: {dd}")

