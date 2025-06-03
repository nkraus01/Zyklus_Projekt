import streamlit as st
st.set_page_config(page_title="Der weibliche Zyklus", page_icon="👸", layout="wide")

import numpy as np
import pandas as pd
import plotly.graph_objects as go


# Seiteneinstellungen

st.title("💡 Dein Hormonverlauf")

# Auswahl Zyklusart
modus = st.selectbox("Zyklusart", ["Natürlich", "Pille (21+7)", "Pille (28 Tage)"])

# Eingabe Zykluslänge
if modus == "Natürlich":
    zykluslaenge = st.slider("Zykluslänge (in Tagen)", min_value=21, max_value=40, value=28)
    hinweis = ""
else:
    zykluslaenge = 28
    hinweis = "Bei Pilleneinnahme ist die Zykluslänge auf 28 Tage festgelegt."

st.markdown(f"🛈 {hinweis}" if hinweis else "")

# Zyklustag auswählen
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

real_oe = 50 + 250 * np.exp(-0.5 * ((tage - (ovulation - 1)) / 3)**2) + 70 * np.exp(-0.5 * ((tage - (zykluslaenge - 7)) / 2)**2)
real_pr = 0.5 + 15 * np.exp(-0.5 * ((tage - (zykluslaenge - 7)) / 3)**2)
real_lh = 5 + 75 * np.exp(-0.5 * ((tage - ovulation) / 1.5)**2)
real_fsh = 4 + 25 * np.exp(-0.5 * ((tage - 3) / 2)**2) + 15 * np.exp(-0.5 * ((tage - ovulation) / 2)**2)

oe = real_oe / np.max(real_oe)
pr = real_pr / np.max(real_pr)
lh = real_lh / np.max(real_lh)
fsh = real_fsh / np.max(real_fsh)

if modus == "Pille (21+7)":
    oe = np.concatenate([np.full(21, 0.5), np.full(zykluslaenge - 21, 0.1)])
    pr = np.concatenate([np.full(21, 0.7), np.full(zykluslaenge - 21, 0.1)])
    lh = fsh = np.full(zykluslaenge, 0.1)
    real_oe = np.concatenate([np.full(21, 100), np.full(zykluslaenge - 21, 30)])
    real_pr = np.concatenate([np.full(21, 10), np.full(zykluslaenge - 21, 1)])
    real_lh = real_fsh = np.full(zykluslaenge, 3)
elif modus == "Pille (28 Tage)":
    oe = np.full(zykluslaenge, 0.5)
    pr = np.full(zykluslaenge, 0.7)
    lh = fsh = np.full(zykluslaenge, 0.1)
    real_oe = np.full(zykluslaenge, 100)
    real_pr = np.full(zykluslaenge, 10)
    real_lh = real_fsh = np.full(zykluslaenge, 3)

# Plot erzeugen
fig = go.Figure()
fig.add_trace(go.Scatter(x=tage, y=oe, name="Östrogen", line=dict(color='purple')))
fig.add_trace(go.Scatter(x=tage, y=pr, name="Progesteron", line=dict(color='orange')))
fig.add_trace(go.Scatter(x=tage, y=lh, name="LH", line=dict(color='green')))
fig.add_trace(go.Scatter(x=tage, y=fsh, name="FSH", line=dict(color='blue')))
fig.add_shape(type="line", x0=tag, x1=tag, y0=0, y1=1.05, line=dict(color="red", width=2, dash="dash"))

fig.update_layout(
    title=f"Hormonverlauf ({modus}, {zykluslaenge} Tage)",
    xaxis_title="Zyklustag",
    yaxis_title="relativer Hormonspiegel",
    yaxis=dict(range=[0, 1.05]),
    width=950,
    height=500
)
st.plotly_chart(fig, use_container_width=True)

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
    ]
})
st.markdown("#### 📊 Hormonspiegel an diesem Tag")
st.dataframe(df, use_container_width=True)

# --- Zusätzliche Infos zu Phasen und Hormonen ---
st.markdown("---")
st.header("📚 Zusatzinfos zu Zyklusphasen & Hormonen")

# Phaseninfo
zyklusphasen = {
    "Menstruation": """🧠 Coole Facts über die Menstruation:
1. Du blutest ca. 6–9 Jahre deines Lebens. 

   Eine Frau hat im Schnitt etwa 450 Menstruationen im Leben – das entspricht rund 6 bis 9 Jahren Menstruation in Summe. 

2. Die Blutmenge ist gar nicht so viel.

   Auch wenn es oft nach „viel“ aussieht: Die durchschnittliche Menge Menstruationsblut liegt nur bei 30–70 ml pro Zyklus – das sind gerade mal 2–5 Esslöffel.

3. Tiere menstruieren auch – aber nur wenige.

   Die meisten Säugetiere bauen ihre Gebärmutterschleimhaut einfach wieder ab, ohne zu bluten. Nur wenige Arten wie Primaten, Fledermäuse oder Elefantenrüssler haben echte Menstruationszyklen.

4. Menstruation kann ein Vitalzeichen sein.

   In der Medizin wird der Zyklus manchmal als "fünftes Vitalzeichen" angesehen – ähnlich wichtig wie Puls, Blutdruck oder Atmung. Zyklusveränderungen können Hinweise auf Stress, Essstörungen, Schilddrüsenerkrankungen oder hormonelle Dysbalancen geben.

🚫 Und was ist mit Mythen?

- „Man darf beim Schwimmen nicht ins Wasser“ – Quatsch! Mit Tampon, Cup oder Periodenunterwäsche geht das problemlos.

- „Alle haben Schmerzen“ – Viele haben leichte Krämpfe, aber starke Schmerzen sind nicht normal und sollten ärztlich abgeklärt werden (z. B. Endometriose).

- „Menstruation ist unrein“ – Dieser Mythos stammt aus alten patriarchalen Gesellschaften. Fakt: Menstruation ist ein gesunder Vorgang.

💬 Fazit:
Die Menstruation ist kein „Makel“, sondern ein ausgeklügeltes Zusammenspiel von Hormonen und Organen – ein Zeichen dafür, dass der Körper funktioniert!

""",
    "Follikelphase": """Nach der Menstruation beginnt im weiblichen Körper eine neue Runde der Vorbereitung: die Follikelphase, bei der sich alles darauf vorbereitet, ein neues Ei zur Reife zu bringen.

🔬 Was passiert in der Follikelphase?
Die Follikelphase startet am ersten Tag der Menstruation und endet mit dem Eisprung (Ovulation). Ihr Name kommt vom Wort Follikel – das sind kleine Bläschen in den Eierstöcken, die jeweils ein Ei enthalten.

Während dieser Phase:
reifen mehrere Follikel heran, wobei aber nur einer dominant wird und sich auf den Eisprung vorbereitet.
Gleichzeitig baut sich die Gebärmutterschleimhaut wieder auf – als Vorbereitung auf eine mögliche Einnistung.

🧠 Fun Facts zur Follikelphase:
1. Du wirst hormonell aufgedreht.

Das Hormon Östrogen steigt in dieser Phase kräftig an. Es sorgt nicht nur für den Schleimhautaufbau, sondern beeinflusst auch Haut, Stimmung, Energielevel und sogar dein Gedächtnis. Viele fühlen sich in dieser Zeit besonders motiviert und aktiv.

2. Mehrere Eizellen starten – aber nur eine gewinnt.

Anfangs beginnen 10–20 Follikel gleichzeitig zu reifen, aber am Ende wird nur ein "Leitfollikel" dominant und löst den Eisprung aus. Die anderen bilden sich zurück.

3. Die Phase kann unterschiedlich lang sein.

Im Gegensatz zur Lutealphase (die fast immer ca. 14 Tage dauert), kann die Follikelphase zwischen 7 und 21 Tagen oder sogar noch länger dauern. Sie ist der Hauptgrund dafür, warum sich Zyklen in der Länge unterscheiden.

4. Dein Körper wird "empfängnisbereit".

Östrogen sorgt auch dafür, dass der Zervixschleim dünn und durchlässig wird – optimal für Spermien. Außerdem wird die Haut oft klarer, die Libido kann steigen und manche spüren sogar mehr Kreativität oder Fokus.

""",
    "Ovulation": """Die Ovulation, auch Eisprung, ist das zentrale Ereignis im weiblichen Zyklus: Ein reifes Ei verlässt den Eierstock und macht sich auf den Weg – bereit für eine mögliche Befruchtung. Klingt simpel, ist aber ein präzise getimter, hormonell gesteuerter Vorgang.

🔬 Was passiert bei der Ovulation?

Rund um die Zyklusmitte – also etwa am 14. Tag eines 28-Tage-Zyklus – passiert Folgendes:

Der dominierende Follikel „platzt“ auf,
das Ei wird freigesetzt und wandert in den Eileiter,
dort bleibt es für ca. 12–24 Stunden befruchtungsfähig.
Der Startschuss dafür ist der sogenannte LH-Peak – ein starker Anstieg des luteinisierenden Hormons (LH), der wie ein interner Countdown funktioniert.

🧠 Coole Facts zur Ovulation:

1. Du merkst (vielleicht), dass es passiert

   Einige Frauen spüren den Eisprung als leichtes Ziehen im Unterleib – den sogenannten Mittelschmerz. Andere bemerken veränderten Zervixschleim (spinnbar, durchsichtig – wie rohes Eiweiß).

2. Die fruchtbare Phase ist kurz – aber nicht zu kurz

   Das Ei selbst lebt nur ca. 1 Tag. Spermien hingegen bis zu 5 Tage. Deshalb gilt: Die „fruchtbare Phase“ umfasst etwa 5–6 Tage vor und am Tag des Eisprungs.

3. Die Körpertemperatur verrät den Eisprung – aber erst danach

   Nach der Ovulation steigt das Hormon Progesteron – das erhöht die Basaltemperatur leicht (ca. 0,3–0,5 °C). Das wird in der natürlichen Familienplanung (NFP) genutzt, um den Eisprung rückwirkend zu erkennen.

4. Du bist vielleicht sozialer, flirtfreudiger, kreativer

   Studien zeigen: Um den Eisprung herum steigt oft die Lust, das Selbstbewusstsein – und sogar die Wahrscheinlichkeit, dass jemand "mehr riskiert" oder extrovertierter auftritt.

 """,
    "Lutealphase": """Nach dem Eisprung beginnt die Lutealphase – eine Zeit, in der sich der Körper darauf vorbereitet, ein eventuell befruchtetes Ei „einzunisten“. Diese Phase ist hormonell ruhiger, aber keineswegs unwichtig.

🔬 Was passiert in der Lutealphase?

Nachdem das Ei den Eierstock verlassen hat, wandelt sich der leere Follikel in den sogenannten Gelbkörper (lateinisch: corpus luteum). Dieser produziert das Hormon Progesteron – und das hat es in sich:
Es sorgt dafür, dass die Gebärmutterschleimhaut dick und nährstoffreich bleibt,
es erhöht die Körpertemperatur leicht (um ca. 0,3–0,5 °C),
und es stabilisiert den Zyklus für ca. 14 Tage.
Wenn keine Befruchtung stattfindet, schrumpft der Gelbkörper, Progesteron fällt ab – und die Menstruation beginnt.

🧠 Coole Facts zur Lutealphase:

1. Sie ist fast immer gleich lang
   Im Gegensatz zur Follikelphase ist die Lutealphase bei den meisten Menschen ziemlich konstant: ca. 12–14 Tage. Das macht sie wichtig für die Zyklusberechnung.

2. Progesteron beruhigt – aber auch nicht immer nur positiv

   Progesteron wirkt beruhigend und entspannend, kann aber auch Stimmungsschwankungen, Heißhunger oder Müdigkeit auslösen. Deshalb erleben manche in dieser Phase PMS (prämenstruelles Syndrom).

3. Temperatur steigt – ein NFP-Indikator

   Die Temperaturerhöhung nach dem Eisprung bleibt über die Lutealphase bestehen – bis zur nächsten Menstruation. Das nutzen viele zur natürlichen Zyklusbeobachtung oder zur Unterstützung bei Kinderwunsch.

4. Ein kleiner Energieshift

   Manche fühlen sich in der Lutealphase introvertierter, reflektierter oder emotionaler – was übrigens gar nicht schlecht sein muss! Es ist eine Phase, in der der Körper bewusst langsamer fährt.

"""
}
phase = st.selectbox("ℹ️ Zyklusphase wählen", list(zyklusphasen.keys()))
st.subheader(f"📅 {phase}")
st.write(zyklusphasen[phase])

# Hormoninfo
hormon_infos = {
    "Östrogen": "Östrogen: Aufbau der Schleimhaut, Follikelreifung, Einfluss auf Stimmung & Haut.",
    "Progesteron": "Progesteron: Erhalt der Schleimhaut, Temperaturerhöhung, beruhigend.",
    "LH": "LH: Auslöser des Eisprungs durch LH-Peak.",
    "FSH": "FSH: Stimuliert Follikelwachstum und Östrogenbildung."
}
hormon = st.selectbox("ℹ️ Hormon wählen", list(hormon_infos.keys()))
st.subheader(f"🧪 {hormon}")
st.write(hormon_infos[hormon])
