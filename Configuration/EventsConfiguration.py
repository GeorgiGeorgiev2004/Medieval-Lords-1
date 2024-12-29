import TraitConfiguration as tc
from Models.Choice import Choice
from Models.Event import Event
from Models.Trait import Trait
from Common.Constants import Modifiers as ccm

non_chain_events = []
e = Event(name = "Event1 - Unruly noble",
        description = "A tyrannical lord has been ruling in his people with an iron fist. The populace is unhappy!",
        choices = [Choice(text='Off with his head!',
                          consequences={"traits": Trait("Man of the people",("army-upkeep",-0.1))},
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
                          consequences={{'gold':+50}},
                          flag=ccm.gold),
                   Choice(text="Invest the found funds into our skills",
                          consequences={'stats':{ccm.stats_administrative:1}},
                          flag=ccm.army_morale),
                   Choice(text="Invest in our heir",
                          consequences={'stats':{ccm.stats_administrative:1}},
                          flag=ccm.army_morale,
                          )
                   ],
          )
non_chain_events.append(e)