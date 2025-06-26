def berechne_fruchtbarkeitswkt(alter,bmi,raucher_status,alkohol_status,eisprung_entfernung):
    # Zuerst wird für jede Option die Wahrscheinlichkeit angegeben
    alter_wkt = (1.0 if 16 <= alter <= 26 else 0.882 
                 if 26 < alter <= 29 else 0.765 if 29 < alter <= 34 
                 else 0.588 if 35 <= alter <= 39 else 0.05) 
    bmi_wkt = (0.35 if bmi < 17 else 0.89 if 17 <= bmi <= 20 else 1.0 
               if 20 < bmi < 25 else 0.93 if 25 <= bmi < 30 else 0.33 )
    raucher_status_wkt = (1.0 if raucher_status == "nein" else 0.25)
    alkohol_status_wkt = (1.0 if alkohol_status == "nein" else 0.16)
    # Alkohol- und Drogenkonsum führt zu einer stark verminderten Fruchtbarkeit
    beides = (1 if raucher_status_wkt == 1 and alkohol_status_wkt == 1 else 0.77)
    eisprung_entfernung_wkt = {
        -7: 0.024, -6: 0.049, -5: 0.146, -4: 0.415,
        -3: 0.561, -2: 1.0, -1: 0.683, 0: 0.195,
         1: 0.024 }.get(eisprung_entfernung, 0.007)
   
    
    # Der Vektor enthält nun die entsrechenden Wahrscheinlichkeiten
    wkten = [alter_wkt,bmi_wkt,raucher_status_wkt,alkohol_status_wkt, beides,eisprung_entfernung_wkt]
    return wkten

def gewichtung_fwkt(wkten):
    basis_wkt = 0.25
    gewichtung = [0.3,0.1,0.1,0.1,0.1,0.3]
    # Hier werden die Wahrscheinlichkeiten, die anhand eingegebener Daten berechnet wurden, gewichtet.
    wkten_gewichtet = [w * g for w, g in zip(wkten, gewichtung)]
    # Zum Schluss wird die Basiswahrscheinlichkeit von 25% mit dem Ergebnis multipliziert.
    return sum(wkten_gewichtet) * basis_wkt
