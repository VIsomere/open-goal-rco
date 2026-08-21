def openFile(seed):
    file = open("RCO_Splits_" + str(seed) + ".lss", "w")
    file.truncate()
    file.write("""
<?xml version="1.0" encoding="UTF-8"?>
<Run version="1.7.0">
  <GameIcon />
  <GameName>OpenGOAL: Jak 1</GameName>
  <CategoryName>Random Collectible Order</CategoryName>
  <LayoutPath>
  </LayoutPath>
  <Metadata>
    <Run id="" />
    <Platform usesEmulator="False">
    </Platform>
    <Region>
    </Region>
    <Variables />
    <CustomVariables />
  </Metadata>
  <Offset>00:00:00</Offset>
  <AttemptCount>0</AttemptCount>
  <AttemptHistory>
  </AttemptHistory>
  <Segments>
  """)
    file.write("\n")

    return file


def closeFile(file, seed):
    file.write("""  
  </Segments>
  <AutoSplitterSettings>
    <Start>True</Start>
    <Reset>True</Reset>
    <Split>True</Split>
    <CustomSettings>
      <Setting id="asl_settings" type="bool">True</Setting>
      <Setting id="asl_settings_debug" type="bool">True</Setting>
      <Setting id="jak1_level_all_orbs" type="bool">False</Setting>
      <Setting id="training_num_orbs" type="bool">True</Setting>
      <Setting id="village1_num_orbs" type="bool">True</Setting>
      <Setting id="beach_num_orbs" type="bool">True</Setting>
      <Setting id="jungle_num_orbs" type="bool">True</Setting>
      <Setting id="misty_num_orbs" type="bool">True</Setting>
      <Setting id="firecanyon_num_orbs" type="bool">True</Setting>
      <Setting id="village2_num_orbs" type="bool">True</Setting>
      <Setting id="sunken_num_orbs" type="bool">True</Setting>
      <Setting id="swamp_num_orbs" type="bool">True</Setting>
      <Setting id="rolling_num_orbs" type="bool">True</Setting>
      <Setting id="ogre_num_orbs" type="bool">True</Setting>
      <Setting id="village3_num_orbs" type="bool">True</Setting>
      <Setting id="snow_num_orbs" type="bool">True</Setting>
      <Setting id="cave_num_orbs" type="bool">True</Setting>
      <Setting id="lavatube_num_orbs" type="bool">True</Setting>
      <Setting id="citadel_num_orbs" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_training" type="bool">True</Setting>
      <Setting id="training_num_flies_1" type="bool">True</Setting>
      <Setting id="training_num_flies_2" type="bool">True</Setting>
      <Setting id="training_num_flies_3" type="bool">True</Setting>
      <Setting id="training_num_flies_4" type="bool">True</Setting>
      <Setting id="training_num_flies_5" type="bool">True</Setting>
      <Setting id="training_num_flies_6" type="bool">True</Setting>
      <Setting id="training_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_village1" type="bool">True</Setting>
      <Setting id="village1_num_flies_1" type="bool">True</Setting>
      <Setting id="village1_num_flies_2" type="bool">True</Setting>
      <Setting id="village1_num_flies_3" type="bool">True</Setting>
      <Setting id="village1_num_flies_4" type="bool">True</Setting>
      <Setting id="village1_num_flies_5" type="bool">True</Setting>
      <Setting id="village1_num_flies_6" type="bool">True</Setting>
      <Setting id="village1_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_beach" type="bool">True</Setting>
      <Setting id="beach_num_flies_1" type="bool">True</Setting>
      <Setting id="beach_num_flies_2" type="bool">True</Setting>
      <Setting id="beach_num_flies_3" type="bool">True</Setting>
      <Setting id="beach_num_flies_4" type="bool">True</Setting>
      <Setting id="beach_num_flies_5" type="bool">True</Setting>
      <Setting id="beach_num_flies_6" type="bool">True</Setting>
      <Setting id="beach_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_jungle" type="bool">True</Setting>
      <Setting id="jungle_num_flies_1" type="bool">True</Setting>
      <Setting id="jungle_num_flies_2" type="bool">True</Setting>
      <Setting id="jungle_num_flies_3" type="bool">True</Setting>
      <Setting id="jungle_num_flies_4" type="bool">True</Setting>
      <Setting id="jungle_num_flies_5" type="bool">True</Setting>
      <Setting id="jungle_num_flies_6" type="bool">True</Setting>
      <Setting id="jungle_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_misty" type="bool">True</Setting>
      <Setting id="misty_num_flies_1" type="bool">True</Setting>
      <Setting id="misty_num_flies_2" type="bool">True</Setting>
      <Setting id="misty_num_flies_3" type="bool">True</Setting>
      <Setting id="misty_num_flies_4" type="bool">True</Setting>
      <Setting id="misty_num_flies_5" type="bool">True</Setting>
      <Setting id="misty_num_flies_6" type="bool">True</Setting>
      <Setting id="misty_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_firecanyon" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_1" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_2" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_3" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_4" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_5" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_6" type="bool">True</Setting>
      <Setting id="firecanyon_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_village2" type="bool">True</Setting>
      <Setting id="village2_num_flies_1" type="bool">True</Setting>
      <Setting id="village2_num_flies_2" type="bool">True</Setting>
      <Setting id="village2_num_flies_3" type="bool">True</Setting>
      <Setting id="village2_num_flies_4" type="bool">True</Setting>
      <Setting id="village2_num_flies_5" type="bool">True</Setting>
      <Setting id="village2_num_flies_6" type="bool">True</Setting>
      <Setting id="village2_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_sunken" type="bool">True</Setting>
      <Setting id="sunken_num_flies_1" type="bool">True</Setting>
      <Setting id="sunken_num_flies_2" type="bool">True</Setting>
      <Setting id="sunken_num_flies_3" type="bool">True</Setting>
      <Setting id="sunken_num_flies_4" type="bool">True</Setting>
      <Setting id="sunken_num_flies_5" type="bool">True</Setting>
      <Setting id="sunken_num_flies_6" type="bool">True</Setting>
      <Setting id="sunken_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_swamp" type="bool">True</Setting>
      <Setting id="swamp_num_flies_1" type="bool">True</Setting>
      <Setting id="swamp_num_flies_2" type="bool">True</Setting>
      <Setting id="swamp_num_flies_3" type="bool">True</Setting>
      <Setting id="swamp_num_flies_4" type="bool">True</Setting>
      <Setting id="swamp_num_flies_5" type="bool">True</Setting>
      <Setting id="swamp_num_flies_6" type="bool">True</Setting>
      <Setting id="swamp_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_rolling" type="bool">True</Setting>
      <Setting id="rolling_num_flies_1" type="bool">True</Setting>
      <Setting id="rolling_num_flies_2" type="bool">True</Setting>
      <Setting id="rolling_num_flies_3" type="bool">True</Setting>
      <Setting id="rolling_num_flies_4" type="bool">True</Setting>
      <Setting id="rolling_num_flies_5" type="bool">True</Setting>
      <Setting id="rolling_num_flies_6" type="bool">True</Setting>
      <Setting id="rolling_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_ogre" type="bool">True</Setting>
      <Setting id="ogre_num_flies_1" type="bool">True</Setting>
      <Setting id="ogre_num_flies_2" type="bool">True</Setting>
      <Setting id="ogre_num_flies_3" type="bool">True</Setting>
      <Setting id="ogre_num_flies_4" type="bool">True</Setting>
      <Setting id="ogre_num_flies_5" type="bool">True</Setting>
      <Setting id="ogre_num_flies_6" type="bool">True</Setting>
      <Setting id="ogre_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_village3" type="bool">True</Setting>
      <Setting id="village3_num_flies_1" type="bool">True</Setting>
      <Setting id="village3_num_flies_2" type="bool">True</Setting>
      <Setting id="village3_num_flies_3" type="bool">True</Setting>
      <Setting id="village3_num_flies_4" type="bool">True</Setting>
      <Setting id="village3_num_flies_5" type="bool">True</Setting>
      <Setting id="village3_num_flies_6" type="bool">True</Setting>
      <Setting id="village3_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_snow" type="bool">True</Setting>
      <Setting id="snow_num_flies_1" type="bool">True</Setting>
      <Setting id="snow_num_flies_2" type="bool">True</Setting>
      <Setting id="snow_num_flies_3" type="bool">True</Setting>
      <Setting id="snow_num_flies_4" type="bool">True</Setting>
      <Setting id="snow_num_flies_5" type="bool">True</Setting>
      <Setting id="snow_num_flies_6" type="bool">True</Setting>
      <Setting id="snow_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_cave" type="bool">True</Setting>
      <Setting id="cave_num_flies_1" type="bool">True</Setting>
      <Setting id="cave_num_flies_2" type="bool">True</Setting>
      <Setting id="cave_num_flies_3" type="bool">True</Setting>
      <Setting id="cave_num_flies_4" type="bool">True</Setting>
      <Setting id="cave_num_flies_5" type="bool">True</Setting>
      <Setting id="cave_num_flies_6" type="bool">True</Setting>
      <Setting id="cave_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_lavatube" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_1" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_2" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_3" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_4" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_5" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_6" type="bool">True</Setting>
      <Setting id="lavatube_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_level_scout_flies_citadel" type="bool">True</Setting>
      <Setting id="citadel_num_flies_1" type="bool">True</Setting>
      <Setting id="citadel_num_flies_2" type="bool">True</Setting>
      <Setting id="citadel_num_flies_3" type="bool">True</Setting>
      <Setting id="citadel_num_flies_4" type="bool">True</Setting>
      <Setting id="citadel_num_flies_5" type="bool">True</Setting>
      <Setting id="citadel_num_flies_6" type="bool">True</Setting>
      <Setting id="citadel_num_flies_7" type="bool">True</Setting>
      <Setting id="jak1_need_res" type="bool">True</Setting>
      <Setting id="num_power_cells" type="bool">False</Setting>
      <Setting id="jak1_need_res_training" type="bool">True</Setting>
      <Setting id="res_training_gimmie" type="bool">True</Setting>
      <Setting id="res_training_door" type="bool">True</Setting>
      <Setting id="res_training_climb" type="bool">True</Setting>
      <Setting id="res_training_buzzer" type="bool">True</Setting>
      <Setting id="jak1_need_res_village1" type="bool">True</Setting>
      <Setting id="res_village1_yakow" type="bool">True</Setting>
      <Setting id="res_misty_muse" type="bool">True</Setting>
      <Setting id="res_village1_mayor_money" type="bool">True</Setting>
      <Setting id="res_jungle_lurkerm" type="bool">True</Setting>
      <Setting id="res_village1_uncle_money" type="bool">True</Setting>
      <Setting id="res_village1_oracle_money1" type="bool">True</Setting>
      <Setting id="res_village1_oracle_money2" type="bool">True</Setting>
      <Setting id="res_village1_buzzer" type="bool">True</Setting>
      <Setting id="jak1_need_res_beach" type="bool">True</Setting>
      <Setting id="res_beach_ecorocks" type="bool">True</Setting>
      <Setting id="res_beach_pelican" type="bool">True</Setting>
      <Setting id="res_beach_flutflut" type="bool">True</Setting>
      <Setting id="res_beach_seagull" type="bool">True</Setting>
      <Setting id="res_beach_cannon" type="bool">True</Setting>
      <Setting id="res_beach_buzzer" type="bool">True</Setting>
      <Setting id="res_beach_gimmie" type="bool">True</Setting>
      <Setting id="res_beach_sentinel" type="bool">True</Setting>
      <Setting id="jak1_need_res_jungle" type="bool">True</Setting>
      <Setting id="res_jungle_eggtop" type="bool">True</Setting>
      <Setting id="com_jungle_lurkerm" type="bool">False</Setting>
      <Setting id="res_jungle_tower" type="bool">True</Setting>
      <Setting id="res_jungle_fishgame" type="bool">True</Setting>
      <Setting id="res_jungle_plant" type="bool">True</Setting>
      <Setting id="res_jungle_buzzer" type="bool">True</Setting>
      <Setting id="res_jungle_canyon_end" type="bool">True</Setting>
      <Setting id="res_jungle_temple_door" type="bool">True</Setting>
      <Setting id="int_jungle_fishgame" type="bool">False</Setting>
      <Setting id="jak1_need_res_misty" type="bool">True</Setting>
      <Setting id="com_misty_muse" type="bool">False</Setting>
      <Setting id="res_misty_boat" type="bool">True</Setting>
      <Setting id="res_misty_warehouse" type="bool">True</Setting>
      <Setting id="res_misty_cannon" type="bool">True</Setting>
      <Setting id="res_misty_bike" type="bool">True</Setting>
      <Setting id="res_misty_buzzer" type="bool">True</Setting>
      <Setting id="res_misty_bike_jump" type="bool">True</Setting>
      <Setting id="res_misty_eco_challenge" type="bool">True</Setting>
      <Setting id="jak1_need_res_firecanyon" type="bool">True</Setting>
      <Setting id="res_firecanyon_buzzer" type="bool">True</Setting>
      <Setting id="res_firecanyon_end" type="bool">True</Setting>
      <Setting id="jak1_need_res_village2" type="bool">True</Setting>
      <Setting id="res_rolling_race" type="bool">True</Setting>
      <Setting id="res_village2_gambler_money" type="bool">True</Setting>
      <Setting id="res_rolling_moles" type="bool">True</Setting>
      <Setting id="res_village2_geologist_money" type="bool">True</Setting>
      <Setting id="res_village2_warrior_money" type="bool">True</Setting>
      <Setting id="res_village2_oracle_money1" type="bool">True</Setting>
      <Setting id="res_village2_oracle_money2" type="bool">True</Setting>
      <Setting id="res_village2_buzzer" type="bool">True</Setting>
      <Setting id="jak1_need_res_sunken" type="bool">True</Setting>
      <Setting id="res_sunken_platforms" type="bool">True</Setting>
      <Setting id="res_sunken_pipe" type="bool">True</Setting>
      <Setting id="res_sunken_slide" type="bool">True</Setting>
      <Setting id="res_sunken_room" type="bool">True</Setting>
      <Setting id="res_sunken_sharks" type="bool">True</Setting>
      <Setting id="res_sunken_buzzer" type="bool">True</Setting>
      <Setting id="res_sunken_top_of_helix" type="bool">True</Setting>
      <Setting id="res_sunken_spinning_room" type="bool">True</Setting>
      <Setting id="jak1_need_res_swamp" type="bool">True</Setting>
      <Setting id="res_swamp_billy" type="bool">True</Setting>
      <Setting id="res_swamp_flutflut" type="bool">True</Setting>
      <Setting id="res_swamp_battle" type="bool">True</Setting>
      <Setting id="res_swamp_tether_4" type="bool">True</Setting>
      <Setting id="res_swamp_tether_1" type="bool">True</Setting>
      <Setting id="res_swamp_tether_2" type="bool">True</Setting>
      <Setting id="res_swamp_tether_3" type="bool">True</Setting>
      <Setting id="res_swamp_buzzer" type="bool">True</Setting>
      <Setting id="jak1_need_res_rolling" type="bool">True</Setting>
      <Setting id="com_rolling_race" type="bool">False</Setting>
      <Setting id="res_rolling_robbers" type="bool">True</Setting>
      <Setting id="com_rolling_moles" type="bool">False</Setting>
      <Setting id="res_rolling_plants" type="bool">True</Setting>
      <Setting id="res_rolling_lake" type="bool">True</Setting>
      <Setting id="res_rolling_buzzer" type="bool">True</Setting>
      <Setting id="res_rolling_ring_chase_1" type="bool">True</Setting>
      <Setting id="res_rolling_ring_chase_2" type="bool">True</Setting>
      <Setting id="jak1_need_res_ogreboss" type="bool">True</Setting>
      <Setting id="res_ogre_boss" type="bool">True</Setting>
      <Setting id="res_ogre_end" type="bool">True</Setting>
      <Setting id="res_ogre_buzzer" type="bool">True</Setting>
      <Setting id="res_ogre_secret" type="bool">True</Setting>
      <Setting id="jak1_need_res_village3" type="bool">True</Setting>
      <Setting id="res_village3_extra1" type="bool">True</Setting>
      <Setting id="res_village3_buzzer" type="bool">True</Setting>
      <Setting id="res_village3_miner_money1" type="bool">True</Setting>
      <Setting id="res_village3_miner_money2" type="bool">True</Setting>
      <Setting id="res_village3_miner_money3" type="bool">True</Setting>
      <Setting id="res_village3_miner_money4" type="bool">True</Setting>
      <Setting id="res_village3_oracle_money1" type="bool">True</Setting>
      <Setting id="res_village3_oracle_money2" type="bool">True</Setting>
      <Setting id="jak1_need_res_snowy" type="bool">True</Setting>
      <Setting id="res_snow_eggtop" type="bool">True</Setting>
      <Setting id="res_snow_ram" type="bool">True</Setting>
      <Setting id="res_snow_fort" type="bool">True</Setting>
      <Setting id="res_snow_ball" type="bool">True</Setting>
      <Setting id="res_snow_bunnies" type="bool">True</Setting>
      <Setting id="res_snow_buzzer" type="bool">True</Setting>
      <Setting id="res_snow_bumpers" type="bool">True</Setting>
      <Setting id="res_snow_cage" type="bool">True</Setting>
      <Setting id="jak1_need_res_spidercave" type="bool">True</Setting>
      <Setting id="res_cave_gnawers" type="bool">True</Setting>
      <Setting id="res_cave_dark_crystals" type="bool">True</Setting>
      <Setting id="res_cave_dark_climb" type="bool">True</Setting>
      <Setting id="res_cave_robot_climb" type="bool">True</Setting>
      <Setting id="res_cave_swing_poles" type="bool">True</Setting>
      <Setting id="res_cave_spider_tunnel" type="bool">True</Setting>
      <Setting id="res_cave_platforms" type="bool">True</Setting>
      <Setting id="res_cave_buzzer" type="bool">True</Setting>
      <Setting id="jak1_need_res_lavatube" type="bool">True</Setting>
      <Setting id="res_lavatube_end" type="bool">True</Setting>
      <Setting id="res_lavatube_buzzer" type="bool">True</Setting>
      <Setting id="res_lavatube_balls" type="bool">False</Setting>
      <Setting id="jak1_need_res_citadel" type="bool">True</Setting>
      <Setting id="res_citadel_sage_green" type="bool">True</Setting>
      <Setting id="res_citadel_sage_blue" type="bool">True</Setting>
      <Setting id="res_citadel_sage_red" type="bool">True</Setting>
      <Setting id="res_citadel_sage_yellow" type="bool">True</Setting>
      <Setting id="res_citadel_buzzer" type="bool">True</Setting>
      <Setting id="unk_finalboss_movies" type="bool">False</Setting>
      <Setting id="jak1_misc_tasks" type="bool">True</Setting>
      <Setting id="int_finalboss_movies" type="bool">True</Setting>
    </CustomSettings>
  </AutoSplitterSettings>
</Run>""")
    file.close()


def writeSplit(file, split_name):
    file.write("    <Segment>\n")
    file.write("      <Name>" + split_name + "</Name>\n")
    file.write("      <Icon />\n")
    file.write("      <SplitTimes>\n")
    file.write('        <SplitTime name="Personal Best" />\n')
    file.write("      </SplitTimes>\n")
    file.write("      <BestSegmentTime />\n")
    file.write("      <SegmentHistory />\n")
    file.write("    </Segment>\n")

# Time Estimate

original_travel_time_graph = [
  #  GR  SV  SB  FJ  MI  FC  RV  LPC BS  PB  MP  VC  SM  SC  LT  C           <- TO
    [ 0,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # GR
    [10,  0, 20, 30, 43, 28,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # SV
    [ 0,  9,  0, 25, 44, 23,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # SB
    [ 0, 10, 26,  0, 58, 23,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # FJ
    [ 0, 38, 45, 57,  0, 57,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # MI
    [ 0, 12, 20, 20, 51,  0,215,  0,  0,  0,  0,  0,  0,  0,  0,  0], # FC
    [ 0,  0,  0,  0,  0, 65,  0, 25, 31, 18, 54,  0,  0,  0,  0,  0], # RV
    [ 0,  0,  0,  0,  0,  0, 17,  0, 32, 40, 65,  0,  0,  0,  0,  0], # LPC   <- FROM
    [ 0,  0,  0,  0,  0,  0, 25, 24,  0, 20, 44,  0,  0,  0,  0,  0], # BS
    [ 0,  0,  0,  0,  0,  0, 19, 35, 26,  0, 49,  0,  0,  0,  0,  0], # PB
    [ 0,  0,  0,  0,  0,  0, 48, 60, 39, 42,  0, 76,  0,  0,  0,  0], # MP
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,122,  0, 45, 21, 30,  0], # VC
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 34,  0, 55, 42,  0], # SM
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  8, 49,  0, 32,  0], # SC
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 46, 43,  0,375], # LT
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,125,  0]] # C

locations = [
      "GR", "SV", "SB", "FJ", "MI", "FC", "RV", "LPC",
      "BS", "PB", "MP", "VC", "SM", "SC", "LT", "C"
  ]

'''
Later Changes
- travel between hubs using warp gates
    -> SV -> RV: 14
    -> SV -> VC: 15
    -> SV -> C : 22

    -> RV -> SV: 11
    -> RV -> VC: 13
    -> RV -> C : 19

    -> VC -> SV: 15
    -> VC -> RV: 15
    -> VC -> C : 21

    -> C  -> SV: 15
    -> C  -> RV: 15
    -> C  -> VC: 16

- adjust times when unlocking zoomer in transition levels
    -> FC -> RV: 65 with zoomer
    -> VC -> MP: 76 with zoomer
    -> LT -> C : 125 with zoomer
'''

def setNode(table, start, end, time):
    table[locations.index(start)][locations.index(end)] = time

def floydWarshall(time_table):

    n = len(time_table)

    # convert non-connections to infinity
    dist = [
        [
          0 if i == j else
          time_table[i][j] if time_table[i][j] != 0 else float("inf")
          for j in range(n)
        ]
        for i in range(n)
    ]

    #floyd-warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def getDist(table, start, end):
  times = floydWarshall(table)

  return times[locations.index(start)][locations.index(end)]

def format_seconds(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"