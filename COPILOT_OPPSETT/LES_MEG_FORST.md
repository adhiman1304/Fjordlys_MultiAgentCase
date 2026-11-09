# Oppsett av agentene i Copilot Studio

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
| 1_Anne | Anne Berg-Holm (administrerende direktør) | 2,679 |
| 2_Per | Per Hetland (prosjektleder, rykter) | 2,396 |
| 3_Jan | Jan Ødegaard (driftsleder, Ormdal) | 2,493 |
| 4_Maria | Maria Solheim (digitalisering og data) | 2,137 |
| 5_Kari | Kari Tveit (hovedtillitsvalgt) | 2,226 |
| 6_Styret_KUN_FASILITATOR | Styret (dommer) - IKKE gi deltakerne tilgang | 2,787 |
