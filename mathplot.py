import matplotlib.pyplot as plt
slices=[7,2,2,13]
activity=['sleeping','eating','working','playing']

cols=['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activity,
        colors=cols,
        startangle=90,
        shadow = True,
        explode = (0.1,0,0,0),
        autopot = '%1.1f%%')
plt.title
plt.show()

