import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")     #背景画像のsurface
    bg_img2=pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")         #こうかとんのsurface
    kk_img=pg.transform.flip(kk_img,True,False) #こうかとんの左右反転
    kk_rect=kk_img.get_rect()                   #こうかとん画像のrect
    kk_rect.center = 300,200                    #こうかとん画像の中心画像確定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed()        #キーの押下状態を取得
        if key_list[pg.K_UP]:
            kk_rect.move_ip((0,-1))
        elif key_list[pg.K_DOWN]:
            kk_rect.move_ip((0,1))
        elif key_list[pg.K_LEFT]:
            kk_rect.move_ip((-1,0))
        elif key_list[pg.K_RIGHT]:
            kk_rect.move_ip((1,0))
        

        x=tmr%3200
        screen.blit(bg_img, [-x, 0])     #1枚目
        screen.blit(bg_img2,[-x+1600,0]) #2枚目
        screen.blit(bg_img,[-x+3200,0])  #3枚目
        screen.blit(kk_img, kk_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()