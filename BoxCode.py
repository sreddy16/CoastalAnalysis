import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, aspect='equal')

ax2.add_patch(
     patches.Rectangle(
        (0.1, 0.1),
        0.5,
        0.5,
        fill=False      # remove background
     ) ) 
fig2.savefig(r'C:\Users\prane\Desktop\box.png', dpi=90, bbox_inches='tight')
