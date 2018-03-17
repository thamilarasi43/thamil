def insert_line_para_nums(infile, outfile):
    f = open(infile, 'r')
    out = open(outfile, 'w')
    linecount = 0
        for i in f:
            paragraphcount = 0
            if '\n' in i:
                linecount += 1
            if len(i) < 2: paragraphcount *= 0
            elif len(i) > 2: paragraphcount = paragraphcount + 1
            out.write('%-4d %4d %s' % (paragraphcount, linecount, i))
    f.close()
    out.close()
