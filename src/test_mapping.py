from deeponto.onto import Ontology # type: ignore
from deeponto.align.bertmap import BERTMapPipeline, DEFAULT_CONFIG_FILE # type: ignore


src_onto = Ontology("oeo-full.owl")
tgt_onto = Ontology("TheCimOntology.owl")


config = BERTMapPipeline.load_bertmap_config(DEFAULT_CONFIG_FILE)

config.bert.pretrained_path = r"bertmap/bert/checkpoint-3780"
config.global_matching.enabled = True 
config.global_matching.num_raw_candidates = 500
config.global_matching.num_best_predictions = 50
config.global_matching.mapping_filtered_threshold = 0.5
config.global_matching.mapping_extension_threshold = 0.5
# config.annotation_property_iris = [
#     "http://www.w3.org/2000/01/rdf-schema#label",
#     "http://www.w3.org/2004/02/skos/core#prefLabel",
#     "http://www.w3.org/2004/02/skos/core#altLabel",
#     "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym",
#     "http://www.geneontology.org/formats/oboInOwl#hasSynonym"
# ]



bertmap = BERTMapPipeline(src_onto, tgt_onto, config)
bertmap.save_mappings("BERTMap/match/mappings.json")