"""Contains the Undertaker Character class"""

import json 
from botc import Townsfolk, Character, NonRecurringAction
from ._utils import TroubleBrewing, TBRole

with open('botc/gamemodes/troublebrewing/character_text.json') as json_file: 
    character_text = json.load(json_file)[TBRole.undertaker.value.lower()]


class Undertaker(Townsfolk, TroubleBrewing, Character, NonRecurringAction):
    """Undertaker: Each night, you learn which character died by execution today.

    ===== UNDERTAKER ===== 

    true_self = undertaker
    ego_self = undertaker
    social_self = undertaker

    commands:
    - None

    initialize setup? -> NO
    initialize role? -> NO

    ----- First night
    START:
    override first night instruction? -> NO  # default is to send instruction string only

    ----- Regular night
    START:
    override regular night instruction -> YES  # default is to send nothing
                                       => Send passive nightly information
    """

    def __init__(self):
        
        Character.__init__(self)
        TroubleBrewing.__init__(self)
        Townsfolk.__init__(self)

        self._desc_string = character_text["description"]
        self._examp_string = character_text["examples"]
        self._instr_string = character_text["instruction"]
        self._lore_string = character_text["lore"]
        self._brief_string = character_text["brief"]
        self._action = character_text["action"]
                            
        self._art_link = "http://bloodontheclocktower.com/wiki/images/f/fe/Undertaker_Token.png"
        self._art_link_cropped = "https://imgur.com/3CpqHsL.png"
        self._wiki_link = "http://bloodontheclocktower.com/wiki/Undertaker"

        self._role_enum = TBRole.undertaker
        self._emoji = "<:undertaker:722687110599147541>"

    def create_n1_instr_str(self):
        """Create the instruction field on the opening dm card"""

        # First line is the character instruction string
        msg = f"{self.emoji} {self.instruction}"
        addendum = character_text["n1_addendum"]
        
        # Some characters have a line of addendum
        if addendum:
            with open("botutils/bot_text.json") as json_file:
                bot_text = json.load(json_file)
                scroll_emoji = bot_text["esthetics"]["scroll"]
            msg += f"\n{scroll_emoji} {addendum}"
            
        return msg
    
