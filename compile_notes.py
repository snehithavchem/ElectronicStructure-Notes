#!/usr/bin/python

import os
from shutil import copy

chapters = ['advice',
            'background',
            'basis-sets',
            'dft',
            'electronic-wavefunctions',
            'excited-state-methods',
            'hartree-fock',
            'huckel',
            'molecular-hamiltonian',
            'multireference-methods',
            'properties',
            'relativistic',
            'slater-rules',
            'second-quantization',
            'symmetry',
            'wavefunction-methods']

root_dir = os.getcwd()

for ch in chapters:
    print(ch)
    chapter_dir = ch #os.path.join('Notes',ch)
    os.chdir(chapter_dir)
    os.system(f'xelatex {ch}.tex')
    os.system(f'bibtex {ch}.tex')
    os.system(f'xelatex {ch}.tex')
    os.system(f'xelatex {ch}.tex')
    copy(f'{ch}.pdf', f'../pdf')
    os.chdir(root_dir)

#main_dir = os.path.join('Notes','Main')
#main = 'chem371-notes'
#os.chdir(main_dir)
#os.system(f'xelatex {main}.tex')
#os.system(f'bibtex {main}.tex')
#os.system(f'xelatex {main}.tex')
#os.system(f'xelatex {main}.tex')
#copy(f'{main}.pdf', f'../../pdfs')
#os.chdir(root_dir)
