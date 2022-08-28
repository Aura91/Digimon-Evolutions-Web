label battles_dober:
    screen simple_stats_screen:
        frame:
            xalign 0.99 yalign 0.05
            vbox:
                text "[s]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value blanc_hp
                        range blanc_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                    
                    null width 5
                
                    text "[blanc_hp] / [blanc_max_hp]" size 16
                
                
        frame:
            xalign 0.01 yalign 0.05
            vbox:
                text "Dobermon" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value dober_hp
                        range dober_max_hp
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                    
                    null width 5
                
                    text "[dober_hp] / [dober_max_hp]" size 16
                
        text "FIGHT!!!" xalign 0.5 yalign 0.05 size 30

# The game starts here.
label startbattle_1:
    $ dober_max_hp = 80
    $ blanc_max_hp = 50
    $ dober_hp = dober_max_hp
    $ blanc_hp = blanc_max_hp
    $ cookies_left = 10


label battle_1:

    call dice
    
    scene field:
        zoom 1.9
    show screen simple_stats_screen

    show sistermon mad at right:
            zoom 1.0
    show dobermon at left
    with fade
    
    while (dober_hp > 0) and (blanc_hp > 0):
        $ renpy.block_rollback()
        show sistermon mad at right:
            zoom 1.0
        show dobermon at left
        
        menu:
            "Attack":
                $ renpy.block_rollback()
                show sistermon attack at center:
                        zoom 1.3
                with moveinleft
                if d10 >= 10:        #30% chance
                    $ blanc_damage = d4+d6
                    $ dober_hp -= blanc_damage
                    "Critical Hit! ([s] did [blanc_damage] damage!)"
                else:
                    $ dober_hp -= d4
                    "([s] did [d4] damage!)"
            
            "Divine Pierce (Accuracy: 70)":
                show sistermon attack at center:
                        zoom 1.3
                with moveinleft
                show dobermon
                with glowing
                if d10 >= 9:            #20% chance
                    $ blanc_damage = (d6 + d4)*2
                    $ dober_hp -= blanc_damage
                    "Pierced damage! ([s] did [blanc_damage] damage!)"
                
                elif d10 >= 4:          #50%
                    $ blanc_damage = d4*2
                    $ dober_hp -= blanc_damage
                    "Direct hit! ([s] did [blanc_damage] damage!)"
                else:                   #30%
                    "[s] missed!"
                
            "Heal I([cookies_left] uses left)" if cookies_left > 0:
                $ renpy.block_rollback()
                $ blanc_hp = min(blanc_hp+10, blanc_max_hp)
                $ cookies_left -= 1
                show sistermon happy:
                    zoom 1.1
                with healglow
                s "Restored 10hp"
        
        if dober_hp <= 0:
            $ flagbattle = 1
            $ renpy.block_rollback()
            hide screen simple_stats_screen
            jump after_battle_dober
        else:
            pass
        
        
        $ dober_damage = renpy.random.randint(5, 7)
        
        $ blanc_hp -= dober_damage
        $ renpy.block_rollback()
        show sistermon shocked at right:
            zoom 1.0
        show dobermon at center
        with moveinright
        show sistermon cry at right:
            zoom 1.0
        "[d] used Black Beam! \n(Damage dealt-[dober_damage]hp!)"
        call dice
        if blanc_hp <= 0:
            "You lost!"
            $ flagbattle = 0
            $ renpy.block_rollback()
            hide screen simple_stats_screen
            jump gameover
        else: 
            pass

label after_battle_dober:
    hide dobermon
    show sistermon happy at right:
        zoom 1.1
    with fade
    s "We won!"