from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

# здесь ввести текст
user_text = "Привет, Лев Камбек! Как твои дела?"

# настраиваем видеоклип
size = (100, 100)
duration = 3
color = (234, 68, 247)
clip = ColorClip(size, color, duration=duration)

# настраиваем текстовый блок
font = 'Arial'
text_clip = TextClip(user_text, fontsize=70, color="white", font=font)
text_clip = text_clip.set_pos("left").set_duration(duration)
text_width = text_clip.w

# чем больше время, тем дальше по оси икс в сторону отрицательной бесконечности
def scroll(t):
    x_pos = text_width - t * text_width
    return (x_pos, 'center')

# скроллим
text_clip = text_clip.set_pos(scroll)

# совмещаем в клип
video = CompositeVideoClip([clip, text_clip])

# пишем в файл
video.write_videofile("./sticker_export.mp4", fps=24)