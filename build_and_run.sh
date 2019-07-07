#!/usr/bin/bash
export SDL_AUDIODRIVER=alsa
export AUDIODEV=pulse

./generate_configs.sh
python main.py
