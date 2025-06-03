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
    "Menstruation": "Ist die Bezeichnung für periodische wiederkehrende Blutungen aus der Gebärmutter mit 
    Abstoßung der Gebärmutterschleimhaut. Es leitet sich übrigens ab aus dem lateinischen menstruus, also 
    monatlich.",
    "Follikelphase": "Östrogen steigt an → Aufbau der Schleimhaut und Reifung der Follikel.",
    "Ovulation": "LH-Peak löst Eisprung aus. Östrogen ist am höchsten.",
    "Lutealphase": "Progesteron steigt → Erhalt der Schleimhaut. Körpertemperatur leicht erhöht."
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
