import os
from dotenv import load_dotenv

load_dotenv()

SUPPORTED_CHANNELS = (
    'ematerasu__',
    'furazek'
)

STREAMELEMENTS_MAPPING = {
    'ematerasu__': os.getenv('EMATERASU_STREAM_ELEMENT_ACCOUNT_ID'),
    'furazek': os.getenv('FURAZEK_STREAM_ELEMENT_ACCOUNT_ID')
}

TWITCH_ID_MAPPING = {
    'ematerasu__': '47911419',
    'furazek': '89709140',
    'EmaterasuBot': '896496342'
}

FURAZEK_EMOTES_LIST = (
    'TriKool', 'BRUHBRUH', 'pepeJAM', 'FloppaHey', 'Sadeg', 'VibePls', 'xd', 'SALAMI', 'catKISS', 'BRUHMM', 'TriDance', 'modCheck', 'zyzzBass', 'ABDULpls', 'AlienPls', 'HYPERCLAP', 'COPIUM', 'TwitchTV', 
    'catJAM', 'witamCieKolezanko', 'blobDance', 'Bedge', 'GIGACHAD', 'BOOBA', 'Stab', 'gdzietamuza', 'COCKA', 'jasperSmiech', 'jasperMuza', 'Madeg', 'MmmHmm', '5Head', 'TROLL', 'WideDude', 'xD', 'whotBass', 
    '2Head', 'FeelsOldMan', 'peepoNerd', 'SmileW', 'PepeCringe', 'jasperPompki', 'pepeW', 'peepoJAMMER', 'Flushge', 'Szarpanina', 'jasperKiss', 'pepeVIXA', 'Popoga', 'Tusiejebnij', 'okge', 'PogO', 'wuda', 
    'widepeepoGlad', 'cmonBrug', 'OOOO', 'Chatting', 'Okayge', 'FIRE', 'Zamieszki', 'LIKE', 'HarambeMLADY', 'SUSSY', 'lebronJAM', 'DogO', 'PykPykPyk', 'jasperWtopa', 'jasperJAMMER', 'peepoAwesome', 'demonzX', 
    'peepoShy', 'DooooooooogLookingSussyAndCute', 'mamon', 'HarambeGun', 'Glumlenie', 'dymanko', 'kac', 'zapierdol', 'HarambeSalute', 'CatJAM2', 'rockstar', 'EBLAN', 'Kretyn', 'EZY', 'peepoDJ', 'lodzik', 'Starege', 
    'peepoSadCat', 'Gambage', 'sick', 'DIESOFCRINGE', 'boxdelPls', 'Hejka', 'Muted', 'jasperSad', 'HmmBeg', 'Wokege', 'jasperPyk', 'peepi', 'kagjagfi745692874568734268yiuagdhvkuai7yq34gakyugt4rai7w34kgti7a3gtri7a6tweurgtiq3gt8iytiy7yr7kuayer', 
    'BatChesting', 'harambeWave', 'xnfurazek', 'JasperVixa', 'kochamfurazka', '60', 'jasperL', 'bazylKretyn', 'bazylLodzik', 'bazylBedge', 'Hmm', 'arquelCosplay', 'fifka', 'MORIS', 'cpunDance', 'paluszek', 'okok', 'papa', 'Mamm0nSad', 'oklaski', 
    'spadaj', 'okurwaalesmieszne', 'bork', 'BrugJam', 'czaty', 'h2p_ygus', 'ZPASTOREM', 'classic', 'GIGA60', 'brugHappy', 'brugSad', 'brugEZ', 'FurazekWuda', 'whot', 'wideVibe', 'furazekChlanie', 'brugJam', 'kissahomie', 'Vibe', 'meczennik', 
    'furHappy', 'ZGODA', 'bazylGineer', 'ZJEBINDUSTRIES', 'niechcemisie', 'paulinabije', 'ok', 'ZEZJEBEM', 'aha', 'JasperWTF', 'cypekD', 'WOMEN', 'aktimelek', 'widepeepoMASTURBATION77769420GANGSHITNOMOREFORTNITE19DOLLERFORTNITECARD', 'NOOOO', 
    'okurwa', 'praca', 'szalom', 'HarambeEZ', 'Dance', 'mitoman', 'jasperAwantura', 'jupijej', 'lezkawoku', 'Spierdalaj', 'idiota', 'nieuczBASS', 'essa', 'ZMERGHANIM', 'witom', 'japierdole', 'pierdoli', 'jasperTragedia', 'jasperAktywacja', 
    'pierdolsie', 'trup', 'HAHAHA', 'DEBIL', 'oho', 'SZOK', 'ZDZIWKO', 'Clueless', 'Rage', 'halo', 'mad', 'jamm', 'pogg', 'heyy', 'hehe', 'xdddd', 'flushedCat', 'deruki', 'aimstar', 'alegowno', 'Aware', 'dyniuh', 'NPC', 'peepoVanish', 'ZTIGEREM', 
    'ochujeje', 'piesek', 'hura', 'chujwie', 'jasperFajka', 'Ukrainiec', 'aok', 'jasperCzilera', 'jasperokurwa', 'jasperUsmiech', 'gituwa', 'SmokeTime', 'HUH', 'GAMBA', 'jasperSleeper', 'zazero', 'Cheergi', 'jasperSerduszko', 'dobani', 'xqcTake', 
    'gratulujemuzgukretynie', 'EDM', 'kerfus', 'Despairge', 'jasperZOOM', 'jasperBoobsy', 'beka', 'Gagrige', 'VeryPog', 'jasperNerd', 'jasperSTARE', 'jasperGarda', 'pajac', 'jasperLOKIETA', 'jasperPerkusja', 'jasperRockstar', 'jasperHey', 'jasperCoomer', 
    'slejH', 'FuckingYourMom2', 'jasperMLADY', 'wypierdalaj', 'Wyjebane', 'xdders', 'Heartgers', 'WICKED', 'Nerd', 'auu', 'jasperSUSSY', 'PetTheFurazek', 'jezykJAM', 'xqcTWISTED', 'rekinodtylu', ':0', 'rambo', 'medyk', 'Comfi', 'Cockgers', 
    'stopbeingMean', 'ppLove', 'jasperPaluszek', 'Hmmm', 'sonic', 'peepoSit', 'rybsonVibe', 'Jamgers', 'WorryRun', 'padaczka', 'peepochujmontaniewgardlo', 'tutorial', 'catRose', 'verySadge', 'WHY', 'sadWankge', 'SadgeJAM', 'pepeLost', 'Eternalsleepgers', 
    'jasperWakawaka', 'Aloo', 'cpun', 'ewroniak', 'pirateJAM', 'peepoSnow', 'xddd', 'xdd', 'banned', ':d', 'fikolek', 'przemarsz', 'ahha', 'xqcCheer', 'Excitedgers', 'Wavegers', 'Dabgers', 'Praygers', 'Drinkgers', 'Notegers', 'Okaygers', 'Thinkgers', 
    'THISgers', 'Gymgers', 'SlowClapgers', 'Plsgers', 'Realization', 'peepoHappyLove', 'peepoDetective', 'DiscoPajac', 'zEWRONEM', 'IKEA', 'TSSK', 'Tssk', 'BURATINO', 'tatozajebiscie', 'psejebane', 'Chill', 'FullTimeStreaming', ':3', 'shyygers', 
    'WEEBSDETECTED', 'CatNum', 'kok', 'yoooo', 'Zjebek', 'pupu', 'cozyCat', 'CatNotLikeThisMeow', 'meow', 'catSad', 'CuteDoggo', 'MADdog', 'VeryDog', 'bruuuuuuuuuuuuuuuuuuuuuuuuh', 'SENTINO', 'Pepespitting', 'waaa', 'Saved', 'Lovegers', 'Shruge', 
    'zjebindustries', 'prosilemcie', 'okgi', 'pepeGuitar', 'NOOOYOUCANT', 'Moodge', 'Stronge', 'SaguiPls', 'yawN', ':))', 'Hmmge', 'jasperJagaJaga', 'MADcat', 'catDrive', 'makowiec', 'lecimyrp', 'cysterna', 'CoffeeTime', 'ESKA', 'catPunch', 'blushCat', 
    'SadCat', 'catWiggle', 'CatO', 'WideBoris', 'piksele', 'Fiddy', 'Listening', 'gumpy', 'NOWAY', 'SHTO', 'MammonTlumaczenie', 'aha2', 'rat', 'samica', 'cpunDance2', 'lol', 'jasperDymy', 'BIKE', 'superstream', 'SaguiPls2', 'Dawid', 'TAKZROBIMY', 'miska', 
    'BrugWhite', 'kacci', 'gucci', 'taniec', 'cpunDance3', 'Taniec', 'kapitan', 'donowall', 'mion', 'BrugPoint', 'Blocked', 'peepoPog', 'TriTasty', 'emiruVibe', 'paranoja', 'yo', 'czolgistazplocka', 'loudzik', 'MadgeLate', 'xpp', 'mhm', 'CATBOOBS',
    'posluchajdzieciaku', 'gucciGang', 'smalcci', 'mamonni', 'guciobardzohapi', 'postrimku', 'Skateparkge', 'HUHH', 'stareCat', 'koklick', 'BASED', 'sigma', 'catEat', 'ModCheck', 'MonkeKiss', 'Waiting', 'emiruDance', 'whoAsked', 'peepoHey', 
    'hoSway', 'RobloxDance', 'POGGIES', 'clapped', 'kuleczki', 'Allahgers', 'Inshallah', 'jasperOOO', 'jasperPIFKO', 'wideDvaAss', 'STUCK', 'furrazi', 'jasperMiensko', 'YOURMOM', 'ReallyMad', 'RAGEY', 'PoliceCHASE', 'VIP', 'Applecatrun', 
    'gucioCo', 'gucioPls', 'ematerasu', 'RuszSieFurazek', 'rainbowPls', 'NODDERS', 'zultakartka', 'czerwonakartka', 'veryCat', 'plonk', 'LETHIMCOOK', 'NOWAYING', 'BUSSERS', 'plink', 'OneGuy', 'actually', 'FLASHBANG', 'catPls', 'WOOW', 
    'tadimason', 'NPCing', 'catJAMPARTY', 'duckass', 'mlem', 'THAT', 'SNIFF', 'FURAZEK', 'TheVoices', 'ratunku', 'catsittingverycomfortablearoundacampfirewithitsfriends', 'MyHonestReaction', 're', 'IveGonePastThePointOfInsanity', 'aledobre',
    'TookANap', 'StoryTime', 'SLORPGLORPIN', 'plinkge', 'catSleep', 'please', 'hiheyhello', 'jasperGadget', 'dziadyga', 'pillow', 'LEKI', 'brugBike2', 'AINTNOWAY', 'AnySubGiftersInChat', 'aha3', 'furazekFuck', 'aha5', 'aha4', 'jasperRADOSC', 
    'taktak', 'furazekKiss', ':00', 'Teatimegers', 'plunk', 'jasperNanana', 'foxsittingverycomfortablearoundacampfirewithitsfriends', 'UltraMad', 'jasperRap', 'edenOK', 'WOO', 'SalamAlejkum', 'aha7', 'aha6', 'FrogDance', 'MMEOWDY', 'wuh', 'Sure', 
    'ohstop', 'buh', 'DIDSOMEONESAYMEOW', 'Scared', 'PLEASE', 'VAR', 'zoltepapiery', 'mitosis', 'jasperModlitwa', 'jasperKobra', 'aha10', 'Gladge', 'suetolog', 'wesele', 'PikachuRave', 'serduszko', 'NIEWSPIERAM', 'cosiekurwagapisz', 'ahaspoko', 
    'forma', 'peepoLeave', 'NOTED', 'NewOutfit', 'GoodNight', 'HUGS', 'THIS', 'mods', 'jasperRADOSC2', 'jasperVixapol', 'jasperBania', 'mammonDance', 'xgamerekzrana', 'IMDEAD', 'pjpj', 'rawr', 'egirlStop', 'HutaoDance', 'alewtopa', 'cpunJam', 'vreypgo', 
    'rowerek', 'plank', 'JasperKlask', 'jasperFAJURA', 'ostatniaszansa', 'legless', 'grypsik', '!sr', 'aha11', 'mamm0nPolicja', 'notListening', 'xddShrug', 'imNOTcrying', 'ThugShaker'
)

BANNED_VIDEOS = (
    'nUCT0YeNCgE', 'rcVb6l4TpHw', 'k7WnXmOFR8I', 'h6V74FuW4Ac', '8ddRoYK4X80', 'NjD0H4eBfng',
    '2EqINpSNOPM', 'uxZoH0H74HI', '6BzWjuDK_kA', 'pceHY7rkiTg', 'Y2qsl0z-NBk', 'CWmI_4SkrD0',
    'myIvgyeVXMo', 'YG4iTGjuoKw', 'scXlu4staJA', 'YyUGPRRB42A'
)

SONG_REQUEST_SAVE_PLAYLISTS = {
    'eska': 'https://www.youtube.com/watch?v=7C-Ky2D2lZE',
    'nightclub': 'https://www.youtube.com/watch?v=MehaUz9s5MY',
    'techno': 'https://www.youtube.com/watch?v=w1lc8LKgLIY',
    'rap': 'https://www.youtube.com/watch?v=a0pexLfjn-s',
    'disco': 'https://www.youtube.com/watch?v=VodMgPR74UQ',
    'phonk': 'https://www.youtube.com/watch?v=phuY3ucYk88',
}

