import traceback
from midl import MidlDefinition, MidlInterface, MidlTypeDef, MidlVarDef, MidlEnumDef
from .state import InterfaceState, State
import string
from . import midltokenizer as mt


"""This file contains a series of classes that are responsible for parsing discrete parts of a MIDL file.

    MidlParser
    MidlVarDefParser
    MidlTypeDefParse
    MidlInterfaceParser
    TODO: MidlProcedureParser

""" 

class MidlParser():
    """Parses a complete MIDL file into a MidlDefiniton object

        This class maintains a state machine.
    """
    def handle_instantiation(self, const = False):
        """Handles instantiation statements.
        """

        #TODO this function should be split off into its own class.
        # next(self.tokens) should only ever be invoked from a `parse()` function.
        tok = next(self.tokens)
        if tok.data == "int":
            name = next(self.tokens)
            if name.type != mt.Token.SYMBOL:
                raise Exception(f"Expecting SYMBOL, got {name.type}")
            eq = next(self.tokens)
            if eq.data != "=":
                raise Exception(f"Expecting EQUALS, got {eq.data}")
            rhs = ""
            rhs_tok = next(self.tokens)
            while rhs_tok.type != mt.Token.SEMICOLON:
                rhs += " "
                rhs += rhs_tok.data
                rhs_tok = next(self.tokens)
            self.definition.add_instantiation(tok.data, name.data, rhs, const)
            self.state=State.DEFAULT
                
                
    def handle_keyword(self,token):
        """Handles encountered keywords
        """
        # Only 2 keywords should ever be encountered here: [const, import]
        if token.data == "import":
            self.state = State.IMPORT
        elif token.data == "const":
            self.state = State.DEFINTION
            self.handle_instantiation(const=True)
        else:
            raise Exception(f"Unhandled keyword: {token.data}")

    def handle_string(self,token):
        """Encountered a string. Should only ever be imports encountered here.
        """
        if self.state == State.IMPORT:
            # Encountered an import statement so add it to the definiton's imports
            assert(token.type == mt.Token.STRING), f"Unexpected token in import definition: {token.data}"
            self.definition.add_import(token.data)
            # Reset the state
            self.state = State.DEFAULT
        else:
            # If a string is encountered outside of the import statements, raise an exception
            # TODO This may not necessarily be true, there can be variable instantiations that are strings!
            raise Exception(f"Unhandled state : {self.state}")

    def handle_sqbracket(self, token):
        """Encountered a square bracket. Only opening brackets are handled here.
        """
        if token.data == "[":
            if self.state == State.DEFAULT:
                # we hit the start of an interface definition, specifically the header, spin up a parser
                interface = MidlInterfaceParser(self.tokens).parse(token)
                self.definition.add_interface(interface)
            else:
                #Somehow we ended up in an invalid state when encountering an opening square bracket
                raise Exception(f"Invalid State for `{token.data}` in MidlParser")
        else:
            # Note that the closing square bracket is handled within the MidlInterfaceParser
            raise Exception(f"Invalid token data `{token.data}` for token type")

    def handle_semicolon(self,token):
        """A semicolon was encountered, so reset the parsing state.
        """
        self.state = State.DEFAULT

    def __init__(self):
        self.state = State.DEFAULT # Current state of the parsing
        self.definition = MidlDefinition() # data to be returned by calling parse()
        self.tok_handlers = { # Jump table to handle different token types
            mt.Token.KEYWORD : MidlParser.handle_keyword,
            mt.Token.STRING : MidlParser.handle_string,
            mt.Token.SQBRACKET : MidlParser.handle_sqbracket,
            mt.Token.SEMICOLON : MidlParser.handle_semicolon
        }
        self.sqbracket_lvl  = 0 # Maintains the embedding level of square brackets `[]`
        self.tokens = None # The generator that yields tokens to parse

    def parse(self, data:str ) -> MidlDefinition:
        """Parsing loop that iterates over tokens and invokes their handler function.
             If an unhandled token does not have a registered handler, an out of bounds access will occur in the tok_handlers dict.
             Note that this should never happen with a well formed test case (unless something hasn't been considered.)

        Args:
            data (str): [description]

        Returns:
            MidlDefinition: [description]
        """
        tokenizer = mt.MidlTokenizer(data)
        self.tokens = tokenizer.get_token()
        cur_token = next(self.tokens)
        while cur_token is not None:
            try:
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)
            except Exception:
                print(self.definition)
                traceback.print_exc()
                exit()
        return self.definition


class MidlVarDefParser():
    def handle_keyword(self,cur_tok):
        if cur_tok.data == "enum":
            raise Exception("Unexpected enum")
        if self.sq_bracket_level == 0:
            self.cur_type = cur_tok.data
        else:
            pass
    def handle_symbol(self,cur_tok):
        if self.sq_bracket_level == 0:
            if self.cur_type is None:
                self.cur_type = cur_tok.data
            else:
                self.vds.append(MidlVarDef(self.cur_type,cur_tok.data))

    def handle_comma(self,cur_tok):
        pass
    
    def handle_sqbracket(self,cur_tok):
        if cur_tok.data =="]":
            assert(self.sq_bracket_level >0)
            self.sq_bracket_level -= 1
        elif cur_tok.data == "[":
            self.sq_bracket_level +=1
        # for now, ignore square bracket vardefs, may need to revisit later
        
    def handle_rbracket(self,cur_tok):
        # for now, ignore square bracket vardefs, may need to revisit later
        pass
    def handle_brace(self,cur_tok):
        if cur_tok.data =="}":
            assert(self.brace_level >0)
            self.brace_level -= 1
        elif cur_tok.data == "{":
            self.brace_level +=1
        else:
            raise Exception("Illegal Brace")
        
    def handle_semicolon(self,cur_tok):
        self.cur_type = None

    def handle_operator(self, cur_tok):
        if cur_tok.data == "*":
            self.cur_type += "*"
        else:
            raise Exception(f"Illegal Operator  '{cur_tok.data}' in variable definition")

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.vds = []
        self.cur_type = None
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.sq_bracket_level = 0
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlVarDefParser.handle_keyword,
            mt.Token.SQBRACKET : MidlVarDefParser.handle_sqbracket,
            mt.Token.RBRACKET : MidlVarDefParser.handle_rbracket,
            mt.Token.SYMBOL : MidlVarDefParser.handle_symbol,
            mt.Token.COMMA : MidlVarDefParser.handle_comma,
            mt.Token.SEMICOLON : MidlVarDefParser.handle_semicolon,
            mt.Token.BRACE : MidlVarDefParser.handle_brace,
            mt.Token.OPERATOR : MidlVarDefParser.handle_operator,
        }

    def parse(self, cur_tok) -> MidlVarDef:
        cur_token = cur_tok
        while cur_token is not None:
            try:
                if cur_token.data == "}" and self.brace_level == 1: #exit once the def is done
                    return self.vds
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)

            except Exception:
                traceback.print_exc()
                exit()
        if len(self.vds) == 0 :
            raise Exception("Parsing Typedef failed")
        return self.vds


class MidlTypedefParser():
    def handle_context_handle(self,token):
        tok_closing_sqbracket = next(self.tokens)
        if tok_closing_sqbracket.data != "]":
            raise Exception("Malformed typedef")
        tok_type = next(self.tokens)
        tok_name = next(self.tokens)
        self.td = MidlTypeDef(tok_type.data, tok_name.data, is_context_handle=True)

    def handle_var_defs(self,token):
        vds =  MidlVarDefParser(self.tokens).parse(token)
        return vds

    def handle_struct_def(self,token):
        tok_private_name = next(self.tokens)
        if tok_private_name.type != mt.Token.SYMBOL:
            raise Exception(f"Invalid struct name {tok_private_name.data}")
        else:
            self.private_name =  tok_private_name.data
        t = next(self.tokens)
        if t.data != "{":
            raise Exception(f"Expecting 'lbrace' {t.data}")
        self.brace_level += 1
        var_defs = self.handle_var_defs(t)
        self.brace_level-=1
        self.vds.extend( var_defs)

    def handle_brace(self, token):
        if token.data =="}":
            assert(self.brace_level > 0)
            self.brace_level -= 1
        elif token.data == "{":
            self.brace_level += 1
        else:
            raise Exception("Illegal Brace")
    def handle_enum_def(self, token):
        # TODO handle enum defs
        name = next(self.tokens).data
        if next(self.tokens).data != "{":
            raise Exception("Expecting opening brace")
        self.brace_level += 1
        enums = {}
        while True:
            name = next(self.tokens).data
            t = next(self.tokens)
            if t.data == "=":
                val = next(self.tokens).data
                enums[name] = val
                t = next(self.tokens)
            if t.data == ",":
                enums[name] = None
                continue
            if t.data == "}":
                self.brace_level -=1
                #end of defintion
                break
            else:
                raise Exception(f"Unexpected token: {t.data}")
        self.enums = enums

    def handle_keyword(self,token):
        if token.data == "context_handle":
            self.handle_context_handle(token)
        elif token.data == "struct":
            self.handle_struct_def(token)
        elif token.data == "enum":
            self.handle_enum_def(token)


    def handle_sqbracket(self,token):
        token = next(self.tokens)
        if token.data != "v1_enum":
            self.handle_keyword(token)
            #var_defs = self.handle_var_defs(token)
            #self.vds.extend( var_defs)
            
        
    def handle_rbracket(self,token):
        #print(token.data)
        pass
    def handle_semicolon(self,token):
        pass
    def handle_comma(self,token):
        #print(token.data)
        pass
    def handle_symbol(self,token):
        if self.brace_level == 0:
            self.public_name = token.data
    def handle_string(self,token):
        pass

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.td = None
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.vds = []
        self.private_name = None
        self.public_name = None
        self.enums = None
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlTypedefParser.handle_keyword,
            mt.Token.STRING : MidlTypedefParser.handle_string,
            mt.Token.SQBRACKET : MidlTypedefParser.handle_sqbracket,
            mt.Token.SYMBOL : MidlTypedefParser.handle_symbol,
            mt.Token.RBRACKET : MidlTypedefParser.handle_rbracket,
            mt.Token.COMMA : MidlTypedefParser.handle_comma,
            mt.Token.BRACE : MidlTypedefParser.handle_brace,
            mt.Token.SEMICOLON : MidlTypedefParser.handle_semicolon,

        }

    def parse(self, cur_tok) -> MidlTypeDef:
        cur_token = cur_tok
        while cur_token is not None:
            try:
                if cur_token.type == mt.Token.SEMICOLON and self.brace_level == 0:
                    break
                #print(cur_token.data, cur_token.type, self.brace_level)
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)

            except Exception:
                for v in self.vds:
                    #print(v)
                    pass
                traceback.print_exc()
                exit()
        if self.td is None:
            if self.enums is not None:
                self.td = MidlEnumDef(self.public_name, self.enums)
            else:
                self.td = MidlTypeDef(self.vds, self.public_name, is_complex=True)
                self.td.private_name = self.private_name
        return self.td


class MidlInterfaceParser():
    """Responsible for parsing an interface definiton.

        Mostly, this class delegates to other classes to handle parsing
    """
    def handle_sqbracket(self,token):
        """Detected the beginning of an interface header, set the current state appropriately
        """
        if token.data == "[":
            self.state = InterfaceState.HEADER_START
        elif token.data =="]":
            self.state = InterfaceState.DEFAULT
        else: 
            raise Exception("Illegal token, expecting sqbracket")

    def handle_rbracket(self,token):
        """Round brackets detected

            Sets the appropriate header variable, or reverts the state.
        """
        if token.data == "(":
            if self.state == InterfaceState.UUID:
                tok = next(self.tokens)
                self.interface.uuid = tok.data
            elif self.state == InterfaceState.VERSION:
                tok = next(self.tokens)
                self.interface.version = tok.data
            elif self.state == InterfaceState.POINTER_DEFAULT:
                tok = next(self.tokens)
                self.interface.pointer_default = tok.data
            elif self.state == InterfaceState.CPP_QUOTE:
                #tok = next(self.tokens)
                pass
                #TODO handle cpp_quote, not really urgent and super hard to convert to Python
            else:
                raise Exception("Illegal state transition")
        elif token.data == ")":
            if self.state == InterfaceState.UUID:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.VERSION:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.POINTER_DEFAULT:
                self.state = InterfaceState.HEADER_START
            elif self.state == InterfaceState.CPP_QUOTE:
                self.state = InterfaceState.DEFAULT
            else:
                raise Exception("Illegal state transition")

    def handle_procedure(self,token):
        """Delegates to a MidlProcedureParser

            TODO: UNIMPLEMENTED
        """
        # TODO parse out the procedures
        # For now, just seek until the first ");" to skip procedure parsing
        cur_tok = token
        prev_tok = token
        while True:
            if prev_tok.data == ")" and cur_tok.data ==";":
                return None
            prev_tok = cur_tok
            cur_tok = next(self.tokens)
        return None

        
    def handle_keyword(self,token):
        """Parses keywords [uuid, version, pointer_default,interface, error_status_t, typedef, cpp_quote]
        """
        if token.data == "uuid" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.UUID
        elif token.data == "version" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.VERSION
        elif token.data == "pointer_default" and self.state == InterfaceState.HEADER_START:
            self.state = InterfaceState.POINTER_DEFAULT
        elif token.data == "interface" and self.state == InterfaceState.DEFAULT:
            tok = next(self.tokens)
            assert(tok.type == mt.Token.SYMBOL)
            self.interface.name = tok.data
        elif token.data == "error_status_t":
            proc = self.handle_procedure(token)
            if proc != None:
                self.interface.add_procedure(proc)
        elif token.data == "typedef" and self.state == InterfaceState.DEFAULT:
            # spin up a TypeDef parser to parse out typedefs
            td = MidlTypedefParser(self.tokens).parse(token)
            self.interface.add_typedef(td)
        elif token.data == "cpp_quote":
            self.state = InterfaceState.CPP_QUOTE
        else:
            raise Exception(f"Unhandled keyword: {token.data} in state InterfaceState: {self.state}")

    def handle_comma(self, token):
        """no-op to handle encountered commas
        """
        pass

    def handle_string(self,token):
        if self.state == InterfaceState.CPP_QUOTE:
            #TODO handle CPP_QUOTE
            # no-op for now
            return
        else:
            raise Exception("Unexpected string")
    def handle_brace(self,token):
        """Sets the brace level appropriately
        """
        if token.data == "{":
            self.brace_level +=1
        elif token.data =="}":
            assert(self.brace_level >0), "Something went terribly wrong, you ended up with a brace imbalance!"
            self.brace_level -=1

    def __init__(self, token_generator):
        self.tokens = token_generator
        self.interface = MidlInterface()
        self.state = InterfaceState.DEFAULT
        self.brace_level = 0
        self.tok_handlers = {
            mt.Token.KEYWORD : MidlInterfaceParser.handle_keyword,
            mt.Token.STRING : MidlInterfaceParser.handle_string,
            mt.Token.SQBRACKET : MidlInterfaceParser.handle_sqbracket,
            mt.Token.RBRACKET : MidlInterfaceParser.handle_rbracket,
            mt.Token.COMMA : MidlInterfaceParser.handle_comma,
            mt.Token.BRACE : MidlInterfaceParser.handle_brace,
        }

    def parse(self, cur_tok) -> MidlInterface:
        """Parsing loop
        """
        cur_token = cur_tok
        while cur_token is not None:
            try:
                #print(cur_token.data, cur_token.type, self.brace_level)
                self.tok_handlers[cur_token.type](self, cur_token)
                cur_token = next(self.tokens)
            except Exception:
                return self.interface
        return self.interface