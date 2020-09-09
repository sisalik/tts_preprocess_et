# -*- coding: utf-8 -*-

from collections import defaultdict

audible_symbols = {'@': 'ät', '$': 'dollar', '%': 'protsent', '&': 'ja', '+': 'pluss',
                   '=': 'võrdub', '€': 'euro', '£': 'nael', '§': 'paragrahv', '°': 'kraad',
                   '±': 'pluss miinus', '‰': 'promill', '×': 'korda', 'x': 'korda',
                   '*': 'korda', '∙': 'korda', ':': 'jagada', '-': 'miinus'}  # TODO jagada vs jagatud

# sümbolid, mis häälduvad vaid siis, kui asuvad kahe arvu vahel
audible_connecting_symbols = ('×', 'x', '*', ':', '-')

# any symbols still left unreplaced (neutral character namings which may be different from audible_symbols)
# used on the final text right before output as str.maketrans dictionary, thus the spaces
last_resort = {
    '@': ' ätt ',
    '=': ' võrdub ',
    '/': ' kaldkriips ',
    '(': ' sulgudes ',
    '#': ' trellid ',
    '*': ' tärn ',
    '&': ' ampersand ',
    '%': ' protsent ',
    '_': ' allkriips ',
}

# sümbolid ja lühendid, mis käänduvad vastavalt eelnevale arvule (nt 1 meeter vs 5 meetrit)
units = ('$', '%', '‰', '€', '£', '°', 'a', 'atm', 'km', 'km²', 'm', 'm²', 'm³', 'mbar', 'cm',
         'ct', 'd', 'dB', 'eks', 'h', 'ha', 'hj', 'hl', 'mm', 'tk', 'p', 'rbl', 'rm', 'lk',
         'pk', 's', 'sl', 'spl', 'sek', 'tk', 'tl', 'kr', 'min', 't', 'mln', 'mld', 'mg',
         'g', 'kg', 'ml', 'l', 'cl', 'dl')

# kaassõnad, mille korral eelnev või järgnev arvsõna läheb omastavasse käändesse
genitive_prepositions = ('üle', 'alla')
genitive_postpositions = ('võrra', 'ümber', 'pealt', 'peale', 'ringis', 'paiku', 'aegu', 'eest')
# sõnad, mille korral järgnev arvsõna läheb nimetavasse käändesse (kui oma kääne määramata)
nominative_preceeding_words = ('kell', 'number', 'aasta', 'kl', 'nr', 'a')

abbreviations = defaultdict(None,
{
                                   'apr': 'aprill',
                                   'aug': 'august',
                                   'aü': 'ametiühing',
                                   'ca': 'umbes',
                                   'cl': 'sentiliiter',
                                   'cm': 'sentimeeter',
                                   'dB': 'detsibell',
                                   'dets': 'detsember',
                                   'dl': 'detsiliiter',
                                   'dr': 'doktor',
                                   'e.m.a': 'enne meie ajaarvamist',
                                   'eKr': 'enne Kristuse sündi',
                                   'hj': 'hobujõud',
                                   'hr': 'härra',
                                   'hrl': 'harilikult',
                                   'IK': 'isikukood',
                                   'ingl': 'inglise keeles',
                                   'j.a': 'juures asuv',
                                   'jaan': 'jaanuar',
                                   'jj': 'ja järgmine',
                                   'jm': 'ja muud',
                                   'jms': 'ja muud sellised',
                                   'jmt': 'ja mitmed teised',
                                   'jn': 'joonis',
                                   'jne': 'ja nii edasi',
                                   'jpt': 'ja paljud teised',
                                   'jr': 'juunior',
                                   'Jr': 'juunior',
                                   'jsk': 'jaoskond',
                                   'jt': 'ja teised',
                                   'jun': 'juunior',
                                   'jv': 'järv',
                                   'k.a': 'kaasa arvatud',
                                   'kcal': 'kilokalor',
                                   'kd': 'köide',
                                   'kg': 'kilogramm',
                                   'kk': 'keskkool',
                                   'kl': 'kell',
                                   'klh': 'kolhoos',
                                   'km': 'kilomeeter',
                                   'km/h': 'kilomeetrit tunnis',
                                   'km²': 'ruutkilomeeter',
                                   'kod': 'kodanik',
                                   'kpl': 'kauplus',
                                   'kr': 'kroon',
                                   'krt': 'korter',
                                   'kt': 'kohusetäitja',
                                   'kv': 'kvartal',
                                   'lg': 'lõige',
                                   'lk': 'lehekülg',
                                   'LK': 'looduskaitse',
                                   'lp': 'lugupeetud',
                                   'LP': 'LP',
                                   'lüh': 'lühend',
                                   'm.a.j': 'meie ajaarvamise järgi',
                                   'm/s': 'meetrit sekundis',
                                   'mbar': 'millibaar',
                                   'mg': 'milligramm',
                                   'mh': 'muu hulgas',
                                   'ml': 'milliliiter',
                                   'mld': 'miljard',
                                   'mln': 'miljon',
                                   'mm': 'millimeeter',
                                   'MM': 'MM',
                                   'mnt': 'maantee',
                                   'm²': 'ruutmeeter',
                                   'm³': 'kuupmeeter',
                                   'Mr': 'mister',
                                   'Ms': 'miss',
                                   'Mrs': 'missis',
                                   'n-ö': 'nii-öelda',
                                   'nim': 'nimeline',
                                   'nn': 'niinimetatud',
                                   'nov': 'november',
                                   'nr': 'number',
                                   'nt': 'näiteks',
                                   'NT': 'NT',
                                   'okt': 'oktoober',
                                   'p.o': 'peab olema',
                                   'pKr': 'pärast Kristuse sündi',
                                   'pa': 'poolaasta',
                                   'pk': 'postkast',
                                   'pms': 'peamiselt',
                                   'pr': 'proua',
                                   'prl': 'preili',
                                   'prof': 'professor',
                                   'ps': 'poolsaar',
                                   'PS': 'PS',
                                   'pst': 'puiestee',
                                   'ptk': 'peatükk',
                                   'raj': 'rajoon',
                                   'rbl': 'rubla',
                                   'reg-nr': 'registreerimisnumber',
                                   'rg-kood': 'registrikood',
                                   'rmtk': 'raamatukogu',
                                   'rmtp': 'raamatupidamine',
                                   'rtj': 'raudteejaam',
                                   's.a': 'sel aastal',
                                   's.o': 'see on',
                                   's.t': 'see tähendab',
                                   'saj': 'sajand',
                                   'sealh': 'sealhulgas',
                                   'seals': 'sealsamas',
                                   'sen': 'seenior',
                                   'sept': 'september',
                                   'sh': 'sealhulgas',
                                   'skp': 'selle kuu päeval',
                                   'SKP': 'SKP',
                                   'sl': 'supilusikatäis',
                                   'sm': 'seltsimees',
                                   'SM': 'SM',
                                   'snd': 'sündinud',
                                   'spl': 'supilusikatäis',
                                   'srn': 'surnud',
                                   'stj': 'saatja',
                                   'surn': 'surnud',
                                   'sü': 'säilitusüksus',
                                   'sünd': 'sündinud',
                                   'tehn': 'tehniline',
                                   'tel': 'telefon',
                                   'tk': 'tükk',
                                   'tl': 'teelusikatäis',
                                   'tlk': 'tõlkija',
                                   'tn': 'tänav',
                                   'tv': 'televisioon',
                                   'u': 'umbes',
                                   'ukj': 'uue, Gregoriuse kalendri järgi',
                                   'v.a': 'välja arvatud',
                                   'veebr': 'veebruar',
                                   'vkj': 'vana, Juliuse kalendri järgi',
                                   'vm': 'või muud',
                                   'vms': 'või muud sellist',
                                   'vrd': 'võrdle',
                                   'vt': 'vaata',
                                   'õa': 'õppeaasta',
                                   'õp': 'õpetaja',
                                   'õpil': 'õpilane',
})

pronounceable_acronyms = ('ABBA', 'AIDS', 'ALDE', 'API', 'ARK', 'ATKO', 
                          'BAFTA', 'BENU', 'CERN', 'CRISPR', 'DARPA', 
                          'EFTA', 'EKA', 'EKI', 'EKRE', 'EKSA', 'EMO', 'EMOR', 'ERM', 'ERSO', 'ESTO', 'ETA', 'EÜE', 
                          'FIDE', 'FIFA', 'FISA',
                          'GAZ', 'GITIS', 'IBAN', 'ISIS', 'ISO', 'JOKK', 'NASA', 'NATO', 
                          'PERH', 'PID', 'PIN', 'PRIA', 'RAF', 'RET', 
                          'SALT', 'SARS', 'SETI', 'SIG', 'SIM', 'SMIT', 'SORVVO', 'TASS', 
                          'UNESCO', 'VAZ', 'VEB', 'WADA', 'WiFi')

cardinal_numbers = defaultdict(lambda: '', {'0': 'null',
                                            '1': 'üks',
                                            '2': 'kaks',
                                            '3': 'kolm',
                                            '4': 'neli',
                                            '5': 'viis',
                                            '6': 'kuus',
                                            '7': 'seitse',
                                            '8': 'kaheksa',
                                            '9': 'üheksa',
                                            2: 'tuhat',
                                            3: 'miljon',
                                            4: 'miljard',
                                            5: 'triljon',
                                            6: 'kvadriljon',
                                            7: 'kvintiljon',
                                            8: 'sekstiljon',
                                            9: 'septiljon',
                                            ',': 'koma',
                                            })

ordinal_numbers = defaultdict(lambda: '', {
    'üks': 'esimene',
    'kaks': 'teine',
    'kolm': 'kolmas',
    'neli': 'neljas',
    'viis': 'viies',
    'kuus': 'kuues',
    'seitse': 'seitsmes',
    'kaheksa': 'kaheksas',
    'üheksa': 'üheksas',
    'kümme': 'kümnes',
    'kümmend': 'kümnes',
    'teist': 'teistkümnes',
    'sada': 'sajas',
    'tuhat': 'tuhandes',
    'miljon': 'miljones',
    'miljard': 'miljardes',
    'triljon': 'triljones',
    'kvadriljon': 'kvadriljones',
    'kvintiljon': 'kvintiljones',
    'sekstiljon': 'sekstiljones',
    'septiljon': 'septiljones',
})

roman_numbers = defaultdict(lambda: 0, {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})

alphabet = defaultdict(lambda: '', {
    'A': 'aa',
    'B': 'bee',
    'C': 'tsee',
    'D': 'dee',
    'E': 'ee',
    'F': 'eff',
    'G': 'gee',
    'H': 'haa',
    'I': 'ii',
    'J': 'jott',
    'K': 'kaa',
    'L': 'ell',
    'M': 'emm',
    'N': 'enn',
    'O': 'oo',
    'P': 'pee',
    'Q': 'kuu',
    'R': 'err',
    'S': 'ess',
    'Š': 'šaa',
    'Z': 'zett',
    'Ž': 'žee',
    'T': 'tee',
    'U': 'uu',
    'V': 'vee',
    'W': 'kaksisvee',
    'Õ': 'õõ',
    'Ä': 'ää',
    'Ö': 'öö',
    'Ü': 'üü',
    'X': 'iks',
    'Y': 'igrek'
})
