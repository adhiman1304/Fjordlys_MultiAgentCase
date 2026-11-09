import re, os
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = B + "/materiale/"
def read(p): return open(p, encoding="utf-8").read()
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
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            lines.append(f"| {cells[0]} | {cells[1]} |")
    return "# M10 – Rykter du har hørt (status kjenner du ikke)\n\n" + "\n".join(lines) + "\n"

m01 = read(M+"M01_company_profile.md")
m02 = read(M+"M02_key_figures_production_cost.md")
m03 = read(M+"M03_board_deadline_and_targets.md")
m04 = read(M+"M04_competence_mapping.md")
m05 = read(M+"M05_previous_transformation_programme.md")
m06 = read(M+"M06_ai_pilot_digitalisation.md")
m07 = read(M+"M07_customer_dialogue_nordhav_gass.md")
m08 = read(M+"M08_internal_emails.md")
m09 = read(M+"M09_hse_and_employee_participation.md")
m10 = read(M+"M10_rumour_log_and_source_checks.md")
m00 = read(M+"M00_answer_key_fact_sheet.md")
case = read(B+"/01_case_description.md")
leveransemal = read(B+"/02_leveransemal.md")

def hdr(name): return read(B+"/agenter_src/"+name)
def block(title, body): return f"\n\n---\n\n# MATERIALE: {title}\n\n{body.strip()}\n"

agents = {
 "A1_Anne_leader.md": ("H1_anne.md", [
    ("M01 Selskapsprofil", m01),
    ("M02 Nøkkeltall (kun tabell A og B)", pick_sections(m02, ["Tabell A","Tabell B"])),
    ("M03 Styrets frist og mål", m03),
    ("M05 Tidligere endringsprogram (kun sammendrag)", upto(m05, "## 2.")),
    ("M08 Interne e-poster (E-1, E-3, E-6)", emails(m08, {1,3,6})),
 ]),
 "A2_Per_rumour_spreader.md": ("H2_per.md", [
    ("M01 Selskapsprofil", m01),
    ("M10 Rykter du har hørt", rumours_only(m10)),
 ]),
 "A3_Jan_memory.md": ("H3_jan.md", [
    ("M01 Selskapsprofil", m01),
    ("M02 Nøkkeltall (kun Ormdal: tabell C og E)", pick_sections(m02, ["Tabell C","Tabell E"])),
    ("M04 Kompetansekartlegging", m04),
    ("M05 Tidligere endringsprogram", m05),
    ("M08 Interne e-poster (E-1, E-2, E-7)", emails(m08, {1,2,7})),
 ]),
 "A4_Maria_technology.md": ("H4_maria.md", [
    ("M01 Selskapsprofil", m01),
    ("M02 Nøkkeltall", m02),
    ("M06 KI-pilot og digitalisering", m06),
    ("M08 Interne e-poster (E-4)", emails(m08, {4})),
 ]),
 "A5_Kari_union_representative.md": ("H5_kari.md", [
    ("M01 Selskapsprofil", m01),
    ("M04 Kompetansekartlegging (seksjon 1–2 kun)", upto(m04, "## 3.")),
    ("M05 Tidligere endringsprogram", m05),
    ("M08 Interne e-poster (E-2, E-7, E-8)", emails(m08, {2,7,8})),
    ("M09 HMS, arbeidsmiljø og medvirkning", m09),
 ]),
 "A6_Board_judge.md": ("H6_board.md", [
    ("Casebeskrivelse", case),
    ("Leveransemal", leveransemal),
    ("M01 Selskapsprofil", m01),
    ("M02 Nøkkeltall", m02),
    ("M03 Styrets frist og mål", m03),
    ("M04 Kompetansekartlegging", m04),
    ("M05 Tidligere endringsprogram", m05),
    ("M06 KI-pilot og digitalisering", m06),
    ("M07 Kundedialog Nordhav Gass", m07),
    ("M08 Interne e-poster", m08),
    ("M09 HMS, arbeidsmiljø og medvirkning", m09),
    ("M10 Ryktelogg og kildekontroll", m10),
    ("M00 Fasit og faktaark", m00),
 ]),
}
os.makedirs(B+"/agenter", exist_ok=True)
for out, (h, parts) in agents.items():
    text = hdr(h)
    for title, body in parts:
        text += block(title, body)
    open(B+"/agenter/"+out, "w", encoding="utf-8").write(text)
    print(out, len(text))
