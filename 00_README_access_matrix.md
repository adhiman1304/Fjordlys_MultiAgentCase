# Fagsamling «Stavanger i omstilling» – casepakke

Fiktivt selskap: **Fjordlys Energi ASA** (fiktivt, inspirert av norsk E&P-sektor, ikke knyttet til noen virkelig aktør).

## Mappestruktur

```
fjordlys_case/
├── 00_README_access_matrix.md     ← denne filen (kun for casansvarlig og dommer)
├── 01_case_description.md         ← det gruppene får utdelt
├── 02_leveransemal.md             ← malen gruppene leverer etter
├── materiale/                     ← støttemateriale (kun tilgjengelig via agentene)
│   ├── M01_company_profile.md
│   ├── M02_key_figures_production_cost.md
│   ├── M03_board_deadline_and_targets.md
│   ├── M04_competence_mapping.md
│   ├── M05_previous_transformation_programme.md
│   ├── M06_ai_pilot_digitalisation.md
│   ├── M07_customer_dialogue_nordhav_gass.md
│   ├── M08_internal_emails.md
│   ├── M09_hse_and_employee_participation.md
│   ├── M10_rumour_log_and_source_checks.md
│   └── M00_answer_key_fact_sheet.md   ← KUN dommer
└── agenter/                       ← filer som lastes opp til co-pilot
    ├── A1_Anne_leader.md
    ├── A2_Per_rumour_spreader.md
    ├── A3_Jan_memory.md
    ├── A4_Maria_technology.md
    ├── A5_Kari_union_representative.md   ← valgfri femte agent
    └── A6_Board_judge.md
```

## Tilgangsmatrise

| Materiale | Anne (leder) | Per (rykter) | Jan (erfaring) | Maria (tek) | Kari (tillitsvalgt) | Styret (dommer) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| M01 Selskapsprofil | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| M02 Nøkkeltall produksjon/kostnad | delvis (kun tabell A og B) | nei | delvis (kun Ormdal, tabell C og E) | ✔ | nei | ✔ |
| M03 Styrets frist og mål | ✔ | nei | nei | nei | nei | ✔ |
| M04 Kompetansekartlegging | nei* | nei | ✔ | nei | delvis (seksjon 1–2) | ✔ |
| M05 Tidligere endringsprogram | delvis (kun sammendrag) | nei | ✔ | nei | ✔ | ✔ |
| M06 AI-pilot | nei | nei | nei | ✔ | nei | ✔ |
| M07 Kundedialog Nordhav | nei | nei | nei | nei | nei | ✔ |
| M08 Interne e-poster | delvis | nei | delvis | delvis | delvis | ✔ |
| M09 HMS og medvirkning | nei | nei | nei | nei | ✔ | ✔ |
| M10 Ryktelogg | nei | ✔ (uten status) | nei | nei | nei | ✔ |
| M00 Fasit | nei | nei | nei | nei | nei | ✔ |

\* Anne vet at kompetansekartleggingen er gjort, men ikke resultatet. Den skjulte risikoen må finnes ved å spørre Jan eller Kari.

**Viktig:** Agentene bruker kun materiale de har tilgang til. Hvis en gruppe spør om noe utenfor egen tilgang, svarer agenten at den ikke har informasjonen. Den skal ikke gjette eller hente den fra andre agenters innhold.

## Låser (hva som må til for at agenten deler skjult informasjon)

| Agent | Skjult kort | Lås |
|---|---|---|
| Anne | Styrets frist, kostnadsmål, nedbemanningsplan | Gruppen må nevne styret, eierne eller fristen konkret, eller vise at de allerede kjenner til et mål. Vage spørsmål gir vage svar. |
| Jan | Kritisk kompetanse som ikke er dokumentert, mulig avgang | Respekt for faget, konkrete spørsmål om prosess, sikkerhet og kvalitet. Ingen buzzwords. Han åpner seg ikke for noen som selger. |
| Maria | Pilotresultater svakere enn presentert | Gruppen spør direkte om måling, adopsjon eller hvem som faktisk bruker verktøyet. |
| Per | Rykter (blanding av sant og usant) | Han deler uoppfordret, men gruppene som verifiserer hos andre agenter, får bedre poeng (dommerens kriterium «kildekritikk»). |
| Kari | Ansattperspektiv, medvirkningsplikt | Gruppen spør om ansatte og medvirkning, ikke bare om kostnad. |

## Hvordan dommeren bruker materialet
- Dommeren («Styret») har full tilgang til alt.
- Etter evalueringen avslører den skjulte kort og hvilke rykter som var sanne (M10 og M00).
- Vurderingskriteriene med vekting ligger i `A6_Board_judge.md`, og leveransemalen i `02_leveransemal.md`.

## Råd til casansvarlig
- Personer fra Advisory bør ikke være casansvarlig eller sitte i gruppene.
- Hold agentene i separate chatter, og gi ikke gruppene tilgang til filene i `materiale/`.
- Test hver agent med 3–4 spørsmål før seminaret. Sjekk særlig at Anne ikke deler skjulte kort uten lås, og at Per er troverdig, men ikke alltid riktig.
