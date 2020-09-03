__all__ = ['add_Peccerillo_fields']


class MissingModuleException(Exception):
    pass


# Plot Peccerillo and Taylor (1976) lines
def add_Peccerillo_fields(plot_axes, fontsize=8, color=(0.6, 0.6, 0.6)):
    """Add fields for geochemical classifications from Peccerillo and Taylor(1976)
    to pre-existing axes.  If necessary, the axes object can be retrieved via
    plt.gca() command. e.g.

    ax1 = plt.gca()
    add_Peccerillo_fields(ax1)
    ax1.plot(silica, total_alkalis, 'o')

    Fontsize and color options can be used to change from the defaults.

    It may be necessary to follow the command with plt.draw() to update
    the plot.

    Peccerillo A, Taylor SR (1976) Geochemistry of Eocene Calc-Alkaline Volcanic
        Rocks from the Kastamonu Area, Northern Turkey. Contributions to Mineralogy
        and Petrology 58, 63-81.
"""

    # Check matplotlib is imported
    import sys
    if 'matplotlib.pyplot' not in sys.modules:
        raise MissingModuleException("""Matplotlib not imported.
        Matplotlib is installed as part of many scientific packages and is
        required to create plots.""")

    # Check that plot_axis can plot
    if 'plot' not in dir(plot_axes):
        raise TypeError('plot_axes is not a matplotlib axes instance.')

    # Prepare the field information
    from collections import namedtuple
    from collections import namedtuple
    FieldLine = namedtuple('FieldLine', 'x1 y1 x2 y2')
    lines = (FieldLine(x1=45, y1=0.2, x2=70, y2=1.3),
              FieldLine(x1=45, y1=0.85, x2=70, y2=3),
              FieldLine(x1=45, y1=1.0, x2=56, y2=3.2),
              FieldLine(x1=56, y1=3.2, x2=70, y2=4.8))

    FieldName = namedtuple('FieldName', 'name x y rotation')
    names = (FieldName('Low K Calc-Alkaline\nSeries/Tholeite Series', 65, 0.7, 0),
             FieldName('Calc-alkaline\nSeries', 67, 2.2, 0),
             FieldName('High K Calc-alkaline\nSeries', 65, 3.5, 0),
             FieldName('Shoshonite Series', 48, 3.8, 0))

    # Plot the lines and fields
    for line in lines:
        plot_axes.plot([line.x1, line.x2], [line.y1, line.y2],
                       '-', color=color, zorder=0)
    for name in names:
        plot_axes.text(name.x, name.y, name.name, color=color, size=fontsize,
                       horizontalalignment='center', verticalalignment='top',
                       rotation=name.rotation, zorder=0)