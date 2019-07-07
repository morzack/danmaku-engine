//bullet configuration
// IMAGES
images: {
    bullets: {
        green: "greenblob"
    }
    circles: {
        red: "redcircle"
    }
}

// PARAMS
// speed: the speed of the bullet
// radius: the radius of the hitbox and image
// image_location: the name of the image file in the bullet image dir
// locking: whether or not the bullet starts off heading towards the player
// imagespinrate (OPTIONAL): rate at which to rotate the image

bullets: {
    basichoming: {
        speed: 2
        radius: 5
        image_location: images.bullets.green
        locking: true
    }

    basicnondirectional: {
        speed: 1.5
        radius: 10
        image_location: images.circles.red
        locking: false
    }
    
    hypernondirectional: {
        speed: 3
        radius: 10
        image_location: images.circles.red
        locking: false
    }

    hyperhoming: {
        speed: 3
        radius: 7
        image_location: images.bullets.green
        locking: true
    }

    playerbullet: {
        speed: 20
        radius: 8
        image_location: "playerbullet"
        locking: false
    }
}
