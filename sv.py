from moviepy.editor import*
video=VideoFileClip("C:/Users/suman/OneDrive/Desktop/ies pie/WIN_20240906_10_55_11_Pro.mp4").subclip(00,2)
video.write_gif("image.gif")