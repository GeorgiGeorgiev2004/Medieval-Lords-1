from Services.ModelServices import CharacterService as cs
from Services.ModelServices import EventService as es
from Models.Choice import Choice, chance_the_choice
from Models.Event import Event
from Models.Trait import Trait
from Common.Constants import Modifiers as ccm
from Common.Constants import GameEssentials as ccge

chars = cs.generate_heroes()

non_chain_events = []
e = Event(name = "Event1 - Unruly noble",
        description = "A tyrannical lord has been ruling in his people with an iron fist. The populace is unhappy!",
        choices = [Choice(text='Off with his head!',
                          consequences={"traits": Trait("Man of the people",("army-upkeep",-0.1),ccm.stats_tactics)},
                          flag=ccm.upkeep_cost),
                   Choice(text="Ignore this outrageous demand! (Sponsored by the lord)",
                          consequences={'army_morale':-0.3,"gold":+25},
                          flag=ccm.army_morale),
                   Choice(text="Pay the lord off! (Sponsored by the lord)",
                          consequences={'army_morale':-0.1,"gold":-15},
                          flag=ccm.army_morale)
                   ],
        affected_characters=[])
non_chain_events.append(e)

e = Event(name = "Event2 - Heir found a purse",
        description = "Our heir seems to have a talent for managing funds!",
        choices = [Choice(text='Obtain the coins!',
                          consequences={'gold':+50},
                          flag=ccm.gold),
                   Choice(text="Invest the found funds into your own education",
                          consequences={'stats':{ccm.stats_administrative:1}},
                          flag=ccm.army_morale),
                   Choice(text="Invest in our heir",
                          consequences={'stats':{ccm.stats_administrative:1}},
                          flag=ccm.army_morale,
                          func_to_handle=cs.moddify_stat,
                          other_char=ccge.PLAYER_CHARACTER.family.heir
                          )
                   ],
          affected_characters=[ccge.PLAYER_CHARACTER.family.heir, ])
non_chain_events.append(e)

e = Event(name = "Event3 - A transgression!",
        description = "An orc warband is raiding a village in our territory! How should we deal with these monstrous beasts",
        choices = [
            Choice(
                text='Send the army in to deal with the foul creatures.',
                consequences=chance_the_choice([
                    ({'army_morale': +0.2, 'gold': +50}, 0.2),
                    ({'army_morale': +0.1, 'gold': +20}, 0.5),
                    ({'army_morale': -0.2, 'gold': -22}, 0.3)]),
                flag=ccm.gold),
            Choice(
                text="Ignore the danger!",
                consequences={'army_morale':-0.2,"gold":-120},
                flag=ccm.army_morale),
                   ],
          affected_characters=[])
non_chain_events.append(e)

e = Event(name = "Event4 - Take accountability?",
        description = "Our heir seems to have a deeply rooted interest in your attention!",
        choices = [Choice(text='Ignore the child',
                          consequences={'gold':+70},
                          flag=ccm.gold),
                   Choice(text="Start spending more time with the precious thing",
                          consequences=chance_the_choice([
                              ({'stats':{ccm.stats_administrative:1}}, 0.1),
                              ({'stats':{ccm.stats_infrastructural:1}}, 0.3),
                              ({'stats':{ccm.stats_tactics:1}}, 0.2),
                              ({'stats':{ccm.stats_infrastructural:0}}, 0.4)]),
                          flag=ccm.stats,
                          func_to_handle=cs.moddify_stat,
                          other_char=ccge.PLAYER_CHARACTER.family.heir
                          )
                   ],
          affected_characters=[ccge.PLAYER_CHARACTER.family.heir, ])
non_chain_events.append(e)

e = Event(name = "Event5 - Wisdom?",
        description = "Having had a drink you ponder on what reality is.",
        choices = [Choice(text="This really is an intricate ponder to have... mayhaps",
                          consequences=chance_the_choice([
                              ({'stats':{ccm.stats_knowledge:1}}, 0.5),
                              ({'stats':{ccm.stats_knowledge:0}}, 0.5)]),
                          flag=ccm.stats_knowledge,
                          func_to_handle=cs.moddify_stat,
                          other_char=ccge.PLAYER_CHARACTER
                          )
                   ],
          affected_characters=[ccge.PLAYER_CHARACTER, ])
non_chain_events.append(e)

e = Event(name = "Event6 - The massage",
        description = "After a night out with the fellow nobles a friend suggests visiting the massage salon!",
        choices = [Choice(text="Hell yeah tone my MUSCLES sister!",
                          consequences=chance_the_choice([
                              ({'stats':{ccm.stats_strength:1},"gold":-20}, 0.5),
                              ({'stats':{ccm.stats_strength:0},"gold":-20}, 0.5)]),
                          flag=ccm.stats_strength,
                          func_to_handle=cs.moddify_stat,
                          other_char=ccge.PLAYER_CHARACTER
                          )
                   ],
          affected_characters=[ccge.PLAYER_CHARACTER, ])
non_chain_events.append(e)

e = Event(name = "Event7 - Meningit",
        description = "Vqtur me vee na bql kon!",
        choices = [Choice(text="Yeah but I looked like a badass!",
                          consequences=chance_the_choice([
                              ({'stats':{ccm.stats_strength:-1},"gold":-20}, 0.5),
                              ({'stats':{ccm.stats_strength:0},"gold":-20}, 0.5)]),
                          flag=ccm.stats_strength,
                          func_to_handle=cs.moddify_stat,
                          other_char=ccge.PLAYER_CHARACTER
                          )
                   ],
          affected_characters=[ccge.PLAYER_CHARACTER, ])
non_chain_events.append(e)

def get_events():
    return non_chain_events