# Erweiterung für Männer

import streamlit as st
st.set_page_config(page_title="Der weibliche Zyklus", page_icon="🌹", layout="wide")

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from berechne_fruchtbarkeitswkt import berechne_fruchtbarkeitswkt,gewichtung_fwkt
#streamlit run app.py

st.title("Der weibliche Zyklus 🌹")

### Start ########################################################################################

def set_page(page_name):
    """Funktion zum Setzen der aktuellen Seite"""
    st.session_state.current_page = page_name

start, nathi, chiara, lou = st.tabs(["🏠 Start", "💡 Hormonverlauf", "🌡️ Zyklus und Temperatur", "📊 Fruchtbarkeitsrechner"])


with start:
    # Text zentrieren mit HTML:
    willkommen = """
    <h2 style='text-align: center; color: steelblue;'>
        Willkommen bei unserer Streamlit App!
    </h2>


    """
  #  <p style='text-align: center; font-size:18px;'>
  #      Hier findest du alle möglichen Infos zum weiblichen Zyklus.
  #  </p>
    
    st.markdown(willkommen, unsafe_allow_html=True)
    st.write("")
    
    st.subheader("""Du interessierst dich für deinen Zyklus? - Dann bist du hier genau richtig!""")
    name = st.text_input("Verrate uns bitte deinen Namen:")
             
    st.write(f"Hallo {name}, schön dass du da bist!")
    st.write("Wir sind drei Studentinnen und haben im Rahmen einer Projektarbeit diese Website erstellt.")
    st.write("Hier findest du viele interessante Facts und Darstellungen rund um den weiblichen Zyklus im Allgemeinen sowie ganz individuell auf dich abgestimmt.")
    st.write("""Wir möchten betonen, dass wir **keine Experten** sind und unsere Website daher Fehler enthalten kann! """)
    st.write("")
   
    st.subheader(" ")
    
    ueberblick = """
    <h2 style='text-align: center; color: black;'>
        Überblick
    """
    st.markdown(ueberblick, unsafe_allow_html=True)
    st.write("")
    
    spalte1, spalte2, spalte3 = st.columns(3)
    
    with spalte1:
        st.write("Nathalie hat dir verschiedenste Informationen über die einzelnen Zyklusphasen, die weiblichen Hormone und ihre Rolle im Zyklus zusammengestellt.")
        st.info("Klicke dafür oben auf 'Hormonverlauf'!")
            
    
    with spalte2:
        st.write("Mit Hilfe von Chiaras Code kannst du deinen Zyklus tracken, dir veschieden Daten berechnen lassen und mithilfe einer Körpertemperaturkurve deinen Eisprung erkennen.")
        st.info("Klicke dafür oben auf 'Zyklus und Temperatur'!")
    
    with spalte3:
        st.write("Mit Hilfe von Lous Programmierung kannst du dir in Bezug auf verschiedene Faktoren deine Fruchtbarkeitswahrscheinlichkeit berechnen lassen.")
        st.info("Klicke dafür oben auf 'Fruchtbarkeitsrechner'!")

    st.write("")
    st.write("")
    gruesse = f"""
    <p style='text-align: center; font-size:17px;'>
        Wir wünschen dir viel Spaß, {name}!
    </p>
    <p style='text-align: center; font-size:17px;'>
        Liebe Grüße Lou, Chiara & Nathalie
    """
    st.markdown(gruesse, unsafe_allow_html=True)


    # Anzeigen der Quellen
    quellen_anzeigen = st.radio(
        "Möchtest du unsere Quellen sehen?",
        ("Ja, gerne!", "Nein, danke."),
        index=1  # ← Das sorgt dafür, dass "Nein, danke" vorausgewählt ist
    )
    if quellen_anzeigen == "Ja, gerne!":
        st.info("""Bereich 'Hormonverlauf':
        
                https://docs.streamlit.io/develop/tutorials (03.06.25)
                https://docs.github.com/de/get-started/start-your-journey (21.05.25)
                https://plotly.com/python/renderers/ (22.05.25)
                https://arxiv.org/pdf/1712.00117 (05.06.25)
                https://www.researchgate.net/publication/2282598_A_Model_For_The_Production_Of_Ovarian_Hormones_During_The_Menstrual_Cycle (05.06.25)
                https://proceedings.mlr.press/v106/urteaga19a/urteaga19a.pdf? (05.06.25)
                https://github.com/uja-works/Programmieren2 (20.05.25)
                https://www.ncbi.nlm.nih.gov/books/NBK500020/ (23.05.25)
                https://www.ncbi.nlm.nih.gov/books/NBK500020/ (23.05.25)
                https://de.wikipedia.org/wiki/Menstruationszyklus#Hormonzyklus (18.05.25)
                https://www.wikiwand.com/de/articles/Menstruation (18.05.25)
                https://de.wikipedia.org/wiki/Progesteron (15.06.25)
                https://www.wikiwand.com/de/search?q=%C3%B6strogen (16.06.25)
                https://de.wikipedia.org/wiki/Follikelstimulierendes_Hormon (16.06.25)
                https://de.wikipedia.org/wiki/Luteinisierendes_Hormon (15.05.25)
                https://www.news-medical.net/health/Estradiol-Measurement.aspx? (01.06.25)
                https://www.news-medical.net/health/Estradiol-Measurement.aspx? (01.06.25)
                https://shop.miracare.com/blogs/resources/fsh-levels?srsltid=AfmBOooOHKqp3qDe808khcB2uvJ8EHcYf8Sy9Lr0Y4Pbq-FsEn0XXMU9& (02.06.25)
                https://www.straighthealthcare.com/female-hormone-physiology.html (02.06.25)
                https://chatgpt.com (23.06.25)
                """)
        st.info("""Bereich 'Fruchtbarkeitswahrscheinlichkeit':
        
                https://www.msdmanuals.com/de/heim/gesundheitsprobleme-von-frauen/das-weibliche-fortpflanzungssystem/menstruationszyklus (25.05.2025) 
                file:///h:/win.v2/Downloads/978-3-031-58516-6.pdf (26.05.2025) 
                https://pubmed.ncbi.nlm.nih.gov/14967378/ (26.05.2025) 
                https://www.nature.com/articles/s41598-017-14261-8 (31.05.2025) 
                https://pubmed.ncbi.nlm.nih.gov/7477165/ (31.05.2025) 
                https://europepmc.org/article/PMC/4893975 (31.05.2025)
                https://www.academia.edu/27558043/Changes_with_age_in_the_level_and_duration_of_fertility_in_the_menstrual_cycle (31.05.2025)
                https://www.fertilityiq.com/fertilityiq/lifestyle/smoking-caffeine-alcohol-impacts-on-fertility (21.06.2025)
                https://www.sciencedirect.com/science/article/pii/S0022519307001166 (21.06.2025)
                https://www.kaggle.com/datasets/gabbygab/fertility-data-set (21.06.2025)
                https://www.swissmom.ch/de/kinderwunsch/vorbereitungen-auf-ein-baby/gewicht-und-fruchtbarkeit-20258 (23.06.2025)
                https://www.ukbonn.de/gynaekologische-endokrinologie-und-reproduktionsmedizin/behandlungsspektrum/kinderwunschbehandlung/lebensfuehrung/ (23.06.2025)
                """)
        
        st.info("""Bereich 'Zyklus und Temperatur':

                https://www.apotheken-umschau.de/familie/kinderwunsch/eisprungrechner/eisprungrechner-fruchtbare-tage-eisprung-berechnen-791975.html (03.06.2025)
                https://www.aok.de/pk/magazin/familie/verhuetung/basaltemperatur-messen-darauf-kommt-es-an/ (04.06.2025)
                https://www.dkv.com/gesundheit-themenwelt-familie-zyklus-so-erkennen-sie-die-fruchtbaren-tage.html (04.06.2025)
                https://www.frauenaerzte-im-netz.de/familienplanung-verhuetung/natuerliche-familienplanung/fruchtbare-tage-selbst-bestimmen-methoden/ (04.06.2025)
                https://www.frauenaerzte-im-netz.de/familienplanung-verhuetung/natuerliche-familienplanung/weiblicher-zyklus-wann-sind-die-fruchtbaren-tage/ (03.06.2025)
                https://docs.streamlit.io/develop/api-reference (10.06.2025)
                """)

### Nathi #####################################################################################

with nathi:
    
    
    st.header("💡 Dein Hormonverlauf")
    
    # Auswahl Zyklusart
    modus = st.selectbox("Zyklusart", ["Natürlich", "Pille (21+7)", "Pille (28 Tage)"])
    
    # Eingabe Zykluslänge (nur bei "Natürlich", da sonst die Pille die Zykluslänge entscheidet)
    if modus == "Natürlich":
        zykluslaenge = st.slider("Zykluslänge (in Tagen)", min_value=21, max_value=40, value=28)
        hinweis = "" 
    else:
        zykluslaenge = 28
        hinweis = "Bei Pilleneinnahme ist die Zykluslänge auf 28 Tage festgelegt."
    
    st.markdown(f"🛈 {hinweis}" if hinweis else "")
    
    # Zyklustag auswählen, Form: (label, min_value, max_value, value als Startwert)
    tag = st.slider("Zyklustag auswählen", 1, zykluslaenge, 1)
    
    # Phasenbestimmung
    def zyklus_phase(tag, modus, zykluslaenge):
        ovulation = zykluslaenge - 14
        if modus == "Natürlich":
            if tag <= 5:
                return "🩸 **Menstruation**"
            elif tag < ovulation:
                return "🌱 **Follikelphase**"
            elif tag == ovulation:
                return "🥚 **Ovulation**"
            else:
                return "🌙 **Lutealphase**"
        elif modus == "Pille (21+7)":
            return "💊 **Pille aktiv**" if tag <= 21 else "🩸 **Pillenpause**"
        elif modus == "Pille (28 Tage)":
            return "💊 **Stabile Hormongabe**"
    
    # Daten vorbereiten
    tage = np.arange(1, zykluslaenge + 1)
    ovulation = zykluslaenge - 14

    # modellhaft, mit Gaußschen Normalverteilung rekonstruiert 
    # f(x) = A * exp(-1/2*((x-q)/sigma)^2)), A: Höhe/Amplitude, q: Mittelpunkt der Kurve (Maximum), sigma: Standartabweichung
    
    real_oe = 50 + 250 * np.exp(-0.5 * ((tage - (ovulation - 1)) / 3)**2) + 70 * np.exp(-0.5 * ((tage - (zykluslaenge - 7)) / 2)**2)
    real_pr = 0.5 + 15 * np.exp(-0.5 * ((tage - (zykluslaenge - 7)) / 3)**2)
    real_lh = 5 + 75 * np.exp(-0.5 * ((tage - ovulation) / 1.5)**2)
    real_fsh = 4 + 25 * np.exp(-0.5 * ((tage - 3) / 2)**2) + 15 * np.exp(-0.5 * ((tage - ovulation) / 2)**2) # Addition -> 2 Peaks

    # In Relation mit Maximum gesetzt, Normierung
    oe = real_oe / np.max(real_oe)
    pr = real_pr / np.max(real_pr)
    lh = real_lh / np.max(real_lh)
    fsh = real_fsh / np.max(real_fsh)
    
    if modus == "Pille (21+7)":
        oe = np.concatenate([np.full(21, 10/10), np.full(zykluslaenge - 21, 30/100)])
        pr = np.concatenate([np.full(21, 1/10), np.full(zykluslaenge - 21, 1/100)])
        lh = fsh = np.full(zykluslaenge, 3/100)
        real_oe = np.concatenate([np.full(21, 100), np.full(zykluslaenge - 21, 30)])
        real_pr = np.concatenate([np.full(21, 10), np.full(zykluslaenge - 21, 1)])
        real_lh = real_fsh = np.full(zykluslaenge, 3)
    elif modus == "Pille (28 Tage)":
        oe = np.full(zykluslaenge, 100/100)
        pr = np.full(zykluslaenge, 10/100)
        lh = fsh = np.full(zykluslaenge, 3/100)
        real_oe = np.full(zykluslaenge, 100)
        real_pr = np.full(zykluslaenge, 10)
        real_lh = real_fsh = np.full(zykluslaenge, 3)
    
    # Plot erzeugen
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tage, y=oe, name="Östrogen", line=dict(color='purple', shape='spline')))
    fig.add_trace(go.Scatter(x=tage, y=pr, name="Progesteron", line=dict(color='orange', shape = 'spline')))
    fig.add_trace(go.Scatter(x=tage, y=lh, name="LH", line=dict(color='green', shape='spline')))
    fig.add_trace(go.Scatter(x=tage, y=fsh, name="FSH", line=dict(color='blue', shape = 'spline')))
    fig.add_shape(type="line", x0=tag, x1=tag, y0=0, y1=1, line=dict(color="red", width=2, dash="dash")) #hinzufügen einer vertikalen Linie (durch x0 = x1), dash -> gestrichelte Linie

    
    if modus == "Natürlich":
        yaxis_title = "relativer Hormonspiegel"
    else:
        yaxis_title = "absoluter Hormonspiegel * (1/100)"


    fig.update_layout(
        title=f"Hormonverlauf {modus}",
        xaxis_title="Zyklustag",
        yaxis_title=yaxis_title,
        yaxis=dict(range=[0, 1.2]),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True) #zur interaktiven Ausgabe von fig ,automatische Anpassung der Breite an Bildschirmgröße durch TRUE
    
    # Zyklusphase anzeigen
    st.markdown(f"### 📍 Tag {tag}: {zyklus_phase(tag, modus, zykluslaenge)}")
    
    # Hormonwerte-Tabelle
    df = pd.DataFrame({
        'Hormon': ['Östrogen', 'Progesteron', 'LH', 'FSH'],
        'Wert': [
            f"{round(real_oe[tag - 1], 1)} pg/mL",
            f"{round(real_pr[tag - 1], 2)} ng/mL",
            f"{round(real_lh[tag - 1], 1)} mIU/mL",
            f"{round(real_fsh[tag - 1], 1)} mIU/mL"
        ]  # tag -1, weil Python Index bei 0 beginnt
    })
    st.markdown("#### 📊 Hormonspiegel an diesem Tag")
    st.dataframe(df, use_container_width=True)
    
    # --- Zusätzliche Infos zu Phasen und Hormonen ---
    
    st.markdown("---") # erzeugt horizontale Trennlinie
    st.header("📚 Zusatzinfos zu Zyklusphasen & Hormonen")
    
    
    # Einstiegsfrage mit "Nein, danke" als Standard
    frage = st.radio(
        f"Möchtest du zusätzliche Informationen über deine Zyklusphasen und deine Hormone, {name}?",
        ("Ja, gerne!", "Nein, danke!"),
        index=1  # ← Das sorgt dafür, dass "Nein, danke" vorausgewählt ist
    )
    
    if frage == "Ja, gerne!":
        # Phaseninfo
        zyklusphasen = {
            "Menstruation": """🧠 Coole Facts über die Menstruation:
            
    1. Du blutest ca. 6–9 Jahre deines Lebens. 
    
       Eine Frau hat im Schnitt etwa 450 Menstruationen im Leben – das entspricht rund 6 bis 9 Jahren Menstruation in Summe. 
    
    2. Die Blutmenge ist gar nicht so viel.
    
       Auch wenn es oft nach „viel“ aussieht: Die durchschnittliche Menge Menstruationsblut liegt nur bei 30–70 ml pro Zyklus – 
       das sind gerade mal 2–5 Esslöffel.
    
    3. Tiere menstruieren auch – aber nur wenige.
    
       Die meisten Säugetiere bauen ihre Gebärmutterschleimhaut einfach wieder ab, ohne zu bluten. 
       Nur wenige Arten wie Primaten, Fledermäuse oder Elefantenrüssler haben echte Menstruationszyklen.
       Hunde bluten übrigens - im Gegensatz zu uns Menschen - wenn sich ihre Gebärmutterschleimhaut aufbaut, ausgelöst durch eine 
       verstärkte Durchblutung der Gefäße und hormonelle Einflüsse.
    
    4. Menstruation kann ein Vitalzeichen sein.
    
       In der Medizin wird der Zyklus manchmal als "fünftes Vitalzeichen" angesehen – ähnlich wichtig wie Puls, Blutdruck oder Atmung. 
       Zyklusveränderungen können Hinweise auf Stress, Essstörungen, Schilddrüsenerkrankungen oder hormonelle Dysbalancen geben.
    
    🚫 Und was ist mit Mythen?
    
    - „Man darf beim Schwimmen nicht ins Wasser“ – Quatsch! Mit Tampon, Cup oder Periodenunterwäsche geht das problemlos.
    
    - „Alle haben Schmerzen“ – Viele haben leichte Krämpfe, aber starke Schmerzen sind nicht normal und sollten ärztlich abgeklärt werden (z. B. Endometriose).
    
    - „Menstruation ist unrein“ – Dieser Mythos stammt aus alten patriarchalen Gesellschaften. Fakt: Menstruation ist ein gesunder Vorgang.
    
    💬 Fazit:
    Die Menstruation ist kein „Makel“, sondern ein ausgeklügeltes Zusammenspiel von Hormonen und Organen – ein Zeichen dafür, dass der Körper funktioniert!
    """,
            "Follikelphase": """Nach der Menstruation beginnt im weiblichen Körper eine neue Runde der Vorbereitung: 
            die Follikelphase, bei der sich alles darauf vorbereitet, ein neues Ei zur Reife zu bringen.
    
    🔬 Was passiert in der Follikelphase?
    Die Follikelphase startet am ersten Tag der Menstruation und endet mit dem Eisprung (Ovulation). 
    Ihr Name kommt vom Wort Follikel – das sind kleine Bläschen in den Eierstöcken, die jeweils ein Ei enthalten.
    
    Während dieser Phase:
    - reifen mehrere Follikel heran, wobei aber nur einer dominant wird und sich auf den Eisprung vorbereitet.
    - Gleichzeitig baut sich die Gebärmutterschleimhaut wieder auf – als Vorbereitung auf eine mögliche Einnistung.
    
    🧠 Fun Facts zur Follikelphase:
    1. Du wirst hormonell aufgedreht.
    
       Das Hormon Östrogen steigt in dieser Phase kräftig an. Es sorgt nicht nur für den Schleimhautaufbau, 
       sondern beeinflusst auch Haut, Stimmung, Energielevel und sogar dein Gedächtnis. Viele fühlen sich in dieser Zeit besonders motiviert und aktiv.
    
    2. Mehrere Eizellen starten – aber nur eine gewinnt.
    
       Anfangs beginnen 10–20 Follikel gleichzeitig zu reifen, aber am Ende wird nur ein "Leitfollikel" dominant und löst den Eisprung aus. 
       Die anderen bilden sich zurück.
    
    3. Die Phase kann unterschiedlich lang sein.
    
       Im Gegensatz zur Lutealphase (die fast immer ca. 14 Tage dauert), kann die Follikelphase zwischen 7 und 21 Tagen oder sogar noch länger dauern. 
       Sie ist der Hauptgrund dafür, warum sich Zyklen in der Länge unterscheiden.
    
    4. Dein Körper wird "empfängnisbereit".
    
       Östrogen sorgt auch dafür, dass der Zervixschleim dünn und durchlässig wird – optimal für Spermien. 
       Außerdem wird die Haut oft klarer, die Libido kann steigen und manche spüren sogar mehr Kreativität oder Fokus.
    """,
            "Ovulation": """Die Ovulation ist das zentrale Ereignis im weiblichen Zyklus: 
            Ein reifes Ei verlässt den Eierstock und macht sich auf den Weg – bereit für eine mögliche Befruchtung. 
            Klingt simpel, ist aber ein präzise getimter, hormonell gesteuerter Vorgang.
    
    🔬 Was passiert bei der Ovulation?
    
    Rund um die Zyklusmitte – also etwa am 14. Tag eines 28-Tage-Zyklus – passiert Folgendes:
    - Der dominierende Follikel „platzt“ auf,
    - das Ei wird freigesetzt und wandert in den Eileiter,
    - dort bleibt es für ca. 12–24 Stunden befruchtungsfähig.
    
    Der Startschuss dafür ist der sogenannte LH-Peak – ein starker Anstieg des luteinisierenden Hormons (LH), der wie ein interner Countdown funktioniert.
    
    🧠 Coole Facts zur Ovulation:
    
    1. Du merkst (vielleicht), dass es passiert
    
       Einige Frauen spüren den Eisprung als leichtes Ziehen im Unterleib – den sogenannten Mittelschmerz. 
       Andere bemerken veränderten Zervixschleim (spinnbar, durchsichtig – wie rohes Eiweiß).
    
    2. Die fruchtbare Phase ist kurz – aber nicht zu kurz
    
       Das Ei selbst lebt nur ca. 1 Tag. Spermien hingegen bis zu 5 Tage. Deshalb gilt: Die „fruchtbare Phase“ umfasst etwa 5–6 Tage vor und am Tag des Eisprungs.
    
    3. Die Körpertemperatur verrät den Eisprung – aber erst danach
    
       Nach der Ovulation steigt das Hormon Progesteron – das erhöht die Basaltemperatur leicht (ca. 0,3–0,5 °C). 
       Das wird in der natürlichen Familienplanung (NFP) genutzt, um den Eisprung rückwirkend zu erkennen.
    
    4. Du bist vielleicht sozialer, flirtfreudiger, kreativer
    
       Studien zeigen: Um den Eisprung herum steigt oft die Lust, das Selbstbewusstsein – und sogar die Wahrscheinlichkeit, 
       dass jemand "mehr riskiert" oder extrovertierter auftritt.
    """,
            "Lutealphase": """Nach dem Eisprung beginnt die Lutealphase – eine Zeit, in der sich der Körper darauf vorbereitet, 
            ein eventuell befruchtetes Ei „einzunisten“. Diese Phase ist hormonell ruhiger, aber keineswegs unwichtig.
    
    🔬 Was passiert in der Lutealphase?
    
    Nachdem das Ei den Eierstock verlassen hat, wandelt sich der leere Follikel in den sogenannten Gelbkörper (lateinisch: corpus luteum). 
    Dieser produziert das Hormon Progesteron – und das hat es in sich:
    - Es sorgt dafür, dass die Gebärmutterschleimhaut dick und nährstoffreich bleibt,
    - es erhöht die Körpertemperatur leicht (um ca. 0,3–0,5 °C),
    - und es stabilisiert den Zyklus für ca. 14 Tage.
    
    Wenn keine Befruchtung stattfindet, schrumpft der Gelbkörper, Progesteron fällt ab – und die Menstruation beginnt.
    
    🧠 Coole Facts zur Lutealphase:
    
    1. Sie ist fast immer gleich lang
    
       Im Gegensatz zur Follikelphase ist die Lutealphase bei den meisten Menschen ziemlich konstant: ca. 12–14 Tage. Das macht sie wichtig für 
       die Zyklusberechnung.
    
    2. Progesteron beruhigt – aber auch nicht immer nur positiv
    
       Progesteron wirkt beruhigend und entspannend, kann aber auch Stimmungsschwankungen, Heißhunger oder Müdigkeit auslösen. 
       Deshalb erleben manche in dieser Phase PMS (prämenstruelles Syndrom).
    
    3. Temperatur steigt – ein NFP-Indikator
    
       Die Temperaturerhöhung nach dem Eisprung bleibt über die Lutealphase bestehen – bis zur nächsten Menstruation. 
       Das nutzen viele zur natürlichen Zyklusbeobachtung oder zur Unterstützung bei Kinderwunsch.
    
    4. Ein kleiner Energieshift
    
       Manche fühlen sich in der Lutealphase introvertierter, reflektierter oder emotionaler – was übrigens gar nicht schlecht sein muss! 
       Es ist eine Phase, in der der Körper bewusst langsamer fährt.
    """
        }
    
        phase = st.selectbox("ℹ️ Zyklusphase wählen", list(zyklusphasen.keys()))
        st.subheader(f"📅 {phase}")
        st.write(zyklusphasen[phase])
    
        # Hormoninfo
        hormon_infos = {
            "Östrogen": """Östrogen ist eines der wichtigsten Hormone im weiblichen Körper – und wirkt weit über den Zyklus hinaus. 
            Es ist so etwas wie der Dirigent im hormonellen Orchester und beeinflusst Fruchtbarkeit, Haut, Stimmung, Knochen und sogar das Gehirn.
    
    🔬 Was genau macht Östrogen?
    
    Östrogen wird vor allem in den Eierstöcken produziert – vor allem in der ersten Zyklushälfte (Follikelphase). Es:
    - regt das Wachstum der Gebärmutterschleimhaut an,
    
    - sorgt dafür, dass sich Follikel (Eibläschen) im Eierstock entwickeln,
    
    - beeinflusst den Zervixschleim (macht ihn durchlässiger für Spermien),
    
    - wirkt auf Haut, Haare, Knochen, Gehirn, Herz und mehr.
    
    🧠 Coole Fakten über Östrogen:
    
    - Stimmungsbooster & Energiegeber
    
    Östrogen hat direkten Einfluss auf das Gehirn: Es steigert das Serotonin-Level, wirkt stimmungsaufhellend, motivierend – und kann sogar das Gedächtnis stärken.
    
    - Beauty-Hormon? Nicht ganz falsch.
    
    In der Hochphase von Östrogen (vor dem Eisprung) berichten viele von strahlender Haut, glänzendem Haar und mehr Ausstrahlung. 
    Das ist evolutionär sogar sinnvoll – der Körper zeigt sich „von seiner besten Seite“.
    
    
    - Es schützt deine Knochen
    
    Östrogen sorgt dafür, dass der Knochenstoffwechsel im Gleichgewicht bleibt. Nach den Wechseljahren – wenn der Östrogenspiegel sinkt – steigt das Risiko für Osteoporose.
    
    
    - Mehr als nur „weiblich“
    
    Auch Männer haben Östrogen – nur in viel geringerer Menge. Es spielt auch dort eine Rolle für Libido, Knochen und Gehirn. 
    Umgekehrt ist Östrogen auch bei Frauen kein „alleiniges Hormon der Weiblichkeit“ – es wirkt systemweit.
    
    
    Sowohl ein Östrogenmangel (z. B. bei Essstörungen oder in den Wechseljahren) als auch ein Überschuss (z. B. durch Hormonstörungen) können Beschwerden verursachen: 
    von Stimmungsschwankungen bis Zyklusunregelmäßigkeiten oder Hautproblemen.""",
    
            
            "Progesteron": """Progesteron ist das dominante Hormon der zweiten Zyklushälfte (Lutealphase) – und spielt eine 
            Schlüsselrolle, wenn es um Vorbereitung auf eine Schwangerschaft, innere Balance und körperliche Stabilität geht.
    
    🔬 Was macht Progesteron im Körper?
    
    
    Progesteron wird nach dem Eisprung vom sogenannten Gelbkörper produziert – das ist der Rest des Follikels, aus dem die Eizelle gesprungen ist. Es:
    
    - erhält und stabilisiert die Gebärmutterschleimhaut,
    
    - erhöht leicht die Körpertemperatur (ca. 0,3–0,5 °C),
    
    - bereitet den Körper auf eine mögliche Schwangerschaft vor,
    
    - wirkt beruhigend auf das Nervensystem.
    
    
    🧠 Spannende Fakten über Progesteron:
    
    - Das „Kuschelhormon“ unter den Zyklushormonen
    
    Progesteron wirkt dämpfend und entspannend auf das zentrale Nervensystem. Viele Frauen fühlen sich in dieser Phase ruhiger, 
    reflektierter – manche aber auch sensibler oder müder.
    
    - Temperatur-Anstieg als natürlicher Zyklustracker
    
    Der Temperaturanstieg nach dem Eisprung ist messbar – und ein zentrales Werkzeug in der natürlichen Familienplanung (NFP). 
    Bleibt die Temperatur erhöht, ist das oft ein erstes Anzeichen für eine Schwangerschaft.
    
    - Schutz für Schwangerschaft – oder Startsignal für die Menstruation
    
    Wird eine Eizelle befruchtet, sorgt Progesteron dafür, dass die Schleimhaut erhalten bleibt. Wird keine befruchtete Eizelle 
    eingenistet, fällt der Progesteronspiegel wieder ab – und die Menstruation beginnt.
    
    - Es hat Einfluss auf deine Haut – und dein Hungergefühl
    
    Progesteron kann Wassereinlagerungen und Heißhunger (besonders auf Süßes) fördern. Manche bekommen in dieser Phase auch eher 
    Unreinheiten – der Hormonshift macht sich spürbar.
    
    - Ein Ungleichgewicht kann PMS begünstigen
    
    Wenn zu wenig Progesteron da ist (z. B. durch Stress, Schilddrüsenprobleme oder nach Absetzen der Pille), kann das PMS-Symptome wie 
    Reizbarkeit, Brustspannen oder Schlafstörungen verstärken.""",
    
            
            "LH": """Das luteinisierende Hormon – kurz LH – ist so etwas wie der „Zünder“ im Zyklusgeschehen. 
            Es sorgt dafür, dass ein reifes Ei den Follikel verlässt und der Eisprung stattfindet. Ohne LH gäbe es keinen Eisprung – und damit auch keine Fruchtbarkeit.
    
    
    🔬 Was genau macht LH im Zyklus?
    
    
    LH wird in der Hirnanhangdrüse (Hypophyse) gebildet und ist zusammen mit FSH (follikelstimulierendes Hormon) an der Steuerung des Zyklus beteiligt.
    
    Seine Hauptaufgabe:
    
    🧨 Der sogenannte LH-Peak – ein sprunghafter Anstieg – löst den Eisprung aus!
    
    
    Etwa zur Zyklusmitte steigt die LH-Konzentration im Blut plötzlich stark an.
    Das bewirkt, dass der dominante Follikel „aufplatzt“ und das Ei freigibt.
    Danach hilft LH, dass sich der Follikel in den Gelbkörper umwandelt (→ der produziert Progesteron).
    
    
    🧠 Spannende Fakten zu LH:
    
    - Der LH-Peak ist wie ein Countdown
    Sobald LH stark ansteigt, ist der Eisprung in den nächsten 24–36 Stunden zu erwarten. Darauf basieren viele Ovulationstests – sie messen den LH-Wert im Urin.
    
    - Es ist der Eisprung-Anzeiger Nr. 1
    Wer seinen Kinderwunsch natürlich unterstützen will, beobachtet oft den LH-Peak – er markiert die fruchtbarste Zeit im Zyklus.
    
    - LH wirkt nicht nur im Eierstock
    Bei Männern stimuliert LH übrigens die Hoden, Testosteron zu produzieren – ein gutes Beispiel dafür, wie „weibliche“ und „männliche“ Hormone in 
    beiden Geschlechtern eine Rolle spielen.
    
    - Zu viel oder zu wenig LH kann stören
    Bei hormonellen Störungen wie dem PCOS (Polyzystisches Ovarialsyndrom) ist der LH-Spiegel häufig dauerhaft erhöht – was den Eisprung behindern kann. 
    Auch Stress, Untergewicht oder Schilddrüsenprobleme können LH beeinflussen.""",
            
            "FSH": """FSH steht für Follikelstimulierendes Hormon – und ist sozusagen der „Anschubser“ des weiblichen Zyklus. 
            Es bringt den ganzen Prozess in Bewegung, indem es die Reifung der Eibläschen (Follikel) im Eierstock anstößt.
    
    
    🔬 Was genau macht FSH?
    
    
    FSH wird – wie LH – in der Hypophyse (Hirnanhangdrüse) gebildet. Es ist vor allem in der ersten Zyklushälfte aktiv (Follikelphase) und:
    
    - stimuliert die Reifung mehrerer Follikel im Eierstock,
    
    - regt die Östrogenproduktion in diesen Follikeln an,
    
    - bereitet so den Körper auf den Eisprung vor.
    
    
    🧠 Wissenswerte Facts über FSH:
    
    - FSH startet die „Auswahlrunde“ der Eizellen
    Jeden Zyklus beginnen ca. 10–20 Follikel zu wachsen – aber nur einer wird der sogenannte „Leitfollikel“. 
    Dieser reift vollständig heran und ist der Kandidat für den Eisprung.
    
    
    - FSH und Östrogen arbeiten als Team
    Je mehr die Follikel wachsen, desto mehr Östrogen produzieren sie. Und dieses steigende Östrogen signalisiert 
    dem Gehirn irgendwann: „Danke, reicht!“, woraufhin FSH wieder absinkt.
    
    - Zu hohe FSH-Werte können ein Warnsignal sein
    Wenn die Eierstöcke nicht mehr gut auf FSH reagieren (z. B. bei beginnender Wechseljahre oder bei verminderter Fruchtbarkeit), 
    steigt der FSH-Wert stark an – weil der Körper „mehr schreien muss“, um eine Reaktion zu bekommen.
    
    - auch Männer brauchen FSH
    Bei Männern fördert FSH die Reifung der Samenzellen – auch hier ist es also für Fruchtbarkeit unerlässlich."""
        }
        hormon = st.selectbox("ℹ️ Hormon wählen", list(hormon_infos.keys()))
        st.subheader(f"🧪 {hormon}")
        st.write(hormon_infos[hormon])
    
    else:
        st.info("Kein Problem! Du kannst jederzeit später auf diese Infos zurückkommen. 🌸")


### Chiara ####################################################################################

with chiara:  
    
### Allgemeines berechnen ###
    
    import csv
    import os
    from datetime import datetime, timedelta
    import streamlit as st

# === Konstanten ===
    DATEINAME = "zyklen.csv"
    STANDARD_ZYKLUSLAENGE = 28

# === Alte Daten laden ===
    def lade_zyklen():
        zyklen = []
        if os.path.exists(DATEINAME):
            with open(DATEINAME, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        datum = datetime.strptime(row[0], "%d.%m.%Y")
                        dauer = int(row[1])
                        zyklen.append((datum, dauer))
                    except:
                        continue
        return zyklen

# === Zyklusanalyse ===
    def analyse(zyklen):
        if not zyklen:
            st.info("Keine Daten vorhanden zur Analyse.")
            return

        zyklen.sort(key=lambda x: x[0])
        zykluslaengen = [(zyklen[i][0] - zyklen[i - 1][0]).days for i in range(1, len(zyklen))]
        durchschnitt = round(sum(zykluslaengen) / len(zykluslaengen)) if zykluslaengen else STANDARD_ZYKLUSLAENGE
        letzter_start, letzte_dauer = zyklen[-1]
        naechste_periode = letzter_start + timedelta(days=durchschnitt)
        eisprung = naechste_periode - timedelta(days=14)
        fruchtbar_von = eisprung - timedelta(days=5)

        st.subheader("📊 Analyse")
        st.write(f"**Zykluslängen:** {zykluslaengen}")
        st.write(f"**Durchschnittliche Zykluslänge:** {durchschnitt} Tage")
        st.write(f"**Letzte Periode:** {letzter_start.strftime('%d.%m.%Y')} ({letzte_dauer} Tage)")
        st.write(f"**Nächste Periode voraussichtlich am:** {naechste_periode.strftime('%d.%m.%Y')}")
        st.write(f"**Eisprung voraussichtlich am:** {eisprung.strftime('%d.%m.%Y')}")
        st.write(f"**Fruchtbare Phase:** {fruchtbar_von.strftime('%d.%m.%Y')} bis {eisprung.strftime('%d.%m.%Y')}")

# === Speichern ===
    def speichere_zyklen(zyklen):
        zyklen.sort(key=lambda x: x[0])
        with open(DATEINAME, "w", newline="") as f:
            writer = csv.writer(f)
            for eintrag in zyklen:
                writer.writerow([eintrag[0].strftime("%d.%m.%Y"), eintrag[1]])
    
# === Streamlit App ===
    st.header("🩸 Zyklus-Tracker")
    zyklen = lade_zyklen()

# === Neue Einträge ===
    with st.form("neuer_eintrag"):
        datum_str = st.text_input("Datum der Periode (TT.MM.JJJJ):")
        dauer = st.number_input("Dauer (Tage):", min_value=1, max_value=14, value=5)
        submitted = st.form_submit_button("➕ Eintrag hinzufügen")

        if submitted:
            try:
                datum = datetime.strptime(datum_str.strip(), "%d.%m.%Y")
                zyklen.append((datum, dauer))
                speichere_zyklen(zyklen)
                st.success(f"Eintrag hinzugefügt: {datum.strftime('%d.%m.%Y')} ({dauer} Tage)")
            except ValueError:
                st.error("❌ Bitte ein gültiges Datum eingeben (TT.MM.JJJJ)")

# === Einträge anzeigen und löschen ===
    st.subheader("📝 Aktuelle Einträge")
    if zyklen:
        for idx, (datum, dauer) in enumerate(zyklen):
            col1, col2 = st.columns([4, 1])
            col1.write(f"{idx+1}. {datum.strftime('%d.%m.%Y')} ({dauer} Tage)")
            if col2.button("🗑️ Löschen", key=f"del_{idx}"):
                del zyklen[idx]
                speichere_zyklen(zyklen)
                st.experimental_rerun()
    else:
        st.write("Noch keine Einträge vorhanden.")

# === Analysebereich ===
    if st.button("💾 Berechnung ausführen"):
        analyse(zyklen)

### Tempratur berechnen #######
    import streamlit as st
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta

# === Standardzyklusdaten ===
    def beispiel_daten():
        start = datetime(2025, 6, 1)
        werte = [
        # Follikelphase – niedrige Temperaturen
            36.4, 36.3, 36.4, 36.5, 36.4, 36.3, 36.5,
            36.4, 36.4, 36.3, 36.5, 36.4, 36.3,
        
        # Eisprung – Temperaturanstieg
            36.6, 36.8, 36.9,

        # Lutealphase – höhere Temperaturen
            37.0, 36.9, 36.8, 36.9, 37.0, 36.8, 36.9, 36.7,

        # Prämenstruell – leichte Absenkung
            36.6, 36.5, 36.4
        ]
        return [(start + timedelta(days=i), t) for i, t in enumerate(werte)]


# === Session State Initialisieren ===
    if "temperaturdaten" not in st.session_state:
        st.session_state.temperaturdaten = beispiel_daten()
    if "beispiel_aktiv" not in st.session_state:
        st.session_state.beispiel_aktiv = True

    temperaturdaten = st.session_state.temperaturdaten

    st.header("🌡️ Basaltemperatur-Tracker & Eisprung-Analyse")

# === Neueingabe ===
    st.subheader("➕ Eintrag hinzufügen")
    eingabe = st.text_input("Format: TT.MM.JJJJ 36.5", key="eingabe_text")
   
    if st.button("Hinzufügen"):
        try:
            datum_str, temp_str = eingabe.strip().split()
            datum = datetime.strptime(datum_str, "%d.%m.%Y")
            temperatur = float(temp_str.replace(",", "."))

            # Entferne Beispiel beim ersten Eintrag
            if st.session_state.beispiel_aktiv:
                st.session_state.temperaturdaten = []
                st.session_state.beispiel_aktiv = False

            # Prüfe auf Duplikat (Datum bereits vorhanden)
            vorhandene_daten = [d.date() for d, _ in st.session_state.temperaturdaten]
            if datum.date() in vorhandene_daten:
                st.error(f"❌ Für den {datum.strftime('%d.%m.%Y')} existiert bereits ein Eintrag.")
            else:
                st.session_state.temperaturdaten.append((datum, temperatur))
                st.session_state.temperaturdaten.sort()
                st.success(f"Hinzugefügt: {datum.strftime('%d.%m.%Y')} – {temperatur:.2f} °C")

        except Exception:
            st.error("❌ Ungültiges Format! Beispiel: 01.06.2025 36.5")    

    temperaturdaten = st.session_state.temperaturdaten

# === Anzeige der Daten ===
    st.subheader("📅 Temperaturdaten")
    if temperaturdaten and not st.session_state.beispiel_aktiv:
        for i, (d, t) in enumerate(temperaturdaten, 1):
            st.markdown(f"{i}. **{d.strftime('%d.%m.%Y')}** – {t:.2f} °C")
    elif st.session_state.beispiel_aktiv:
        st.info("⚠️ Es werden Beispielwerte angezeigt. Füge eigene Daten ein, um loszulegen.")
    else:
        st.info("Noch keine Daten vorhanden.")

# === Bearbeiten / Löschen (nur wenn keine Beispieldaten) ===
    if temperaturdaten and not st.session_state.beispiel_aktiv:
        st.subheader("✏️ Bearbeiten oder löschen")
        eintraege = [f"{i+1}. {d.strftime('%d.%m.%Y')} – {t:.2f}°C" for i, (d, t) in enumerate(temperaturdaten)]
        auswahl = st.selectbox("Eintrag auswählen", eintraege)
        index = eintraege.index(auswahl)

        cols = st.columns([2, 1])
        neuer_wert = cols[0].text_input("Neuer Wert (TT.MM.JJJJ 36.5):", key="bearbeiten_text")
        if cols[1].button("🔁 Aktualisieren"):
            try:
                datum_str, temp_str = neuer_wert.strip().split()
                datum = datetime.strptime(datum_str, "%d.%m.%Y")
                temperatur = float(temp_str.replace(",", "."))
                temperaturdaten[index] = (datum, temperatur)
                temperaturdaten.sort()
                st.success("✅ Eintrag aktualisiert.")
            except:
                st.error("❌ Fehler beim Aktualisieren.")

        if st.button("❌ Eintrag löschen"):
            temperaturdaten.pop(index)
            st.success("🗑️ Eintrag gelöscht.")

# === Analysefunktion ===
    def analysieren_daten(daten):
        daten.sort()
        tage = [d for d, _ in daten]
        temps = [t for _, t in daten]

        def mittel(werte):
            return [(werte[i-1] + werte[i] + werte[i+1]) / 3 for i in range(1, len(werte)-1)]

        gleit = mittel(temps)
        mittel_tage = tage[1:-1]

        eisprung = None
        for i in range(1, len(gleit)):
            if gleit[i] - gleit[i-1] >= 0.2:
                eisprung = mittel_tage[i]
                break

        fig, ax = plt.subplots(figsize=(4, 2))
        ax.plot(tage, temps, marker='.', label="Temperatur", color='blue')
        ax.plot(mittel_tage, gleit, linestyle='--', label="3-Tage-Mittel", color='orange')
        if eisprung:
            ax.axvline(eisprung, color='red', linestyle=':', label=f"Eisprung: {eisprung.strftime('%d.%m.%Y')}")

        ax.set_title("Basaltemperaturkurve", fontsize=8)
        ax.set_xlabel("Datum", fontsize=6)
        ax.set_ylabel("Temperatur (°C)", fontsize=6)
        ax.grid(True)
        ax.legend(loc="upper left", fontsize=4)

        ax.set_ylim(36.2, 37.2)  # feste Achsenskalierung
        ax.tick_params(axis='x', labelsize=4)
        ax.tick_params(axis='y', labelsize=4)
        plt.xticks(rotation=45)
        st.pyplot(fig)


        if eisprung:
            st.success(f"✅ Eisprung wurde am **{eisprung.strftime('%d.%m.%Y')}** erkannt.")
        else:
            st.info("❌ Kein Eisprung erkannt – Temperaturanstieg zu gering.")

# === Automatische Analyse ===
    if len(temperaturdaten) >= 5:
        st.subheader("📊 Analyse")
        analysieren_daten(temperaturdaten)
    else:
        st.write("Zu wenige Temperaturdaten vorhanden")




### Lou #################################################################################

with lou:
    
    st.header("📊 Fruchtbarkeitsrechner")

    st.subheader("Datenabfrage")
    # Hier werden die Daten abgefragt, die gleich in der Formel verwendet werden, um die Wahrscheinlichkeit zu berechnen.
    
    # Alter
    alter = st.slider("Alter",min_value = 16, max_value = 45, value = 30)
    
    # Zykluslänge
    zykluslaenge = st.slider("Durchschnittliche Zykluslänge in Tagen",min_value = 15, max_value = 45, value = 28)
    
    # Tag des Eisprungs (wird benötigt, um den Abstand zum Eisprung zu berechnen, was die Wahrscheinlichkeit mit am meisten beeinflusst)
    tag_eisprung = zykluslaenge - 14
    st.info(f"Dein Eisprung findet durchschnittlich an Zyklustag {tag_eisprung} statt.")
    
    # Aktueller Zyklustag
    zyklustag = st.slider("Aktueller Zyklustag",min_value = 1, max_value = zykluslaenge, value = 15)
    
    # Abstand zum Eisprung
    eisprung_entfernung = zyklustag - tag_eisprung
    
    # BMI berechnen
    gewicht = st.number_input("Gewicht (in kg)", min_value=30.0, max_value=200.0, value=70.0)
    groesse = st.number_input("Größe (in m)", min_value=1.0, max_value=2.5, value=1.70)
    if groesse > 0:
        bmi = gewicht / (groesse ** 2)
        st.info(f"Dein BMI beträgt: {bmi:.2f}")
    else:
        bmi = None
        st.error("Größe muss größer als 0 sein.")
    
    # Raucherstatus
    antwort_r = st.radio("Rauchst du?", ["Ja, täglich mindestens eine Zigarette", "Seltener oder nie"])
    raucher_status = "ja" if "täglich" in antwort_r else "nein"
    
    # Alkoholkonsum
    antwort_a = st.radio("Trinkst du Alkohol?", ["Ja, mindestens 7 Getränke pro Woche", "Seltener oder nie"])
    alkohol_status = "ja" if "mindestens" in antwort_a else "nein"
    
    def bmi_wkt(bmi):
        if bmi < 17:
            return 0.33
        elif 17 < bmi < 20:
            return 0.89
        elif 20 < bmi< 25:
            return 1
        
    
    
    st.subheader("Fruchtbarkeitswahrscheinlichkeit: pro Zyklus")
    if "p_fruchtbarkeit" not in st.session_state:
        st.session_state.p_fruchtbarkeit = None # So wird p_fruchtbarkeit definiert und es wird kein Fehler ausgegeben, weil die Variable unbekannt ist. 
    if st.button("Berechne meine Fruchtbarkeitswahrscheinlichkeit"):
        werte = berechne_fruchtbarkeitswkt(alter,bmi,raucher_status,alkohol_status,eisprung_entfernung)
        # Wir speichern die Fruchbarkeitswahrscheinlichkeit in st.session_state als Speicher, der über mehrere Aktion erhalten bleibt (für die nächste if-Schleife)
        st.session_state.p_fruchtbarkeit = gewichtung_fwkt(werte)
        st.success(f"Geschätzte Fruchtbarkeitswahrscheinlichkeit: {100 * st.session_state.p_fruchtbarkeit:.2f}%")
        st.write("""Die Fruchtbarkeitswahrscheinlichkeit ist anhand von Daten geschätzt und kann stark variieren. 
        Sie bezieht sich auf einmaligen Geschlechtsverkehr am angegebenen Zyklustag.""")

    # Fruchtbarkeitswahrscheinlichkeit über mehrere Zyklen
    if st.session_state.p_fruchtbarkeit is not None:
        st.subheader("Fruchbarkeitswahrscheinlichkeit: über mehrere Zyklen")
        st.info("Wenn du die Daten oben veränderst, muss du zuerst nochmal die Wahrscheinlichkeit pro Zyklus berechnen, um die Wahrscheinlichkeit über mehrere Zyklen hinweg ändern zu können.")
        X = st.number_input("Gib X als Zyklenanzahl ein: ", min_value= 1, value = 3)
        if st.button(f"Berechne meine Fruchtbarkeitswahrscheinlichkeit über {X} Zyklen:"):
            z = st.session_state.p_fruchtbarkeit
            p = 1-(1-z)**X
            st.success(f"Die Wahrscheinlichkeit beträgt ungefähr {round(p*100,2)}%.")
    else: 
        st.write("Bitte zuerst die Fruchtbarkeitswahrscheinlichkeit pro Zyklus berechnen.")

    st.subheader("Fruchbarkeitswahrscheinlichkeit erhöhen")
    # Anzeigen von mehr Informationen, wie die Wahrscheinlichkeit erhöht werden kann.
    infos_anzeigen = st.radio(
        "Möchtest du mehr Infos darüber, wie man die Fruchtbarkeitswahrscheinlichkeit erhöhen kann?",
        ("Ja, gerne!", "Nein, danke!"),
        index=1)
    if infos_anzeigen == "Ja, gerne!":
        st.write("""Die Fruchtbarkeitswahrscheinlichkeit kann durch bestimmte Methoden beeinflusst werden. Dazu zählen:
        
        - gesunde Ernährung, ausreichende Nährstoffaufnahme und zugleich Meiden von verarbeiteten Lebensmitteln und zugesetzten Zuckern
        
        - gesundes Körpergewicht und Maß an Bewegung
        
        - Einnahme von Ergänzungsmitteln, wie Folsäure, Vitamin D, Jod (!! unbedingt vorher mit dem Hausarzt oder Frauenarzt besprechen!!)
        
        - Alkohol und Zigaretten meiden """)

    else: 
        st.info("""Okay! Du kannst gerne später darauf zurückkommen.""")
        
        
    
    
