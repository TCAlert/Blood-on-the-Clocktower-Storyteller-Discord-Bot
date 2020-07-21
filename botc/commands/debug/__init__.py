from .fstop import Fstop
from .modkill import Modkill
from .frole import Frole
from .fnight import Fnight
from .fnomination import Fnomination

def setup(client):
    client.add_cog(Fstop(client))
    client.add_cog(Modkill(client))
    client.add_cog(Frole(client))
    client.add_cog(Fnight(client))
    client.add_cog(Fnomination(client))
