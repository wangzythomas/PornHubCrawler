#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018/3/18 下午9:15
# Author  : Thomas Wang
# File    : wordCloud.py
# Version : 1.0

from collections import OrderedDict

dict = {'teen': 16613, 'cock': 15534, 'big': 15372, 'hot': 15212, 'pussy': 15018, 'fucked': 14555, 'scene': 13775, 'blonde': 11578, 'anal': 11075, 'ass': 11011, 'sex': 10931, 'fuck': 10742, 'milf': 9078, 'girl': 8993, 'sexy': 8424, 'fucks': 8251, 'fucking': 8165, 'black': 7851, 'cum': 7663, 'hard': 7188, 'babe': 7140, 'amateur': 6783, 'busty': 6616, 'brunette': 6355, 'dick': 5936, 'horny': 5270, 'lesbian': 5187, 'tits': 5109, 'young': 4930, 'blowjob': 4863, 'slut': 4739, 'asian': 4594, 'two': 4161, 'dildo': 3882, 'wife': 3870, 'up': 3835, 'pov': 3820, 'huge': 3783, 'takes': 3761, 'tight': 3722, 'loves': 3715, 'creampie': 3644, 'girls': 3616, 'compilation': 3430, 'first': 3421, 'threesome': 3344, 'sucks': 3311, 'latina': 3160, 'white': 2944, 'porn': 2899, 'cute': 2884, 'love': 2851, 'mom': 2784, 'hardcore': 2781, 'step': 2659, 'facial': 2631, 'wet': 2580, 'mature': 2552, 'ebony': 2545, 'sucking': 2517, 'getting': 2514, 'girlfriend': 2466, 'hd': 2459, 'old': 2456, 'orgasm': 2355, 'redhead': 2291, 'lesbians': 2265, 'guy': 2250, 'part': 2207, 'cumshot': 2150, 'bbc': 2101, 'double': 2099, 'chick': 2098, 'couple': 2097, 'massage': 2062, 'video': 2040, 'fun': 2008, 'beautiful': 1998, 'cocks': 1977, 'time': 1977, 'public': 1947, 'deep': 1944, 'some': 1944, 'naughty': 1934, 'rides': 1929, 'dirty': 1887, 'best': 1877, 'teens': 1876, 'petite': 1862, 'party': 1823, 'mouth': 1801, 'masturbates': 1790, 'interracial': 1773, 'tit': 1766, 'babes': 1763, 'real': 1757, 'face': 1740, 'hairy': 1720, 'man': 1718, 'japanese': 1687, 'play': 1675, 'suck': 1647, 'while': 1643, 'riding': 1621, 'casting': 1615, 'little': 1543, 'booty': 1520, 'masturbating': 1511, 'wants': 1507, 'toy': 1505, 'good': 1499, 'masturbation': 1495, 'like': 1493, 'sweet': 1467, 'college': 1413, 'skinny': 1399, 'natural': 1394, 'perfect': 1392, 'home': 1384, 'toys': 1382, 'new': 1378, 'friend': 1369, 'gf': 1362, 'russian': 1356, 'dp': 1355, 'german': 1353, 'couch': 1340, 'tiny': 1332, 'herself': 1325, 'nice': 1321, 'orgy': 1317, 'plays': 1305, 'gangbang': 1298, 'whore': 1293, 'squirt': 1285, 'amazing': 1283, 'sister': 1276, 'rough': 1244, 'shower': 1236, 'squirting': 1232, 'handjob': 1232, 'stockings': 1215, 'body': 1199, 'shows': 1179, 'boyfriend': 1175, 'bitch': 1174, 'daughter': 1171, 'pornstar': 1162, 'boobs': 1160, 'action': 1156, 'gorgeous': 1151, 'licking': 1134, 'cam': 1130, 'slutty': 1127, 'com': 1117, 'playing': 1106, 'makes': 1098, 'pink': 1098, 'euro': 1088, 'webcam': 1085, 'butt': 1085, 'beauty': 1083, 'sluts': 1081, 'red': 1080, 'how': 1068, 'super': 1064, 'wild': 1063, 'french': 1060, 'pounded': 1058, 'solo': 1039, 'brazzers': 1038, 'outdoor': 1024, 'full': 1022, 'hottie': 1019, 'homemade': 1017, 'naked': 1015, 'into': 1002, 'pretty': 995, 'star': 987, 'schoolgirl': 987, 'having': 982, 'enjoys': 980, 'teacher': 980, 'pool': 979, 'cums': 974, 'show': 972, 'caught': 966, 'load': 966, 'great': 964, 'very': 958, 'room': 957, 'head': 944, 'school': 941, 'office': 941, 'bed': 936, 'guys': 921, 'cutie': 919, 'then': 899, 'kinky': 896, 'bang': 893, 's': 887, 'bj': 884, 'each': 883, 'pmv': 880, 'asshole': 880, 'fat': 880, 'swallows': 879, 'holes': 877, 'son': 873, 'czech': 870, 'lingerie': 870, 'fingering': 863, 'husband': 862, 'deepthroat': 860, 'banged': 846, 'ride': 830, 'make': 822, 'x': 814, 'other': 810, 'take': 808, 'fingers': 808, 'angel': 806, 'beach': 801, 'down': 799, 'massive': 797, 'nasty': 795, 'british': 795, 'job': 790, 'creampied': 789, 'k': 789, 'brother': 786, 'student': 785, 'throat': 782, 'mofos': 782, 'share': 781, 'camera': 780, 'orgasms': 779, 'lady': 779, 'extreme': 777, 'taylor': 768, 'thick': 768, 'cunt': 766, 'squirts': 761, 'panties': 758, 'likes': 755, 'bondage': 754, 'fetish': 744, 'friends': 743, 'kitchen': 742, 'small': 740, 'alexis': 738, 'smoking': 738, 'strips': 737, 'daddy': 737, 'long': 733, 'nurse': 730, 'rose': 729, 'crazy': 729, 'lee': 723, 'behind': 719, 'bathroom': 719, 'slave': 718, 'ann': 718, 'hole': 716, 'strapon': 715, 'indian': 711, 'car': 707, 'dicks': 706, 'blond': 706, 'lucky': 700, 'dad': 700, 'bukkake': 699, 'no': 697, 'hotel': 696, 'year': 695, 'three': 693, 'inside': 690, 'ever': 686, 'marie': 679, 'woman': 677, 'titty': 676, 'eating': 675, 'monster': 674, 'pt': 673, 'stunning': 667, 'model': 667, 'blow': 664, 'passion': 661, 'mia': 658, 'fisting': 658, 'tattooed': 657, 'fake': 655, 'way': 655, 'blue': 652, 'more': 648, 'bf': 648, 'swallow': 647, 'cheating': 646, 'taking': 637, 'needs': 632, 'goes': 631, 'back': 631, 'maid': 631, 'cougar': 630, 'day': 630, 'penetration': 628, 'style': 628, 'sensual': 626, 'james': 624, 'nikki': 621, 'outdoors': 620, 'high': 614, 'babysitter': 612, 'cream': 611, 'giving': 608, 'granny': 607, 'doggystyle': 602, 'chicks': 600, 'group': 600, 'milfs': 598, 'erotic': 598, 'made': 597, 'xxx': 595, 'chubby': 594, 'agent': 592, 'private': 586, 'shy': 585, 'shaved': 585, 'nicole': 584, 'boss': 583, 'strap': 582, 'vol': 579, 'juicy': 574, 'volume': 571, 'sloppy': 571, 'tease': 570, 'music': 568, 'stud': 567, 'filled': 566, 'older': 564, 'doggy': 563, 'work': 562, 'boy': 554, 'toying': 554, 'reality': 553, 'lick': 551, 'dude': 551, 'vibrator': 551, 'close': 550, 'nude': 549, 'jessica': 548, 'lovely': 544, 'finger': 541, 'nailed': 539, 'lane': 535, 'films': 535, 'girlfriends': 533, 'licked': 532, 'housewife': 531, 'women': 530, 'pounding': 528, 'seduces': 528, 'tape': 524, 'sara': 523, 'jenna': 521, 'spanish': 521, 'blows': 520, 'eva': 520, 'loving': 515, 'cumshots': 512, 'starr': 511, 'oral': 510, 'bad': 510, 'diamond': 509, 'lisa': 508, 'latin': 508, 'teasing': 506, 'secretary': 505, 'doctor': 504, 'mommy': 501, 'club': 497, 'riley': 494, 'ashley': 492, 'watch': 492, 'morning': 491, 'piss': 489, 'until': 489, 'lynn': 488, 'session': 487, 'strip': 487, 'night': 484, 'pantyhose': 484, 'oiled': 482, 'hubby': 480, 'pleasure': 479, 'drilled': 476, 'kelly': 476, 'movie': 476, 'stepmom': 471, 'thai': 470, 'blondes': 468, 'rubs': 467, 'brutal': 467, 'cuckold': 466, 'amber': 465, 'vanessa': 465, 'intense': 465, 'teases': 464, 'glasses': 459, 'pregnant': 459, 'brooke': 458, 'creamy': 458, 'pornhublive': 458, 'tiffany': 452, 'ava': 452, 'interview': 451, 'jizz': 446, 'awesome': 445, 'kings': 445, 'chase': 445, 'curvy': 444, 'sarah': 442, 'fakeagent': 442, 'exotic': 440, 'baby': 435, 'vr': 435, 'stranger': 434, 'gangbanged': 433, 'european': 432, 'dildos': 432, 'pussies': 432, 'latex': 431, 'angelina': 430, 'dark': 429, 'scenes': 429, 'mother': 429, 'bdsm': 428, 'titted': 428, 'summer': 427, 'grey': 426, 'bath': 425, 'lovers': 425, 'turns': 424, 'west': 423, 'fantasy': 421, 'lexi': 421, 'cowgirl': 420, 'pornpros': 419, 'tied': 412, 'sperm': 412, 'samantha': 412, 'feet': 410, 'machine': 409, 'teeny': 409, 'st': 409, 'lily': 407, 'jayden': 405, 'masturbate': 405, 'outside': 404, 'facials': 404, 'making': 401, 'haired': 401, 'veronica': 398, 'live': 398, 'sasha': 398, 'lover': 398, 'want': 397, 'yoga': 396, 'holly': 394, 'clit': 392, 'chocolate': 391, 'bangbros': 391, 'rachel': 390, 'foot': 390, 'honey': 389, 'jay': 388, 'female': 388, 'cash': 387, 'doing': 386, 'ex': 385, 'chinese': 385, 'dee': 384, 'faketaxi': 384, 'queen': 384, 'passionate': 383, 'stuffed': 381, 'table': 381, 'house': 381, 'fox': 380, 'femdom': 380, 'bikini': 380, 'kissing': 379, 'twat': 378, 'rooms': 376, 'cumming': 375, 'cheerleader': 374, 'innocent': 373, 'please': 373, 'publicagent': 372, 'lesbea': 369, 'ready': 368, 'julia': 368, 'sophie': 368, 'eats': 367, 'nina': 365, 'yo': 365, 'another': 364, 'joi': 364, 'happy': 364, 'doll': 364, 'b': 364, 'sharing': 364, 'gang': 362, 'victoria': 362, 'door': 360, 'rain': 360, 'covered': 360, 'licks': 358, 'madison': 357, 'rubbing': 357, 'danejones': 356, 'taxi': 353, 'puremature': 353, 'really': 352, 'top': 351, 'multiple': 351, 'bubble': 350, 'bangs': 350, 'daisy': 349, 'belle': 349, 'hungry': 347, 'jade': 346, 'surprise': 345, 'voyeur': 344, 'foursome': 344, 'brazilian': 342, 'lucy': 342, 'heels': 341, 'rammed': 341, 'asa': 340, 'fishnet': 340, 'gym': 339, 'reid': 337, 'moore': 337, 'mistress': 334, 'money': 334, 'candy': 331, 'jizzed': 331, 'eat': 331, 'tries': 331, 'front': 331, 'men': 330, 'monroe': 330, 'enjoy': 330, 'audition': 325, 'american': 324, 'carmen': 323, 'valentina': 322, 'stripper': 322, 'jasmine': 322, 'than': 321, 'filipino': 320, 'bella': 320, 'o': 320, 'britney': 319, 'sexual': 317, 'virgin': 317, 'lesson': 317, 'fingered': 316, 'workout': 316, 'blondie': 315, 'dani': 315, 'together': 313, 'worship': 313, 'bound': 313, 'italian': 313, 'banging': 312, 'amateurs': 312, 'pawg': 311, 'family': 311, 'daniels': 310, 'dripping': 310, 'only': 310, 'chloe': 310, 'lets': 309, 'coed': 308, 'oil': 306, 'break': 306, 'katie': 305, 'les': 305, 'uses': 305, 'jane': 305, 'balls': 305, 'akira': 304, 'hottest': 303, 'both': 303, 'moms': 303, 'punished': 302, 'street': 301, 'special': 299, 'bitches': 299, 'meat': 299, 'every': 298, 'gaping': 297, 'amy': 296, 'christmas': 296, 'stone': 296, 'neighbor': 296, 'deepthroats': 296, 'emo': 295, 'fist': 295, 'cosplay': 294, 'legs': 294, 'emma': 293, 'lauren': 293, 'lust': 293, 'striptease': 293, 'picked': 293, 'knows': 293, 'scott': 291, 'megan': 291, 'london': 291, 'twistys': 291, 'ivy': 290, 'game': 290, 'fit': 289, 'till': 289, 'going': 289, 'anna': 289, 'uncensored': 288, 'teaches': 287, 'gloryhole': 287, 'showing': 286, 'sisters': 286, 'jaymes': 286, 'experience': 285, 'classic': 285, 'cumpilation': 285, 'pissing': 284, 'taste': 284, 'michaels': 284, 'seduced': 283, 'fresh': 282, 'facialized': 281, 'gina': 281, 'femaleagent': 281, 'tyler': 280, 'stripping': 279, 'see': 279, 'better': 279, 'birthday': 279, 'cop': 278, 'adams': 277, 'alex': 277, 'rae': 277, 'round': 274, 'pornstars': 274, 'povd': 273, 'erotica': 273, 'ginger': 272, 'whores': 272, 'blowing': 272, 'messy': 272, 'gagging': 271, 'blacked': 271, 'heather': 271, 'p': 270, 'bedroom': 270, 'stretched': 270, 'kitty': 269, 'swallowing': 269, 'sunny': 268, 'titties': 268, 'hidden': 268, 'haze': 268, 'penetrated': 268, 'miss': 268, 'vintage': 268, 'texas': 267, 'park': 267, 'reverse': 267, 'jennifer': 267, 'phoenix': 266, 'creampies': 265, 'patient': 264, 'alexa': 263, 'enjoying': 262, 'foxx': 262, 'dress': 262, 'lelu': 261, 'filthy': 261, 'drunk': 261, 'footjob': 261, 'slim': 261, 'raven': 260, 'date': 259, 'carter': 259, 'castingcouch': 258, 'younger': 258, 'right': 257, 'vixen': 257, 'dana': 256, 'evilangel': 255, 'jada': 255, 'sandra': 255, 'sky': 255, 'again': 254, 'hair': 254, 'life': 254, 'assfucked': 254, 'brunettes': 254, 'jav': 253, 'natasha': 253, 'class': 253, 'goddess': 253, 'sofa': 253, 'fire': 252, 'flexible': 252, 'tori': 252, 'dream': 252, 'phat': 251, 'pie': 251, 'spreads': 250, 'try': 250, 'flashing': 250, 'may': 250, 'jerk': 249, 'nerdy': 249, 'shyla': 249, 'glass': 249, 'kiss': 248, 'mary': 248, 'swinger': 247, 'jordan': 246, 'watching': 246, 'tv': 246, 'sextape': 246, 'alone': 246, 'training': 246, 'around': 245, 'swingers': 245, 'hero': 245, 'loads': 244, 'morgan': 244, 'gold': 244, 'submissive': 243, 'porno': 242, 'gianna': 242, 'dancing': 242, 'pro': 241, 'cherry': 240, 'open': 240, 'playground': 239, 'valentine': 238, 'michelle': 238, 'melissa': 238, 'skills': 238, 'blowjobs': 237, 'using': 236, 'banks': 236, 'lil': 236, 'now': 235, 'snatch': 234, 'green': 234, 'pure': 233, 'ends': 233, 'pierced': 233, 'alison': 232, 'teenage': 231, 'boobed': 231, 'watches': 230, 'pervcity': 230, 'summers': 230, 'asses': 230, 'bbw': 230, 'kendra': 228, 'monica': 227, 'capri': 226, 'lola': 226, 'skye': 225, 'digital': 225, 'sucked': 225, 'film': 225, 'creamed': 225, 'revenge': 224, 'pee': 224, 'fakeagentuk': 224, 'breasted': 223, 'short': 223, 'wicked': 223, 'fantasyhd': 222, 'lips': 221, 'need': 221, 'punishment': 221, 'sophia': 221, 'world': 220, 'boob': 220, 'talk': 219, 'wearing': 219, 'own': 218, 'stepsister': 218, 'quickie': 218, 'mouthful': 218, 'anally': 218, 'enough': 217, 'stop': 217, 'sis': 216, 'client': 215, 'uniform': 215, 'well': 215, 'puma': 214, 'brandi': 214, 'taboo': 214, 'call': 214, 'nubile': 214, 'audrey': 213, 'heart': 213, 'kate': 213, 'begs': 213, 'stepson': 213, 'ultimate': 212, 'wifey': 212, 'dance': 212, 'finds': 212, 'woods': 211, 'mason': 211, 'us': 211, 'halloween': 211, 'paradise': 211, 'stevens': 211, 'catches': 211, 'bombshell': 210, 'roxy': 210, 'tongue': 210, 'talking': 210, 'nylon': 210, 'uk': 209, 'devine': 209, 'swap': 208, 'fakehospital': 208, 'virtual': 208, 'look': 208, 'slammed': 208, 'fitness': 208, 'glory': 208, 'stepdaughter': 207, 'shot': 207, 'quick': 207, 'olivia': 206, 'large': 206, 'eve': 206, 'favorite': 206, 'giant': 206, 'thigh': 205, 'cheats': 205, 'throated': 205, 'perky': 205, 'these': 205, 'india': 205, 'adriana': 205, 'jessie': 205, 'saint': 204, 'skin': 204, 'looking': 204, 'secret': 203, 'hooker': 203, 'facesitting': 203, 'milk': 203, 'nympho': 202, 'lesbo': 202, 'wankz': 202, 'pornhub': 201, 'bar': 200, 'mandy': 199, 'luna': 199, 'parody': 199, 'games': 199, 'ending': 199, 'destroyed': 198, 'nipples': 198, 'tub': 197, 'shoot': 197, 'ryan': 196, 'fest': 196, 'trainer': 196, 'naomi': 195, 'spanked': 195, 'retro': 194, 'helps': 194, 'slow': 194, 'fine': 194, 'jolie': 194, 'finally': 193, 'exgf': 192, 'brown': 192, 'swede': 192, 'penny': 192, 'fan': 192, 'alice': 191, 'breasts': 191, 'fast': 191, 'courtney': 191, 'hands': 191, 'law': 191, 'streets': 190, 'aniston': 190, 'bouncing': 190, 'brooks': 190, 'inch': 190, 'princess': 190, 'jones': 190, 'von': 189, 'cindy': 189, 'challenge': 189, 'fisted': 189, 'plug': 189, 'here': 189, 'shares': 188, 'hotties': 188, 'arab': 188, 'oily': 188, 'jerks': 188, 'boots': 188, 'couples': 188, 'jenny': 188, 'free': 188, 'pants': 188, 'self': 187, 'bro': 187, 'away': 187, 'melanie': 187, 'lubed': 187, 'magic': 187, 'sweetheart': 187, 'laura': 186, 'maria': 185, 'maya': 185, 'leather': 185, 'emily': 185, 'poolside': 183, 'help': 183, 'floor': 183, 'desk': 183, 'through': 182, 'internal': 182, 'korean': 182, 'jensen': 182, 'master': 181, 'team': 181, 'abella': 181, 'penis': 181, 'august': 180, 'hitachi': 180, 'threeway': 180, 'hand': 179, 'daughters': 179, 'them': 179, 'claudia': 179, 'paige': 178, 'christy': 178, 'works': 178, 'yr': 178, 'rock': 178, 'come': 178, 'kay': 177, 'warm': 177, 'receives': 177, 'angela': 177, 'tory': 176, 'know': 176, 'jerking': 175, 'there': 175, 'never': 175, 'rebecca': 175, 'stepdad': 174, 'grandma': 174, 'used': 174, 'lhermite': 174, 'toilet': 174, 'vagina': 173, 'vacation': 173, 'students': 173, 'harper': 173, 'service': 172, 'sybian': 172, 'bus': 172, 'four': 172, 'tall': 172, 'sun': 171, 'strong': 171, 'use': 171, 'lana': 170, 'extra': 170, 'goo': 170, 'twice': 170, 'pigtailed': 170, 'angels': 170, 'deepthroating': 169, 'aka': 169, 'gyno': 169, 'strokes': 169, 'mac': 168, 'rhodes': 167, 'charley': 167, 'classy': 167, 'escort': 167, 'ryder': 167, 'years': 166, 'most': 166, 'sins': 166, 'faye': 165, 'luv': 165, 'sissy': 165, 'gefickt': 165, 'driver': 165, 'gone': 164, 'cox': 164, 'eyes': 164, 'art': 164, 'exclusive': 163, 'amwf': 163, 'shaking': 163, 'under': 163, 'snow': 163, 'tushy': 163, 'preston': 162, 'side': 162, 'steele': 162, 'muff': 162, 'styles': 162, 'en': 161, 'delicious': 161, 'bunny': 161, 'castings': 161, 'america': 160, 'dillion': 160, 'adventure': 160, 'incredible': 160, 'sabrina': 160, 'parents': 159, 'bree': 159, 'always': 159, 'true': 159, 'between': 159, 'african': 159, 'driving': 159, 'times': 158, 'ladies': 158, 'santa': 158, 'biggest': 158, 'boyfriends': 158, 'raw': 158, 'benz': 157, 'ball': 157, 'sylvia': 157, 'stretching': 157, 'lena': 157, 'phone': 157, 'panty': 157, 'seduction': 156, 'barbie': 156, 'f': 156, 'chair': 155, 'fishnets': 155, 'gag': 155, 'kayla': 155, 'craving': 155, 'had': 154, 'starring': 154, 'rossi': 154, 'hunter': 154, 'romi': 154, 'thing': 154, 'wanna': 154, 'its': 154, 'domination': 154, 'masseuse': 153, 'elle': 153, 'secrets': 153, 'mit': 153, 'crystal': 153, 'wide': 153, 'sierra': 152, 'jean': 152, 'teenager': 152, 'gia': 152, 'zoey': 152, 'missy': 151, 'kristina': 151, 'adventures': 151, 'desperate': 151, 'alix': 151, 'closeup': 151, 'others': 151, 'english': 151, 'pleasures': 150, 'cruz': 150, 'father': 150, 'teamed': 150, 'hart': 150, 'stacy': 150, 'boat': 150, 'ripped': 149, 'van': 149, 'afternoon': 148, 'april': 148, 'grace': 148, 'comes': 148, 'lot': 148, 'grandpa': 148, 'dildoing': 148, 'presley': 148, 'fuckin': 147, 'filipina': 147, 'deville': 147, 'plowed': 147, 'nikita': 147, 'bounce': 146, 'coeds': 146, 'keisha': 146, 'hung': 146, 'cassidy': 146, 'facialed': 145, 'fetishnetwork': 145, 'strangers': 145, 'charlee': 145, 'many': 145, 'mack': 145, 'romantic': 145, 'sorority': 145, 'tricky': 144, 'parties': 144, 'alicia': 144, 'atm': 144, 'nubiles': 144, 'chanel': 143, 'pole': 143, 'diana': 143, 'tia': 143, 'last': 142, 'hungarian': 142, 'cuties': 142, 'pegging': 142, 'kylie': 142, 'intimate': 142, 'bailey': 142, 'collection': 142, 'working': 141, 'bell': 141, 'dudes': 141, 'bathtub': 141, 'alyssa': 141, 'hoe': 141, 'mega': 141, 'trio': 141, 'cat': 140, 'mae': 140, 'craves': 140, 'treat': 140, 'addams': 139, 'leads': 139, 'spanking': 139, 'married': 139, 'masseur': 139, 'videos': 139, 'sativa': 139, 'penthouse': 138, 'tattoo': 138, 'cant': 138, 'spring': 138, 'naturals': 138, 'punk': 138, 'rimming': 138, 'fay': 138, 'much': 137, 'sitting': 137, 'nadia': 137, 'ariana': 137, 'freaky': 137, 'trying': 137, 'sticky': 137, 'adorable': 137, 'kat': 137, 'bush': 137, 'desi': 137, 'tina': 137, 'exxxtrasmall': 136, 'sleeping': 136, 'screwed': 136, 'cfnm': 136, 'mr': 136, 'drinking': 136, 'glamour': 136, 'oriental': 136, 'stylez': 136, 'teenie': 135, 'rod': 135, 'cole': 135, 'sandy': 135, 'propertysex': 135, 'tanned': 135, 'meets': 134, 'swapping': 134, 'dorm': 134, 'eaten': 134, 'hood': 134, 'japan': 134, 'forest': 134, 'myself': 134, 'abigail': 134, 'molly': 134, 'natalia': 133, 'casey': 133, 'ice': 133, 'steamy': 133, 'price': 133, 'luscious': 133, 'freak': 133, 'exam': 133, 'groupsex': 133, 'canadian': 133, 'screaming': 132, 'jamie': 132, 'parker': 132, 'misty': 132, 'nylons': 132, 'caprice': 132, 'dreams': 132, 'leone': 132, 'latinas': 132, 'stuffing': 131, 'stars': 131, 'elsa': 131, 'straight': 131, 'care': 131, 'boys': 131, 'stiff': 131, 'shanda': 130, 'studs': 130, 'loud': 130, 'banana': 130, 'pornfidelity': 130, 'control': 130, 'shared': 129, 'blindfolded': 129, 'cherie': 129, 'holiday': 129, 'train': 129, 'bridgette': 129, 'heaven': 129, 'orgasmic': 128, 'dong': 128, 'brooklyn': 128, 'lex': 127, 'rub': 127, 'brandy': 127, 'stella': 127, 'bounces': 127, 'schoolgirls': 127, 'place': 127, 'position': 127, 'wand': 126, 'allie': 126, 'brit': 126, 'ames': 126, 'mya': 126, 'casual': 126, 'teamskeet': 126, 'danger': 126, 'contest': 126, 'dearmond': 126, 'tan': 126, 'quinn': 125, 'estate': 125, 'king': 125, 'nerd': 125, 'gagged': 125, 'mama': 125, 'dakota': 125, 'clean': 125, 'cocksucking': 125, 'anderson': 125, 'twerking': 124, 'personal': 124, 'silver': 124, 'kendall': 124, 'leigh': 124, 'skirt': 124, 'triple': 124, 'barely': 124, 'bffs': 124, 'positions': 123, 'puts': 123, 'epic': 123, 'eager': 123, 'ffm': 123, 'nuru': 123, 'wake': 122, 'tasty': 122, 'gape': 122, 'came': 122, 'keyes': 122, 'sucker': 122, 'dominated': 122, 'end': 122, 'must': 122, 'dicked': 121, 'fantastic': 121, 'professor': 121, 'stage': 121, 'juice': 121, 'teenfidelity': 121, 'mirror': 121, 'ana': 121, 'chrystall': 121, 'rich': 120, 'breast': 120, 'purple': 120, 'rayne': 120, 'haley': 120, 'anita': 120, 'learns': 120, 'traffic': 119, 'exposed': 119, 'pleasing': 119, 'v': 119, 'ho': 119, 'dabs': 119, 'lacey': 119, 'therapy': 119, 'dahlia': 119, 'dean': 118, 'episode': 118, 'throats': 118, 'stocking': 118, 'maggie': 118, 'pale': 118, 'playful': 118, 'amanda': 118, 'muscle': 118, 'male': 118, 'krystal': 118, 'leah': 118, 'golden': 117, 'sub': 117, 'cover': 117, 'treatment': 117, 'missionary': 117, 'looks': 117, 'avn': 117, 'scandal': 117, 'wives': 116, 'cherokee': 116, 'pornhubtv': 116, 'pays': 116, 'lesbos': 116, 'chastity': 116, 'tribbing': 116, 'eyed': 116, 'ariel': 116, 'tag': 116, 'abby': 115, 'roommate': 115, 'u': 115, 'humping': 115, 'darling': 115, 'monique': 115, 'austin': 115, 'same': 115, 'strippers': 115, 'nova': 115, 'foxxx': 115, 'lynx': 115, 'sugar': 115, 'once': 115, 'tara': 115, 'layla': 115, 'kagney': 115, 'turned': 114, 'moon': 114, 'chechik': 114, 'blake': 114, 'pleases': 114, 'johnny': 114, 'lucie': 114, 'nubilefilms': 114, 'dutch': 114, 'outfit': 114, 'sin': 114, 'stepbrother': 114, 'perverted': 113, 'malkova': 113, 'julie': 113, 'vid': 113, 'stick': 113, 'view': 113, 'beauties': 112, 'der': 112, 'wakes': 112, 'piper': 112, 'hospital': 112, 'water': 112, 'north': 111, 'trailer': 111, 'familystrokes': 111, 'talks': 111, 'bimbo': 111, 'brothers': 111, 'vaginal': 111, 'hdvpass': 111, 'bobbi': 111, 'aurora': 110, 'rimjob': 110, 'blair': 110, 'soccer': 110, 'stephanie': 110, 'edition': 110, 'spread': 110, 'spy': 110, 'tutor': 110, 'damn': 110, 'tourist': 110, 'coach': 110, 'sextreme': 110, 'evans': 110, 'pumped': 110, 'road': 110, 'spreading': 110, 'mrs': 109, 'store': 109, 'xmas': 109, 'gloves': 109, 'keep': 109, 'sonia': 109, 'pain': 109, 'light': 109, 'auditions': 109, 'trinity': 109, 'violet': 109, 'drilling': 108, 'paid': 108, 'fills': 108, 'milking': 108, 'cameron': 108, 'bonnie': 108, 'harmony': 108, 'business': 108, 'gags': 108, 'charlotte': 107, 'met': 107, 'nappi': 107, 'vicky': 107, 'lonely': 107, 'stuffs': 107, 'moans': 106, 'cavanni': 106, 'shay': 106, 'cross': 106, 'harley': 106, 'selena': 106, 'season': 106, 'lots': 105, 'timer': 105, 'rodriguez': 105, 'backyard': 105, 'oh': 105, 'filmed': 105, 'angelica': 105, 'lopez': 105, 'vegas': 105, 'linares': 105, 'backseat': 105, 'clip': 104, 'jenaveve': 104, 'sapphic': 104, 'wifes': 104, 'mans': 104, 'hendrix': 104, 'erin': 104, 'ruined': 104, 'carmella': 104, 'charlie': 104, 'lela': 103, 'joins': 103, 'oils': 103, 'tryouts': 103, 'extremely': 103, 'bts': 103, 'cleaning': 103, 'jynx': 102, 'peach': 102, 'isabella': 102, 'smith': 102, 'lessons': 102, 'kayden': 102, 'torture': 102, 'brianna': 102, 'paris': 102, 'ray': 102, 'zoe': 101, 'natalie': 101, 'ocean': 101, 'joy': 101, 'mexican': 101, 'pigtails': 101, 'legal': 101, 'tanya': 101, 'topless': 101, 'sweetsinner': 101, 'avluv': 101, 'trash': 101, 'divine': 100, 'nurses': 100, 'anissa': 100, 'tastes': 100, 'soapy': 100, 'changing': 100, 'pm': 100, 'desire': 100, 'un': 100, 'rocco': 100, 'briana': 100, 'eye': 100, 'gal': 100, 'husbands': 100, 'dped': 100, 'seductive': 100, 'shop': 100, 'karter': 100, 'soft': 100, 'brittany': 100, 'dancer': 100}
wordList = []
for i in dict.keys():
    tup = (dict[i], i)
    wordList.append(tup)

dictSorted = sorted(wordList, reverse=True)



cloud_text = open('cloud_text.txt', 'w')
for i in range(100):
    # print dictSorted[i]
    for j in range(dictSorted[i][0]/100):
        print >> cloud_text, dictSorted[i][1]

cloud_text.close()
