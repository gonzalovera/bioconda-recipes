#!/usr/bin/env python

import os
import shutil
import sys

"""
This script produces for every binary a new shell script similar to:

--------------------------------------------
#!/bin/bash

export EMBOSS_ACDROOT=../share/EMBOSS/acd/
export EMBOSS_DATA=../share/EMBOSS/data
export PLPLOT_LIB=../share/EMBOSS

_water "$@"

--------------------------------------------

Run this script on the binary directory of EMBOSS tools:

    python fix_acd_path.py $PREFIX/bin/

"""

EMBOSS_BINARIES = [
    'aaindexextract',
    'abiview',
    'acdc',
    'acdpretty',
    'acdtable',
    'acdtrace',
    'acdvalid',
    'antigenic',
    'backtranambig',
    'backtranseq',
    'banana',
    'bdftogd',
    'biosed',
    'btwisted',
    'cai',
    'chaos',
    'charge',
    'checktrans',
    'chips',
    'cirdna',
    'codcmp',
    'codcopy',
    'coderet',
    'compseq',
    'cons',
    'cpgplot',
    'cpgreport',
    'cusp',
    'cutgextract',
    'cutseq',
    'dan',
    'dbiblast',
    'dbifasta',
    'dbiflat',
    'dbigcg',
    'dbxfasta',
    'dbxflat',
    'dbxgcg',
    'degapseq',
    'descseq',
    'diffseq',
    'digest',
    'distmat',
    'dotmatcher',
    'dotpath',
    'dottupv',
    'dreg',
    'edialign',
    'einverted',
    'embossdata',
    'embossversion',
    'emma',
    'emowse',
    'entret',
    'epestfind',
    'eprimer3',
    'equicktandem',
    'est2genome',
    'etandem',
    'extractalign',
    'extractfeat',
    'extractseq',
    'fclique',
    'fconsense',
    'fcontml',
    'fcontrast',
    'fdiscboot',
    'fdnacomp',
    'fdnadist',
    'fdnainvar',
    'fdnaml',
    'fdnamlk',
    'fdnamove',
    'fdnapars',
    'fdnapenny',
    'fdollop',
    'fdolmove',
    'fdolpenny',
    'fdrawgram',
    'fdrawtree',
    'ffactor',
    'ffitch',
    'ffreqboot',
    'fgendist',
    'findkm',
    'fkitsch',
    'fmix',
    'fmove',
    'fneighbor',
    'fpars',
    'fpenny',
    'fproml',
    'fpromlk',
    'fprotdist',
    'fprotpars',
    'freak',
    'frestboot',
    'frestdist',
    'frestml',
    'fretree',
    'fseqboot',
    'fseqbootall',
    'ftreedist',
    'ftreedistpair',
    'fuzznuc',
    'fuzzpro',
    'fuzztran',
    'garnier',
    'gd2copypal',
    'gd2togif',
    'gd2topng',
    'gdcmpgif',
    'gdlib-config',
    'gdparttopng',
    'gdtopng',
    'geecee',
    'getorf',
    'giftogd2',
    'helixturnhelix',
    'hmoment',
    'iep',
    'infoalign',
    'infoseq',
    'isochore',
    'jembossctl',
    'lindna',
    'listor',
    'makenucseq',
    'makeprotseq',
    'marscan',
    'maskfeat',
    'maskseq',
    'matcher',
    'megamerger',
    'merger',
    'msbar',
    'mwcontam',
    'mwfilter',
    'needle',
    'newcpgreport',
    'newcpgseek',
    'newseq',
    'noreturn',
    'notseq',
    'nthseq',
    'octanol',
    'oddcomp',
    'palindrome',
    'pasteseq',
    'patmatdb',
    'patmatmotifs',
    'pepcoil',
    'pepinfo',
    'pepnet',
    'pepstats',
    'pepwheel',
    'pepwindow',
    'pepwindowall',
    'plotcon',
    'plotorf',
    'pngtogd',
    'pngtogd2',
    'polydot',
    'preg',
    'prettyplot',
    'prettyseq',
    'primersearch',
    'printsextract',
    'profit',
    'prophecy',
    'prophet',
    'prosextract',
    'pscan',
    'psiphi',
    'rebaseextract',
    'recoder',
    'redata',
    'remap',
    'restover',
    'restrict',
    'revseq',
    'runJemboss.csh',
    'seealso',
    'seqmatchall',
    'seqret',
    'seqretsplit',
    'showalign',
    'showdb',
    'showfeat',
    'showorf',
    'showseq',
    'shuffleseq',
    'sigcleave',
    'silent',
    'sirna',
    'sixpack',
    'skipseq',
    'splitter',
    'stretcher',
    'stssearch',
    'supermatcher',
    'syco',
    'tcode',
    'textsearch',
    'tfextract',
    'tfm',
    'tfscan',
    'tmap',
    'tranalign',
    'transeq',
    'trimest',
    'trimseq',
    'twofeat',
    'union',
    'vectorstrip',
    'water',
    'webpng',
    'whichdb',
    'wobble',
    'wordcount',
    'wordfinder',
    'wordmatch',
    'wossname',
    'xml2-config',
    'xmlcatalog',
    'xmllint',
    'xslt-config',
    'xsltproc',
    'yank']


for filename in os.listdir(sys.argv[1]):
    if filename in EMBOSS_BINARIES:
        source = os.path.join(sys.argv[1], filename)
        dest = os.path.join(sys.argv[1], "_%s" % filename)
        shutil.move(source, dest)
        with open(source, 'w+') as handle:
            handle.write('#!/bin/sh\n\n')
            handle.write('BIN_DIR=$(dirname $(which %s))\n' % filename)

            handle.write('export EMBOSS_ACDROOT=$BIN_DIR/../share/EMBOSS/acd/\n')
            handle.write('export EMBOSS_DATA=$BIN_DIR/../share/EMBOSS/data/\n')
            handle.write('export PLPLOT_LIB=$BIN_DIR/../share/EMBOSS/\n')
            handle.write('_%s "$@"\n' % filename)
