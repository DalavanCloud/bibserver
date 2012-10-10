SECRET_KEY = 'default-key'

# service and super user accounts
SERVICE_NAME = "BibSoup"
SITE_URL = "http://bibsoup.net"
HOST = "0.0.0.0"
DEBUG = True
PORT = 5000
SUPER_USER = ["test"]

# elasticsearch settings
ELASTIC_SEARCH_HOST = "http://127.0.0.1:9200"
ELASTIC_SEARCH_DB = "bibserver"

# bibserver functionality settings
# set to false if no frontend upload wanted
ALLOW_UPLOAD = True

# external API service settings and keys (should overwrite from local_config)
EXTERNAL_APIS = {
	"servicecore" : {
		"url" : "http://core.kmi.open.ac.uk/api/search/",
		"key" : "",
		"docs" : "http://core-project.kmi.open.ac.uk/api-doc/"
	}
}

# The default fields and settings for which faceting should be made available on
# these can be nested fields, e.g. links.url
SEARCH_FACET_FIELDS = [
    {
        "field":"collection.exact",
        "order":"term",
        "size":200,
        "display":"collection"
    },
    {
        "field":"type.exact",
        "order":"count",
        "display":"type"
    },
    {
        "field":"journal.name.exact",
        "display":"journal"
    },
    {
        "field":"author.name.exact",
        "order":"term",
        "size":500,
        "display":"author"
    },
    {
        "field":"year.exact",
        "size":100,
        "order":"reverse_term",
        "display":"year"
    }
]

# search result display layout
# a list of lists. each list represents a line on the display.
# in each line, there are objects for each key to include on the line.
# must specify the key, and optional "pre" and "post" params for displaying round it
SEARCH_RESULT_DISPLAY = [
    [
        {
            "field": "author.name"
        },
        {
            "pre": "(",
            "field": "year",
            "post": ")"
        }
    ],
    [
        {
            "pre":"<span style=\"font-weight:bold;font-size:120%;\"><a title=\"view record\" style=\"color:#666;text-decoration:underline;\" href=\"/record/",
            "field":"_id",
            "post":"\">"
        },
        {
            "field":"title",
            "post":"</a></span>"
        }
    ],
    [
        {
            "field": "howpublished"
        },
        {
            "pre": "in <em>",
            "field": "journal.name",
            "post": "</em>,"
        },
        {
            "pre": "<em>",
            "field": "booktitle",
            "post": "</em>,"
        },
        {
            "pre": "vol. ",
            "field": "volume"
        },
        {
            "field": "publisher"
        }
    ],
    [
        {
            "field": "link.url"
        }
    ]
]

# default view for collections page
COLLS_RESULT_DISPLAY = [
    [
        {
            "pre":'<h3><a href="/',
            "field":"owner",
            "post":"/"
        },
        {
            "field":"collection",
            "post":'">'
        },
        {
            "field":"label",
            "post":"</a></h3>"
        }
    ],
    [
        {
            "field":"description"
        },
        {
            "pre":' (created by <a href="/',
            "field":"owner",
            "post":'">'
        },
        {
            "field":"owner",
            "post":"</a>)"
        }
    ]
]

# a dict of the ES mappings. identify by name, and include name as first object name
# and identifier for how non-analyzed fields for faceting are differentiated in the mappings
FACET_FIELD = ".exact"
MAPPINGS = {
    "record" : {
        "record" : {
            "date_detection" : False,
            "dynamic_templates" : [
                {
                    "default" : {
                        "match" : "*",
                        "match_mapping_type": "string",
                        "mapping" : {
                            "type" : "multi_field",
                            "fields" : {
                                "{name}" : {"type" : "{dynamic_type}", "index" : "analyzed", "store" : "no"},
                                "exact" : {"type" : "{dynamic_type}", "index" : "not_analyzed", "store" : "yes"}
                            }
                        }
                    }
                }
            ]
        }
    },
    "collection" : {
        "collection" : {
            "date_detection" : False,
            "dynamic_templates" : [
                {
                    "default" : {
                        "match" : "*",
                        "match_mapping_type": "string",
                        "mapping" : {
                            "type" : "multi_field",
                            "fields" : {
                                "{name}" : {"type" : "{dynamic_type}", "index" : "analyzed", "store" : "no"},
                                "exact" : {"type" : "{dynamic_type}", "index" : "not_analyzed", "store" : "yes"}
                            }
                        }
                    }
                }
            ]
        }
    }
},

# list of external sites to search for record data at    
SEARCHABLES = {
    "Google" : "http://www.google.com/search?q=",
    "Google scholar" : "http://scholar.google.com/scholar?q=",
    "Google video" : "http://www.google.com/search?tbm=vid&q=",
    "Google blogs" : "http://www.google.com/search?tbm=blg&q=",
    "Google books" : "http://www.google.com/search?tbm=bks&q=",
    "Google images" : "http://www.google.com/search?tbm=isch&q=",
    "Google search ResearcherID" : "http://www.google.com/search?q=XXXX+site%3Awww.researcherid.com",
    "Google search ACM Author Profiles" : "http://www.google.com/search?q=XXXX+ACM+author+profile+site%3Adl.acm.org",
    "Google search Mathemtatics Genealogy" : "http://www.google.com/search?q=XXXX+site%3Agenealogy.math.ndsu.nodak.edu",
    "Microsoft academic search" : "http://academic.research.microsoft.com/Search?query=",
    "Zentralblatt Math" : "http://www.zentralblatt-math.org/zmath/en/search/?q=",
    "Zentralblatt Math authors" : "http://www.zentralblatt-math.org/zmath/en/authors/?au=",
    "MathSciNet" : "http://www.ams.org/mathscinet-mref?ref=",
    "DOI resolver" : "http://dx.doi.org/",
    "PubMed" : "http://www.ncbi.nlm.nih.gov/pubmed?term=",
    "PubMed Central" : "http://www.ncbi.nlm.nih.gov/pmc/?term=",
    "BioMed Central" : "http://www.biomedcentral.com/search/results?terms="
}
