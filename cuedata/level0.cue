// level configuration
// audio configuration
soundfile: "l0bgm"

// DEFAULTS
types: {
    wall: {
        homing: "testhomingwall"
        thicc: "testhomingthiccwall"
    }
    circle: {
        default: "testcircle"
        hyper: "hypertestcircle"
    }
    line: {
        default: "testhoming"
        hyper: "hypertesthoming"
    }
}
paths: {
    a: "tl->tr"
    b: "tr->tl"
    c: "tl->bl"
    d: "tr->br"
}
waves: {
    a: {
        starttime: 140
        endtime: 800
        path: paths.a
        spacing: 21
    }
    b: {
        starttime: 300
        endtime: 800
        path: paths.b
        spacing: 21
    }
    c: {
        starttime: 658
        endtime: 1200
        path: paths.c
        spacing: 8
    }
    d: {
        starttime: 658
        endtime: 1200
        path: paths.d
        spacing: 8
    }
    e: {
        starttime: 830
        endtime: 1600
        path: paths.a
        spacing: 21
    }
    f: {
        starttime: 995
        endtime: 1600
        path: paths.b
        spacing: 21
    }
    g: {
        starttime: 1340
        endtime: 1600
        path: paths.c
        spacing: 8
    }
    h: {
        starttime: 1340
        endtime: 1600
        path: paths.d
        spacing: 8
    }
}

// enemy declarations
enemies: [
    {
        wave: waves.a
        type: types.wall.homing
    },
    {
        wave: waves.a
        type: types.circle.default
    },
    {
        wave: waves.a
        type: types.line.default
    },
    {
        wave: waves.b
        type: types.wall.homing
    },
    {
        wave: waves.b
        type: types.circle.default
    },
    {
        wave: waves.b
        type: types.line.default
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.circle.hyper
    },
    {
        wave: waves.c
        type: types.line.default
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.circle.hyper
    },
    {
        wave: waves.d
        type: types.line.default
    },
    {
        wave: waves.e
        type: types.wall.homing
    },
    {
        wave: waves.e
        type: types.circle.default
    },
    {
        wave: waves.e
        type: types.line.default
    },
    {
        wave: waves.f
        type: types.wall.homing
    },
    {
        wave: waves.f
        type: types.circle.default
    },
    {
        wave: waves.f
        type: types.line.default
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.circle.hyper
    },
    {
        wave: waves.g
        type: types.line.default
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.circle.hyper
    },
    {
        wave: waves.h
        type: types.line.default
    }
]