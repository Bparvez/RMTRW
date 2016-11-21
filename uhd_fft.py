#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: UHD FFT
# Author: Bilal
# Description: UHD FFT Waveform Plotter
# Generated: Mon Nov 21 10:12:07 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import time


class uhd_fft(gr.top_block):

    def __init__(self, antenna="RX2", args="fpga=usrp1_fpga_4rx.rbf ", fft_size=1024, freq=2.412e9, gain=45, maxrate=0, samp_rate=10e6, spec="A:0", stream_args="", update_rate=.1, wire_format=""):
        gr.top_block.__init__(self, "UHD FFT")

        ##################################################
        # Parameters
        ##################################################
        self.antenna = antenna
        self.args = args
        self.fft_size = fft_size
        self.freq = freq
        self.gain = gain
        self.maxrate = maxrate
        self.samp_rate = samp_rate
        self.spec = spec
        self.stream_args = stream_args
        self.update_rate = update_rate
        self.wire_format = wire_format

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((args, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec(spec, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(float(freq), 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.fft_vcc_0 = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1024, -60)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1024, 100)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1024, "/home/bilal/Desktop/RMTRW/value", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1024)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vcc_0, 0))    
        self.connect((self.fft_vcc_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_stream_to_vector_0, 0))    

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna

    def get_args(self):
        return self.args

    def set_args(self, args):
        self.args = args

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(float(self.freq), 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        	

    def get_maxrate(self):
        return self.maxrate

    def set_maxrate(self, maxrate):
        self.maxrate = maxrate

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)

    def get_spec(self):
        return self.spec

    def set_spec(self, spec):
        self.spec = spec

    def get_stream_args(self):
        return self.stream_args

    def set_stream_args(self, stream_args):
        self.stream_args = stream_args

    def get_update_rate(self):
        return self.update_rate

    def set_update_rate(self, update_rate):
        self.update_rate = update_rate

    def get_wire_format(self):
        return self.wire_format

    def set_wire_format(self, wire_format):
        self.wire_format = wire_format


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-A", "--antenna", dest="antenna", type="string", default="RX2",
        help="Set Antenna [default=%default]")
    parser.add_option(
        "-a", "--args", dest="args", type="string", default="fpga=usrp1_fpga_4rx.rbf ",
        help="Set UHD device address args [default=%default]")
    parser.add_option(
        "", "--fft-size", dest="fft_size", type="intx", default=1024,
        help="Set Set number of FFT bins [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.412e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(45),
        help="Set Set gain in dB (default is midpoint) [default=%default]")
    parser.add_option(
        "", "--maxrate", dest="maxrate", type="intx", default=0,
        help="Set max [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(10e6),
        help="Set Sample Rate [default=%default]")
    parser.add_option(
        "", "--spec", dest="spec", type="string", default="A:0",
        help="Set Subdev [default=%default]")
    parser.add_option(
        "", "--stream-args", dest="stream_args", type="string", default="",
        help="Set Set additional stream args [default=%default]")
    parser.add_option(
        "", "--update-rate", dest="update_rate", type="eng_float", default=eng_notation.num_to_str(.1),
        help="Set Set GUI widget update rate [default=%default]")
    parser.add_option(
        "", "--wire-format", dest="wire_format", type="string", default="",
        help="Set Wire format [default=%default]")
    return parser


def main(top_block_cls=uhd_fft, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(antenna=options.antenna, args=options.args, fft_size=options.fft_size, freq=options.freq, gain=options.gain, maxrate=options.maxrate, samp_rate=options.samp_rate, spec=options.spec, stream_args=options.stream_args, update_rate=options.update_rate, wire_format=options.wire_format)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
