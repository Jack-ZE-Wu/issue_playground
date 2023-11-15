def select_channels(audio, n_channels, ignored_channels=None):
    """Chose the channels which want to leave or not.

    Augments
    --------
    audios : numpy.ndarray
        An 1-D audio time series.
    n_channels : int
        Number of channels.
    ignored_channels : List | None
        Select the channels which want to quit.

    Returns
    -------
    y : numpy.ndarray
        Audio time series. Multi-channel is supported.
        The output array has the format [(batch, time_steps, channels)].
    
    Examples
    --------
    >>> n_channels = 6
    >>> fake_audio = np.tile(np.arange(n_channels), 9)
    >>> y = select_channels(fake_audio, n_channels, ignored_channels=[0, 5])
    >>> y.shape
    ... (1, 9, 4)
    """
    # Tips: np.reshape(), np.ones()

    #####################
    # Inplement in here #
    #####################
    return audio

def multi_channels_selection():
    n_channels = 6
    fake_audio = np.tile(np.arange(n_channels), 9)
    y = select_channels(fake_audio, n_channels, ignored_channels=[0, 5])

    print(fake_audio)
    print(y)
    print(y.shape)

multi_channels_selection()
