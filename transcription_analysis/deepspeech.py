#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Some of the code below were taken from Mozilla's client.py
#
from __future__ import absolute_import, division, print_function

import argparse
import shlex
import subprocess
import sys
import wave
from timeit import default_timer as timer

import numpy as np
from deepspeech import Model, printVersions

try:
    from shhlex import quote
except ImportError:
    from pipes import quote

# These constants control the beam search decoder


# Beam width used in the CTC decoder when building candidate transcriptions
BEAM_WIDTH = 500

# The alpha hyperparameter of the CTC decoder. Language Model weight
LM_ALPHA = 0.75

# The beta hyperparameter of the CTC decoder. Word insertion bonus.
LM_BETA = 1.85

# These constants are tied to the shape of the graph used (changing them changes
# the geometry of the first layer), so make sure you use the same constants that
# were used during training

# Number of MFCC features to use
N_FEATURES = 26

# Size of the context window used for producing timesteps in the input vector
N_CONTEXT = 9


def convert_samplerate(audio_path):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate 16000 --encoding signed-integer ' \
              '--endian little --compression 0.0 --no-dither - '.format(quote(audio_path))
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use 16kHz files or install it: {}'.format(e.strerror))

    return 16000, np.frombuffer(output, np.int16)


class VersionAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        super(VersionAction, self).__init__(nargs=0, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        printVersions()
        exit(0)


def prepare_audio(audio_path):
    fin = wave.open(audio_path, 'rb')
    fs = fin.getframerate()
    if fs != 16000:
        print('Warning: original sample rate ({}) is different than 16kHz. '
              'Resampling might produce erratic speech recognition.'.format(fs), file=sys.stderr)
        fs, audio = convert_samplerate(audio_path)
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1 / 16000)
    fin.close()
    return audio, fs, audio_length


path = "/mnt/c/Users/Ameen/Development/deepspeech/models/"


class DeepSpeech:
    ds = None

    def __init__(self, modal_path=path + "output_graph.pbmm",
                 alphabet_path=path + "alphabet.txt",
                 lm_path=path + "lm.binary",
                 trie_path=path + "trie"):
        self.modal_path = modal_path
        self.alphabet_path = alphabet_path
        self.lm_path = lm_path
        self.trie_path = trie_path

    def load_modal(self):
        print('Loading model from file {}'.format(self.modal_path), file=sys.stderr)
        model_load_start = timer()
        DeepSpeech.ds = Model(self.modal_path, N_FEATURES, N_CONTEXT, self.alphabet_path, BEAM_WIDTH)
        model_load_end = timer() - model_load_start
        print('Loaded model in {:.3}s.'.format(model_load_end), file=sys.stderr)

        if self.lm_path and self.trie_path:
            print('Loading language model from files {} {}'.format(self.lm_path, self.trie_path), file=sys.stderr)
            lm_load_start = timer()
            DeepSpeech.ds.enableDecoderWithLM(self.alphabet_path, self.lm_path, self.trie_path, LM_ALPHA, LM_BETA)
            lm_load_end = timer() - lm_load_start
            print('Loaded language model in {:.3}s.'.format(lm_load_end), file=sys.stderr)

    def transcribe(self, audio_path):
        # Load modal if not loaded yet
        if not DeepSpeech.ds:
            self.load_modal()

        # Transcribe
        audio, fs, audio_length = prepare_audio(audio_path)
        print('Running inference.', file=sys.stderr)
        inference_start = timer()
        transcription = self.ds.stt(audio, fs)
        inference_end = timer() - inference_start
        print('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length), file=sys.stderr)
        return transcription

ds = DeepSpeech()
ds.load_modal()
# ds.transcribe()
