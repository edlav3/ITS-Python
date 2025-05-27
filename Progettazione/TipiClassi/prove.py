from fpdf import FPDF

class PDFDiet(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Dieta Settimanale - 1800 kcal al giorno', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1)
        self.ln(3)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDFDiet()
pdf.add_page()

pdf.chapter_title("Colazione (fissa)")
pdf.chapter_body(
    "- 3 albumi + 1 uovo intero (omelette)\n"
    "- 30 g fiocchi d’avena\n"
    "- 1 cucchiaino burro d’arachidi (5 g)\n"
    "- 100 ml latte scremato o vegetale\n\n"
    "Macro: ~25g proteine / 20g carboidrati / 10g grassi - 280 kcal"
)

pdf.chapter_title("Spuntino (metà mattina o post-allenamento)")
pdf.chapter_body(
    "- 25 g proteine whey\n"
    "- 1 frutto medio (es. mela o banana piccola)\n\n"
    "Macro: ~25g proteine / 20g carboidrati / 2g grassi - 200 kcal"
)

pdf.chapter_title("Pranzo (Lun–Sab)")
pdf.chapter_body(
    "- 120 g petto di pollo o tacchino\n"
    "- 60 g riso basmati o integrale (peso crudo)\n"
    "- Verdure a piacere (zucchine, carote, peperoni, insalata)\n"
    "- 1 cucchiaino olio extravergine d’oliva (5 g)\n\n"
    "Macro: ~40g proteine / 45g carboidrati / 10g grassi - 450 kcal"
)

pdf.chapter_title("Cena (variazione su 6 giorni)")
pdf.chapter_body(
    "Lunedì: 140g tacchino, 50g riso, verdure, 5g olio EVO\n"
    "Martedì: 2 uova + 3 albumi, 1 fetta pane integrale, verdure, 1 cucchiaino olio\n"
    "Mercoledì: 150g pollo, 60g riso, verdure, 5g olio EVO\n"
    "Giovedì: 120g tonno al naturale, 40g pane integrale, insalata, 1 cucchiaio olio\n"
    "Venerdì: 150g tacchino, 50g riso, verdure, 5g olio EVO\n"
    "Sabato: 2 uova + 3 albumi, 40g pane integrale, verdure, 1 cucchiaino olio\n\n"
    "Macro medio cena: ~35g proteine / 35-40g carboidrati / 15g grassi - 450 kcal"
)

pdf.chapter_title("Domenica – Leggermente flessibile")
pdf.chapter_body(
    "- Mantieni porzioni simili ma puoi sostituire il riso con pasta integrale o cous cous.\n"
    "- Evita dolci, fritture, alcol.\n"
    "- Aggiungi solo un pasto più 'libero' se vuoi (es: un pranzo più abbondante)."
)

pdf.chapter_title("Totale giornaliero medio")
pdf.chapter_body(
    "- Proteine: 140–150 g\n"
    "- Carboidrati: 130–140 g\n"
    "- Grassi: 50–55 g\n"
    "- Calorie: ~1800 kcal"
)

pdf_file_path = "/home/its/dieta_settimanale_1800kcal.pdf"
pdf.output(pdf_file_path)