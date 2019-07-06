// enemies configuration file
defaults: { 
    // sizes
    smallenemy: {
        width: 30
        height: 30
        hitbox: 15
    }
    mediumenemy: {
        width: 40
        height: 40
        hitbox: 20
    }
    largeenemy: {
        width: 60
        height: 60
        hitbox: 30
    }

    // shooting patterns
    slowline: {
        shootrate: 60
        shootingpattern: "line"
        bullets: 5
    }
    fastline: {
        shootrate: 30
        shootingpattern: "line"
        bullets: 3
    }
    slowcircle: {
        shootrate: 80
        shootingpattern: "circle"
        bullets: 10
    }
    fastcircle: {
        shootrate: 40
        shootingpattern: "circle"
        bullets: 7
    }
    slowwall: {
        shootrate: 70
        shootingpattern: "wall"
        bullets: 3
    }
    fastwall: {
        shootrate: 50
        shootingpattern: "wall"
        bullets: 2
    }
}

// IMAGES
images: {
    homing: {
        green: "g1"
        blue: "b2"
    }
    tank: {
        green: "g2"
        blue: "b1"
    }
}

// ENEMIES
enemies: {
    hypertesthoming: {
        size: defaults.mediumenemy
        shotpattern: defaults.fastline
        bullettype: "hyperhoming"
        image: images.homing.green
        health: 7
    }
    testcircle: {
        size: defaults.mediumenemy
        shotpattern: defaults.slowcircle
        bullettype: "basicnondirectional"
        image: images.tank.blue
        health: 15
    }
    testhoming: {
        size: defaults.mediumenemy
        shotpattern: defaults.slowline
        bullettype: "basichoming"
        image: images.homing.blue
        health: 5
    }
    testhomingwall: {
        size: defaults.mediumenemy
        shotpattern: defaults.slowwall
        bullettype: "basicnondirectional"
        image: images.tank.green
        health: 15
    }
}
