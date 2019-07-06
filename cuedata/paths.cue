// path configuration
// FORMAT
// id: the id of the path as referenced by objects
// points: a list of points [x,y] that make up the path
// maxspeed: the max speed than an object following the path will go at
// rotatewith: whether or not an object should rotate to point towards the next point in the path

paths: [
    {
        id: "topu"
        points: [[38, -60], [38, 10], [76, 144], [164, 252], [246, 296], [376, 266], [442, 120], [460, 24], [460, -100]]
        maxspeed: 3
        rotatewith: true
    },
    {
        id: "toptsu"
        points: [[-50, 54], [108, 54], [296, 76], [394, 140], [432, 186], [464, 250], [428, 334], [320, 396], [104, 424], [-72, 424]]
        maxspeed: 3
        rotatewith: true
    },
    {
        id: "L"
        points: [[66, -58], [66, 46], [92, 228], [198, 330], [372, 364], [526, 364], [600, 364]]
        maxspeed: 3
        rotatewith: true
    },
    {
        id: "J"
        points: [[452, -38], [446, 82], [400, 244], [250, 326], [62, 360], [-110, 360]]
        maxspeed: 3
        rotatewith: true
    },
    {
        id: "loop"
        points: [[-52, 202], [90, 202], [240, 192], [348, 166], [428, 98], [464, 10], [464, -72], [244, -110], [136, -110], [136, 8], [156, 98], [246, 188], [368, 298], [494, 332], [604, 332]]
        maxspeed: 5
        rotatewith: true
    },
    {
        id: "leftbottomup"
        points: [[60, 788], [60, 632], [108, 414], [266, 212], [420, 96], [554, 38]]
        maxspeed: 5
        rotatewith: true
    },
    {
        id: "oof de loop"
        points: [[-84, 294], [94, 294], [96, 294], [98, 294], [276, 294], [328, 284], [376, 258], [406, 224], [424, 176], [424, 120], [408, 68], [340, 40], [272, 40], [204, 64], [164, 130], [150, 204], [182, 288], [250, 352], [336, 404], [430, 432], [554, 432]]
        maxspeed: 3
        rotatewith: true
    },
    {
        id: "tl to br"
        points: [[-42, -46], [40, 38], [194, 224], [320, 440], [412, 636], [466, 784]]
        maxspeed: 2
        rotatewith: true
    },
    {
        id: "tr to bl"
        points: [[546, -48], [480, 14], [366, 170], [214, 344], [80, 528], [-22, 696]]
        maxspeed: 2
        rotatewith: true
    }
]