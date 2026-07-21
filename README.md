# Python pro seminář

Zdrojový repozitář online učebnice Pythonu vytvořené v MkDocs Material.

## Lokální spuštění

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Otevři `http://127.0.0.1:8000`.

## Publikování

1. Ujisti se, že `site_url` a `repo_url` v `mkdocs.yml` odpovídají skutečnému GitHub repozitáři.
2. Odešli větev `main` na GitHub.
3. Na GitHubu otevři **Settings → Pages** a nastav **Source** na **GitHub Actions**.
4. Každý další push do `main` automaticky publikuje novou verzi.

## Poznámka k obsahu

První verze obsahuje základy Pythonu a projekty z dodaných studijních podkladů:
Generátor hesel, Devět životů, Stavitel robota, Kaleido-spirála,
Hvězdná noc a Mutantní duha.
