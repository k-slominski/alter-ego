# ALTER EGO – Gabinet Psychoterapii Bożena Słomińska (Toruń)

Nowa, minimalistyczna wersja strony [www.alterego-torun.pl](https://www.alterego-torun.pl/).
Zachowane są wszystkie treści, zdjęcia, logotypy i dane kontaktowe z oryginału –
zmieniony jest wyłącznie wygląd.

Statyczny serwis (HTML + CSS + odrobina JS). Nie wymaga budowania – wystarczy otworzyć
`index.html` albo opublikować katalog, np. przez GitHub Pages
(Settings → Pages → Deploy from a branch → folder `/`).

## Strony
| plik | odpowiednik w starej stronie |
|---|---|
| `index.html` | alter ego (strona główna) |
| `komu-pomagam.html` | komu pomagam |
| `formy-pomocy.html` | formy pomocy + 6 podstron (psychoterapia indywidualna, grupowa, terapia par, terapia DDA i DDD, poradnictwo rodzinne, interwencja kryzysowa) |
| `oferta-szkoleniowa.html` | oferta szkoleniowa + trening interpersonalny, programy rozwoju osobistego |
| `o-mnie.html` | o mnie |
| `wspolpracuje.html` | współpracuję |
| `orientacja-teoretyczna.html` | orientacja teoretyczna |
| `cennik.html` | cennik |
| `kontakt.html` | kontakt |
| – | aktualności → link do profilu na Facebooku (jak w oryginale) |

## Udogodnienia
- **Mapa Google** z lokalizacją gabinetu na stronie głównej (sekcja „Dojazd i kontakt”) i na stronie Kontakt
- przycisk **„Wyznacz trasę”** – otwiera nawigację Google Maps do gabinetu (także w stopce)
- **pasek szybkiego kontaktu** na telefonach: Zadzwoń / Dojazd / E-mail
- **„Zapisz kontakt w telefonie”** – wizytówka `assets/alter-ego-bozena-slominska.vcf`
- przycisk **„Kopiuj”** przy numerze konta w cenniku
- dane strukturalne schema.org (adres, telefon, położenie) – lepsza widoczność w Google i Mapach
- podgląd przy udostępnianiu linku (Open Graph), `sitemap.xml`, `robots.txt`, strona `404.html`

Adres `https://www.alterego-torun.pl/` jest wpisany w `tools/build.py` (`SITE_URL`) –
zmień go, jeśli strona będzie działać pod innym adresem.

## Edycja treści
Wspólny nagłówek, menu i stopka są generowane skryptem – treść stron znajduje się w
`tools/build.py`. Po zmianie uruchom:

```sh
python3 tools/build.py
```

## Struktura
- `assets/css/style.css` – style (paleta: ciepła biel, grafit, zieleń drzewa z logo)
- `assets/js/main.js` – menu mobilne, delikatne pojawianie się sekcji
- `assets/img/` – zdjęcia i logotypy z oryginalnej strony; `drzewo.png` to logo (drzewo) wycięte z oryginalnego nagłówka
