'''
usefull open lib

*My DOC could be sucks, I need doc PR*

[DOCS]
    [__DOC__ DATA OBJ, (FUNC, CLASS)]
        they have they own docs
        see docs to use help() or .__doc__
    [NO __DOC__ DATA]
        [VARS]
            o = open
            modo = mod_open
            cc = JNCLib.customd_type_tool.checker_cores
            MLSC = ModLambdaSrcCore
            MLS = ModLambdaSrc
        [LAMBDAS]
            mod_open = lambda opener, f, mod : opener(f, mod)
                see example
            ModLambdaSrcCore = lambda core, modoption : core(mstr(*modoption[0], **modoption[1]))
                WARNING : THIS IS SPECAIL LOL
                use core func to generate ModLambda's SRC PART
            ex)
                1 | mode_opener = lambda f, x : mod_open(o, f, x)

WARNING : this module dosen't give use csv open func, see opener.py

'''

from JNCLib.customd_type_tool import checker_cores as cc

#DEFINE BASIC FUNCTIONS
o = open #JUST SEE DOCS
modo = mod_open = (lambda opener, f, mod : opener(f, mod)) #[WARN;PLZ,C,DOCS!] opener can be anythin' 2 argv. BUT target is only 1, as U know.

def ModoDeco(data, mod_index = 0):
    '''
    it looks like deco type but
    actually, it just function

    f = ModDeco([DATA THAT TYPES THAT WILL DETERMINE]), f([ANTHER ABSTRACT PART]) to can use it moded open.
    TMI : data is opener or mod
    '''
    _checker = cc(mod_index) #PUT a index by get FUNC
    if _checker(data, str): #MOD IS determined, opener is abstract
        def deco(opener):
            '''
            modo is descriped in module docs
            return lambda (lambda f : modo())
            opener's deco
            '''
            return (lambda f : modo(opener, f, data))
    else: #realy else case, it's verbatim
        def deco(mod):
            '''
            modo is descriped in module docs
            return lambda (lambda f : modo())
            actually mod-str input func
            '''
            return (lambda f : modo(data, f, mod))

class UsingModStrGenIsWrongErr(Exception): #will fix it all
    '''
    See Menual at ModStrGen 3~4
    '''

def ModStrGen(r = False, w = False, RWisA = False, w_must_be_x = False, binType = False, PlusAlpha = False):
    '''
    ModStrGen(r = False, w = False, RWisA = False, w_must_be_x = False, binType = False, PlusAlpha = False)

    WARNING :
        both r and w is False ->  'AssertionalError ; UsingModStrGenIsWrongErr ; You must choose. "r or w"?, (r : [VAR r 's value], w : [VAR w 's value])'

    just return mod-str that can use at open()
    '''
    try: #it I'll fix at custom_assert_tool update
        assert r or w, f'AssertionalError ; UsingModStrGenIsWrongErr ; You must choose. "r or w"?, (r : {r}, w : {w})'
    except AssertionError as err:
        raise UsingModStrGenIsWrongErr(str(err))
    m = 'x' if w and w_must_be_x else 'w
    m = m if w else 'r'
    m = 'a' if r and w and RWisA else m
    if binType: m += 'b'
    if PlusAlpha: m += '+'
    return m
    
def mstr(r = False, w = False, a = False, x = False, b = False, pp = False):
    '''
        see help(ModStrGen)
        return ModStrGen(r = r, w = w, RWisA = a, w_must_be_x = x, binType = b, PlusAlpha = pp)
    '''
    return ModStrGen(r = r, w = w, RWisA = a, w_must_be_x = x, binType = b, PlusAlpha = pp)

MLSC = ModLambdaSrcCore = lambda core, modoption : core(mstr(*modoption[0], **modoption[1]))

def ModLambdaSrc(core, *modoptions1, **modoptions2):
    '''
    ModLambdaSrc(core, *modoptions1, **modoptions2) = MLSC(core, [modoptions1, modoptions2])

    Tip: MLSC is explain at module docs
    '''
    return MLSC(core, [modoptions1, modoptions2])

MLS = ModLambdaSrc

class ThisModulesCore: #will update. (long year later (that I felt))
    '''
    actualy not module, it's class
    but all func is static method so it works like module

    p is +

    all of this is decorator

    function name also can gen at mstr
    '''

    #OME!!!!!!!!!!!
    #OHHHHH MYYYYYY EYESSSSSS@!!!!!!!!!

    @staticmethod
    def w(core):
        return MLS(core, w = True)
    
    @staticmethod
    def r(core):
        return MLS(core, r = True)
    
    @staticmethod
    def x(core):
        return MLS(core, w = True, x = True)
    
    @staticmethod
    def a(core):
        return MLS(core, r = True, w = True, a = True)
    
    @staticmethod
    def wb(core):
        return MLS(core, w = True, b = True)
    
    @staticmethod
    def rb(core):
        return MLS(core, r = True, b = True)
    
    @staticmethod
    def xb(core):
        return MLS(core, w = True, x = True, b = True)
    
    @staticmethod
    def ab(core):
        return MLS(core, r = True, w = True, a = True, b = True)

    @staticmethod
    def wp(core):
        return MLS(core, w = True, pp = True)
    
    @staticmethod
    def rp(core):
        return MLS(core, r = True, pp = True)
    
    @staticmethod
    def xp(core):
        return MLS(core, w = True, x = True, pp = True)
    
    @staticmethod
    def ap(core):
        return MLS(core, r = True, w = True, a = True, pp = True)
    
    @staticmethod
    def wbp(core):
        return MLS(core, w = True, b = True, pp = True)
    
    @staticmethod
    def rbp(core):
        return MLS(core, r = True, b = True, pp = True)
    
    @staticmethod
    def xbp(core):
        return MLS(core, w = True, x = True, b = True, pp = True)
    
    @staticmethod
    def abp(core):
        return MLS(core, r = True, w = True, a = True, b = True, pp = True)
    
class TMC(ThisModulesCore):
    '''
    actually this :
    TMP = ThisModulesCore
    '''

class OpenModuleCore:
    '''

    CORE OF OMC

    DOC OF OMC :

    open functioned ver of ThisModulesCore

    I can't explain it
    I Can't descript
    I'm tired
    I got no times
    
    so
    now...

    I just give up now
    NAH.
    '''
    core = ModoDeco(o)

class OMC(OpenModuleCore):
    pass


class OpenMdule(OMC):
    w = staticmethod(TMC.w(OMC.core))
    r = staticmethod(TMC.r(OMC.core))
    a = staticmethod(TMC.a(OMC.core))
    x = staticmethod(TMC.x(OMC.core))
    wb = staticmethod(TMC.wb(OMC.core))
    rb = staticmethod(TMC.rb(OMC.core))
    ab = staticmethod(TMC.ab(OMC.core))
    xb = staticmethod(TMC.xb(OMC.core))
    wp = staticmethod(TMC.wp(OMC.core))
    rp = staticmethod(TMC.rp(OMC.core))
    ap = staticmethod(TMC.ap(OMC.core))
    xp = staticmethod(TMC.xp(OMC.core))
    wbp = staticmethod(TMC.wbp(OMC.core))
    rbp = staticmethod(TMC.rbp(OMC.core))
    abp = staticmethod(TMC.abp(OMC.core))
    xbp = staticmethod(TMC.xbp(OMC.core))

#ENOUGH 4 2DAY!!!!!!!!!!

#real usefull part

def wither(opener):
    '''
    decorator that use opener

    `@wither(opener)`

    def with_deco(func):
        \'\'\'
        get func part
        see wither
        \'\'\'
        def with_opener(f):
            \'\'\'
            with to use opener (get by wither)
            to make obj ([VAR NAME] fp)
            and throw it to func!!! (Like FW)
            as you know this is gen by with_deco
            \'\'\'
            with opener(f) as fp:
                return func(fp)
        return with_deco
    '''
    def with_deco(func):
        '''
        get func part
        see wither
        '''
        def with_opener(f):
            '''
            with to use opener (get by wither)
            to make obj ([VAR NAME] fp)
            and throw it to func!!! (Like FW)
            as you know this is gen by with_deco
            '''
            with opener(f) as fp:
                return func(fp)
        return with_deco