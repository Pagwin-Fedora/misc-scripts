#!/usr/bin/python
#written to make it possible to speed up and slowdown videos(whiel I don't use this at all I do find it kinda elegant how few lines I wrote it in and how nice it kinda just looks)
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
