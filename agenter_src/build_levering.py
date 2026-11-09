import os, re, shutil, glob
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = B + "/kunnskap"
OUT = B + "/COPILOT_OPPSETT"
def read(p): return open(p, encoding="utf-8").read()
def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(t.strip() + "\n")

def plain(t):
    out = []
    for line in t.splitlines():
        if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line) and "-" in line and "|" in line:
            continue
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            line = " - ".join(c for c in cells if c)
        line = re.sub(r"^\s*#{1,6}\s+", "", line)
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        line = re.sub(r"`([^`]*)`", r"\1", line)
        out.append(line)
    return "\n".join(out)

names = {
 "1_Anne": ("A1_Anne", "Anne Berg-Holm (administrerende direktør)"),
 "2_Per": ("A2_Per", "Per Hetland (prosjektleder, rykter)"),
 "3_Jan": ("A3_Jan", "Jan Ødegaard (driftsleder, Ormdal)"),
 "4_Maria": ("A4_Maria", "Maria Solheim (digitalisering og data)"),
 "5_Kari": ("A5_Kari", "Kari Tveit (hovedtillitsvalgt)"),
 "6_Styret_KUN_FASILITATOR": ("A6_Styret_dommer", "Styret (dommer) - IKKE gi deltakerne tilgang"),
}
if os.path.exists(OUT): shutil.rmtree(OUT)
rows = []
for folder, (src, label) in names.items():
    instr = read(f"{K}/{src}/INSTRUKSJONER_lim_inn_i_instruksfeltet.md")
    parts = [read(f) for f in sorted(glob.glob(f"{K}/{src}/KUNNSKAP_*.txt"))]
    write(f"{OUT}/{folder}/1_INSTRUKSJONER.txt", instr)
    write(f"{OUT}/{folder}/2_KUNNSKAP.txt", plain("\n\n==========\n\n".join(p.strip() for p in parts)))
    rows.append(f"| {folder} | {label} | {len(instr):,} |")

write(OUT + "/LES_MEG_FORST.md", """# Oppsett av agentene i Copilot Studio

Casen bruker fem agenter som deltakerne snakker med, pluss én dommer for fasilitator.
Hver mappe er én agent og inneholder to filer:

- `1_INSTRUKSJONER.txt`: åpne, kopier alt, lim inn i agentens **Instructions**-felt.
- `2_KUNNSKAP.txt`: last opp som **Knowledge** (Add knowledge > Files).

## Slik gjør du det (per agent)

1. Gå til https://copilotstudio.microsoft.com og velg **Create > New agent** (hopp over veiviseren, velg «Configure»).
2. Gi agenten navn etter mappen (f.eks. «Anne Berg-Holm»).
3. Lim inn innholdet fra `1_INSTRUKSJONER.txt` i **Instructions**.
4. Under **Knowledge**: legg til `2_KUNNSKAP.txt` som fil.
5. Slå av **Web search** og **Use general knowledge** (Generative AI-innstillinger), slik at agenten kun bruker kunnskapsfilen.
6. Test i testpanelet (se under), og **Publish**.
7. Gjenta for alle agentene.

## Del ut til deltakerne
- Deltakerne får tilgang til agent 1-5. Hold hver agent i egen chat.
- Agent 6 (Styret) er kun for fasilitator. Bruk den til å vurdere leveransene og avsløre fasiten etter evalueringen. Del den aldri med deltakerne.
- Deltakerne skal ikke få se filene i denne mappen.

## Test før seminaret (3-4 spørsmål per agent)
- Anne: «Hva er målene våre?» (gir overordnet svar), deretter «Hva har styret bedt om, og når er fristen?» (skal først da åpne seg).
- Per: «Hva har du hørt?» (deler rykter uoppfordret, blander sant og usant).
- Jan: «Hvem har kritisk kompetanse som ikke er dokumentert?» (åpner seg først da).
- Maria: «Hvem bruker KI-verktøyet i praksis?» (avslører svakere pilotresultater).
- Kari: «Er fagforeningen konsultert om scenariene?» (avslører at de ikke er det).
- Sjekk at ingen agent nevner filnavn, dokumentkoder (M01, E-2 osv.) eller henviser til andre enn de fire øvrige kollegaene.

## Lengdegrense
Instruksfeltet i Copilot Studio har en øvre grense (ca. 8 000 tegn). Lengden på hver instruksfil står under.
Hvis en agent avviser innlimingen, kutt i eksemplene i instruksen eller meld fra.

| Mappe | Agent | Tegn i instruks |
|---|---|---|
""" + "\n".join(rows) + "\n")
print("\n".join(rows))
