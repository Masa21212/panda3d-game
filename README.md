# Panda3D 3D-peli

Yksinkertainen 3D-peli Panda3D:llä - täydellistä aloittelijoille! 🎮

## Asennus

### Vaatimukset
- Python 3.6 tai uudempi
- pip (Python-pakettien hallinta)

### Asennusohjeet

1. **Kloonaa repository:**
```bash
git clone https://github.com/Masa21212/panda3d-game.git
cd panda3d-game
```

2. **Luo virtuaaliympäristö (valinnainen mutta suositeltava):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# tai
venv\Scripts\activate  # Windows
```

3. **Asenna riippuvuudet:**
```bash
pip install -r requirements.txt
```

## Käynnistäminen

```bash
python main.py
```

## Ohjaimet

| Näppäin | Toiminto |
|---------|----------|
| **Nuoli ylös** ↑ | Liiku eteenpäin |
| **Nuoli alas** ↓ | Liiku taaksepäin |
| **Nuoli vasemmalle** ← | Liiku vasemmalle |
| **Nuoli oikealle** → | Liiku oikealle |
| **Välilyönti** | Hyppää |

## Mitä pelissä tapahtuu?

- **Peli**: Voit liikuttaa sinistä kuutiota nuolinäppäimillä
- **Hyppääminen**: Välilyönnillä voit hypätä
- **Painovoima**: Kuutio putoaa maahan painovoiman vaikutuksesta
- **Kamera**: Kamera seuraa pelaajaa automaattisesti

## Projektin rakenne

```
panda3d-game/
├── main.py              # Pääpeliohjelma
├── requirements.txt     # Python-riippuvuudet
└── README.md           # Tämä tiedosto
```

## Seuraavat vaiheet

Kun hallitset perusasiat, voit lisätä:
- 🎨 Värejä ja tekstuureita
- 🎵 Ääniefektejä ja musiikkia
- 🎯 Tavoitteita (keräily, vihollisia)
- 📊 Pisteitä ja scoreboardia
- 🗺️ Lisää 3D-malleja ja levelejä
- 💥 Fysiikkajärjestelmä

## Oppimisresurssit

- [Panda3D dokumentaatio](https://www.panda3d.org/)
- [Panda3D tutoriaali](https://www.panda3d.org/documentation/)
- [Python dokumentaatio](https://docs.python.org/3/)

## Lisensssi

MIT

---

**Hauskaa koodausta!** 🚀
