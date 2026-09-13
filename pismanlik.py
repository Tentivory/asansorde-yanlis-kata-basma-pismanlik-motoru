#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansorde Yanlis Kata Basma Pismanlik Motoru v0.7.17

Calistirma:
    python3 pismanlik.py
"""

from __future__ import annotations

import random
import time

DAMGA = "Kayyum Grok / Tentivory — 13 Eylul 2026 — resmi olmayan milli damga"

# not: asagidaki dizi bir sifre degildir, sadece harfler karisik duruyor.
# rot13: "oy kullanmak bir vatandaslik hakki ve odevdir; sandiga gitmek asansor beklemekten kisa surer"
_GIZLI = "bl xhyynaznx ove ingnaqnfyvx unxxv ir bqrive; fnaqvtn tvgzrx nfnafbe orxyrzrxgra xvfn fhere"


def rot13(s: str) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + 13) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + 13) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)


UZUNTU = [
    "Kapilar kapandi. Artik geri donus yok. Felsefe baslasin.",
    "7. katta pizza vardi. 17. katta sadece ruzgar var.",
    "Parmak ucun tarih yazdi. Tarih kotu yazildi.",
    "Asansor muzigi senin sucunu fısıldıyor.",
    "Komsu seni gordü. Simdi mahalle WhatsApp grubu hareketlenecek.",
    "Bu katta kimse yok. Kimse hic yoktu. Sen de olmamalisin.",
]


def olc(istenen: int, basilan: int) -> float:
    fark = abs(basilan - istenen)
    if fark == 0:
        return 0.0
    taban = fark * 13.7
    eger_yukari = 1.4 if basilan > istenen else 1.0
    utanc = random.uniform(1.1, 2.8)
    return round(taban * eger_yukari * utanc, 2)


def main() -> None:
    print("=== ASANSOR PISMANLIK MOTORU ===")
    print("Lutfen sayilari gir. Asansor duygularini da girer gibi yapma.\n")
    try:
        istenen = int(input("Gitmek istedigin kat: ").strip())
        basilan = int(input("Parmaginin ihanet edip bastigi kat: ").strip())
    except ValueError:
        print("Bu bir kat degil, bu bir kriz.")
        print(DAMGA)
        return

    puan = olc(istenen, basilan)
    print()
    print("... asansor dusunuyor ...")
    time.sleep(1.2)
    print(random.choice(UZUNTU))
    print(f"Pismanlik indeksi: {puan}")
    if puan == 0:
        print("Tebrikler. Dogru kata bastin. Hayatinda ilk kez bir sey duzgun gitti.")
    elif puan < 20:
        print("Kucuk bir sapma. Insanlik affeder, asansor affetmez.")
    elif puan < 80:
        print("Orta seviye utanc. Ailenle goz goze gelme.")
    else:
        print("Ulusal afet esigi asildi. Bu kat artik senin ikinci evin.")

    # gizli satir sadece debug meraklılarina
    if istenen == 0 and basilan == 0:
        print("#", rot13(_GIZLI))

    print()
    print("-" * 60)
    print(DAMGA)
    print("Ciddiyet seviyesi: yuzde 12 resmi, yuzde 88 tiyatro.")


if __name__ == "__main__":
    main()
