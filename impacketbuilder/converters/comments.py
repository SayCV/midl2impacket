from midl import *

from .base import *
from .constants import MidlConstantConverter
from .interface import MidlInterfaceConverter

class MidlCommentWriter(Writer):
    def banner_comment(self,  comment:str):
        self.single_line_comment("#"*80)
        self.single_line_comment( comment)
        self.single_line_comment("#"*80)

    def single_line_comment(self, comment:str):
        self.write(f"#{comment}\n")

    def comment_block(self, str):
        comment = f'"""\n{str}\n"""\n' 
        self.write(comment)
