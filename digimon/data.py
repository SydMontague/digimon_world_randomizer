# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

"""
Hard coded data values and binary offsets.
"""

lastPartnerDigimon = 0x41
lastNonfinishTech  = 0x39

types = {
            0x01 : 'DATA',
            0x02 : 'VACCINE',
            0x03 : 'VIRUS'
        }

levels = {
            0x01 : 'FRESH',
            0x02 : 'IN-TRAINING',
            0x03 : 'ROOKIE',
            0x04 : 'CHAMPION',
            0x05 : 'ULTIMATE'
        }

levelsByName = {
            'FRESH'         : 0x01,
            'IN-TRAINING'   : 0x02,
            'ROOKIE'        : 0x03,
            'CHAMPION'      : 0x04,
            'ULTIMATE'      : 0x05
        }

specs = {
            0x00 : 'FIRE',
            0x01 : 'BATTLE',
            0x02 : 'AIR',
            0x03 : 'EARTH',
            0x04 : 'ICE',
            0x05 : 'MECH',
            0x06 : 'FILTH'
        }

ranges = {
            0x01 : 'SHORT',
            0x02 : 'LARGE',
            0x03 : 'WIDE',
            0x04 : 'SELF'
        }

effects = {
            0x00 : 'NONE',
            0x01 : 'POISON',
            0x02 : 'CONFUSE',
            0x03 : 'STUN',
            0x04 : 'FLAT'
        }

techs = {
            0x00 : 'Fire Tower',
            0x01 : 'Prominence Beam',
            0x02 : 'Spit Fire',
            0x03 : 'Red Inferno',
            0x04 : 'Magma Bomb',
            0x05 : 'Heat Laser',
            0x06 : 'Inifinity Burn',
            0x07 : 'Meltdown',
            0x08 : 'Thunder Justice',
            0x09 : 'Spinning Shot',
            0x0A : 'Electric Cloud',
            0x0B : 'Megalo Spark',
            0x0C : 'Static Elect',
            0x0D : 'Wind Cutter',
            0x0E : 'Confused Storm',
            0x0F : 'Hurricane',
            0x10 : 'Giga Freeze',
            0x11 : 'Ice Statue',
            0x12 : 'Winter Blast',
            0x13 : 'Ice Needle',
            0x14 : 'Water Blit',
            0x15 : 'Aqua Magic',
            0x16 : 'Aurora Freeze',
            0x17 : 'Tear Drop',
            0x18 : 'Power Crane',
            0x19 : 'All Range Beam',
            0x1A : 'Metal Sprinter',
            0x1B : 'Pulse Laser',
            0x1C : 'Delete Program',
            0x1D : 'DG Dimension',
            0x1E : 'Full Potential',
            0x1F : 'Reverse Prog',
            0x20 : 'Poison Powder',
            0x21 : 'Bug',
            0x22 : 'Mass Morph',
            0x23 : 'Insect Plague',
            0x24 : 'Charm Perfume',
            0x25 : 'Poison Claw',
            0x26 : 'Danger Sting',
            0x27 : 'Green Trap',
            0x28 : 'Tremar',
            0x29 : 'Muscle Charge',
            0x2A : 'War Cry',
            0x2B : 'Sonic Jab',
            0x2C : 'Dynamite Kick',
            0x2D : 'Counter',
            0x2E : 'Megaton Punch',
            0x2F : 'Buster Dive',
            0x30 : 'Dynamite Kick v2',
            0x31 : 'Odor Spray',
            0x32 : 'Poop Spd Toss',
            0x33 : 'Big Poop Toss',
            0x34 : 'Big Rnd Toss',
            0x35 : 'Poop Rnd Toss',
            0x36 : 'Rnd Spd Toss',
            0x37 : 'Horizontal Kick',
            0x38 : 'Ult Poop Hell',
            0x39 : 'Horizontal Kick v2',
            0x3A : 'Blaze Blast',
            0x3B : 'Pepper Breath',
            0x3C : 'Lovely Attack',
            0x3D : 'Fireball',
            0x3E : 'Death Claw',
            0x3F : 'Mega Flame',
            0x40 : 'Howling Blaster',
            0x41 : 'Party time',
            0x42 : 'Electric Shock',
            0x43 : 'Abduction Beam',
            0x44 : 'Smiley Bomb',
            0x45 : 'Spnning Needle',
            0x46 : 'Spiral Twister',
            0x47 : 'Boom Bubble',
            0x48 : 'Sweet Breath',
            0x49 : 'Bit Bomb',
            0x4A : 'Deadly Bomb',
            0x4B : 'Drill Spin',
            0x4C : 'Electric Thread',
            0x4D : 'Energy Bomb',
            0x4E : 'Genoside Attack',
            0x4F : 'Giga Scissor Claw',
            0x50 : 'Dark Shot',
            0x51 : 'Pummel Whack',
            0x52 : 'Hand of Fate',
            0x53 : 'Dark Claw',
            0x54 : 'Aerial Attack',
            0x55 : 'Bone Boomerang',
            0x56 : 'Solar Ray',
            0x57 : 'Hydro Pressure',
            0x58 : 'Ice Blast',
            0x59 : 'Iga School Knife Throw',
            0x5A : 'Blasting Spout',
            0x5B : 'Fist of the Beast King',
            0x5C : 'Dark Network & Concert Crush',
            0x5D : 'Electro Shocker',
            0x5E : 'Meteor Wing',
            0x5F : 'Super Slap',
            0x60 : 'Nightmare Syndromer',
            0x61 : 'Frozen Fire Shot',
            0x62 : 'Poison Ivy',
            0x63 : 'Blue Blaster',
            0x64 : 'Scissor Claw',
            0x65 : 'Super Thunder Strike',
            0x66 : 'Spiral Sword',
            0x67 : 'Variable Darts',
            0x68 : 'Volcanic Strike',
            0x69 : 'Subzero Ice Punch',
            0x6A : 'Infinity Cannon',
            0x6B : 'Party time',
            0x6C : 'Party time',
            0x6D : 'Crimson Flare',
            0x6E : 'Glacial Blast',
            0x6F : 'Mail Strome',
            0x70 : 'High Electro Shocker',
            0x71 : 'Bubble',
            0x72 : 'Bubble',
            0x73 : 'Bubble',
            0x74 : 'Bubble',
            0x75 : 'Bubble',
            0x76 : 'Bubble',
            0x77 : 'Bubble',
            0x78 : 'Bubble'
            }

digimonIDFormat   = '<B'

rookies = ( 0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39 )

techIDFormat      = '<B'
animIDFormat      = '<B'

evoItemPatchOffset = 0x14CF5AFC
evoItemPatchValue  = 0x00
evoitemPatchFormat = '<B'

woahPatchOffset = 0x14D76EF4
woahPatchValue = 'Oh shit!'
woahPatchFormat = '<10s'

scriptOffsetInBinary = 0x13FD5809

chestItemFormat   = '<BB'

chestItemOffsets = (
            0x13FE3118, #706
            0x13FE6844,
            0x13FEE01E,
            0x13FEE02A,
            0x13FEE036,
            0x13FF4DE8,
            0x13FF4DF4,
            0x13FF6978,
            0x13FF6984,
            0x13FFA098,
            0x13FFD7BC,
            0x13FFE0F0,
            0x13FFF35C,
            0x14000EDC,
            0x14000EE8,
            0x14000EF4,
            0x14003398,
            0x140033A4,
            0x14005868,
            0x140073E8,
            0x140073F4,
            0x14008F7C,
            0x14021168,
            0x14021174,
            0x14022D04,
            0x14023624,
            0x14023630,
            0x14023F54,
            0x14023F60,
            0x14030964,
            0x140377A8,
            0x13FF58AA,
            0x13FF58B6,
            0x14038A04,
            0x13FFA508,
            0x14039338,
            0x140396CA,
            0x1403AEC4,
            0x1403AED0,
            0x1403AEDC,
            0x1403AEE8,
            0x14045424,
            0x1404A6DC,
            0x140539EC,
            0x140539F8,
            0x1405430C,
            0x14054318,
            0x14054324,
            0x1405836C,
            0x14058C9C,
            0x14067B7C,
            0x1406970C,
            0x14073334,
            0x14078F1C, #707
            0x14079848, #709
            0x14079854, #708
            0x14079860, #710
            0x1407986C, #711
            0x1407A178, #712
            0x1407A184, #713
            0x1407AA94, #700
            0x1407AAA0, #701
            0x1407AAAC, #702
            0x1407AAB8, #703
            0x1407BD46, #696
            0x1407BD52, #697
            0x1407BD5E, #698
            0x1407F430, #686
            0x1407FD54, #687
            0x14080688, #688
            0x14080FB4, #689
            0x140818F4, #690
            0x14081900, #691
            )

mapItemFormat = '<BB'

mapItemOffsets = (
            0x13FDD564,
            0x13FDD57A,
            0x13FDD590,
            0x13FDD596,
            0x13FDD59C,
            0x13FDD5B2,
            0x13FDD5C8,
            0x13FDDE88,
            0x13FDDE9E,
            0x13FDE7B4,
            0x13FDE7CA,
            0x13FDE7E0,
            0x13FDF0EC,
            0x13FDF102,
            0x13FDF118,
            0x13FDF12E,
            0x13FE0348,
            0x13FE035E,
            0x13FE0374,
            0x13FE038A,
            0x13FE1598,
            0x13FE2800,
            0x13FE3134,
            0x13FE314A,
            0x13FE43D8,
            0x13FE43EE,
            0x13FE43D8,
            0x13FE43EE,
            0x13FE5F28,
            0x13FE5F3E,
            0x13FE6860,
            0x13FE6876,
            0x13FE688C,
            0x13FE68A2,
            0x13FE7188,
            0x13FE719E,
            0x13FE71B4,
            0x13FE7AB4,
            0x13FE7ACA,
            0x13FE8D10,
            0x13FE8D26,
            0x13FE9FDC,
            0x13FE9FF2,
            0x13FEA008,
            0x13FEA01E,
            0x13FEA034,
            0x13FEA04A,
            0x13FEA060,
            0x13FEA076,
            0x13FEA08C,
            0x13FEA0A2,
            0x13FEA0B8,
            0x13FEA0CE,
            0x13FEA0E4,
            0x13FEA0FA,
            0x13FEA10E,
            0x13FEC444,
            0x13FEC45A,
            0x13FEC470,
            0x13FECD64,
            0x13FECD7A,
            0x13FECD90,
            0x13FED694,
            0x13FED6AA,
            0x13FED6C0,
            0x13FEDFC0,
            0x13FEDFD6,
            0x13FEDFEC,
            0x13FEE002,
            0x13FEE018,
            0x13FEF230,
            0x13FEF246,
            0x13FEF25C,
            0x13FEF230,
            0x13FEF246,
            0x13FEF25C,
            0x13FF72D0,
            0x13FF72E6,
            0x13FF72FC,
            0x13FF7C00,
            0x13FF7C16,
            0x13FF7C2C,
            0x13FF7C42,
            0x13FF852C,
            0x13FF8542,
            0x13FF8558,
            0x13FF856E,
            0x13FF8E68,
            0x13FF8E7E,
            0x13FF8E94,
            0x13FF8EAA,
            0x13FF9794,
            0x13FF8E7E,
            0x13FF97C0,
            0x13FF97D6,
            0x13FFA9D8,
            0x13FFA9EE,
            0x13FFAA04,
            0x13FFAA1A,
            0x13FFB320,
            0x13FFB336,
            0x13FFBC4C,
            0x13FFBC62,
            0x13FFBC78,
            0x13FFC584,
            0x13FFC59A,
            0x13FFCEA8,
            0x13FFCEBE,
            0x13FFCED4,
            0x1400C6B4,
            0x1400C6CA,
            0x1400C6E0,
            0x1400CFEC,
            0x1400D002,
            0x1400D018,
            0x1400D02E,
            0x1400D920,
            0x1400D936,
            0x1400D94C,
            0x1400E244,
            0x1400E25A,
            0x1400E270,
            0x1400EB9C,
            0x1400EBB2,
            0x1400EBC8,
            0x1400EBDE,
            0x1400FDE0,
            0x1400FDF6,
            0x1400FE0C,
            0x1400FE22,
            0x14010700,
            0x14010716,
            0x14011030,
            0x14011046,
            0x1401105C,
            0x14011072,
            0x14011968,
            0x1401197E,
            0x14012290,
            0x140122A6,
            0x140122BC,
            0x140134F4,
            0x1401350A,
            0x14014758,
            0x1401476E,
            0x14014784,
            0x1401479A,
            0x14015088,
            0x1401509E,
            0x140150B4,
            0x140162E4,
            0x140162FA,
            0x14016310,
            0x14016326,
            0x140190C8,
            0x1401AC6C,
            0x1401AC82,
            0x1401AC98,
            0x1401B594,
            0x1401B5AA,
            0x1401BEC4,
            0x1401BEDA,
            0x1401BEF0,
            0x1401C7FC,
            0x1401C812,
            0x1401C828,
            0x1401DA60,
            0x1401DA76,
            0x1401DA8C,
            0x1401E388,
            0x1401E39E,
            0x1401E3B4,
            0x1401ECB8,
            0x1401ECCE,
            0x1401ECE4,
            0x1401ECFA,
            0x1401FF14,
            0x1401FF2A,
            0x140251D8,
            0x1402B6FC,
            0x1402B712,
            0x1402B728,
            0x1402C92C,
            0x1402C942,
            0x1402C958,
            0x1402C92C,
            0x1402C942,
            0x1402C958,
            0x140312B8,
            0x140312CE,
            0x140312E4,
            0x140312FA,
            0x14031BF4,
            0x14031C0A,
            0x14031C20,
            0x14032530,
            0x14032546,
            0x1403255C,
            0x14032572,
            0x1403377C,
            0x14033792,
            0x140337A8,
            0x14034098,
            0x140340AE,
            0x140340C4,
            0x140340DA,
            0x14035C34,
            0x14035C4A,
            0x14035C60,
            0x14036578,
            0x1403658E,
            0x140365A4,
            0x140365BA,
            0x14039C8C,
            0x14039CA2,
            0x14010700,
            0x14010716,
            0x1403C144,
            0x1403C15A,
            0x1403CA6C,
            0x1403CA82,
            0x1403DCD0,
            0x1403E604,
            0x140413F8,
            0x1404140E,
            0x14041424,
            0x1404143A,
            0x14041D24,
            0x14041D3A,
            0x14041D50,
            0x1407B3EA,
            0x1407B400,
            0x1407B416,
            0x1407B42C,
            0x1407BD08,
            0x1407BD0E,
            0x1407BD14,
            0x1407BD2A,
            0x1407BD40
            )

recruitFormat = '<BxH'

# ( setTrigger(s), if trigger )
recruitOffsets = (
            ( ( 0x13FE9098, ), 0x140B4572 ) #204, Betamon
            ( ( 0x1405B8C6, ), 0x140B51F6 ) #205, Greymon
            ( ( 0x1407870A, ), 0x140B6668 ) #206, Devimon
            ( ( 0x14078706, ), 0x140B672A ) #207, Airdramon
            ( ( 0x140172B4, ), 0x140B47C0 ) #208, Tyrannomon
            ( ( 0x13FF572C, ), 0x140B4880 ) #209, Meramon
            ( ( 0x1407462E, ), 0x140B5A62 ) #211, Numemon
            ( ( 0x14078702, ), 0x140B6316 ) #212, MetalGreymon
            ( ( 0x13FED050, ), 0x140B598E ) #213, Mamemon
            ( ( 0x14047766, ), 0x140B644A ) #214, Monzaemon
            ( ( 0x140360A0, ), 0x140B563C ) #217, Gabumon
            ( ( 0x1400DD08, ), 0x140B4D44 ) #218, Elecmon
            ( ( 0x1402950A, ), 0x140B5B3A ) #219, Kabuterimon
            ( ( 0x14020E82, ), 0x140B54BA ) #220, Angemon
            ( ( 0x1403AAF4, ), 0x140B4BCE ) #221, Birdramon
            ( ( 0x1401F634, ), 0x140B4B26 ) #222, Garurumon
            ( ( 0x14040D62, ), 0x140B4A80 ) #223, Frigimon
            ( ( 0x140450AC, ), 0x140B57F4 ) #224, Whamon
            ( ( 0x13FE88DE, ), 0x140B46F0 ) #225, Vegiemon
            ( ( 0x1400BA8A, ), 0x140B68BE ) #226, SkullGreymon
            ( ( 0x1404CF3C, ), 0x140B617C ) #227, MetalMamemon
            ( ( 0x13FEECB6, ), 0x140B626E ) #228, Vademon
            ( ( 0x1400E6D4, ), 0x140B507C ) #231, Patamon
            ( ( 0x13FDE352, ), 0x140B432E ) #232, Kunemon
            ( ( 0x13FEE506, ), 0x140B4FB8 ) #233, Unimon
            ( ( 0x13FF1970, ), 0x140B5E82 ) #234, Ogremon
            ( ( 0x140396AE, ), 0x140B4C64 ) #235, Shellmon
            ( ( 0x13FEB63A, ), 0x140B43DC ) #236, Centarumon
            ( ( 0x13FF8016, ), 0x140B462E ) #237, Bakemon
            ( ( 0x13FF6454, ), 0x140B5568 ) #238, Drimogemon
            ( ( 0x1404FAD6, ), 0x140B6990 ) #240, Andromon
            ( ( 0x14052A78, ), 0x140B5DE0 ) #241, Giromon
            ( ( 0x13FDF54C, ), 0x140B60CE ) #242, Etemon
            ( ( 0x1400F912, ), 0x140B5132 ) #245, Biyomon
            ( ( 0x13FDEB8A, ), 0x140B4266 ) #246, Palmon
            ( ( 0x14000C4C, ), 0x140B4ED0 ) #247, Monochromon
            ( ( 0x14012926, ), 0x140B5F30 ) #248, Leomon
            ( ( 0x13FE08F0, ), 0x140B44C0 ) #249, Coelamon
            ( ( 0x14032EE2, ), 0x140B4E06 ) #250, Kokatorimon
            ( ( 0x1402A740, ), 0x140B5D3C ) #251, Kuwagamon
            ( ( 0x1403E082, ), 1403CE82, 1403D1B0 ), 0x140B58A4 ) #252, Mojyamon
            ( ( 0x13FFFADA, 0x14019D78, 0x140304F0, 14030EA6, 14031966, 14032338, 1404BD0E, 14074850 ), 0x140B63C6 ) #253, Nanimon
            ( ( 0x13FE6B50, ), 0x140B600A ) #255, Piximon
            ( ( 0x14077508, ), 0x140B67EF ) #256, Digitamamon
            ( ( 0x14096842, ), 0x140B53E6 ) #257, Penguinmon
            ( ( 0x13FE4B14, ), 0x140B573A ) #258, Ninjamon
            )

tokoItemFormat = '<BxBB'

tokoItemOffsets = (
            0x14071064,
            0x14071068,
            0x1407106C,
            0x14071070,
            0x14071074,
            0x14071078,
            )

learnMoveFormat = '<2B'

learnMoveOffsets = (
            0x14029E3E,     #bug
            0x13FE219A,     #seadra1
            0x13FE21E4,     #seadra2
            0x13FE2232      #seadra3
            )

checkMoveFormat = '<B'

checkMoveOffsets = (
            0x14029B32,     #bug
            0x13FE2192,     #seadra1
            0x13FE21DC,     #seadra2
            0x13FE222A      #seadra3
            )

techDataFormat           = '<H7B5xBx'

techDataBlockOffset      = 0x14D66DF8
techDataBlockSize        = 0x8C0
techDataBlockCount       = 0x79

techDataExclusionOffsets = (
            0x14D673B8,
            )
techDataExclusionSize    = 0x130

techTierListFormat       = '<8B'

techTierListBlockOffset  = 0x14C8E554
techTierListBlockSize    = 0x38
techTierListBlockCount   = 0x07

techTierListExclusionOffsets = (    #no exclusions in this block since it is tiny
            )
techTierListExclusionSize= 0x130

digimonDataFormat        = '<20sihh23Bx'

digimonDataBlockOffset   = 0x14D6E9DC       #start of digimon data block
digimonDataBlockSize     = 0x2A80           #total number of bytes
digimonDataBlockCount    = 0xB4             #number of digimon blocks

digimonDataExclusionOffsets = (
            0x14D6EB28, #in Devimon
            0x14D6F458, #in Biyomon
            0x14D6FD88, #in Piddomon
            0x14D706B8, #in Master Tyrannomon
            0x14D70FE8  #in Biyomon
            )
digimonDataExclusionSize = 0x130

evoToFromFormat          = '<11B'

evoToFromBlockOffset     = 0x14D6CE04       #start of evo to/from block
evoToFromBlockSize       = 0x3FB            #total number of bytes
evoToFromBlockCount      = 0x41

evoToFromExclusionOffsets = (
            0x14D6CF98, #in to Bakemon 3-4
            )
evoToFromExclusionSize = 0x130

itemDataFormat    = '<20sIHHb?2x'

itemDataBlockOffset     = 0x14D676C4       #start of item data block
itemDataBlockSize       = 0x1260           #total number of bytes
itemDataBlockCount      = 0x80             #number of item blocks

itemDataExclusionOffsets = (
            0x14D67CE8, #in Red Berry
            0x14D68618, #in Coral charm
            )
itemDataExclusionSize = 0x130

starterSetDigimonOffset  = ( 0x14D271C0, 0x14D271B8 )   #set digimon id
starterChkDigimonOffset  = ( 0x14CD1D24, 0x14CD1D44 )   #check digimon id to set tech
starterLearnTechOffset   = ( 0x14CD1D40, 0x14CD1D60 )   #tech to learn
starterEquipAnimOffset   = ( 0x14CD1D30, 0x14CD1D50 )   #animation to equip

