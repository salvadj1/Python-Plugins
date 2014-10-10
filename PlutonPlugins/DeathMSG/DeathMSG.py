__author__ = 'DreTaX'
__version__ = '1.0'

import clr

clr.AddReferenceByPartialName("Pluton")
import Pluton
import math

"""
    Class
"""


class DeathMSG:

    def DeathMSGConfig(self):
        if not Plugin.IniExists("DeathMSGConfig"):
            loc = Plugin.CreateIni("DeathMSGConfig")
            loc.AddSetting("Settings", "SysName", "Equinox DeathMSG")
            loc.AddSetting("Settings", "SuicideMsgs", "1")
            loc.AddSetting("Settings", "KillMessage", "victim was killed by killer , Damage Caused: dmg , Distance: dist")
            loc.Save()
        return Plugin.GetIni("TpFriendConfig")

    def On_PlayerDied(self, PlayerDeathEvent):
        attacker = PlayerDeathEvent.Attacker.ToPlayer()
        if attacker is not None:
            Server.BroadcastFrom("DeathMSG", str(attacker.Name + " | " + PlayerDeathEvent.Victim.Name + " | " + PlayerDeathEvent.DamageType  + " | " + PlayerDeathEvent.DamageAmount))
            if PlayerDeathEvent.Victim is not None and attacker != PlayerDeathEvent.Victim:
                ini = self.DeathMSGConfig()
                sysname = ini.GetSetting("Settings", "SysName")
                dmgmsg = ini.GetSetting("Settings", "KillMessage")
                victim = PlayerDeathEvent.Victim
                vloc = victim.Location
                aloc = attacker.Location
                dist = round(Util.GetVectorsDistance(vloc, aloc), 2)
                damage = PlayerDeathEvent.DamageAmount
                dmgmsg.replace("killer", attacker.Name)
                dmgmsg.replace("victim", victim.Name)
                dmgmsg.replace("dmg", str(damage))
                dmgmsg.replace("dist", str(dist))
                # = dmgmsg.replace("weapon", WEAPONMISSINGOMG)
                Server.BroadcastFrom(sysname, dmgmsg)

            if PlayerDeathEvent.Attacker is not None and PlayerDeathEvent.Victim is not None and PlayerDeathEvent.Attacker == PlayerDeathEvent.Victim:
                ini = self.DeathMSGConfig()
                suicidemsg = int(ini.GetSetting("Settings", "SuicideMsgs"))
                sysname = ini.GetSetting("Settings", "SysName")
                if suicidemsg == 1:
                    victim = PlayerDeathEvent.Victim
                    Server.BroadcastFrom(sysname, victim.Name + " suicided...")