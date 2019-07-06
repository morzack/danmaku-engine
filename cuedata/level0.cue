// level configuration
// DEFAULTS
types: {
    wall: {
        homing: "testhomingwall"
    }
    circle: {
        default: "testcircle"
    }
    line: {
        default: "testhoming"
        hyper: "hypertesthoming"
    }
}
paths: {
    u: "topu"
    tsu: "toptsu"
    l: "L"
    j: "J"
    loop: "loop"
    blup: "leftbottomup"
    oofloop: "oof de loop" // what even
}
waves: {
    a: {
        starttime: 100
        endtime: 800
        path: paths.u
        spacing: 30
    }
    b: {
        starttime: 220
        endtime: 800
        path: paths.tsu
        spacing: 30
    }
    c: {
        starttime: 800
        endtime: 1600
        path: paths.l
        spacing: 20
    }
    d: {
        starttime: 900
        endtime: 1600
        path: paths.j
        spacing: 20
    }
    e: {
        starttime: 1400
        endtime: 2000
        path: paths.j
        spacing: 40
    }
    f: {
        starttime: 1400
        endtime: 2000
        path: paths.l
        spacing: 40
    }
    g: {
        starttime: 1810
        endtime: 2400
        path: paths.loop
        spacing: 10
    }
    h: {
        starttime: 1950
        endtime: 2400
        path: paths.blup
        spacing: 10
    }
    i: {
        starttime: 2210
        endtime: 3000
        path: paths.oofloop
        spacing: 10
    }
}

// enemy declarations
enemies: [
    {
        wave: waves.a
        type: types.wall.homing
    },
    {
        wave: waves.a,
        type: types.circle.default
    },
    {
        wave: waves.a,
        type: types.line.default
    },
    {
        wave: waves.b
        type: types.line.default
    },
    {
        wave: waves.b,
        type: types.circle.default
    },
    {
        wave: waves.b,
        type: types.wall.homing
    },
    {
        wave: waves.b,
        type: types.circle.default
    },
    {
        wave: waves.b,
        type: types.line.default
    },
    {
        wave: waves.c,
        type: types.line.default
    },
    {
        wave: waves.c,
        type: types.wall.homing
    },
    {
        wave: waves.c
        type: types.wall.homing
    },
    {
        wave: waves.c
        type: types.circle.default
    },
    {
        wave: waves.d
        type: types.line.default
    },
    {
        wave: waves.d
        type: types.wall.homing
    },
    {
        wave: waves.d
        type: types.wall.homing
    },
    {
        wave: waves.d
        type: types.circle.default
    },
    {
        wave: waves.e
        type: types.line.hyper
    },
    {
        wave: waves.e
        type: types.circle.default
    },
    {
        wave: waves.f
        type: types.line.hyper
    },
    {
        wave: waves.f
        type: types.circle.default
    },
    {
        wave: waves.g
        type: types.line.hyper
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.circle.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.wall.homing
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.circle.default
    },
    {
        wave: waves.i
        type: types.wall.homing
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.line.default
    },
    {
        wave: waves.i
        type: types.circle.default
    }
]