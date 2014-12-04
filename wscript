srcdir = '.'
blddir = 'build'

def options(opt):
    opt.load('compiler_c compiler_cxx')

def configure(conf):
    conf.load('compiler_c compiler_cxx')
    conf.check(features='cxx cxxprogram', cflags=['-Wall'], cxxflags=['-std=c++14'])

def build(bld):
    source = bld.path.ant_glob('**/src/*.cpp')
    cxxflags = ['-std=c++14']
    includes = ['include']
    bld(features='c cxx cxxprogram', source=source, target='app', cxxflags=cxxflags,
        includes=includes)
