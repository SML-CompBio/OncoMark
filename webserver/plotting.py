import numpy as np

def check_if_matplotlib(return_mpl=False):
    if not return_mpl:
        try:
            import matplotlib.pyplot as plt
        except Exception:
            raise ImportError('matplotlib is not installed. Please install it with: pip install matplotlib')
        return plt
    else:
        try:
            import matplotlib as mpl
        except Exception:
            raise ImportError('matplotlib is not installed. Please install it with: pip install matplotlib')
        return mpl


def check_if_seaborn():
    try:
        import seaborn as sns
    except Exception:
        raise ImportError('seaborn is not installed. Please install it with: pip install seaborn')
    return sns

def set_limits(vmin, vcenter, vmax, values):

    if vmin is None:
        vmin = values.min()

    if vmax is None:
        vmax = values.max()

    if vcenter is None:
        vcenter = values.mean()

    if vmin >= vcenter:
        vmin = -vmax

    if vcenter >= vmax:
        vmax = -vmin

    return vmin, vcenter, vmax

def plot_barplot(acts, contrast, top=25, vertical=False, cmap='coolwarm', vmin=None, vcenter=0, vmax=None,
                 figsize=(7, 5), dpi=100, ax=None, return_fig=False):
    """
    Plot barplots showing the top absolute value activities.

    Parameters
    ----------
    acts : DataFrame
        Activities obtained from any method.
    contrast : str
        Name of the contrast (row) to plot.
    top : int
        Number of top features to plot.
    vertical : bool
        Whether to plot verticaly or horizontaly.
    cmap : str
        Colormap to use.
    vmin : float, None
        The value representing the lower limit of the color scale.
    vcenter : float, None
        The value representing the center of the color scale.
    vmax : float, None
        The value representing the upper limit of the color scale.
    figsize : tuple
        Figure size.
    dpi : int
        DPI resolution of figure.
    ax : Axes, None
        A matplotlib axes object. If None returns new figure.
    return_fig : bool
        Whether to return a Figure object or not.
    save : str, None
        Path to where to save the plot. Infer the filetype if ending on {``.pdf``, ``.png``, ``.svg``}.

    Returns
    -------
    fig : Figure, None
        If return_fig, returns Figure object.
    """

    # Load plotting packages
    sns = check_if_seaborn()
    plt = check_if_matplotlib()
    mpl = check_if_matplotlib(return_mpl=True)

    # Check for non finite values
    if np.any(~np.isfinite(acts)):
        raise ValueError('Input acts contains non finite values.')

    # Process df
    df = acts.loc[[contrast]]
    df.index.name = None
    df.columns.name = None
    df = (df

          # Sort by absolute value and transpose
          .iloc[:, np.argsort(abs(df.values))[0]].T

          # Select top features and add index col
          .tail(top).reset_index()

          # Rename col
          .rename({contrast: 'acts'}, axis=1)

          # Sort by activities
          .sort_values('acts'))

    if vertical:
        x, y = 'acts', 'index'
    else:
        x, y = 'index', 'acts'

    # Plot
    fig = None
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize, dpi=dpi)
    sns.barplot(data=df, x=x, y=y, ax=ax)

    if vertical:
        sizes = np.array([bar.get_width() for bar in ax.containers[0]])
        ax.set_xlabel('Activity')
        ax.set_ylabel('')
    else:
        sizes = np.array([bar.get_height() for bar in ax.containers[0]])
        ax.tick_params(axis='x', rotation=90)
        ax.set_ylabel('Activity')
        ax.set_xlabel('')

    # Compute color limits
    vmin, vcenter, vmax = set_limits(vmin, vcenter, vmax, df['acts'])

    # Rescale cmap
    divnorm = mpl.colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
    cmap_f = plt.get_cmap(cmap)
    div_colors = cmap_f(divnorm(sizes))
    for bar, color in zip(ax.containers[0], div_colors):
        bar.set_facecolor(color)

    # Add legend
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=divnorm)
    sm.set_array([])
    ax.get_figure().colorbar(sm, ax=ax)

    if return_fig:
        return fig
