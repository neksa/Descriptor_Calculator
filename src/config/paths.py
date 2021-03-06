import os

ROOT = "/".join(os.path.dirname(__file__).split("/")[:-2])
DATA = os.path.join(ROOT, 'data')
USER_INPUT = os.path.join(ROOT, 'input')
USER_OUTPUT = os.path.join(ROOT, 'output')
INTERNAL = os.path.join(DATA, 'internal')
DEBUG = os.path.join(DATA, 'debug')
SRC = os.path.join(ROOT, 'src')
INPUT_PDB_INFO = os.path.join(USER_INPUT, 'pdb_info.pkl')
OUTPUT_DESCRS = os.path.join(USER_OUTPUT, 'descrs.pkl')

MATCHERS = os.path.join(INTERNAL, 'matchers')
DESCRS = os.path.join(INTERNAL, 'descrs')


# PREPROCESS = os.path.join(SRC, 'preprocessing')
# MEME_SUITE = os.path.join(PREPROCESS, 'meme_suite')
#
# PROSITE_EXTRACT = os.path.join(USER_INPUT, 'prosite_extract.txt')
# IONCOM_EXTRACT = os.path.join(USER_INPUT, 'ioncom_extract.txt')
# IONCOM_BINDING_SITES = os.path.join(USER_INPUT, 'ioncom_binding_sites.txt')
# REF_MEME_TXT = os.path.join(USER_INPUT, 'ref_meme.txt')
#
# PNAME_CID = os.path.join(INTERNAL, 'pname_cid_map.pkl')
# PDB_FOLDER = os.path.join(INTERNAL, 'pdb_files')
# MOTIF_POS = os.path.join(INTERNAL, 'motif_pos.pkl')
# TMP = os.path.join(INTERNAL, 'tmp')
# MEME_MAST_FOLDER = os.path.join(TMP, 'meme_mast')
#
# FULL_SEQS = os.path.join(INTERNAL, 'seqs.fasta')
# CONV_SEED_SEQS = os.path.join(INTERNAL, 'seed_seqs.fasta')
# CONV_MEME_FILE = os.path.join(INTERNAL, 'cov_meme.txt')
# TEMPLATE_SEQFILE = os.path.join(INTERNAL, 'seq_template.fasta')
#
# BASH_EXEC = "/bin/bash"
# MEME_EXEC = os.path.join(MEME_SUITE, 'meme', 'bin', 'meme')
# MAST_EXEC = os.path.join(MEME_SUITE, 'meme', 'bin', 'mast')

# CONVERGE_EXEC = os.path.join(EXTERNAL, "converge")
#
# INPUT = os.path.join(DATA, 'input')
# EXTERNAL = os.path.join(ROOT, 'input')
#
#
# STORE = os.path.join(DATA, 'store')
# OUTPUT = os.path.join(DATA, 'output')
#
# PROSITE_INPUT = os.path.join(INPUT, "prosite_extract.txt")
# IONCOM_INPUT = os.path.join(INPUT, "ioncom.txt")
#
# PNAME_CID = os.path.join(STORE, "pname_cid_map.pkl")

# fasta_fpath = os.path.join(store_dir, "prosite_seqs.fasta")

# mast_out = os.path.join(store_dir, "mast_out")
# mast_txt_path = os.path.join(mast_out, "mast.txt")
