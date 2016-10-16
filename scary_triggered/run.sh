#!/bin/bash

sudo sh -c "TERM=linux setterm -foreground black -clear all >/dev/tty0"
python run.py
