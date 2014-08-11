# -*- coding: utf-8 -*-
"""
The :mod:`pambox.speech.material` module gathers classes to facilitate
working with different speech materials.
"""
from __future__ import division, print_function, absolute_import
import os

import numpy as np
import scipy.io.wavfile
from six.moves import zip, range


class Material(object):
    """Load and manipulate speech materials for intelligibility experiments"""

    def __init__(self,
                 fs=22050,
                 root_path='../stimuli/clue',
                 path_to_sentences='sentencesWAV22',
                 path_to_maskers=None,
                 path_to_ssn='SSN_CLUE22.wav',
                 ref_level='74',
                 name='CLUE'):
        """

        """
        self.fs = fs
        self.root_path = root_path
        self.path_to_sentences = path_to_sentences
        self.path_to_maskers = path_to_maskers
        self.ref_level = ref_level
        self.name = name
        self._ssn = None
        self._path_to_ssn = None
        self.path_to_ssn = path_to_ssn

    @property
    def files(self):
        return self.files_list()

    @property
    def path_to_ssn(self):
        return self._path_to_ssn

    @path_to_ssn.setter
    def path_to_ssn(self, path):
        self._path_to_ssn = path
        self._ssn = self._load_ssn()

    def load_file(self, filename):
        """Read a speech file by name.

        Parameters
        ----------
        filename : string
            Name of the file to read. The file just be in the directory
            defined by `root_path` and `path_to_sentences`.

        Returns
        -------
        ndarray
            Wav file read from disk, as floating point array.
        """
        path = os.path.join(self.root_path, self.path_to_sentences, filename)
        _, int_sentence = scipy.io.wavfile.read(path)
        return int_sentence.T / np.iinfo(int_sentence.dtype).min

    def files_list(self):
        """Return a list of all the files in the corpus.

        :return: list of str, list of all CRM files.
        """
        return os.listdir(os.path.join(self.root_path, self.path_to_sentences))

    def load_files(self, n=None):
        """Read files from disk, starting from the first one.

        Parameters
        ----------
        n : int, optional
            Number of files to read. Default (`None`) is to read all files.

        Returns
        -------
        generator
            Generator where each item is an `ndarray` of the file loaded.
        """
        if not n:
            n = len(self.files)

        for _, name in zip(range(n), self.files):
            yield self.load_file(name)

    def _load_ssn(self):
        try:
            filepath = os.path.join(self.root_path, self._path_to_ssn)
            _, int_sentence = scipy.io.wavfile.read(filepath)
            ssn = int_sentence.T / np.iinfo(int_sentence.dtype).min
        except IOError:
            raise IOError('File not found: %s' % filepath)
        return ssn

    def ssn(self, x=None):
        """Returns the speech-shaped noise appropriate for the speech material.

        Parameters
        ----------
        x : int or ndarray, optional
            If an integer is given, returns a speech-shaped noise of length
            `n` Alternatively,  if a sentenced is given,  the speech-shaped
            noise  returned will be of the same length as the input signal.
            If `x` is `None`, the full SSN signal is returned.
        Returns
        -------
        ndarray
            Speech-shaped noise signal.
        """
        len_noise = self._ssn.shape[-1]
        if x is None:
            len_sig = len_noise
            ii = 0
        elif isinstance(x, int):
            len_sig = x
            ii = np.random.randint(len_sig, len_noise - len_sig)
        else:
            len_sig = np.asarray(x).shape[-1]
            ii = np.random.randint(len_sig, len_noise - len_sig)
        return self._ssn[..., ii:ii + len_sig]

    def set_level(self, x, level):
        """Set level of a sentence, in dB.

        Parameters
        ----------
        x : ndarray
            sentence
        level : float
            Level, in dB, at which the sentences are recorded. The reference
            is that and RMS of 1 corresponds to 0 dB SPL.

        Returns
        -------
        array_like
            Adjusted sentences with a `level` db SPL with the reference
            that a signal with an RMS of 1 corresponds to 0 db SPL.
        """
        return x * 10 ** ((level - (-self.ref_level)) / 20)





