#!/usr/bin/python
from moviepy.editor import *
import click
@click.command()
@click.option('--input','-i','inp',required=True,type=str)
@click.option('--rate','-r',default=1,type=float)
@click.option('--output','-o',default='output.mp4',type=str)
def convert_video(inp,rate,output):
    clip = VideoFileClip(inp)
    modded_clip = clip.speedx(rate)
    modded_clip.write_videofile(output)
if __name__ == '__main__':
    convert_video()
