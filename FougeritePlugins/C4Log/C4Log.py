__author__ = 'DreTaX'
__version__ = '1.2'
import clr

clr.AddReferenceByPartialName("Fougerite")
import Fougerite
import System

"""
    Class
"""

class C4Log:
    """
        Methods
    """

    def On_PluginInit(self):
        Util.ConsoleLog("C4Log by" + __author__ + " Version: " + __version__ + " loaded.", False)


    def C4Log(self):
        if not Plugin.IniExists("C4Log"):
            ini = Plugin.CreateIni("C4Log")
            ini.AddSetting("C4Log")
            ini.Save()
        return Plugin.GetIni("C4Log")

    def TrytoGrabID(self, Player):
        try:
            id = Player.SteamID
            return id
        except:
            return None

    #There is an error while converting ownerid to string in C#. Hax it.
    def GetIt(self, Entity):
        try:
            if Entity.IsDeployableObject():
                return Entity.Object.ownerID
            if Entity.IsStructure():
                return Entity.Object._master.ownerID
        except:
            return None


    def On_EntityHurt(self, HurtEvent):
        if HurtEvent.Attacker is not None and HurtEvent.Entity is not None and not HurtEvent.IsDecay and HurtEvent.DamageType is not None:
            #On Entity hurt the attacker is an NPC and a Player for some reason. We will try to grab his ID
            id = self.TrytoGrabID(HurtEvent.Attacker)
            if id is None:
                return
            if HurtEvent.Entity.IsStructure() or HurtEvent.Entity.IsDeployableObject():
                if HurtEvent.DamageType == "Explosion":
                    entityloc = str(Util.CreateVector(HurtEvent.Entity.X, HurtEvent.Entity.Y, HurtEvent.Entity.Z))
                    entityid = str(self.GetIt(HurtEvent.Entity))
                    if HurtEvent.WeaponName == "Explosive Charge":
                        Plugin.Log("C4", str(HurtEvent.Attacker.Location) + " | " + HurtEvent.Attacker.Name + " | " + id + " | Entity: " + HurtEvent.Entity.Name + " | " + entityloc + " | " + entityid)
                    else:
                        Plugin.Log("Grenade", str(HurtEvent.Attacker.Location) + " | " +  HurtEvent.Attacker.Name + " | " + id + " | Entity: " + HurtEvent.Entity.Name + " | " + entityloc + " | " + entityid)