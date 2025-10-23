from writing import openFile, writeSplit, closeFile
from data import geyser_data_original, data_original
#from init_debug import *
from init import *
import random

#technical stuff
geyser_data = geyser_data_original.copy()
data = data_original.copy()
old_split = None
double_split = 0
splits = 0
counter = 0
written_splits = 0

#meta_data
splits_list = []
if seed == 0:
    seed = random.randint(1, 9999999999999999)
random.seed(seed)
power_cells = 0
available_orbs = 337
if exclude_scout_flies:
    scout_flies = {"GR": 7, "SV": 7, "FJ": 7, "MI": 0, "SB": 7, "FC": 7, "RV": 7, "PB": 7, "LPC": 7, "BS": 7, "MP": 7, "VC": 7, "SC": 7, "SM": 0, "LT": 7, "C": 0}
else:
    scout_flies = {"GR": 0, "SV": 0, "FJ": 0, "MI": 0, "SB": 0, "FC": 0, "RV": 0, "PB": 0, "LPC": 0, "BS": 0, "MP": 0, "VC": 0, "SC": 0, "SM": 0, "LT": 0, "C": 0}
orbs = {"GR": 50, "SV": 50, "FJ": 99, "MI": 0, "SB": 138, "FC": 0, "RV": 50, "PB": 0, "LPC": 200, "BS": 200, "MP": 0, "VC": 50, "SC": 185, "SM": 0, "LT": 0, "C": 0}

#prepare file
file = openFile(seed)

#randomizer stuff
if exclude_misc_items:
    precursor_door = True
else:
    precursor_door = False

#geyser
while power_cells < 4:
    write = True

    rnd = random.randint(0, len(geyser_data) - 1)

    item = geyser_data[rnd]
    item_type = item.split("|")[1].split("]")[0]

    if item_type == "SF":
        scout_flies["GR"] += 1
        if exclude_scout_flies:
            write = False
            geyser_data.pop(rnd)

    if item == "[GR|PC] Free 7 Scout Flies":
        if scout_flies["GR"] < 7:
            write = False

    if item == "[GR|MISC] Open The Locked Precursor Door":
        if exclude_misc_items:
            write = False
            geyser_data.pop(rnd)
        else:
            precursor_door = True

    if item == "[GR|PC] Open The Precursor Door" or item == "[GR|PC] Climb Up The Cliff":
        if not allow_precursor_door_skip and not precursor_door:
            write = False

    if write:
        if item_type == "PC":
            power_cells += 1
        splits_list.append(geyser_data[rnd])
        written_splits += 1
        geyser_data.pop(rnd)

#rest of game
if exclude_misc_items:
    exclude_warp_buttons = True
#hub 1
if exclude_misc_items:
    yakows = 5
    mirror = True
    mirrors = 5
    temple_door = True
    temple_elevator = False
    force_plant_boss = False
    plant_boss = True
    blue_eco = False
    sentinel_cannon = True
    seagulls = 3
    egg = True
    eco_blockers = 5
    misty = False
    muse = True
    misty_cannon = True
    balloon_lurkers = True
    fc_cell = False
else:
    yakows = 0
    mirror = False
    mirrors = 0
    temple_door = False
    temple_elevator = False
    force_plant_boss = False
    plant_boss = False
    blue_eco = False
    sentinel_cannon = False
    seagulls = 0
    egg = False
    eco_blockers = 0
    misty = False
    muse = False
    misty_cannon = False
    balloon_lurkers = False
    fc_cell = False
#hub 2
blue_button = False
if exclude_misc_items:
    flying_lurkers = 3
    moles = 4
    race = True
    plants = True
    purp_rings = True
    blue_rings = True
    ring_cell = False
    chamber_opened = True
    boulder_one = True
    boulder_two = True
    boulder_three = True
    boulder_four = True
    ambush = True
    klaww_boulder = False
    klaww = False
    bomb_lurker = False
    force_mp_cell = False
    mp_cell = False
else:
    flying_lurkers = 0
    moles = 0
    race = False
    plants = False
    purp_rings = False
    blue_rings = False
    ring_cell = False
    chamber_opened = False
    boulder_one = False
    boulder_two = False
    boulder_three = False
    boulder_four = False
    ambush = False
    klaww_boulder = False
    klaww = False
    bomb_lurker = False
    force_mp_cell = False
    mp_cell = False
if allow_on_foot_basin:
    basin = True
else:
    basin = False
#hub 3
red_button = False
if exclude_misc_items:
    crater_crate = True
    force_miners_cell = False
    miners_count = 0
    snowy_cells = 0
    snowy_flut = False
    snowy = False
    snowy_crate = False
    glacier_troops = 3
    blockers = 13
    yellow_eco = False
    snowy_gate_open = False
    gnawing_lurkers = 9
    crystals = 5
    oranges = True
    citadel = False
    citi_button = False
    force_lt_cell = False
    lt_cell = False
    citadel_stairs = 0
else:
    crater_crate = False
    force_miners_cell = False
    miners_count = 0
    snowy_cells = 0
    snowy_flut = False
    snowy = False
    snowy_crate = False
    glacier_troops = 0
    blockers = 0
    yellow_eco = False
    snowy_gate_open = False
    gnawing_lurkers = 0
    crystals = 0
    oranges = False
    citadel = False
    citi_button = False
    force_lt_cell = False
    lt_cell = False
    citadel_stairs = 0

while len(data) > 0:
    counter += 1
    write = True

    if power_cells < 20 and not allow_fcs: #prevent fcs
        rnd = random.randint(0, 86 - splits)
    elif not fc_cell: #end of fc softlock
        rnd = random.randint(0, 99 - splits)
    elif power_cells < 45 and not allow_boulder_skip: #prevent bs
        rnd = random.randint(0, 177 - splits)
    elif not bomb_lurker: #bomb lurker softlock
        rnd = random.randint(0, 202 - splits)
    elif power_cells < 72 and not allow_lts: #prevent lts
        rnd = random.randint(0, 282 - splits)
    else:
        rnd = random.randint(0, len(data) - 1)

    item = data[rnd]
    item_type = item.split("|")[1].split("]")[0]
    item_area = item.split("|")[0][1:]

    if exclude_misc_items and item_type == "MISC":
        write = False
        splits += 1
        data.pop(rnd)
    if exclude_scout_flies and item_type == "SF":
        if item_area == "MI" and not misty:
            pass
        elif item_area == "SM" and not snowy:
            pass
        else:
            splits += 1
            data.pop(rnd)
        write = False

    #general
    #buttons
    if "Warp Gate Button" in item and exclude_warp_buttons:
        write = False
        if not exclude_misc_items:
            data.pop(rnd)
            splits += 1

    #geyser rock
    #door
    if item == "[GR|MISC] Open The Locked Precursor Door":
        if precursor_door:
            if not exclude_misc_items:
                data.pop(rnd)
                splits += 1
            write = False

    #sandover village
    #yakows
    if item_area == "SV" and item_type == "MISC":
        yakows += 1
    if item == "[SV|PC] Herd The Yakows Into Their Pen":
        if yakows < 5:
            write = False

    #forbidden jungle
    #mirrors
    if item == "[FJ|MISC] Destroy Mirror":
        mirror = True
    if item == "[FJ|MISC] Connect A Mirror":
        if not mirror:
            write = False
        else:
            mirrors += 1
            item = item + " (" + str(mirrors) + ")"
    if item == "[FJ|PC] Connect The Eco Beams":
        if mirrors < 5:
            write = False
        else:
            mirrors += 1
    if item == "[SV|PC] Bring 90 Orbs To The Mayor":
        if mirrors == 5:
            write = False
    #temple deload
    if item == "[FJ|PC] Get To The Top Of The Temple":
        temple_elevator = True
    if item in ["[FJ|PC] Find The Blue Vent Switch", "[FJ|MISC] Beat Plant Boss"]:
        if not allow_temple_deload and not temple_elevator:
            write = False
        #temple leave early
        elif item == "[FJ|PC] Find The Blue Vent Switch":
            blue_eco = True
            if not allow_leaving_temple_early:
                if not plant_boss:
                    force_plant_boss = True
    #plant boss
    if item == "[FJ|MISC] Beat Plant Boss":
        if plant_boss:
            write = False
            if not exclude_misc_items:
                data.pop(rnd)
                splits += 1
        if not allow_temple_skip and not blue_eco:
            write = False
        elif not plant_boss:
            plant_boss = True
    if item == "[FJ|PC] Defeat The Dark Eco Plant":
        if not plant_boss:
            write = False
    #temple door skip
    if item == "[FJ|MISC] Open Locked Temple Door":
        temple_door = True
    if item == "[FJ|PC] Open The Locked Temple Door":
        if not allow_locked_temple_skip and not temple_door:
            write = False

    #sentinel beach
    #flut flut
    if item == "[SB|PC] Push The Flut Flut Egg Off The Cliff":
        snowy_flut = True
    #cannon
    if item == "[SB|MISC] Stop The Shooting Cannon":
        if not allow_tower_climb and not blue_eco:
            write = False
        else:
            sentinel_cannon = True
    if item == "[SB|PC] Launch Up To The Cannon Tower":
        if not sentinel_cannon:
            write = False
    #seagulls
    if item == "[SB|MISC] Chase Seagulls 1st Time":
        seagulls += 1
    if item == "[SB|MISC] Chase Seagulls 2nd Time":
        if seagulls < 1:
            write = False
        else:
            seagulls += 1
    if item == "[SB|MISC] Chase Seagulls 3rd Time":
        if seagulls < 2:
            write = False
        else:
            seagulls += 1
    if item == "[SB|PC] Chase The Seagulls":
        if seagulls < 3:
            write = False
    #flut flut egg
    if item == "[SB|PC] Push The Flut Flut Egg Off The Cliff":
        if not egg:
            write = False
    if item == "[SB|MISC] Push Flut Flut Egg":
        egg = True
    #eco blockers
    if item_type == "MISC" and "Harvester" in item:
        eco_blockers += 1
    if item == "[SB|PC] Unblock The Eco Harvesters":
        if eco_blockers < 5:
            write = False

    #misty island
    if item_area == "MI":
        if not misty:
            write = False
    if item == "[FJ|PC] Catch 200 Pounds Of Fish":
        misty = True
        scout_flies["MI"] = 7
    #muse
    if item == "[MI|PC] Catch The Sculptor's Muse":
        if not muse:
            write = False
    if item == "[MI|MISC] Catch Muse":
        if misty:
            muse = True
    #cannon
    if item == "[MI|PC] Stop The Cannon":
        if not misty_cannon:
            write = False
    if item == "[MI|MISC] Stop The Shooting Cannon":
        if misty:
            misty_cannon = True
    #balloon lurkers
    if item == "[MI|PC] Destroy The Balloon Lurkers":
        if not balloon_lurkers:
            write = False
    if item == "[MI|MISC] Stop The Balloon Lurkers":
        if misty:
            balloon_lurkers = True

    #fire canyon
    if item_area == "FC" and item_type == "SF":
        if power_cells < 20 and not fc_cell:
            write = False
    if item == "[FC|PC] Reach The End Of Fire Canyon":
        if fc_cell:
            write = False
            data.pop(rnd)
            splits += 1
        else:
            fc_cell = True
            if exclude_warp_buttons:
                blue_button = True

    #rock village
    #button
    if item == "[RV|MISC] Press The Blue Warp Gate Button" or exclude_warp_buttons:
        blue_button = True
        basin = True

    #precursor basin
    if item_area == "PB":
        if not basin:
            write = False
    #flying lurkers
    if item_type == "MISC" and "Flying Lurker" in item:
        if blue_button:
            flying_lurkers += 1
            if flying_lurkers == 4:
                write = False
                if not exclude_misc_items:
                    data.pop(rnd)
                    splits += 1
        else:
            write = False
    if item == "[PB|PC] Catch The Flying Lurkers":
        if flying_lurkers < 3:
            write = False
    #moles
    if item == "[PB|MISC] Herd A Mole":
        if basin:
            moles += 1
    if item == "[PB|PC] Herd The Moles Into Their Hole":
        if moles < 4:
            write = False
        else:
            moles += 1
    if item == "[RV|PC] Bring 90 Orbs To The Geologist":
        if moles == 4:
            write = False
    #race
    if item == "[PB|MISC] Beat The Record Time":
        if not allow_on_foot_race and not blue_button:
            write = False
        elif write:
            race = True
    if item == "[PB|PC] Beat The Record Time On The Gorge":
        if not race:
            write = False
        else:
            race = False
    if item == "[RV|PC] Bring 90 Orbs To The Gambler":
        if race:
            write = False
    #plants
    if item == "[PB|MISC] Cure The Plants":
        if not blue_button:
            write = False
        else:
            plants = True
    if item == "[PB|PC] Cure Dark Eco Infected Plants":
        if not plants:
            write = False
    #rings
    if item == "[PB|MISC] Beat The Purple Rings":
        if not basin:
            write = False
        else:
            purp_rings = True
    if item == "[PB|PC] Navigate The Purple Precursor Rings":
        if not purp_rings:
            write = False
        else:
            ring_cell = True

    if item == "[PB|MISC] Beat The Blue Rings":
        if not ring_cell or not blue_button:
            write = False
        else:
            blue_rings = True
    if item == "[PB|PC] Navigate The Blue Precursor Rings":
        if not blue_rings:
            write = False

    #lpc
    #button clip
    if item == "[LPC|MISC] Open The Sunken Chamber":
        chamber_opened = True
    if item == "[LPC|PC] Raise The Chamber":
        if not allow_button_clip and not chamber_opened:
            write = False
    
    #boggy swamp
    #boulders
    if item == "[BS|MISC] Shoot 1st Boulder":
        boulder_one = True
    if item == "[BS|PC] Break The 1st Tether On The Zeppelin":
        if not boulder_one:
            write = False
    
    if item == "[BS|MISC] Shoot 2nd Boulder":
        boulder_two = True
    if item == "[BS|PC] Break The 2nd Tether On The Zeppelin":
        if not boulder_two:
            write = False

    if item == "[BS|MISC] Shoot 3rd Boulder":
        boulder_three = True
    if item == "[BS|PC] Break The 3rd Tether On The Zeppelin":
        if not boulder_three:
            write = False

    if item == "[BS|MISC] Shoot 4th Boulder":
        boulder_four = True
    if item == "[BS|PC] Break The 4th Tether On The Zeppelin":
        if not boulder_four:
            write = False
    #ambush
    if item == "[BS|MISC] Defeat Ambush":
        ambush = True
    if item == "[BS|PC] Deafeat The Lurker Ambush":
        if not ambush:
            write = False

    #mountain pass
    #klaww boulder
    if item == "[RV|MISC] Lift Boulder":
        if power_cells < 45 or not blue_button:
            write = False
        else:
            if klaww_boulder:
                write = False
                if not exclude_misc_items:
                    data.pop(rnd)
                    splits += 1
            else:
                klaww_boulder = True
    #klaww
    if item == "[MP|MISC] Stop Klaww":
        if not klaww_boulder and not allow_boulder_skip:
            write = False
        else:
            if klaww:
                write = False
                if not exclude_misc_items:
                    data.pop(rnd)
                    splits += 1
            else:
                klaww = True
    if item_area == "MP":
        if not klaww:
            write = False
    #bomb lurker
    if item == "[MP|MISC] Stop The Bomb Lurker":
        if bomb_lurker:
            write = False
            if not exclude_misc_items:
                data.pop(rnd)
                splits += 1
        elif write or exclude_misc_items:
            bomb_lurker = True
            if exclude_warp_buttons:
                red_button = True
            #backwards mp
            if not allow_backwards_mp:
                if not mp_cell:
                    force_mp_cell = True
    #secret cell
    if item == "[MP|PC] Find The Hidden Power Cell":
        if not yellow_eco:
            if not allow_tree_stalagmite_hops and not (bomb_lurker and allow_backwards_mp):
                write = False
    #end of mp cell
    if item == "[MP|PC] Reach The End Of The Mountain Pass":
        if mp_cell:
            write = False
            data.pop(rnd)
            splits += 1

    #volcanic crater
    #button
    if item == "[VC|PC] Bring 90 Orbs To The Miners":
        if (miners_count == 2 and not red_button) or miners_count == 4:
            write = False
    if item == "[VC|MISC] Press The Red Warp Gate Button":
        red_button = True
    #secret cell
    if item == "[VC|MISC] Destroy The Hidden Crate":
        crater_crate = True
    if item == "[VC|PC] Find The Hidden Power Cell":
        if not crater_crate:
            write = False

    #snowy
    if item_area == "SM":
        if not snowy:
            write = False
    if snowy_cells > 1:
        snowy = True
    #dumb one in a million fix
    if red_button and not snowy and double_split > 200:
        force_miners_cell = True
    #frozen crate
    if item == "[SM|MISC] Destroy Frozen Crate":
        if snowy:
            snowy_crate = True
    if item == "[SM|PC] Open The Frozen Crate":
        if not snowy_crate:
            write = False
    #glacier troops
    if item_type == "MISC" and "Glacier Troop" in item:
        if snowy:
            glacier_troops += 1
    if item == "[SM|PC] Stop The 3 Lurker Glacier Troops":
        if glacier_troops < 3:
            write = False
    #blockers
    if item_type == "MISC" and "Blocker" in item:
        if snowy:
            blockers += 1
    if item == "[SM|PC] Deactivate The Precursor Blockers":
        if blockers < 13:
            write = False
    #yellow eco
    if item == "[SM|PC] Find The Yellow Vent Switch":
        if snowy:
            yellow_eco = True
            if exclude_misc_items:
                snowy_crate = True
    #fort gate skip
    if item == "[SM|PC] Open The Lurker Fort Gate":
        if snowy:
            snowy_gate_open = True
    if item in ["[SM|PC] Get Through The Lurker Fort", "[SM|SF] On Top Of Fort Tower", "[SM|SF] On Top Of Fort"]:
        if not allow_fort_gate_skip and not snowy_gate_open:
            write = False
        elif exclude_scout_flies:
            scout_flies["SM"] = 7

    #spider cave
    #lurkers
    if item_area == "SC" and item_type == "MISC" and "Lurker" in item:
        gnawing_lurkers += 1
    if item == "[SC|PC] Shoot The Gnawing Lurkers":
        if gnawing_lurkers < 9:
            write = False
    #crystals
    if item_type == "MISC" and "Crystal" in item:
        crystals += 1
    if item == "[SC|PC] Destroy The Dark Eco Crystals":
        if crystals < 5:
            write = False

    #lava tube
    #oranges
    if item == "[LT|MISC] Destroy Oranges":
        if oranges:
            write = False
            if not exclude_misc_items:
                data.pop(rnd)
                splits += 1
        else:
            oranges = True
            
    #end of lava tube
    if item == "[LT|PC] Reach The End Of The Lava Tube":
        if lt_cell:
            write = False
            data.pop(rnd)
            splits += 1
        elif write:
            lt_cell = True
            escape_citadel = True
            if exclude_warp_buttons:
                citi_button = True
                
    if item_area in ["LT", "C"] and not (item == "[LT|SF] 1st Scout Fly" or item == "[LT|SF] 2nd Scout Fly"): 
        if not allow_oranges_skip and not oranges:
            write = False
        elif not lt_cell:
            force_lt_cell = True

    #citadel
    if item == "[LT|MISC] Press Citadel Warp Gate Button":
        citi_button = True
    if item_area == "C":
        if exclude_warp_buttons:
            citi_button = True
    if (allow_early_citadel or lt_cell) and citi_button:
        citadel = True
    if item_area == "C":
        if not citadel:
            write = False
    #citadel skip
    if item in ["[C|PC] Free The Yellow Sage", "[C|PC] Free The Red Sage", "[C|PC] Free The Blue Sage"]:
        if write:
            citadel_stairs += 1
    if item in ["[C|SF] Top Of Rotating Tower", "[C|PC] Free The Green Sage"]:
        if not allow_citadel_skip and not citadel_stairs == 3:
            write = False
        elif exclude_scout_flies:
            scout_flies["C"] = 7

    #scout flies
    if item_type == "SF":
        if item_area in ["FC", "PB", "MP", "LT"] or item == "[MI|SF] On Zoomer Ramps":
            if scout_flies[item_area] >= 6:
                write = False
                scout_flies[item_area] += 1
                if not exclude_scout_flies:
                    data.pop(rnd)
                    splits += 1
        if write:
            scout_flies[item_area] += 1

    if item.split("]")[1] == " Free 7 Scout Flies":
        if scout_flies[item_area] < 7:
            write = False

    #orbs
    #handle orb count
    if item_type == "PC" and "Bring 90 Orbs" in item:
        if available_orbs < 90:
            write = False
        elif write:
            available_orbs -= 90
    if item_type == "PC" and "Bring 120 Orbs" in item:
        if available_orbs < 120:
            write = False
        elif write:
            available_orbs -= 120

    #start (50 + 50 + 138 + 99 = 337)
    #sentinel beach
    if allow_tower_climb or blue_eco:
        if orbs["SB"] == 138:
            orbs["SB"] += 12
            available_orbs += 12
    #forbidden jungle
    if temple_elevator or (allow_temple_deload and (blue_eco or plant_boss)):
        if orbs["FJ"] == 99:
            orbs["FJ"] += 26
            available_orbs += 26
    if blue_eco:
        if orbs["FJ"] in [125, 130]:
            orbs["FJ"] += 20
            available_orbs += 20
    if plant_boss:
        if orbs["FJ"] in [125, 145]:
            orbs["FJ"] += 5
            available_orbs += 5
    #misty island
    if misty:
        if orbs["MI"] == 0:
            orbs["MI"] += 136
            available_orbs += 136
    if misty_cannon:
        if orbs["MI"] == 136:
            orbs["MI"] += 14
            available_orbs += 14
    #fire canyon
    if power_cells == 20:
        if orbs["FC"] == 0:
            orbs["FC"] += 50
            available_orbs += 50
    #hub 2 (50 + 200 + 200 = 450)
    if item == "[FC|PC] Reach The End Of Fire Canyon":
        if write:
            available_orbs += 450
            #precursor basin
            if allow_on_foot_basin:
                orbs["PB"] += 82
                available_orbs += 82
    #precursor basin
    if blue_button or exclude_warp_buttons:
        if orbs["PB"] == 82:
            orbs["PB"] += 118
            available_orbs += 118
        elif orbs["PB"] == 0:
            orbs["PB"] += 200
            available_orbs += 200
    #mountain pass orbs
    if item_area in ["MP", "VC", "SM", "SC", "LT", "C"]:
        if write:
            if orbs["MP"] == 0:
                orbs["MP"] += 50
                available_orbs += 50
    #hub 3 (50 + 185)
    if item == "[MP|MISC] Stop The Bomb Lurker":
        if write:
            available_orbs += 235
    #spider cave
    if item == "[SC|PC] Shoot The Gnawing Lurkers":
        if write:
            orbs["SC"] += 15
            available_orbs += 15
    #snowy mountain
    if snowy:
        if orbs["SM"] == 0:
            orbs["SM"] += 105
            available_orbs += 105
    if allow_fort_gate_skip or snowy_gate_open:
        if orbs["SM"] in [105, 113, 120, 128]:
            orbs["SM"] += 72
            available_orbs += 72
    if snowy_flut:
        if orbs["SM"] in [105, 177]:
            orbs["SM"] += 23
            available_orbs += 23
    if snowy_flut:
        if orbs["SM"] in [113, 185]:
            orbs["SM"] += 15
            available_orbs += 15
    if yellow_eco:
        if orbs["SM"] in [105, 177]:
            orbs["SM"] += 8
            available_orbs += 8
    #lava tube
    if item_area in ["LT", "C"]:
        if write:
            if orbs["LT"] == 0:
                orbs["LT"] += 50
                available_orbs += 50
    #citadel
    if item_area == "C":
        if write:
            if orbs["C"] == 0:
                orbs["C"] += 180
                available_orbs += 180
            if allow_citadel_skip or citadel_stairs:
                if orbs["C"] == 180:
                    orbs["C"] += 20
                    available_orbs += 20

    #write split
    if force_miners_cell:
        force_miners_cell = False
        miners_count += 1
        splits_list.append("[VC|PC] Bring 90 Orbs To The Miners")
        written_splits += 1
        splits += 1
        power_cells += 1
        snowy_cells += 1
    if write:
        if item == "[VC|PC] Bring 90 Orbs To The Miners":
            miners_count += 1
        splits_list.append(item)
        written_splits += 1
        #force cells
        if force_plant_boss:
            force_plant_boss = False
            plant_boss = True
            splits_list.append("[FJ|MISC] Beat Plant Boss")
            written_splits += 1
            splits += 1
        if force_mp_cell:
            force_mp_cell = False
            mp_cell = True
            splits_list.append("[MP|PC] Reach The End Of The Mountain Pass")
            written_splits += 1
            splits += 1
        if force_lt_cell:
            force_lt_cell = False
            lt_cell = True
            splits_list.append("[LT|PC] Reach The End Of The Lava Tube")
            written_splits += 1
            splits += 1
        if item_type == "PC":
            if write:
                power_cells += 1
                if red_button:
                    snowy_cells += 1
        splits += 1
        data.pop(rnd)

    if splits == old_split:
        double_split += 1
    else:
        old_split = splits
        double_split = 0
    if double_split > 250:
        print("ERROR!")
        break

split_count = 0
for split in splits_list:
    progress = ""
    if write_percent_progress:
        progress = str(round(100 / written_splits * split_count, 1)) + "% - "
    if write_split_progress:
        progress += str(split_count) + "/" + str(written_splits) + " - "
    split_count += 1
    writeSplit(file, progress + split)
    
#close file
progress = ""
if write_percent_progress:
    progress = str(round(100 / written_splits * split_count, 1)) + "% - "
if write_split_progress:
    progress += str(split_count) + "/" + str(written_splits) + " - "
if write_split_progress or write_percent_progress:
        progress += " "
writeSplit(file, progress + "Final Boss")
closeFile(file, seed)
if double_split <= 250:
    print("Done :)")
print("[Seed: " + str(seed) + "]")