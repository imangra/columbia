#%%
import cv2
import numpy as np

width = 1920  
height = 1080  
duration = 1 
fps = 30  

num_frames = duration * fps

frames = []
for i in range(num_frames):
    intensity = 255 * (1 - np.abs(2 * (i / num_frames) - 1))

    frame = np.ones((height, width, 3), dtype=np.uint8) * int(intensity)
    
    frames.append(frame)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('flash_transition.mp4', fourcc, fps, (width, height))

for frame in frames:
    out.write(frame)

out.release()

print("Flash transition video saved as 'flash_transition.mp4'")

# %%
import cv2
import numpy as np

width = 1920  
height = 1080 
duration = 5  
fps = 30  

num_frames = duration * fps

def generate_bokeh_circle(frame):
    radius = np.random.randint(20, 100)
    x = np.random.randint(0, width)
    y = np.random.randint(0, height)
    color = np.random.randint(0, 256, size=3).tolist()
    alpha = np.random.uniform(0.3, 0.7)

    overlay = frame.copy()
    cv2.circle(overlay, (x, y), radius, color, -1)

    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

frames = []
for i in range(num_frames):
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    for _ in range(10): 
        generate_bokeh_circle(frame)

    frames.append(frame)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('colorful_bokeh_overlay.mp4', fourcc, fps, (width, height))

for frame in frames:
    out.write(frame)

out.release()

print("Colorful bokeh overlay video saved as 'colorful_bokeh_overlay.mp4'")




# %%
import cv2
import numpy as np

width = 1920  
height = 1080  
duration = 5 
fps = 30  

num_frames = duration * fps

def generate_textured_green(frame, coverage):
    texture_size = 50
    num_squares = int(coverage * (width // texture_size) * (height // texture_size))
    for _ in range(num_squares):
        x = np.random.randint(0, width // texture_size) * texture_size
        y = np.random.randint(0, height // texture_size) * texture_size
        color = (0, np.random.randint(100, 256), 0)  
        frame[y:y+texture_size, x:x+texture_size] = color

frames = []
for i in range(num_frames):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    coverage = i / num_frames
    
    if coverage > 0.8:
        frame[:] = (0, 255, 0)  # Full green flash
    else:
        generate_textured_green(frame, coverage)

    frames.append(frame)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('textured_green_flash_overlay.mp4', fourcc, fps, (width, height))

for frame in frames:
    out.write(frame)

out.release()

print("Textured green flash overlay video saved as 'textured_green_flash_overlay.mp4'")

# %%

