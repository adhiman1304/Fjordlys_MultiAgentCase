import re, os, shutil
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = B + "/materiale/"
OUT = B + "/kunnskap"
def read(p): return open(p, encoding="utf-8").read()
def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(t.strip() + "\n")
def pick_sections(text, keep):
    out = []
    for p in re.split(r"(?m)^(?=## )", text):
        title = p.split("\n", 1)[0]
        if not p.startswith("## ") or any(k in title for k in keep):
            out.append(p)
    return "".join(out)
def upto(text, stop):
    i = text.find(stop)
    return text if i < 0 else text[:i]
def emails(text, ids):
    blocks = text.split("\n---\n")
    out = [blocks[0]]
    for b in blocks[1:]:
        m = re.search(r"\*\*E-(\d+)", b)
        if m and int(m.group(1)) in ids:
            out.append(b)
    return "\n---\n".join(out)
def rumours_only(text):
    lines = []
    for ln in text.splitlines():
        if ln.startswith("| # |"):
            lines.append("| # | Rykte (slik du har hørt det) |")
        elif ln.startswith("|---"):
            lines.append("|---|---|")
        elif re.match(r"\| R\d+ \|", ln):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            lines.append(f"| {c[0]} | {c[1]} |")
    return "# M10 – Rykter du har hørt (status kjenner du ikke)\n\n" + "\n".join(lines)
def instr(h):
    t = read(B + "/agenter_src/" + h)
    t = re.sub(r"\n## Ditt materiale.*$|\n## Fullt casemateriale.*$", "", t, flags=re.S)
    return t + "\n\n## Kunnskap\nMaterialet ditt ligger som kunnskapsfiler. Bruk kun dem.\n"

R = {k: read(M + f) for k, f in {
 "M01":"M01_company_profile.md","M02":"M02_key_figures_production_cost.md",
 "M03":"M03_board_deadline_and_targets.md","M04":"M04_competence_mapping.md",
 "M05":"M05_previous_transformation_programme.md","M06":"M06_ai_pilot_digitalisation.md",
 "M07":"M07_customer_dialogue_nordhav_gass.md","M08":"M08_internal_emails.md",
 "M09":"M09_hse_and_employee_participation.md","M10":"M10_rumour_log_and_source_checks.md",
 "M00":"M00_answer_key_fact_sheet.md"}.items()}

agents = {
 "A1_Anne": ("H1_anne.md", {
   "M01_selskapsprofil.md": R["M01"],
   "M02_nokkeltall_tabell_A_B.md": pick_sections(R["M02"], ["Tabell A","Tabell B"]),
   "M05_tidligere_program_sammendrag.md": upto(R["M05"], "## 2."),
   "M08_eposter_E1_E3_E6.md": emails(R["M08"], {1,3,6}),
   "M03_styrets_frist_og_mal.md": R["M03"]}),
 "A2_Per": ("H2_per.md", {
   "M01_selskapsprofil.md": R["M01"],
   "M10_rykter_uten_status.md": rumours_only(R["M10"])}),
 "A3_Jan": ("H3_jan.md", {
   "M01_selskapsprofil.md": R["M01"],
   "M02_nokkeltall_tabell_C_E.md": pick_sections(R["M02"], ["Tabell C","Tabell E"]),
   "M04_kompetansekartlegging.md": R["M04"],
   "M05_tidligere_program.md": R["M05"],
   "M08_eposter_E1_E2_E7.md": emails(R["M08"], {1,2,7})}),
 "A4_Maria": ("H4_maria.md", {
   "M01_selskapsprofil.md": R["M01"],
   "M02_nokkeltall.md": R["M02"],
   "M06_ki_pilot.md": R["M06"],
   "M08_eposter_E4.md": emails(R["M08"], {4})}),
 "A5_Kari": ("H5_kari.md", {
   "M01_selskapsprofil.md": R["M01"],
   "M04_kompetansekartlegging_sammendrag.md": upto(R["M04"], "## 3."),
   "M05_tidligere_program.md": R["M05"],
   "M08_eposter_E2_E7_E8.md": emails(R["M08"], {2,7,8}),
   "M09_hms_og_medvirkning.md": R["M09"]}),
 "A6_Styret_dommer": ("H6_board.md", {
   "00_casebeskrivelse.md": read(B+"/01_case_description.md"),
   "00_leveransemal.md": read(B+"/02_leveransemal.md"),
   "M01_selskapsprofil.md": R["M01"], "M02_nokkeltall.md": R["M02"],
   "M03_styrets_frist_og_mal.md": R["M03"], "M04_kompetansekartlegging.md": R["M04"],
   "M05_tidligere_program.md": R["M05"], "M06_ki_pilot.md": R["M06"],
   "M07_kundedialog_nordhav.md": R["M07"], "M08_eposter.md": R["M08"],
   "M09_hms_og_medvirkning.md": R["M09"], "M10_ryktelogg.md": R["M10"],
   "M00_fasit.md": R["M00"]}),
}
if os.path.exists(OUT): shutil.rmtree(OUT)
for name, (h, files) in agents.items():
    write(f"{OUT}/{name}/INSTRUKSJONER_lim_inn_i_instruksfeltet.md", instr(h))
    for fn, body in files.items():
        write(f"{OUT}/{name}/KUNNSKAP_{fn[:-3]}.txt", body)
write(OUT + "/LES_MEG.md", """# Kunnskapsmapper per agent

Hver mappe er én agent i Copilot Studio.
- `INSTRUKSJONER_...md`: lim innholdet inn i agentens instruksfelt (ikke last opp som kunnskap).
- `KUNNSKAP_...`: last opp disse som kunnskapsfiler til agenten. Kun disse.

Last aldri opp filer fra én mappe til en annen agent. Dommerens mappe er kun for fasilitatorene.
""")
