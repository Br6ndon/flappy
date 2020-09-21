"""
Title:
Creator: Brandon White
Description: A Flappy bird clone with ufos
"""


# Setup
info.set_score(0)

info.set_life(1)
#TODO add background
#TODO add. clouds effect
 # Create the death objects

ufo = sprites.create(img("""
    . . f f f f . . . . . . . . . .
    . f f 2 7 2 f . . . . . . . . .
    f f 2 7 2 7 2 f . . . . . . . .
    f 2 7 2 7 2 f f . . . . . . . .
    . f 2 7 2 f f . . . . . . . . .
    . . f f f f . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
ufo.ay = 100
ufo.x = 40 
def on_flap():
    ufo.vy = -75 
controller.A.on_event(ControllerButtonEvent.PRESSED, on_flap)

def on_update():
    y = ufo.y

    if y > scene.screen_height():
      death()
    elif y < 0: 
      ufo.y = 0
game.on_update(on_update)

def death():
    info.change_life_by(-1)
    ufo.y = scene.screen_height()/2



scene.set_background_color(9)



building1_top = sprites.create_projectile_from_side(img("""
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffffffffffff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......ffffffffffffffffffffffffffffffff11111ff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffffffffffff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......f11111ffffffffffffffffffffffffff11111ff....
    .......ffffffffffffffffffffffffffffffff11111ff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......fffffffffffffffffffffffffffffff11111fff....
    .......fffffffffffffffffffffffffffffff11111fff....
    .......fffffffffffffffffffffffffffffff11111fff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......f11111fffffffffffffffffffffffff11111fff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......fffffffffffffffffffffffffffffffffffffff....
    .......ffffffffffffffffffbbbffffffffffffffffff....
    .......ffffffffffffffffffbb5ffffffffffffffffff....
    .......ffffffffffffffffffbbbffffffffffffffffff....
"""), -50, 0)
building2_bottom = sprites.create_projectile_from_side(img("""
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ...........................................................................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................fffffffffffffffffffffffff..............................
    ....................fffffffffffffffffffffffff..............................
    ....................f11111fffffffffffffffffff..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................f11111fffffffffffff11111f..............................
    ....................ffffffffffffbbbffff11111f..............................
    ....................ffffffffffffbb5ffffffffff..............................
    ....................ffffffffffffbbbffffffffff..............................
"""), -50, -0)
building2_bottom.y =100

building4_top = sprites.create_projectile_from_side(img("""
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........f11111ffffffffffffffffffffff..............
    ........f11111fffffffffffffff11111ff..............
    ........f11111fffffffffffffff11111ff..............
    ........f11111fffffffffffffff11111ff..............
    ........f11111fffffffffffffff11111ff..............
    ........fffffffffffffffffffff11111ff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........fffff11111ffffffffffffffffff..............
    ........fffff11111fffffffff11111ffff..............
    ........fffff11111fffffffff11111ffff..............
    ........fffff11111fffffffff11111ffff..............
    ........fffff11111fffffffff11111ffff..............
    ........fffffffffffffffffff11111ffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ff11111fffffffffffffffffffff..............
    ........ff11111ffffffffffffff11111ff..............
    ........ff11111ffffffffffffff11111ff..............
    ........ff11111ffffffffffffff11111ff..............
    ........ff11111ffffffffffffff11111ff..............
    ........fffffffffffffffffffff11111ff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffff11111fffffffffff11111fff..............
    ........ffff11111fffffffffff11111fff..............
    ........ffff11111fffffffffff11111fff..............
    ........ffff11111fffffffffff11111fff..............
    ........ffff11111fffffffffff11111fff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffffffffffffffffff..............
    ........ffffffffffffbbbfffffffffffff..............
    ........ffffffffffffbb5fffffffffffff..............
    ........ffffffffffffbbbfffffffffffff..............
"""), -30, 0)
building5_bottom = sprites.create_projectile_from_side(img("""
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................................................................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................ff11111fffffffffffffff11111ff...................
    .................fffffffffffffffffffffffffffff...................
    .................fffffffffffffffffffffffffffff...................
    .................ffffffffffffbbbbbffffffffffff...................
    .................ffffffffffffbbbbbffffffffffff...................
    .................ffffffffffffbbbb5ffffffffffff...................
    .................ffffffffffffbbbbbffffffffffff...................
"""), -30, -0)
building5_bottom.y =100
scene.set_background_image(img("""
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
"""))
info.player1.score()



