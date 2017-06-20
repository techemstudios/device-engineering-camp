import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import mcpi.block as block

pos = mc.player.getTilePos()

for y in range(150):
    mc.setBlock(pos.x+2,pos.y+y,pos.z,block.TNT.id)
