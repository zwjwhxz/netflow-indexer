def get_indexer(indexer_type):
    mod = __import__('netflowindexer.%s' % indexer_type)
    mod = getattr(mod, indexer_type)
    indexer = mod.indexer.indexer_class
    return indexer

def do_index(indexer_type, out_dir, files):
    indexer = get_indexer(indexer_type)

    i = indexer(out_dir)
    return i.index_files(files)

def index():
    from optparse import OptionParser
    parser = OptionParser(usage = "usage: %prog -i indexer [options] /out/dir files")
    parser.add_option("-i", "--indexer", dest="indexer", action="store",
            help="indexer to use")

    (options, args) = parser.parse_args()
    if len(args) < 2 or not options.indexer:
        parser.print_help()
        return 1

    return do_index(options.indexer, args[0], args[1:])

def get_searcher(indexer_type):
    mod = __import__('netflowindexer.%s' % indexer_type)
    mod = getattr(mod, indexer_type)
    searcher = mod.searcher.main
    return searcher

def do_search(indexer_type, *args):
    searcher = get_searcher(indexer_type)
    return searcher(*args)

def search():
    from optparse import OptionParser
    parser = OptionParser(usage = "usage: %prog -i indexer [searcher_options]")
    parser.add_option("-i", "--indexer", dest="indexer", action="store",
            help="indexer to use")

    (options, args) = parser.parse_args()
    if not options.indexer:
        parser.print_help()
        return 1

    return do_search(options.indexer, *args)
