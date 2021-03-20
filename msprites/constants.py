
FFMPEG_THUMBNAIL_IMAGES = """
    ffmpeg -loglevel error -i {input} -vf fps={ips} -s {width}x{height} {output}
"""
# ffmpeg -i ~/Downloads/SampleVideo_360x240_20mb.mp4 -vf fps=1/24 -s 128x72 sprites/images/%d.png

THUMBNAIL_SPRITESHEET = """
    montage -background '#336699' -tile {rows}x{cols} -geometry {width}x{height}+0+0 {input}/* {output}
"""
# magick montage -background '#336699' -tile {rows}x{cols} -geometry {width}x{height}+0+0 {input}/* {output}