IEEE1364_1995_KEYWORDS = [
    "always",
    "and",
    "assign",
    "begin",
    "buf",
    "bufif0",
    "bufif1",
    "case",
    "casex",
    "casez",
    "cmos",
    "deassign",
    "default",
    "defparam",
    "disable",
    "edge",
    "else",
    "end",
    "endcase",
    "endfunction",
    "endmodule",
    "endprimitive",
    "endspecify",
    "endtable",
    "endtask",
    "event",
    "for",
    "force",
    "forever",
    "fork",
    "function",
    "highz0",
    "highz1",
    "if",
    "ifnone",
    "rpmos",
    "initial",
    "rtran",
    "inout",
    "rtranif0",
    "input",
    "rtranif1",
    "integer",
    "scalared",
    "join",
    "small",
    "large",
    "specify",
    "macromodule",
    "specparam",
    "medium",
    "strong0",
    "module",
    "strong1",
    "nand",
    "supply0",
    "negedge",
    "supply1",
    "nmos",
    "table",
    "nor",
    "task",
    "not",
    "time",
    "notif0",
    "tran",
    "notif1",
    "tranif0",
    "or",
    "tranif1",
    "output",
    "tri",
    "parameter",
    "tri0",
    "pmos",
    "tri1",
    "posedge",
    "triand",
    "primitive",
    "trior",
    "pull0",
    "trireg",
    "pull1",
    "vectored",
    "pulldown",
    "wait",
    "pullup",
    "wand",
    "rcmos",
    "weak0",
    "real",
    "weak1",
    "realtime",
    "while",
    "reg",
    "wire",
    "release",
    "wor",
    "repeat",
    "xnor",
    "rnmos",
    "xor",
]

IEEE1364_2001_KEYWORDS = IEEE1364_1995_KEYWORDS + [
    "automatic",
    "cell",
    "config",
    "incdir",
    "include",
    "instance",
    "liblist",
    "library",
    "localparam",
    "noshowcancelled",
    "pulsestyle_ondetect",
    "design",
    "endconfig",
    "endgenerate",
    "generate",
    "genvar",
    "pulsestyle_onevent",
    "showcancelled",
    "signed",
    "unsigned",
    "use",
]

IEEE1364_2001_NOCONFIG_KEYWORDS = [
    kw for kw in IEEE1364_2001_KEYWORDS if kw not in {
        "cell",
        "config",
        "design",
        "endconfig",
        "incdir",
        "include",
        "instance",
        "liblist",
        "library",
        "use",
    }
]

IEEE1364_2005_KEYWORDS = IEEE1364_2001_KEYWORDS + ["uwire"]

IEEE1800_2005_KEYWORDS = IEEE1364_2005_KEYWORDS + [
    "alias",
    "endsequence",
    "pure",
    "always_comb",
    "enum",
    "rand",
    "always_ff",
    "expect",
    "randc",
    "always_latch",
    "export",
    "randcase",
    "assert",
    "extends",
    "randsequence",
    "assume",
    "extern",
    "ref",
    "before",
    "final",
    "return",
    "bind",
    "first_match",
    "sequence",
    "bins",
    "foreach",
    "shortint",
    "binsof",
    "forkjoin",
    "shortreal",
    "bit",
    "iff",
    "solve",
    "break",
    "ignore_bins",
    "static",
    "byte",
    "illegal_bins",
    "string",
    "chandle",
    "import",
    "struct",
    "class",
    "inside",
    "super",
    "clocking",
    "int",
    "tagged",
    "const",
    "interface",
    "this",
    "constraint",
    "intersect",
    "throughout",
    "context",
    "join_any",
    "timeprecision",
    "continue",
    "join_none",
    "timeunit",
    "cover",
    "local",
    "type",
    "covergroup",
    "logic",
    "typedef",
    "coverpoint",
    "longint",
    "union",
    "cross",
    "matches",
    "unique",
    "dist",
    "modport",
    "var",
    "do",
    "new",
    "virtual",
    "endclass",
    "null",
    "void",
    "endclocking",
    "package",
    "wait_order",
    "endgroup",
    "packed",
    "wildcard",
    "endinterface",
    "priority",
    "with",
    "endpackage",
    "program",
    "within",
    "endprogram",
    "property",
    "endproperty",
    "protected",
]

IEEE1800_2009_KEYWORDS = IEEE1800_2005_KEYWORDS + [
    "accept_on",
    "checker",
    "endchecker",
    "eventually",
    "global",
    "implies",
    "let",
    "nexttime",
    "reject_on",
    "restrict",
    "s_always",
    "s_eventually",
    "s_nexttime",
    "s_until",
    "s_until_with",
    "strong",
    "sync_accept_on",
    "sync_reject_on",
    "unique0",
    "until",
    "until_with",
    "untyped",
    "weak",
]

IEEE1800_2012_KEYWORDS = IEEE1800_2009_KEYWORDS + [
    "implements",
    "nettype",
    "interconnect",
    "soft",
]

IEEE1800_2017_KEYWORDS = IEEE1800_2012_KEYWORDS + [
]
