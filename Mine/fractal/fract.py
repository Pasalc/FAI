# -*- coding: utf-8 -*-
import pygame as pg
import numpy as np
import math
import os
import numba
#settings
res = w,h =800,450
offset = np.array([1.3*w,h])//2
max_iter = 30
zoom = 2.2 / h

#texture
texture = pg.image.load('texture.jpg')
texture_size = min(texture.get_size())-1
texture_array=pg.surfarray.array3d(texture)

class Fractal:
    def __init__(self,app):
        self.app=app
        self.screen_array = np.full((w,h,3),[0,0,0],dtype=np.uint8)
        self.x=np.linspace(0,w,num=w,dtype=np.float32)
        self.y=np.linspace(0,h,num=h,dtype=np.float32)
    @staticmethod
    @numba.njit(fastmath=True)
    def render(screen_array,zoom,offset):
        for x in range(w):
            for y in range(h):
                c= (x-offset[0])*zoom+1j*(y-offset[1])*zoom
                z=0            
                it=0
                
                for i in range(max_iter):
                   z=z**2+c
                   if abs(z)>2:
                       break
                   it=it+1

                
                col=int(it*texture_size/max_iter)
                screen_array[x,y]=texture_array[col,col]
        return screen_array
    def update(self):
        global offset,zoom
        o_off=offset
        l_click,m_click,r_click,up_scrl,down_scrl=pg.mouse.get_pressed(num_buttons=5)
        mov=np.array(pg.mouse.get_rel())
        redraw_flag=False
        if l_click:
            offset=offset+mov
            redraw_flag=True
        if r_click:
            offset=np.array([1.3*w,h])//2
            redraw_flag=True
        if m_click:
            zoom = 2.2 / h
            redraw_flag=True
        elif up_scrl or down_scrl:
            up_scrl=int(up_scrl)
            down_scrl=int(down_scrl)
            rel_zoom=zoom*(down_scrl-up_scrl)/10
            
            center=(np.array([w,h])/2.0-offset)*zoom
            zoom=zoom+rel_zoom
            offset=-(center-np.array([w,h])*zoom/2.)/zoom
            redraw_flag=True
        if(redraw_flag):
            Fractal.render(self.screen_array,zoom,offset)
    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)
    def run(self):
        self.update()
        self.draw()
        
class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res,pg.SCALED)
        self.clock = pg.time.Clock()
        self.fract=Fractal(self)
        
    def run(self):
        self.fract.render(self.fract.screen_array,zoom,offset)
        while True:
            [os._exit(i.type) for i in pg.event.get() if i.type == pg.QUIT]
            
            self.screen.fill('black')
            self.fract.run()
            pg.display.flip()
            
            self.clock.tick()
            pg.display.set_caption(f'fps: {self.clock.get_fps()}')

if __name__ == '__main__':
    
    app=App()
    app.run()
            