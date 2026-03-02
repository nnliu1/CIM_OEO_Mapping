# CIM_OEO_Mapping
mapping OEO terms to CIM onto

## OEO to CIM mapping results 
```
bertmap/match/raw_mappings.tsv
```

```
bertmap/match/raw_mappings.json
```


## Run BERTMap
use BERTMap checkpoint-3780, which is already fine-tuned in OEO and CIM
```
bertmap/bert/Checkpoint-3780
```

run
```
src/test_mapping.py
```