// path configuration
// FORMAT
// id: the id of the path as referenced by objects
// points: a list of points [x,y] that make up the path
// maxspeed: the max speed than an object following the path will go at
// rotatewith: whether or not an object should rotate to point towards the next point in the path

paths: [
    {
        id: "tl->tr"
        points: [[-34, 94], [542, 94]]
        maxspeed: 4
        rotatewith: true
    },
    {
        id: "tr->tl"
        points: [[540, 178], [-40, 178]]
        maxspeed: 4
        rotatewith: true
    },
    {
        id: "tl->bl"
        points: [[90, -44], [90, 754]]
        maxspeed: 8
        rotatewith: true
    },
    {
        id: "tr->br"
        points: [[410, -44], [410, 746]]
        maxspeed: 8
        rotatewith: true
    }
]