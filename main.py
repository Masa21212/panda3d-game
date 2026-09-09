#!/usr/bin/env python3
"""
Yksinkertainen 3D-peli Panda3D:llä
Ohjaa kuutiota nuolinäppäimillä ja hyppää välilyönnillä
"""

from panda3d.core import Point3, Vec3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Aseta kameran alkuasema
        self.camera.setPos(0, -20, 8)
        self.camera.lookAt(0, 0, 0)
        
        # Luo pelialusta (lattia)
        self.setup_ground()
        
        # Luo pelaaja (kuutio)
        self.setup_player()
        
        # Luo valaistus
        self.setup_lighting()
        
        # Pelaajan liikkeisiin liittyvät muuttujat
        self.player_velocity = Vec3(0, 0, 0)
        self.gravity = -25  # Painovoima
        self.on_ground = True
        self.jump_power = 20
        
        # Näppäinten tila
        self.keys = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "jump": False
        }
        
        # Rekisteröi näppäimen painallukset ja vapautukset
        self.accept("arrow_up", self.on_key_down, ["up"])
        self.accept("arrow_up-up", self.on_key_up, ["up"])
        self.accept("arrow_down", self.on_key_down, ["down"])
        self.accept("arrow_down-up", self.on_key_up, ["down"])
        self.accept("arrow_left", self.on_key_down, ["left"])
        self.accept("arrow_left-up", self.on_key_up, ["left"])
        self.accept("arrow_right", self.on_key_down, ["right"])
        self.accept("arrow_right-up", self.on_key_up, ["right"])
        self.accept("space", self.on_key_down, ["jump"])
        self.accept("space-up", self.on_key_up, ["jump"])
        
        # Käynnistä pääsilmukka
        self.taskMgr.add(self.update_game, "UpdateGame")
    
    def setup_ground(self):
        """Luo pelialustan"""
        # Luo lattia mallin avulla
        ground = self.loader.loadModel("models/box")
        ground.setScale(25, 25, 1)  # Leveys, Syvyys, Korkeus
        ground.setPos(0, 0, -5)
        ground.setColor(0.5, 0.5, 0.5, 1)  # Harmaa väri
        ground.reparentTo(self.render)
    
    def setup_player(self):
        """Luo pelaajan (kuutio)"""
        self.player = self.loader.loadModel("models/box")
        self.player.setScale(1, 1, 2)  # Pieni kuutio
        self.player.setPos(0, 0, 0)
        self.player.setColor(0, 0.7, 1, 1)  # Sininen väri
        self.player.reparentTo(self.render)
    
    def setup_lighting(self):
        """Aseta valaistus"""
        # Poista oletusambienttiväli
        self.render.setShaderAuto()
        
        # Lisää ambientti valo
        from panda3d.core import AmbientLight
        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.8, 0.8, 0.8, 1))
        ambient_light_np = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_light_np)
        
        # Lisää suuntavalo (aurinko)
        from panda3d.core import DirectionalLight
        sun_light = DirectionalLight("sun_light")
        sun_light.setColor((1, 1, 1, 1))
        sun_light_np = self.render.attachNewNode(sun_light)
        sun_light_np.setHpr(45, -60, 0)
        self.render.setLight(sun_light_np)
    
    def on_key_down(self, key):
        """Näppäimen painallus"""
        self.keys[key] = True
    
    def on_key_up(self, key):
        """Näppäimen vapautus"""
        self.keys[key] = False
    
    def update_game(self, task):
        """Pääsilmukka - päivitä peliä"""
        dt = globalClock.getDt()  # Delta time (aika viime framesta)
        
        # Pelaajan liikuttaminen
        speed = 15
        movement = Vec3(0, 0, 0)
        
        if self.keys["right"]:
            movement.setX(speed)
        if self.keys["left"]:
            movement.setX(-speed)
        if self.keys["up"]:
            movement.setY(speed)
        if self.keys["down"]:
            movement.setY(-speed)
        
        # Hyppy
        if self.keys["jump"] and self.on_ground:
            self.player_velocity.setZ(self.jump_power)
            self.on_ground = False
        
        # Päivitä pystysuuntainen nopeus (painovoima)
        self.player_velocity.setZ(self.player_velocity.getZ() + self.gravity * dt)
        
        # Yhdistä vaakasuuntainen liike ja pystysuuntainen nopeus
        final_movement = movement * dt + self.player_velocity * dt
        
        # Päivitä pelaajan sijainti
        current_pos = self.player.getPos()
        new_pos = current_pos + final_movement
        
        # Lattia on korkeudella -4 (kuution pohja on -5, korkeus on 2, joten keskipiste on -4)
        ground_level = -4
        
        if new_pos.getZ() <= ground_level:
            new_pos.setZ(ground_level)
            self.player_velocity.setZ(0)
            self.on_ground = True
        
        self.player.setPos(new_pos)
        
        # Päivitä kamera seuraamaan pelaajaa
        player_pos = self.player.getPos()
        camera_offset = Vec3(-5, -20, 8)
        self.camera.setPos(player_pos + camera_offset)
        self.camera.lookAt(player_pos + Vec3(0, 0, 2))
        
        return Task.cont


# Käynnistä peli
if __name__ == "__main__":
    game = Game()
    game.run()
