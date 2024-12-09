from Py4GWCoreLib import *


module_name = "FarmingBot"
outpost_coordinate_list = [
( -4268, 11628),
( -5490, 13672)
]

map_paths = { 
    200: [
        (-8394, -9801),
        (-13046, -9347),
        (-17348, -9895),
        (-17929, -10300),
        (-14702, -6671),
        (-11080, -6126),
        (-13426, -2344),
        (-15055, -3226),
        (-9448, -283),
        (-9918, 2826),
        (-8721, 7682),
        (-3749, 8053),
        (-7474, -1144),
        (-9666, 2625),
        (-5895, -3959),
        (-3509, -8000),
        (-195, -9095),
        (6298, -8707),
        (3981, -3295),
        (496, -2581),
        (2069, 1127),
        (5859, 1599),
        (6412, 6572),
        (10507, 8140),
        (14403, 6938),
        (18080, 3127),
        (13518, -35),
        (13450, -6084),
        (13764, -4816),
        (13450, -6084),
        (15390, -8892),
        (13764, -4816)
    ]
}
FARM_MODEL_IDS = [] 
OUTPOST_ID = 389
FARM_END_ID = 389
BLESSING_POSITION = (-8394, -9801)
class BotVars:
    def __init__(self, starting_outpost_id=0, farm_end_id=0):
        self.starting_map = starting_outpost_id
        self.farm_end_id = farm_end_id
        self.bot_started = False
        self.window_module = None
        self.variables = {}
        self.has_env_reset = False

        # Simple Farm Configurations
        self.resign_to_farm = True
        self.pick_up_chests = True
        self.load_skillbar = False

        
        # Simple Farm Tracking Metrics
        self.farm_timer = Py4GW.Timer()
        self.farm_count = 0
        self.chests_found = 0
        self.deaths = 0
        

bot_vars = BotVars(starting_outpost_id=OUTPOST_ID, farm_end_id=FARM_END_ID)
bot_vars.window_module = ImGui.WindowModule(module_name, window_name="Simple Farming", window_size=(300, 350))

class StateMachineVars:
        def __init__(self):
            # FSMs
            self.state_machine = FSM("Main")
            self.path_to_farm_machine = FSM("PathToFarm")
            self.farm_machine = FSM("Farm")
            self.loot_items = FSM("Loot")
            self.loot_chest = FSM("Chest")
            self.fight_enemies = FSM("Fight")

            # Movement
            self.outpost_pathing = Routines.Movement.PathHandler(outpost_coordinate_list)
            self.current_map_pathing = Routines.Movement.PathHandler([])
            self.bounty_npc = Routines.Movement.PathHandler([(-8394, -9801)])  # Added bounty NPC path
            self.chest_found_pathing = None
            self.current_map_id = 0
            self.movement_handler = Routines.Movement.FollowXY()

            # Other tools and variables
            self.ping_handler = Py4GW.PingHandler()
            self.timer = Py4GW.Timer()
            self.timer_check = 0
            self.has_resigned = False
            self.map_loaded = False
            self.explorable_loading = False
            self.finished_resigning = False
            self.collected_coords = []
            self.current_target = None
            self.current_loot_target = None
            self.current_chest_target = 0
            self.completed_chests = []
            

FSM_vars = StateMachineVars()

#Helper Functions
def StartBot():
    global bot_vars

    if not bot_vars.has_env_reset:
        ResetEnvironment()
        bot_vars.has_env_reset = True
        bot_vars.farm_timer.reset()

    bot_vars.bot_started = True

def StopBot():
    global bot_vars
    bot_vars.farm_timer.stop()
    bot_vars.bot_started = False

def IsBotStarted():
    global bot_vars
    return bot_vars.bot_started

def IfActionIsPending():
    if FSM_vars.timer_check != 0 and FSM_vars.timer.get_elapsed_time() > 0:
        if FSM_vars.timer.has_elapsed(FSM_vars.timer_check):
            FSM_vars.timer_check = 0
            FSM_vars.timer.stop()
            return False
    if FSM_vars.timer_check == 0 and FSM_vars.timer.get_elapsed_time() == 0:
        return False
    return True

def SetPendingAction(timer_check=1000):
    FSM_vars.timer_check = timer_check
    FSM_vars.timer.reset()

def DoesNeedInventoryHandling():
    return ( Inventory.GetFreeSlotCount() < 1 or Inventory.GetModelCount(22751) < 1)

def CheckMapLocation():
    global bot_vars, FSM_vars
    if IfActionIsPending():
        return

    if Routines.Transition.IsExplorableLoaded():
        if Map.GetMapID() not in map_paths:
            Routines.Transition.TravelToOutpost(bot_vars.starting_map) # travel to starting outpost if not in one of the zones
            SetPendingAction(2000)
            return
        
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"{Map.GetMapName(Map.GetMapID())} ({Map.GetMapID()}) already loaded. Switching to Farm step.", Py4GW.Console.MessageType.Info)
        FSM_vars.current_map_id = 0
        FSM_vars.current_map_pathing = Routines.Movement.PathHandler([])
        FSM_vars.state_machine.jump_to_state_by_name("Start Pathing for Farm")
        return
        
    if Routines.Transition.IsOutpostLoaded():
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Outpost loaded", Py4GW.Console.MessageType.Info)
        if Map.GetMapID() != bot_vars.starting_map:
            Routines.Transition.TravelToOutpost(bot_vars.starting_map)
            SetPendingAction(3000)
            return
        
        FSM_vars.timer.stop()
        FSM_vars.state_machine.jump_to_state_by_name("Leaving Outpost")
    
    SetPendingAction(int(FSM_vars.ping_handler.GetCurrentPing()) * 2) # to help prevent it from checking too frequently

def LoadSkillBar(): # TODO ould need to set skill templates for the farm
    global bot_vars
    if bot_vars.load_skillbar:
        primary_profession, secondary_profession = Agent.GetProfessionNames(Player.GetAgentID())

        if primary_profession == "Warrior":
            SkillBar.LoadSkillTemplate("OQcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Ranger":
            SkillBar.LoadSkillTemplate("OgcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Monk":
            SkillBar.LoadSkillTemplate("OwcAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Necromancer":
            SkillBar.LoadSkillTemplate("OAdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Mesmer":
            SkillBar.LoadSkillTemplate("OQdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Elementalist":
            SkillBar.LoadSkillTemplate("OgdAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Assassin":
            SkillBar.LoadSkillTemplate("OwBAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Ritualist":
            SkillBar.LoadSkillTemplate("OACiIukLdNVOxMtMVN5D6MNACA")
        elif primary_profession == "Paragon":
            SkillBar.LoadSkillTemplate("OQeAQ3lTQ0kAAAAAAAAAAA")
        elif primary_profession == "Dervish":
            SkillBar.LoadSkillTemplate("OgCjwqpoKThX7XdftXWgOXQX0k")

def IsSkillBarLoaded():
    global bot_vars
    if bot_vars.load_skillbar:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"SkillBar Loaded.", Py4GW.Console.MessageType.Info)       
    return True

def HandleSkills():
    global FSM_vars
    if not Routines.Transition.IsExplorableLoaded():
        return
    
    if IfActionIsPending():
        return

    if not Agent.IsAlive(Player.GetAgentID()):
        return
    
    if Agent.IsCasting(Player.GetAgentID()):
        return

    if Agent.IsKnockedDown(Player.GetAgentID()):
        return

    for i in [1, 2, 3]:
        if Agent.GetEnergy(Player.GetAgentID()) * Agent.GetMaxEnergy(Player.GetAgentID()) >= Skill.Data.GetEnergyCost(SkillBar.GetSkillIDBySlot(i)) and SkillBar.GetSkillData(i).recharge == 0:
            delay = int(Skill.Data.GetActivation(SkillBar.GetSkillIDBySlot(i))) * 1000
            delay += int(Skill.Data.GetAftercast(SkillBar.GetSkillIDBySlot(i))) * 1000
            delay += int(FSM_vars.ping_handler.GetCurrentPing()) * 2
            SetPendingAction(delay)
            SkillBar.UseSkill(i)
            return

def Resign():
    global FSM_vars, bot_vars
    if IfActionIsPending():
        return

    if bot_vars.resign_to_farm == True and FSM_vars.has_resigned == False:
        Player.SendChatCommand("resign") # only resign once
        FSM_vars.has_resigned = True
        bot_vars.farm_count += 1
        SetPendingAction(2000)
    
    if Routines.Transition.IsOutpostLoaded():
        if Map.GetMapID() != bot_vars.starting_map:
            Routines.Transition.TravelToOutpost(bot_vars.starting_map)
            SetPendingAction(3000)
            return
        FSM_vars.state_machine.jump_to_state_by_name("Finished")
    
    SetPendingAction(1000) # make sure to wait before spamming IsLoaded

def UpdateTarget(max_distance=2500):
    if IfActionIsPending():
        return
    
    if not Agent.IsAlive(Player.GetAgentID()): # if not alive
        return
    
    # reset target once its dead
    if FSM_vars.current_target != None and Agent.IsDead(FSM_vars.current_target):
        FSM_vars.current_target = None
        return

    # only look for target if we don't have one
    if FSM_vars.current_target == None:
        enemy_array = AgentArray.GetEnemyArray()
        xy = Player.GetXY()
        filtered_enemy_array = Utils.Filters.FilterAgentArrayByAlive(xy, enemy_array, area=2500)
        filtered_enemy_array = AgentArray.Sort.ByDistance(filtered_enemy_array, xy)
        nearby_enemies = [
            agent for agent in filtered_enemy_array 
            if Utils.Distance(xy, Agent.GetXY(agent)) <= max_distance
        ]
        
        for agent in nearby_enemies:
            try:
                # player_number = Agent.GetPlayerNumber(agent) # if you need to check the model id of the enemy to only farm specific enemies

                FSM_vars.current_target = agent
                Py4GW.Console.Log(bot_vars.window_module.module_name, f"Target Farm found! {agent}", Py4GW.Console.MessageType.Info)
                return agent  # Return the target enemy if found
            except Exception as e:
                # Log any errors that occur during the player number retrieval
                Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error retrieving player number: {str(e)}", Py4GW.Console.MessageType.Error)

    return None  # No valid target found


def EnemyFound():
    global FSM_vars
    UpdateTarget(max_distance=1150)
    return FSM_vars.current_target != None

def ChangeTargeting():
    global FSM_vars
    Player.ChangeTarget(FSM_vars.current_target)

def ResetPathing(pathing):
    global FSM_vars
    if not Routines.Movement.IsFollowPathFinished(pathing, FSM_vars.movement_handler):
        pathing.reset()
    else:
        FSM_vars.farm_machine.jump_to_state_by_name("Finished")

def UpdateLootTarget(max_distance=1250):
    global FSM_vars
    try:
        if IfActionIsPending():
            return

        # Reset loot target if it's no longer valid
        if FSM_vars.current_loot_target is not None:
            try:
                if not Agent.IsItem(FSM_vars.current_loot_target):
                    FSM_vars.current_loot_target = None
            except:
                FSM_vars.current_loot_target = None
            return

        # Only look for a new loot target if we don't have one
        if FSM_vars.current_loot_target is None:
            try:
                # Get player position first
                xy = Player.GetXY()
                if xy is None:
                    return None

                # Retrieve and filter items
                item_array = AgentArray.GetItemArray()
                if not item_array:
                    return None
                
                filtered_item_array = [
                    item for item in item_array 
                    if item is not None and Agent.IsItem(item) and Utils.Distance(xy, Agent.GetXY(item)) <= max_distance
                ]
                
                if filtered_item_array:
                    FSM_vars.current_loot_target = filtered_item_array[0]
                    Py4GW.Console.Log(bot_vars.window_module.module_name, f"Loot Item found! {FSM_vars.current_loot_target}", Py4GW.Console.MessageType.Info)
                    return FSM_vars.current_loot_target
            except Exception as e:
                Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error in UpdateLootTarget: {str(e)}", Py4GW.Console.MessageType.Error)
                FSM_vars.current_loot_target = None

    except Exception as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Critical error in UpdateLootTarget: {str(e)}", Py4GW.Console.MessageType.Error)
        FSM_vars.current_loot_target = None
    
    return None

def LootFound():
    try:
        if not Agent.IsAlive(Player.GetAgentID()):
            return False
        
        UpdateLootTarget(max_distance=1250)
        return FSM_vars.current_loot_target is not None and Agent.IsItem(FSM_vars.current_loot_target)
    except:
        return False

def IsChestFound(max_distance=2500):
    return Routines.Targeting.GetNearestChest(max_distance) != 0

def ResetFollowPathToChest():
    global FSM_vars
    FSM_vars.movement_handler.reset()
    ResetPathing(FSM_vars.current_map_pathing)
    if FSM_vars.current_chest_target != 0:
        chest_x, chest_y = Agent.GetXY(FSM_vars.current_chest_target)
        found_chest_coord_list = [(chest_x, chest_y)]
    
    if found_chest_coord_list != None:
        FSM_vars.chest_found_pathing = Routines.Movement.PathHandler(found_chest_coord_list)
        FSM_vars.loot_chest.jump_to_state_by_name("MoveToChest")
    else:
        FSM_vars.loot_chest.jump_to_state_by_name("Finished")

def CheckForChest():   
    global FSM_vars, bot_vars
    if bot_vars.pick_up_chests != False and FSM_vars.current_chest_target != 0 and FSM_vars.current_chest_target not in FSM_vars.completed_chests:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Chest {FSM_vars.current_chest_target} found and not in completed_chests {FSM_vars.completed_chests}", Py4GW.Console.MessageType.Info)
        FSM_vars.loot_chest.jump_to_state_by_name("Reset Follow Path To Chest")
    else:
        FSM_vars.loot_chest.jump_to_state_by_name("Finished")

def ChestFound(max_distance=1250):
    global FSM_vars
    if IfActionIsPending():
        return False
    
    chest = Routines.Targeting.GetNearestChest(max_distance)
    if chest != 0 and chest not in FSM_vars.completed_chests:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Chest {chest} found!", Py4GW.Console.MessageType.Info)
        FSM_vars.current_chest_target = chest
        return True
    
    FSM_vars.current_chest_target = 0
    return False

def TrackChest():
    global FSM_vars, bot_vars
    
    if FSM_vars.current_chest_target != 0:
        FSM_vars.completed_chests.append(FSM_vars.current_chest_target)
        FSM_vars.current_chest_target = 0
        bot_vars.chests_found += 1

    return True

def PlayerDied():
    global bot_vars
    if not Agent.IsAlive(Player.GetAgentID()):
        FSM_vars.current_target = None # reset target so that it can restart the sub machine
        bot_vars.deaths += 1
        return True
    return False

def CheckForMap():
    global FSM_vars
    if IfActionIsPending():
        return False
    
    current_map = Map.GetMapID()
    if Routines.Transition.IsExplorableLoaded():
        if current_map in map_paths:
            Py4GW.Console.Log(bot_vars.window_module.module_name, f"Setting current map and path to {current_map}", Py4GW.Console.MessageType.Info)
            FSM_vars.current_map_pathing = Routines.Movement.PathHandler(map_paths[current_map])
            FSM_vars.current_map_id = current_map
            return
    
    # not sure if I need to handle the case where this map path doesn't get loaded correctly
    Py4GW.Console.Log(bot_vars.window_module.module_name, f"CheckForMap() when Explorable not loaded.", Py4GW.Console.MessageType.Info)
    SetPendingAction(2000)

def IsCurrentPathFinished():
    return (Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) and not EnemyFound())

def format_elapsed_time(milliseconds):
    """
    Converts elapsed time in milliseconds to a human-readable format.
    Displays seconds if under 60 seconds, otherwise displays minutes and seconds.
    """
    total_seconds = milliseconds / 1000
    if total_seconds < 60:
        return f"{total_seconds:.2f} seconds"
    else:
        minutes = int(total_seconds // 60)
        seconds = total_seconds % 60
        return f"{minutes}m {seconds:.2f}s"
    
def WaitForLoot():
    try:
        if IfActionIsPending():
            return False
        
        if not LootFound():
            return True
        else:
            SetPendingAction(2000)
            return False
    except Exception as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error in WaitForLoot: {str(e)}", Py4GW.Console.MessageType.Error)
        return True

FSM_vars.loot_items.AddState(name="Select Item",
                    execute_fn=lambda: FSM_vars.current_loot_target is not None and Agent.IsItem(FSM_vars.current_loot_target) and Player.ChangeTarget(FSM_vars.current_loot_target),
                    transition_delay_ms=1000)
FSM_vars.loot_items.AddState(name="PickUpItem",
                    execute_fn=lambda: FSM_vars.current_loot_target is not None and Agent.IsItem(FSM_vars.current_loot_target) and Routines.Targeting.InteractTarget(),
                    transition_delay_ms=1000)
FSM_vars.loot_items.AddState(name="Wait for Loot to Finish",
                    exit_condition=lambda: WaitForLoot(),
                    run_once=False)

# FSM Routine for looting chests only
FSM_vars.loot_chest.AddState(name="CheckForChest",
                    execute_fn=lambda: CheckForChest())
FSM_vars.loot_chest.AddState(name="Reset Follow Path To Chest",
                    execute_fn=lambda: ResetFollowPathToChest())
FSM_vars.loot_chest.AddState(name="MoveToChest",
                    execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.chest_found_pathing, FSM_vars.movement_handler),
                    exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.chest_found_pathing, FSM_vars.movement_handler),
                    run_once=False)
FSM_vars.loot_chest.AddState(name="Select Chest",
                    execute_fn=lambda: Player.ChangeTarget(FSM_vars.current_chest_target),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Track Chest",
                    exit_condition=lambda: TrackChest(),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Interact with Chest",
                    execute_fn=lambda: Routines.Targeting.InteractTarget(),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Open With Lockpick",
                    execute_fn=lambda: Player.SendDialog(2),
                    transition_delay_ms=1000)
FSM_vars.loot_chest.AddState(name="Finished")


FSM_vars.fight_enemies.AddState(name="Target Enemy",
                    execute_fn=lambda: Player.ChangeTarget(FSM_vars.current_target),
                    transition_delay_ms=500)
FSM_vars.fight_enemies.AddState(name="Engage Enemy",
                    execute_fn=lambda: Routines.Targeting.InteractTarget(),
                    transition_delay_ms=500)
FSM_vars.fight_enemies.AddState(name="Wait for Combat to Finish",
                    exit_condition=lambda: not Agent.IsAlive(FSM_vars.current_target) or PlayerDied(),
                    run_once=True)
FSM_vars.fight_enemies.AddState(name="Check for Next Enemy",
                    exit_condition=lambda: not EnemyFound() or not Agent.IsAlive(Player.GetAgentID()), # if no enemies found or if Player died, then we are finished
                    run_once=True)

# Farming Map Routine
FSM_vars.farm_machine.AddState(name="Check if Alive",
                       exit_condition=lambda: Agent.IsAlive(Player.GetAgentID()),
                       run_once=False)
FSM_vars.farm_machine.AddState(name="Seek for Farm",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.current_map_pathing, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) or EnemyFound() or ChestFound() or LootFound() or Map.GetMapID() != FSM_vars.current_map_id,
                       run_once=False)
FSM_vars.farm_machine.AddSubroutine(name="Engage Farm",
                       sub_fsm = FSM_vars.fight_enemies,
                       condition_fn=lambda: not EnemyFound() or not Agent.IsAlive(Player.GetAgentID()))
FSM_vars.farm_machine.AddSubroutine(name="Collect Loot",
                       sub_fsm = FSM_vars.loot_items,
                       condition_fn=lambda: not LootFound())
FSM_vars.farm_machine.AddState(name="Reset pather to find nearest point",
                       execute_fn=lambda: ResetPathing(FSM_vars.current_map_pathing) if not Routines.Movement.IsFollowPathFinished(FSM_vars.current_map_pathing, FSM_vars.movement_handler) else None,
                       run_once=True)
FSM_vars.farm_machine.AddState(name="Finished")

# Pathing to Farm Routine
FSM_vars.path_to_farm_machine.AddState(name="Check For Pathing Map",
                        execute_fn=lambda: CheckForMap(),
                        run_once=False)
FSM_vars.path_to_farm_machine.AddState(name="Reset Movement",
                        execute_fn=lambda: FSM_vars.movement_handler.reset(),
                        transition_delay_ms=1200)
FSM_vars.path_to_farm_machine.AddSubroutine(name="Handle Map Pathing",
                       sub_fsm = FSM_vars.farm_machine,
                       condition_fn=lambda: IsCurrentPathFinished() or Map.GetMapID() != FSM_vars.current_map_id) # if path finished or not in same map, then move on

#MAIN STATE MACHINE CONFIGURATION
FSM_vars.state_machine.AddState(name="Map Check for Farm", 
                       execute_fn=lambda: CheckMapLocation(),
                       transition_delay_ms=1000,
                       run_once=False)
FSM_vars.state_machine.AddState(name="Load SkillBar",
                       execute_fn=lambda: LoadSkillBar(),
                       transition_delay_ms=1000,
                       exit_condition=lambda: IsSkillBarLoaded())
FSM_vars.state_machine.AddState(name="Leaving Outpost",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.outpost_pathing, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.outpost_pathing, FSM_vars.movement_handler) or Map.IsMapLoading(),
                       run_once=False)
FSM_vars.state_machine.AddState(name="Waiting for Explorable Map Load",
                       exit_condition=lambda: Routines.Transition.IsExplorableLoaded(log_actions=True),
                       transition_delay_ms=1200)
FSM_vars.state_machine.AddState(name="Reset Movement",
                       execute_fn=lambda: FSM_vars.movement_handler.reset(), 
                       transition_delay_ms=1200)

FSM_vars.state_machine.AddState(name="Go to NPC",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.bounty_npc, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.bounty_npc, FSM_vars.movement_handler),
                       run_once=False)
FSM_vars.state_machine.AddState(name="Target NPC",
                       execute_fn=lambda: Player.SendChatCommand("target Luxon Priest"),
                       transition_delay_ms=1000)
FSM_vars.state_machine.AddState(name="Interact NPC",
                       execute_fn=lambda: Routines.Targeting.InteractTarget(),
                       transition_delay_ms=1000)
FSM_vars.state_machine.AddState(name="Take Bounty",
                       execute_fn=lambda: Take_Bounty(),
                       transition_delay_ms=1500)

FSM_vars.state_machine.AddSubroutine(name="Start Pathing for Farm",
                       sub_fsm = FSM_vars.path_to_farm_machine,
                       condition_fn=lambda: Map.GetMapID() == bot_vars.farm_end_id and IsCurrentPathFinished())
FSM_vars.state_machine.AddState(name="Resign",
                       execute_fn=lambda: Resign(),
                       run_once=False,
                       transition_delay_ms=1000)
FSM_vars.state_machine.AddState(name="Wait if no resign",
                       exit_condition=bot_vars.resign_to_farm, # this will hold unless it gets check (prevents unintentional resign after incomplete vanquish)
                       run_once=False)
FSM_vars.state_machine.AddState(name="Finished")

# NPC Targeting/Interaction Functions
def Target_NPC():
    Player.SendChatCommand("target Luxon Priest")

def Interact_NPC():
    Routines.Targeting.InteractTarget()

def Take_Bounty():
    Player.SendDialog(int("0x85", 16))  # First dialog
    SetPendingAction(1000)  # 1000ms delay
    Player.SendDialog(int("0x86", 16))  # Second dialog
    SetPendingAction(500)   # 500ms delay

# State Machine States for NPC Interaction
FSM_vars.state_machine.AddState(name="Go to NPC",
                       execute_fn=lambda: Routines.Movement.FollowPath(FSM_vars.bounty_npc, FSM_vars.movement_handler),
                       exit_condition=lambda: Routines.Movement.IsFollowPathFinished(FSM_vars.bounty_npc, FSM_vars.movement_handler),
                       run_once=False)

FSM_vars.state_machine.AddState(name="Target NPC",
                       execute_fn=lambda: Player.SendChatCommand("target Luxon Priest"),
                       transition_delay_ms=1000)

FSM_vars.state_machine.AddState(name="Interact NPC",
                       execute_fn=lambda: Routines.Targeting.InteractTarget(),
                       transition_delay_ms=1000)

FSM_vars.state_machine.AddState(name="Take Bounty",
                       execute_fn=lambda: Take_Bounty(),
                       transition_delay_ms=1500)  # Increased delay to account for both dialog actions

def DrawWindow():
    global bot_vars, FSM_vars

    try:
        if bot_vars.window_module.first_run:
            PyImGui.set_next_window_size(bot_vars.window_module.window_size[0], bot_vars.window_module.window_size[1])     
            PyImGui.set_next_window_pos(bot_vars.window_module.window_pos[0], bot_vars.window_module.window_pos[1])
            bot_vars.window_module.first_run = False

        if PyImGui.begin(bot_vars.window_module.window_name, bot_vars.window_module.window_flags):
            if PyImGui.begin_tab_bar("Simple Farming Options"):
                if PyImGui.begin_tab_item("Farm"):
                    if IsBotStarted():
                        if PyImGui.button("Pause Bot"):
                            StopBot()
                        if PyImGui.button("Stop Bot"):
                            ResetEnvironment()
                            bot_vars.has_env_reset = False
                            StopBot()
                    else:
                        if PyImGui.button("Start Bot"):
                            StartBot()
                        if PyImGui.button("Reset Env"):
                            ResetEnvironment()
                            bot_vars.has_env_reset = False

                    bot_vars.resign_to_farm = PyImGui.checkbox("Resign At End?", bot_vars.resign_to_farm)
                    bot_vars.pick_up_chests = PyImGui.checkbox("Loot Chests?", bot_vars.pick_up_chests)
                    bot_vars.load_skillbar = PyImGui.checkbox("Load SkillBar?", bot_vars.load_skillbar)


                    headers = ["Farm Stats","Data"]
                    data = [
                        ("Farm Count:", f"{bot_vars.farm_count}"),
                        ("Tracked Deaths:", f"{bot_vars.deaths}"),
                        ("Chests Found:", f"{bot_vars.chests_found}"),
                        ("Is Path Finished:", f"{IsCurrentPathFinished()}"),
                        ("Farm Timer:", f"{format_elapsed_time(bot_vars.farm_timer.get_elapsed_time())}"),
                        ("Current Map ID:", f"{Map.GetMapID()}")  # Added this line
                    ]

                    ImGui.table("State Machine Info", headers, data)

                    if PyImGui.button("Resign"):
                        if FSM_vars.state_machine != None:
                            FSM_vars.state_machine.jump_to_state_by_name("Resign")

                    PyImGui.end_tab_item() # end Farm Options
            
                # State Machine Debugger
                if PyImGui.begin_tab_item("State Machine Debugging"):
                    PyImGui.separator()

                    if FSM_vars.state_machine != None:
                        fsm_previous_step = FSM_vars.state_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.state_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.state_machine.get_next_step_name()

                        headers = ["Main State Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.state_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.state_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("State Machine Info", headers, data)

                    if FSM_vars.path_to_farm_machine != None:
                        fsm_previous_step = FSM_vars.path_to_farm_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.path_to_farm_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.path_to_farm_machine.get_next_step_name()

                        headers = ["Path To Farm Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.path_to_farm_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.path_to_farm_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Path To Farm Machine Info", headers, data)

                    if FSM_vars.farm_machine != None:
                        fsm_previous_step = FSM_vars.farm_machine.get_previous_step_name()
                        fsm_current_step = FSM_vars.farm_machine.get_current_step_name()
                        fsm_next_step = FSM_vars.farm_machine.get_next_step_name()

                        headers = ["Farm Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.farm_machine.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.farm_machine.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Farm Machine State Machine Info", headers, data)

                    if FSM_vars.fight_enemies != None:
                        fsm_previous_step = FSM_vars.fight_enemies.get_previous_step_name()
                        fsm_current_step = FSM_vars.fight_enemies.get_current_step_name()
                        fsm_next_step = FSM_vars.fight_enemies.get_next_step_name()

                        headers = ["Fight Enemies Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.fight_enemies.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.fight_enemies.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Fight Enemies State Machine Info", headers, data)

                    if FSM_vars.loot_chest != None:
                        fsm_previous_step = FSM_vars.loot_chest.get_previous_step_name()
                        fsm_current_step = FSM_vars.loot_chest.get_current_step_name()
                        fsm_next_step = FSM_vars.loot_chest.get_next_step_name()

                        headers = ["Loot Chest Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.loot_chest.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.loot_chest.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Loot Items Machine Info", headers, data)

                    if FSM_vars.loot_items != None:
                        fsm_previous_step = FSM_vars.loot_items.get_previous_step_name()
                        fsm_current_step = FSM_vars.loot_items.get_current_step_name()
                        fsm_next_step = FSM_vars.loot_items.get_next_step_name()

                        headers = ["Loot Chest Machine","Data"]
                        data = [
                            ("Previous Step:", f"{fsm_previous_step}"),
                            ("Current Step:", f"{fsm_current_step}"),
                            ("Next Step:", f"{fsm_next_step}"),
                            ("State Machine is started:", f"{FSM_vars.loot_items.is_started()}"),
                            ("State Machine is finished:", f"{FSM_vars.loot_items.is_finished()}"),
                            ("Action Timer:", f"{FSM_vars.timer.get_elapsed_time():.2f}"),
                            ("Action Timer Check:", f"{FSM_vars.timer_check}")
                        ]

                        ImGui.table("Loot Items Machine Info", headers, data)
                    PyImGui.separator()

                    PyImGui.end_tab_item() # end State Machine Debugging

                PyImGui.end_tab_bar() # end Skelefarm Options

            PyImGui.end()

    except Exception as e:
        current_function = inspect.currentframe().f_code.co_name
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Error in {current_function}: {str(e)}", Py4GW.Console.MessageType.Error)
        raise

def ResetEnvironment():
    global FSM_vars
    FSM_vars.outpost_pathing.reset()
    FSM_vars.movement_handler.reset()
    FSM_vars.state_machine.reset()
    FSM_vars.path_to_farm_machine.reset()
    FSM_vars.loot_items.reset()
    FSM_vars.farm_machine.reset()
    FSM_vars.fight_enemies.reset()
    FSM_vars.timer.stop()
    FSM_vars.timer_check = 0
    FSM_vars.finished_resigning = False
    FSM_vars.has_resigned = False
    FSM_vars.map_loaded = False
    FSM_vars.explorable_loading = False
    FSM_vars.state_machine.log_actions = False
    FSM_vars.current_map_pathing = Routines.Movement.PathHandler([])
    FSM_vars.current_target = None
    FSM_vars.current_loot_target = None
    FSM_vars.current_chest_target = 0
    FSM_vars.completed_chests = []

def main():
    global bot_vars,FSM_vars
    try:
        DrawWindow()

        if IsBotStarted():
            if FSM_vars.state_machine.is_finished():
                ResetEnvironment()
            else:
                FSM_vars.state_machine.update()

    except ImportError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"ImportError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except ValueError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"ValueError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except TypeError as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"TypeError encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    except Exception as e:
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Unexpected error encountered: {str(e)}", Py4GW.Console.MessageType.Error)
        Py4GW.Console.Log(bot_vars.window_module.module_name, f"Stack trace: {traceback.format_exc()}", Py4GW.Console.MessageType.Error)
    finally:
        pass

if __name__ == "__main__":
    main()