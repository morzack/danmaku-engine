#!/usr/bin/bash

cue export cuedata/configuration.cue > data/configuration.json
cue export cuedata/paths.cue > data/paths.json
cue export cuedata/enemies.cue > data/enemies/enemies.json
cue export cuedata/playerconfig.cue > data/playerdata/playerconfig.json
cue export cuedata/bullets.cue > data/bullets/bullets.json

cue export cuedata/level0.cue > data/levels/0/enemies.json