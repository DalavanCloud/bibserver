# convert a source file to bibjson

"""
from datasource import DataSource
ds = DataSource()
d = ds.import_from("http://bibserver.berkeley.edu/DB/UCB_MATH1/Arveson__William_B.bib")
from serialisers.JsonSerialiser import JsonSerialiser
s = JsonSerialiser()
j = s.serialise(d)

from datasource import DataSource
ds = DataSource()
d = ds.import_from("http://bibserver.berkeley.edu/DB/UCB_MATH1/Arveson__William_B.bib")
from serialisers.SolrSerialiser import SolrSerialiser
solr = SolrSerialiser()
xml = solr.serialise(d)

from datasource import DataSource
ds = DataSource()
d = ds.import_from("http://bibserver.berkeley.edu/DB/UCB_MATH1/Arveson__William_B.bib")
from indexer import Indexer
i = Indexer()
i.index(d)

curl -X POST -H "Content-Type: text/xml" --data "<delete><query>collection:aldous</query></delete>" http://localhost:8983/solr/update?commit=true
"""

import urllib2
import csv
import json
from parsers.BibTexParser import BibTexParser

class DataSet(object):
    
    def convert(self, package):
        self.url = package["source"]
        self.format = package["format"]
        
        # read source and convert
        source = urllib2.urlopen(self.url)
        data = source.read()
        if self.format == "bibtex":
            parser = BibTexParser()
            d = parser.parse(data)
        if self.format == "bibjson":
            d = data
        if self.format == "csv":
            # convert from csv to json
            #dt = csv.dictReader( self.localfile )
            #d = {}
            #for k,v in dt:
            #    d(k) = v
            pass
        
        # add collection information
        collection = self.set_collection(d)
        
        # write data to file (maybe just for testing)
        tidyname = url.replace("/","___")
        fh = open('store/bibjson/' + tidyname, 'w')
        fh.write( json.dumps(collection) )
        fh.close()
        
        return d
    
    def set_collection(self,data,package):        
        jsonObj = []
        
        has_meta = False
        meta = None
        
        source = package["source"]
        collection = package["collection"]
        
        for btrecord in data:
            bibtype = btrecord.get('bibtype')
            if bibtype == "comment" and not has_meta:
                meta = self.get_meta(btrecord)
                meta['source'] = source
                meta['collection'] = collection
                has_meta = True
            else:
                bibjson = btrecord
                bibjson['location'] = location
                bibjson['collection'] = collection
                jsonObj.append(bibjson)
        
        if meta is not None:
            jsonObj = [meta] + jsonObj
        
        return jsonObj

    # used by set_colllection to find meta record
    def get_meta(self, btrecord):
        meta = {}
        meta["class"] = "metadata"
        for k, v in btrecord.iteritems():
            meta[k.lower()] = v
        return meta
    

